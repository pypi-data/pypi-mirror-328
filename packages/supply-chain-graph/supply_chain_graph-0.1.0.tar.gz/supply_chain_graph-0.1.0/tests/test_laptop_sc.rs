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
    use std::fs;
    use function_name::named;
    use supply::resource::Resource;
    use supply::resource_flow::ResourceFlow;
    use supply::operation::OperationVariant;
/* 
    DEMAND LEVEL (DC1)
┌────────────────────────┐              ┌────────────────────────┐
│     Laptop A DC1       │              │     Laptop B DC1       │
│                        │              │                        │
│ Demand: D1 (200 units) │              │ Demand: D2 (150 units) │
└───────────┬────────────┘              └───────────┬────────────┘
            ↑                                       ↑
            │                                       │
     ┌──────┴──────┐                        ┌──────┴──────┐
     │ Transport A │                        │ Transport B │
     │ Lead: 1 day │                        │ Lead: 1 day │
     └──────┬──────┘                        └──────┬──────┘
            │                                       │
            │                                       │
PLANT 1 LEVEL
┌────────────────────────┐              ┌────────────────────────┐
│    Laptop A Plant1     │              │    Laptop B Plant1     │
└───────────┬────────────┘              └───────────┬────────────┘
            ↑                                       ↑
            │                                       │
    ┌───────┴────────┐                    ┌────────┴───────┐
    │ Assembly A     │                    │  Assembly B    │
    │ Lead: 1 days   │                    │  Lead: 1 days  │
    └───────┬────────┘                    └────────┬───────┘
            │                                      │
            └──────────────┐           ┌──────────┘
                           ↓           ↓
            ┌─────────────────────────────────────────────┐
            │            Assembly Resource                │
            │        Capacity: 100 units/day              │
            │         (Shared between A & B)              │
            └─────────────────────────────────────────────┘

COMPONENT LEVEL (Plant 1)
┌─────────────┐   ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
│    Disk     │   │CPU Shared   │   │ Memory 8GB  │   │Memory 16GB  │
│             │   │             │   │             │   │             │
│ Inv: 1000   │   │ Inv: 250    │   │ Inv: 500    │   │ Inv: 500    │
└──────┬──────┘   └──────┬──────┘   └──────┬──────┘   └──────┬──────┘
       │                 │                  │                  │

       
┌────────────────────────────┐    ┌────────────────────────────┐
│      Laptop A BOM          │    │      Laptop B BOM          │
│  - 1x Disk                 │    │  - 1x Disk                 │
│  - 1x CPU                  │    │  - 1x CPU                  │
│  - 2x Memory 8GB           │    │  - 1x Memory 16GB          │
│  - 1x Assembly Resource    │    │  - 1x Assembly Resource    │
└────────────────────────────┘    └────────────────────────────┘

TIMING:
- Planning Horizon: Jan 15 - Jan 31, 2024
- Initial inventory available: Jan 15
- Demands due: Jan 31

CONSTRAINTS:
1. Assembly Resource Capacity: 100 units/day
2. Component Availability
   - Disk: 1000 units
   - CPU: 250 units
   - Memory 8GB: 500 units
   - Memory 16GB: 300 units

*/
    fn create_date(year: i32, month: u32, day: u32) -> NaiveDate {
        NaiveDate::from_ymd_opt(year, month, day).unwrap()
    }

    fn create_laptop_supply_chain() -> (
        // DC1 Products
        Arc<Mutex<SKU>>, // Laptop A DC1
        Arc<Mutex<SKU>>, // Laptop B DC1
        // Plant 1 Products
        Arc<Mutex<SKU>>, // Laptop A Plant1
        Arc<Mutex<SKU>>, // Laptop B Plant1
        Arc<Mutex<SKU>>, // Disk
        Arc<Mutex<SKU>>, // CPU
        Arc<Mutex<SKU>>, // Memory 8GB
        Arc<Mutex<SKU>>, // Memory 16GB
        // Resource
        Arc<Mutex<Resource>>, // Assembly Resource
        // Operations
        Arc<Mutex<Operation>>, // Laptop A Assembly
        Arc<Mutex<Operation>>, // Laptop B Assembly
        Arc<Mutex<Operation>>, // Laptop A Transport
        Arc<Mutex<Operation>>  // Laptop B Transport
    ) {
        // Create SKUs
        let laptop_a_dc1 = SKU::from_name("Laptop_A@DC1");
        let laptop_b_dc1 = SKU::from_name("Laptop_B@DC1");
        let laptop_a_plant1 = SKU::from_name("Laptop_A@Plant1");
        let laptop_b_plant1 = SKU::from_name("Laptop_B@Plant1");
        let disk = SKU::from_name("Disk@Plant1");
        let cpu = SKU::from_name("CPU@Plant1");
        let memory_8gb = SKU::from_name("Memory_8GB@Plant1");
        let memory_16gb = SKU::from_name("Memory_16GB@Plant1");
        
        // Create assembly resource
        let assembly_resource = Resource::from_name("Assemble_Laptop@Plant1");
        let assembly_resource_flow = ResourceFlow::new(1.0, assembly_resource.clone());

        // Create flows for Laptop A assembly
        let laptop_a_output = Flow::new(false, 1.0, laptop_a_plant1.clone());
        let laptop_a_components = SimultaneousFlow::new(vec![
            Flow::new(true, 1.0, disk.clone()),
            Flow::new(true, 1.0, cpu.clone()),
            Flow::new(true, 2.0, memory_8gb.clone()),
        ]);

        // Create flows for Laptop B assembly
        let laptop_b_output = Flow::new(false, 1.0, laptop_b_plant1.clone());
        let laptop_b_components = SimultaneousFlow::new(vec![
            Flow::new(true, 1.0, disk.clone()),
            Flow::new(true, 1.0, cpu.clone()),
            Flow::new(true, 1.0, memory_16gb.clone()),
        ]);

        // Create assembly operations
        let laptop_a_assembly = Operation::new(
            "Make_Laptop_A@Plant1".to_string(),
            1, // lead time
            1, // min batch
            1, // batch multiple
            MaterialFlowVariant::Single(laptop_a_output),
            MaterialFlowVariant::Simultaneous(laptop_a_components),
            ResourceFlowVariant::SingleResource(assembly_resource_flow.clone())
        );

        let laptop_b_assembly = Operation::new(
            "Make_Laptop_B@Plant1".to_string(),
            2, // lead time
            1, // min batch
            1, // batch multiple
            MaterialFlowVariant::Single(laptop_b_output),
            MaterialFlowVariant::Simultaneous(laptop_b_components),
            ResourceFlowVariant::SingleResource(assembly_resource_flow)
        );

        // Create transport operations
        let laptop_a_transport = Operation::new(
            "Move_Laptop_A-to-DC1".to_string(),
            1, // lead time
            1, // min batch
            1, // batch multiple
            MaterialFlowVariant::Single(Flow::new(false, 1.0, laptop_a_dc1.clone())),
            MaterialFlowVariant::Single(Flow::new(true, 1.0, laptop_a_plant1.clone())),
            ResourceFlowVariant::None
        );

        let laptop_b_transport = Operation::new(
            "Move_Laptop_B-to-DC1".to_string(),
            1, // lead time
            1, // min batch
            1, // batch multiple
            MaterialFlowVariant::Single(Flow::new(false, 1.0, laptop_b_dc1.clone())),
            MaterialFlowVariant::Single(Flow::new(true, 1.0, laptop_b_plant1.clone())),
            ResourceFlowVariant::None
        );

        // Set operations on SKUs
        laptop_a_dc1.lock().set_top_producing_operation(OperationVariant::Basic(laptop_a_transport.clone()));
        laptop_b_dc1.lock().set_top_producing_operation(OperationVariant::Basic(laptop_b_transport.clone()));
        laptop_a_plant1.lock().set_top_producing_operation(OperationVariant::Basic(laptop_a_assembly.clone()));
        laptop_b_plant1.lock().set_top_producing_operation(OperationVariant::Basic(laptop_b_assembly.clone()));

        (
            laptop_a_dc1, laptop_b_dc1,
            laptop_a_plant1, laptop_b_plant1,
            disk, cpu, memory_8gb, memory_16gb,
            assembly_resource,
            laptop_a_assembly, laptop_b_assembly,
            laptop_a_transport, laptop_b_transport
        )
    }

    #[test]
    #[named]
    fn test_laptop_planning() {
        SKU::clear_repository();
        Operation::clear_repository();
        Resource::clear_repository();
        Demand::clear_repository();
        let path_to_test_settings_yml = "./tests/config/settings_trace_selected_demands.yml";
        if let Err(e) = supply::logger_config::configure_logger_from_path(path_to_test_settings_yml) {
            eprintln!("Failed to configure logger: {}", e);
        }

        let (
            laptop_a_dc1, laptop_b_dc1,
            _laptop_a_plant1, _laptop_b_plant1,
            disk, cpu, memory_8gb, memory_16gb,
            assembly_resource,
            _laptop_a_assembly, _laptop_b_assembly,
            _laptop_a_transport, _laptop_b_transport
        ) = create_laptop_supply_chain();

        // Set assembly resource capacity
        let mut assembly_resource_ref = assembly_resource.lock();
        for day in 15..=31 {
            assembly_resource_ref.set_capacity(
                create_date(2024, 1, day),
                100.0 // Daily assembly capacity
            );
        }
        drop(assembly_resource_ref);

        // Add component inventory
        let jan_15 = create_date(2024, 1, 15);
        disk.lock().add_inventory(jan_15, 1000.0);
        cpu.lock().add_inventory(jan_15, 250.0); // shared between A and B
        memory_8gb.lock().add_inventory(jan_15, 500.0);
        memory_16gb.lock().add_inventory(jan_15, 500.0);

        // Create demands
        let jan_31 = create_date(2024, 1, 31);
        let demand_a = Demand::new("D1".to_string(), 200.0, jan_31, 1, laptop_a_dc1.clone());
        let demand_b = Demand::new("D2".to_string(), 150.0, jan_31, 2, laptop_b_dc1.clone());

        // Plan demands
        let dp = DemandPlanner::new();
        //let mut specification = Specification::new(2, 0);
        let mut specification = Specification::new_from_settings(2, path_to_test_settings_yml);


        //let result = dp.plan_demand_list(vec![demand_a.clone(), demand_b.clone()], &mut specification);
        let result = dp.plan_demand_list(vec![demand_a.clone(), demand_b.clone()], &mut specification);
        
        assert!(result.is_ok());

        // Export and verify results
        let test_name = function_name!().trim_start_matches("test_");
        PlanExporter::export_all(test_name).unwrap();
        PlanExporter::compare_all(test_name).unwrap();
        fs::remove_dir_all(PlanExporter::get_results_base_dir_parent(test_name)).unwrap();
    }

    #[test]
    #[named]
    fn test_laptop_sc_with_effective_periods() {
        SKU::clear_repository();
        Operation::clear_repository();
        Resource::clear_repository();
        Demand::clear_repository();

        let path_to_test_settings_yml = "./tests/config/settings_trace_selected_demands.yml";
        if let Err(e) = supply::logger_config::configure_logger_from_path(path_to_test_settings_yml) {
            eprintln!("Failed to configure logger: {}", e);
        }

        let (
            laptop_a_dc1, _laptop_b_dc1,
            _laptop_a_plant1, _laptop_b_plant1,
            disk, cpu, memory_8gb, memory_16gb,
            assembly_resource,
            laptop_a_assembly, _laptop_b_assembly,
            _laptop_a_transport, _laptop_b_transport
        ) = create_laptop_supply_chain();

        // Set assembly resource capacity
        let mut assembly_resource_ref = assembly_resource.lock();
        for day in 15..=31 {
            assembly_resource_ref.set_capacity(
                create_date(2024, 1, day),
                100.0 // Daily assembly capacity
            );
        }
        drop(assembly_resource_ref);

        // Add component inventory
        let jan_15 = create_date(2024, 1, 15);
        disk.lock().add_inventory(jan_15, 1000.0);
        cpu.lock().add_inventory(jan_15, 1000.0);
        memory_8gb.lock().add_inventory(jan_15, 1000.0);
        memory_16gb.lock().add_inventory(jan_15, 1000.0);

        // Add effective periods to operations
        let jan_15 = create_date(2024, 1, 15);
        let jan_17 = create_date(2024, 1, 17);
        let jan_19 = create_date(2024, 1, 19);
        let jan_21 = create_date(2024, 1, 21);
        laptop_a_assembly.lock().add_period(Some(jan_15), Some(jan_17), 1);
        laptop_a_assembly.lock().add_period(Some(jan_19), Some(jan_21), 1);

        // Create demands
        let jan_31 = create_date(2024, 1, 31);
        let demand_a = Demand::new("D1".to_string(), 500.0, jan_31, 1, laptop_a_dc1.clone());

        // Plan demands
        let dp = DemandPlanner::new();
        let mut specification = Specification::new(2, 0);
        //let mut specification = Specification::new_from_settings(2, path_to_test_settings_yml);
        let result = dp.plan_demand_list(vec![demand_a.clone()], &mut specification);
        
        assert!(result.is_ok());

        // Export and verify results
        let test_name = function_name!().trim_start_matches("test_");
        PlanExporter::export_all(test_name).unwrap();
        PlanExporter::compare_all(test_name).unwrap();
        fs::remove_dir_all(PlanExporter::get_results_base_dir_parent(test_name)).unwrap();
    }


    #[test]
    #[named]
    fn test_laptop_planning_multiple_capacity_days() {
        SKU::clear_repository();
        Operation::clear_repository();
        Resource::clear_repository();
        Demand::clear_repository();
        let path_to_test_settings_yml = "./tests/config/settings_trace_selected_demands.yml";
        if let Err(e) = supply::logger_config::configure_logger_from_path(path_to_test_settings_yml) {
            eprintln!("Failed to configure logger: {}", e);
        }

        let (
            laptop_a_dc1, _laptop_b_dc1,
            _laptop_a_plant1, _laptop_b_plant1,
            disk, cpu, memory_8gb, memory_16gb,
            assembly_resource,
            _laptop_a_assembly, _laptop_b_assembly,
            _laptop_a_transport, _laptop_b_transport
        ) = create_laptop_supply_chain();

        // Set assembly resource capacity. For each demand multiple capacity periods are needed.
        // Resize of the op plan would also be needed
        let mut assembly_resource_ref = assembly_resource.lock();
        for day in 15..=31 {
            assembly_resource_ref.set_capacity(
                create_date(2024, 1, day),
                100.0 // Daily assembly capacity
            );
        }
        drop(assembly_resource_ref);

        // Add sufficient component inventory
        let jan_15 = create_date(2024, 1, 15);
        disk.lock().add_inventory(jan_15, 5000.0);
        cpu.lock().add_inventory(jan_15, 5000.0);
        memory_8gb.lock().add_inventory(jan_15, 5000.0);
        memory_16gb.lock().add_inventory(jan_15, 5000.0);

        // Create demands only on laptop_a_dc1
        let jan_31 = create_date(2024, 1, 31);
        let demand_a1 = Demand::new("D1".to_string(), 225.0, jan_31, 1, laptop_a_dc1.clone());
        let demand_a2 = Demand::new("D2".to_string(), 225.0, jan_31, 2, laptop_a_dc1.clone());
        let demand_a3 = Demand::new("D3".to_string(), 225.0, jan_31, 3, laptop_a_dc1.clone());

        // Plan demands
        let dp = DemandPlanner::new();
        let mut specification = Specification::new_from_settings(2, path_to_test_settings_yml);
        
        let result = dp.plan_demand_list(vec![demand_a1.clone(), demand_a2.clone(), demand_a3.clone()], &mut specification);
        
        assert!(result.is_ok());

        // Export and verify results
        let test_name = function_name!().trim_start_matches("test_");
        PlanExporter::export_all(test_name).unwrap();
        PlanExporter::compare_all(test_name).unwrap();
        fs::remove_dir_all(PlanExporter::get_results_base_dir_parent(test_name)).unwrap();
    }
}