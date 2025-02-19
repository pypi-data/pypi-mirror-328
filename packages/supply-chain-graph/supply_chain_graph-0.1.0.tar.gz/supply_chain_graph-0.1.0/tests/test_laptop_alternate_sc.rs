// Command to run all tests
// cargo test --release 
// Command to run a specific test
// cargo test --release --test demand_planner_tests test_plan_quality -- --nocapture
// RUST_LOG=info cargo test --release --test test_laptop_sc test_laptop_planning -- --nocapture


#[cfg(test)]
mod tests {
    use supply::demand_planner::DemandPlanner;
    use supply::demand::Demand;
    use supply::sku::SKU;
    use supply::specification::Specification;
    use supply::flow::Flow;
    use supply::simultaneous_flow::SimultaneousFlow;
    use supply::operation::{Operation, MaterialFlowVariant, ResourceFlowVariant};
    use chrono::NaiveDate;
    use std::sync::Arc;
    use parking_lot::Mutex;
    use supply::reports::plan_exporter::PlanExporter;
    use function_name::named;
    use supply::resource::Resource;
    use supply::resource_flow::ResourceFlow;

    fn create_date(year: i32, month: u32, day: u32) -> NaiveDate {
        NaiveDate::from_ymd_opt(year, month, day).unwrap()
    }

    fn create_laptop_supply_chain() -> (
        // DC Products
        Arc<Mutex<SKU>>, // Laptop DC
        // Plant Products
        Arc<Mutex<SKU>>, // Laptop Plant1
        Arc<Mutex<SKU>>, // Laptop Plant2
        // Components Plant1
        Arc<Mutex<SKU>>, // Disk Plant1
        Arc<Mutex<SKU>>, // CPU Plant1
        Arc<Mutex<SKU>>, // Memory Plant1
        // Components Plant2
        Arc<Mutex<SKU>>, // Disk Plant2
        Arc<Mutex<SKU>>, // CPU Plant2
        Arc<Mutex<SKU>>, // Memory Plant2
        // Resources
        Arc<Mutex<Resource>>, // Assembly Resource Plant1
        Arc<Mutex<Resource>>, // Assembly Resource Plant2
        // Operations
        Arc<Mutex<Operation>>, // Laptop Transport Plant1
        Arc<Mutex<Operation>>, // Laptop Transport Plant2
    ) {
        // Create SKUs
        let laptop_dc = SKU::from_name("Laptop@DC"); 
        let laptop_plant1 = SKU::from_name("Laptop@Plant1");
        let laptop_plant2 = SKU::from_name("Laptop@Plant2");
        
        // Create component SKUs for each plant
        let disk_plant1 = SKU::from_name("Disk@Plant1");
        let cpu_plant1 = SKU::from_name("CPU@Plant1");
        let memory_plant1 = SKU::from_name("Memory@Plant1");
        
        let disk_plant2 = SKU::from_name("Disk@Plant2");
        let cpu_plant2 = SKU::from_name("CPU@Plant2");
        let memory_plant2 = SKU::from_name("Memory@Plant2");

        // Create assembly resources
        let assembly_resource_plant1 = Resource::from_name("Assemble_Laptop@Plant1");
        let assembly_resource_plant2 = Resource::from_name("Assemble_Laptop@Plant2");
        let assembly_resource_flow_plant1 = ResourceFlow::new(1.0, assembly_resource_plant1.clone());
        let assembly_resource_flow_plant2 = ResourceFlow::new(1.0, assembly_resource_plant2.clone());

        // Create flows for Laptop assembly at Plant1
        let laptop_plant1_output = Flow::new(false, 1.0, laptop_plant1.clone());
        let laptop_plant1_components = SimultaneousFlow::new(vec![
            Flow::new(true, 1.0, disk_plant1.clone()),
            Flow::new(true, 1.0, cpu_plant1.clone()),
            Flow::new(true, 2.0, memory_plant1.clone()),
        ]);

        // Create flows for Laptop assembly at Plant2
        let laptop_plant2_output = Flow::new(false, 1.0, laptop_plant2.clone());
        let laptop_plant2_components = SimultaneousFlow::new(vec![
            Flow::new(true, 1.0, disk_plant2.clone()),
            Flow::new(true, 1.0, cpu_plant2.clone()),
            Flow::new(true, 2.0, memory_plant2.clone()),
        ]);

        // Create assembly operations for both plants
        let laptop_assembly_plant1 = Operation::new(
            "Make_Laptop@Plant1".to_string(),
            2, // lead time
            1, // min batch
            1, // batch multiple
            MaterialFlowVariant::Single(laptop_plant1_output),
            MaterialFlowVariant::Simultaneous(laptop_plant1_components),
            ResourceFlowVariant::SingleResource(assembly_resource_flow_plant1)
        );

        let laptop_assembly_plant2 = Operation::new(
            "Make_Laptop@Plant2".to_string(),
            3, // lead time (longer at Plant2)
            1, // min batch
            1, // batch multiple
            MaterialFlowVariant::Single(laptop_plant2_output),
            MaterialFlowVariant::Simultaneous(laptop_plant2_components),
            ResourceFlowVariant::SingleResource(assembly_resource_flow_plant2)
        );

        // Create transport operation (from either plant to DC)
        let move_laptop_plant1_to_dc = Operation::new(
            "Move_Laptop@Plant1-to-DC".to_string(),
            1, // lead time
            1, // min batch
            1, // batch multiple
            MaterialFlowVariant::Single(Flow::new(false, 1.0, laptop_dc.clone())),
            MaterialFlowVariant::Single(Flow::new(true, 1.0, laptop_plant1.clone())), // Can consume from Plant1
            ResourceFlowVariant::None
        );

        let move_laptop_plant2_to_dc = Operation::new(
            "Move_Laptop@Plant2-to-DC".to_string(),
            1, // lead time
            1, // min batch
            1, // batch multiple
            MaterialFlowVariant::Single(Flow::new(false, 1.0, laptop_dc.clone())),
            MaterialFlowVariant::Single(Flow::new(true, 1.0, laptop_plant2.clone())), // Can consume from Plant1
            ResourceFlowVariant::None
        );


        let mut laptop_plant1_ref = laptop_plant1.lock();
        laptop_plant1_ref.add_producing_operation(laptop_assembly_plant1.clone());
        laptop_plant1_ref.generate_top_producing_operation();
        drop(laptop_plant1_ref);

        let mut laptop_plant2_ref = laptop_plant2.lock();
        laptop_plant2_ref.add_producing_operation(laptop_assembly_plant2.clone());
        laptop_plant2_ref.generate_top_producing_operation();
        drop(laptop_plant2_ref);
        let mut laptop_dc_ref = laptop_dc.lock();
        laptop_dc_ref.add_producing_operation(move_laptop_plant1_to_dc.clone());
        laptop_dc_ref.add_producing_operation(move_laptop_plant2_to_dc.clone());
        laptop_dc_ref.generate_top_producing_operation();
        drop(laptop_dc_ref);

        (
            laptop_dc,
            laptop_plant1, laptop_plant2,
            disk_plant1, cpu_plant1, memory_plant1,
            disk_plant2, cpu_plant2, memory_plant2,
            assembly_resource_plant1, assembly_resource_plant2,
            move_laptop_plant1_to_dc,
            move_laptop_plant2_to_dc
        )
    }

    #[test]
    #[named]
    fn test_laptop_alternate_sc() {
        let path_to_test_settings_yml = "./tests/config/settings_trace_selected_demands.yml";
        if let Err(e) = supply::logger_config::configure_logger_from_path(path_to_test_settings_yml) {
            eprintln!("Failed to configure logger: {}", e);
        }

        let (laptop_dc, _laptop_plant1, _laptop_plant2, 
            disk_plant1, cpu_plant1, memory_plant1,
             disk_plant2, cpu_plant2, memory_plant2, 
             assembly_resource_plant1, assembly_resource_plant2, 
                _move_laptop_plant1_to_dc, _move_laptop_plant2_to_dc) = create_laptop_supply_chain();

        let mut specification = Specification::new(2, 0);

        let jan_15 = create_date(2024, 1, 15);
        disk_plant1.lock().add_inventory(jan_15, 1000.0);
        cpu_plant1.lock().add_inventory(jan_15, 250.0); // shared between A and B
        memory_plant1.lock().add_inventory(jan_15, 500.0);
        disk_plant2.lock().add_inventory(jan_15, 1000.0);
        cpu_plant2.lock().add_inventory(jan_15, 250.0); // shared between A and B
        memory_plant2.lock().add_inventory(jan_15, 500.0);

        let mut assembly_resource_ref1 = assembly_resource_plant1.lock();
        for day in 15..=31 {
            assembly_resource_ref1.set_capacity(
                create_date(2024, 1, day),
                100.0 // Daily assembly capacity
            );
        }
        drop(assembly_resource_ref1);

        let mut assembly_resource_ref2 = assembly_resource_plant2.lock();
        for day in 15..=31 {
            assembly_resource_ref2.set_capacity(
                create_date(2024, 1, day),
                100.0 // Daily assembly capacity
            );
        }
        drop(assembly_resource_ref2);

        // Create demands
        let jan_31 = create_date(2024, 1, 31);
        let demand_a = Demand::new("D1".to_string(), 200.0, jan_31, 1, laptop_dc.clone());

        // Plan demands
        let dp = DemandPlanner::new();
        let result = dp.plan_demand_list(vec![demand_a.clone()], &mut specification);
        
        assert!(result.is_ok());

        // Export and verify results
        let test_name = function_name!().trim_start_matches("test_");
        PlanExporter::export_all(test_name).unwrap();
        //PlanExporter::compare_all(test_name).unwrap();
        //fs::remove_dir_all(PlanExporter::get_results_base_dir_parent(test_name)).unwrap();
    }
}