// Command to run all tests
// cargo test --release 
// Command to run a specific test
// cargo test --release --test demand_planner_tests test_plan_quality -- --nocapture
// RUST_LOG=info cargo test --release --test test_demand_planning test_two_level_with_resource -- --nocapture
// RUST_LOG=info cargo test --release --test demand_planner_tests test_car_psr_constrained_planning -- --nocapture

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
    use log::info;
    use supply::utilities::memory::get_memory_usage;
    use std::sync::Arc;
    use parking_lot::Mutex;
    use supply::reports::plan_exporter::PlanExporter;
    use std::fs;
    use function_name::named;
    use supply::resource::Resource;
    use supply::resource_flow::ResourceFlow;
    use supply::operation::OperationVariant;
    use serial_test::serial;
    
    fn create_date(year: i32, month: u32, day: u32) -> NaiveDate {
        NaiveDate::from_ymd_opt(year, month, day).unwrap()
    }

    // Common test utilities
    struct TestUtils;
    
    impl TestUtils {
        fn setup_logger(path: Option<&str>) {
            let result = match path {
                Some(p) => supply::logger_config::configure_logger_from_path(p),
                None => supply::logger_config::configure_logger()
            };
            if let Err(e) = result {
                eprintln!("Failed to configure logger: {}", e);
            }
        }

        fn create_dates() -> (NaiveDate, NaiveDate, NaiveDate) {
            let jan_15 = create_date(2024, 1, 15);
            let jan_27 = create_date(2024, 1, 27);
            let jan_31 = create_date(2024, 1, 31);
            (jan_15, jan_27, jan_31)
        }

        fn setup_basic_inventory(
            _car: &Arc<Mutex<SKU>>,
            tyre: &Arc<Mutex<SKU>>,
            body: &Arc<Mutex<SKU>>,
            engine: &Arc<Mutex<SKU>>,
            seat: &Arc<Mutex<SKU>>,
            date: NaiveDate
        ) {
            tyre.lock().add_inventory(date, 2000.0);
            body.lock().add_inventory(date, 100.0);
            engine.lock().add_inventory(date, 200.0);
            seat.lock().add_inventory(date, 1000000.0);
        }

        fn create_planner_and_spec(trace_level: i32, settings_path: Option<&str>) -> (DemandPlanner, Specification) {
            let dp = DemandPlanner::new();
            let spec = match settings_path {
                Some(path) => Specification::new_from_settings(trace_level, path),
                None => Specification::new(trace_level, 0)
            };
            (dp, spec)
        }
    }

    fn create_car_supply_chain() -> 
        (Arc<Mutex<SKU>>, Arc<Mutex<SKU>>, Arc<Mutex<SKU>>, Arc<Mutex<SKU>>, Arc<Mutex<SKU>>, Arc<Mutex<Operation>>, Arc<Mutex<Operation>>) {
        // Create products
        let car = SKU::from_name("Car");
        let tyre = SKU::from_name("Tyre");
        let body = SKU::from_name("Body");
        let engine = SKU::from_name("Engine");
        let seat = SKU::from_name("Seat");

        // Create flows for car assembly
        let tyre_flow = Flow::new(true, 4.0, tyre.clone());
        let body_flow = Flow::new(true, 1.0, body.clone());
        let car_flow = Flow::new(false, 1.0, car.clone());

        // Create flows for body assembly
        let engine_flow = Flow::new(true, 1.0, engine.clone());
        let seat_flow = Flow::new(true, 5.0, seat.clone());
        let body_output_flow = Flow::new(false, 1.0, body.clone());

        // Create simultaneous flows
        let car_sim_flow = SimultaneousFlow::new(vec![tyre_flow, body_flow]);
        let body_sim_flow = SimultaneousFlow::new(vec![engine_flow, seat_flow]);
        
        // Create operations
        let car_assembly = Operation::new(
            "Car Assembly".to_string(),
            2,
            1,
            1,
            MaterialFlowVariant::Single(car_flow),
            MaterialFlowVariant::Simultaneous(car_sim_flow),
            ResourceFlowVariant::None
        );

        let body_assembly = Operation::new(
            "Body Assembly".to_string(),
            3,
            1,
            1,
            MaterialFlowVariant::Single(body_output_flow),
            MaterialFlowVariant::Simultaneous(body_sim_flow),
            ResourceFlowVariant::None
        );

        // Set operations on SKUs
        car.lock().set_top_producing_operation(OperationVariant::Basic(car_assembly.clone()));
        body.lock().set_top_producing_operation(OperationVariant::Basic(body_assembly.clone()));

        (car, tyre, body, engine, seat, car_assembly, body_assembly)
    }


    fn create_2_level_car_supply_chain_with_resources() -> 
        (Arc<Mutex<SKU>>, Arc<Mutex<SKU>>, Arc<Mutex<SKU>>, Arc<Mutex<Resource>>, Arc<Mutex<Operation>>) {
            let car = SKU::from_name("Car");
            let tyre = SKU::from_name("Tyre");
            let body = SKU::from_name("Body");
            let carcapacity = Resource::from_name("CarCapacity");
            // Create flows for car assembly
            let tyre_flow = Flow::new(true, 4.0, tyre.clone());
            let body_flow = Flow::new(true, 1.0, body.clone());
            let car_flow = Flow::new(false, 1.0, car.clone());  
            let car_capacity_flow = ResourceFlow::new(1.0, carcapacity.clone());

            let car_sim_flow = SimultaneousFlow::new(vec![tyre_flow, body_flow]);

            let car_assembly = Operation::new(
                "Car Assembly".to_string(), 
                2, 
                1, 
                1, 
                MaterialFlowVariant::Single(car_flow), 
                MaterialFlowVariant::Simultaneous(car_sim_flow), 
                ResourceFlowVariant::SingleResource(car_capacity_flow)
            );
            // Set operation on car SKU
            car.lock().set_top_producing_operation(OperationVariant::Basic(car_assembly.clone()));
            (car, tyre, body, carcapacity, car_assembly)
    }

    // Add this helper function
    fn clean_all_repositories() {
        Operation::clear_repository();
        SKU::clear_repository();
        Demand::clear_repository();
    }
    
    #[test]
    #[serial]
    fn test_basic_planning() {
        clean_all_repositories();
        TestUtils::setup_logger(None);
        let start_time = std::time::Instant::now();

        let (car, tyre, body, engine, seat, _, _) = create_car_supply_chain();
        let (jan_15, jan_27, jan_31) = TestUtils::create_dates();

        car.lock().inventory_profile().add_inventory(jan_27, 150.0);
        TestUtils::setup_basic_inventory(&car, &tyre, &body, &engine, &seat, jan_15);

        let (dp, mut specification) = TestUtils::create_planner_and_spec(2, None);
        
        let demand = Demand::new("D1".to_string(), 250.0, jan_31, 0, car.clone());
        let result = dp.plan(demand.clone(), &mut specification);
        assert!(result.is_ok());

        let duration = start_time.elapsed();
        info!("Time taken to create model and plan demands: {:?}", duration);
        info!("End of planning");
    }

    #[test]
    #[serial]
    fn test_planning_with_operations() {
        clean_all_repositories();
        TestUtils::setup_logger(None);
        let start_time = std::time::Instant::now();
        // Clear any existing demands from previous tests
        Demand::clear_repository();

        let (car, tyre, body, _, _, _, _) = create_car_supply_chain();
        let (jan_15, _, jan_31) = TestUtils::create_dates();

        // Add inventory for components
        tyre.lock().add_inventory(jan_15, 500.0);
        body.lock().add_inventory(jan_15, 150.0);
        car.lock().add_inventory(jan_15, 100.0);

        // Create planner and specification
        let dp = DemandPlanner::new();
        let mut specification = Specification::new(2, 0);

        // Create demand for 200 cars
        let demand = Demand::new(
            "D2".to_string(),
            200.0,
            jan_31,
            0,
            car.clone()
        );

        // Plan demand
        let result = dp.plan(demand.clone(), &mut specification);
        assert!(result.is_ok());

        // Verify the results
        let demand_ref = demand.lock();
        let plans = &demand_ref.demand_plans;
        assert!(!plans.is_empty(), "Should have created at least one plan");
        
        let total_planned = plans.iter().map(|p| p.get_quantity()).sum::<f64>();
        assert!(total_planned <= 200.0, "Should not plan more than demanded");
        assert!(total_planned > 0.0, "Should plan some quantity");

        let duration = start_time.elapsed();
        info!("Time taken to create model and plan demands: {:?}", duration);
        info!("End of planning with operations");
    }

    #[test]
    #[serial]
    fn test_car_psr_constrained_planning() {
        clean_all_repositories();
        let path_to_test_settings_yml = "./config/settings.yml";
        TestUtils::setup_logger(Some(path_to_test_settings_yml));
        let start_time = std::time::Instant::now();
        info!("Initial memory usage:\n{}", get_memory_usage());
        
        // Clear any existing demands from previous tests
        Demand::clear_repository();
        
        // Create supply chain
        let (car, tyre, body, engine, seat, car_assembly, body_assembly) = create_car_supply_chain();

        // Create dates
        let jan_15 = create_date(2024, 1, 15);
        let jan_31 = create_date(2024, 1, 31);

        // Create multiple demands
        let num_demands = 1000000;
        let demand_qty = 200.0;

        // Create multiple demands using the repository
        for i in 0..num_demands {
            let demand = Demand::new(
                format!("D{}", i + 1),
                demand_qty,
                jan_31,
                0,
                car.clone()
            );
            demand.lock().set_priority(i as i32);
        }

        // Add initial inventory
        tyre.lock().add_inventory(jan_15, 1000.0);
        body.lock().add_inventory(jan_15, 50.0);
        engine.lock().add_inventory(jan_15, 50.0);
        seat.lock().add_inventory(jan_15, 500.0);
        car.lock().add_inventory(jan_15, 50.0);

        info!("Memory usage after model and demand creation:\n{}", get_memory_usage());

        // Create planner and specification
        let dp = DemandPlanner::new();
        let mut specification = Specification::new_from_settings(2, path_to_test_settings_yml);

        // Get all demands from repository and sort them
        let mut all_demands = Demand::get_all_demands();
        all_demands.sort_by(|a, b| {
            let a_priority = a.lock().get_priority();
            let b_priority = b.lock().get_priority();
            a_priority.cmp(&b_priority)
        });

        // Plan all demands
        let mut total_planned_quantity = 0.0;
        for (i, demand) in all_demands.iter().enumerate() {
            let result = dp.plan(demand.clone(), &mut specification);
            assert!(result.is_ok(), "Failed to plan demand {}", i + 1);

            // Verify each demand's results
            let demand_ref = demand.lock();
            let plans = &demand_ref.demand_plans;
            assert!(!plans.is_empty(), "Should have created at least one plan for demand {}", i + 1);
            
            let demand_planned = plans.iter().map(|p| p.get_quantity()).sum::<f64>();
            total_planned_quantity += demand_planned;
            assert!(demand_planned <= demand_qty, "Should not plan more than demanded for demand {}", i + 1);
        }
        
        let duration = start_time.elapsed();

        // Check operation plans
        let car_assembly_ref = car_assembly.lock();
        let body_assembly_ref = body_assembly.lock();
        let car_op_plans = car_assembly_ref.get_all_operation_plans();
        let body_op_plans = body_assembly_ref.get_all_operation_plans();
        
        // Print op plans
        for op_plan in car_op_plans {
            info!("Car Assembly Plan: {}", op_plan.get_quantity());
        }
        for op_plan in body_op_plans {
            info!("Body Assembly Plan: {}", op_plan.get_quantity());
        }

        info!("Number of car assembly operation plans: {}", car_op_plans.len());
        info!("Number of body assembly operation plans: {}", body_op_plans.len());
        
        info!("\nCar Assembly Plans Total Quantity: {}", 
            car_op_plans.iter().map(|p| p.get_quantity()).sum::<f64>());
        info!("Body Assembly Plans Total Quantity: {}", 
            body_op_plans.iter().map(|p| p.get_quantity()).sum::<f64>());

        // Final statistics
        info!("Final memory usage:\n{}", get_memory_usage());
        info!("Time taken Demand Planning: {:.6} seconds", duration.as_secs_f64());
        info!("Time taken: {} nanoseconds", duration.as_nanos());
        info!("Total quantity planned across all demands: {}", total_planned_quantity);
        info!("Average quantity planned per demand: {}", total_planned_quantity / num_demands as f64);
        info!("-----------------------------------------------------");
    }

    #[test]
    #[serial]
    fn test_car_psr_unconstrained_planning() {
        clean_all_repositories();
        // Define config path relative to project root
        let path_to_test_settings_yml = "./config/settings.yml";
        if let Err(e) = supply::logger_config::configure_logger_from_path(path_to_test_settings_yml) {
            eprintln!("Failed to configure logger: {}", e);
        }
        let start_time = std::time::Instant::now();
        info!("Initial memory usage:\n{}", get_memory_usage());
        // Clear any existing demands from previous tests
        Demand::clear_repository();
        // Create supply chain
        let (car, tyre, _body, engine, seat, car_assembly, body_assembly) = create_car_supply_chain();

        // Create dates
        let jan_15 = NaiveDate::from_ymd_opt(2024, 1, 15).unwrap();
        let jan_31 = NaiveDate::from_ymd_opt(2024, 1, 31).unwrap();

        // Create multiple demands
        let num_demands = 1000000;
        let demand_qty = 200.0;

        // Create multiple demands using the repository
        for i in 0..num_demands {
            let demand = Demand::new(format!("D{}", i + 1), demand_qty, jan_31, 0, car.clone());
            demand.lock().set_priority(i as i32);
        }
        // Add initial inventory
        tyre.lock().add_inventory(jan_15, f64::INFINITY);
        engine.lock().add_inventory(jan_15, f64::INFINITY);
        seat.lock().add_inventory(jan_15, f64::INFINITY);

        // After creating demands
        info!("Memory usage after model and demand creation:\n{}", get_memory_usage());

        // Log duration and results
        let duration = start_time.elapsed();
        info!("Time taken Demand List Creation : {:.6} seconds", duration.as_secs_f64());

        // Create planner and specification
        let dp = DemandPlanner::new();
        let mut specification = Specification::new_from_settings(2, path_to_test_settings_yml);

        // Get all demands from repository and sort them
        let mut all_demands = Demand::get_all_demands();
        all_demands.sort_by(|a, b| {
            let a_priority = a.lock().get_priority();
            let b_priority = b.lock().get_priority();
            a_priority.cmp(&b_priority)
        });

        // Plan all demands
        let mut total_planned_quantity = 0.0;
        for (i, demand) in all_demands.iter().enumerate() {
            specification.set_current_demand_id(i as i32);
            if specification.get_trace_level() >= 1 {
                info!("Planning demand {} of {}", i + 1, num_demands);
            }
            let result = dp.plan(demand.clone(), &mut specification);
            assert!(result.is_ok(), "Failed to plan demand {}", i + 1);

            // Verify each demand's results
            let demand_ref = demand.lock();
            let plans = &demand_ref.demand_plans;
            assert!(!plans.is_empty(), "Should have created at least one plan for demand {}", i + 1);
            
            let demand_planned = plans.iter().map(|p| p.get_quantity()).sum::<f64>();
            total_planned_quantity += demand_planned;
            assert!(demand_planned <= demand_qty, "Should not plan more than demanded for demand {}", i + 1);
        }

        let duration = start_time.elapsed();

        // check count of operation plans
        let car_assembly_ref = car_assembly.lock();
        let body_assembly_ref = body_assembly.lock();
        let car_op_plans = car_assembly_ref.get_all_operation_plans();
        let body_op_plans = body_assembly_ref.get_all_operation_plans();
        
        info!("Number of car assembly operation plans: {}", car_op_plans.len());
        info!("Number of body assembly operation plans: {}", body_op_plans.len());
        
        info!("\nCar Assembly Plans Total Quantity: {}", 
            car_op_plans.iter().map(|p| p.get_quantity()).sum::<f64>());
        info!("Body Assembly Plans Total Quantity: {}", 
            body_op_plans.iter().map(|p| p.get_quantity()).sum::<f64>());


        car_assembly_ref.print_operation_plans();
        body_assembly_ref.print_operation_plans();


        // Final statistics
        info!("Final memory usage:\n{}", get_memory_usage());
        info!("Time taken Demand Planning: {:.6} seconds", duration.as_secs_f64());
        info!("Time taken: {} nanoseconds", duration.as_nanos());
        info!("Total quantity planned across all demands: {}", total_planned_quantity);
        info!("Average quantity planned per demand: {}", total_planned_quantity / num_demands as f64);
        info!("-----------------------------------------------------");
    } 


    #[test]
    #[serial]
    #[named]
    fn test_car_sc_constrained_planning() {
        clean_all_repositories();
        let path_to_test_settings_yml = "./tests/config/settings_trace_selected_demands.yml";
        if let Err(e) = supply::logger_config::configure_logger_from_path(path_to_test_settings_yml) {
            eprintln!("Failed to configure logger: {}", e);
        }
        let (car, tyre, _body, engine, seat, _car_assembly, _body_assembly) = create_car_supply_chain();

        // Create dates
        let jan_15 = NaiveDate::from_ymd_opt(2024, 1, 15).unwrap();
        let jan_30 = NaiveDate::from_ymd_opt(2024, 1, 30).unwrap();
        let jan_31 = NaiveDate::from_ymd_opt(2024, 1, 31).unwrap();

        let dp = DemandPlanner::new();
        let mut specification = Specification::new_from_settings(2, path_to_test_settings_yml);


        let demand1 = Demand::new("D1".to_string(), 80.0, jan_31, 0, car.clone());
        demand1.lock().set_priority(1);
        let demand2 = Demand::new("D2".to_string(), 50.0, jan_30, 0, car.clone());
        demand2.lock().set_priority(2);

        seat.lock().add_inventory(jan_15, 500.0);
        tyre.lock().add_inventory(jan_15, 10000.0);
        engine.lock().add_inventory(jan_15, 10000.0);

        let _ = dp.plan_demand_list(vec![demand1.clone(), demand2.clone()], &mut specification);

        let test_name = function_name!().trim_start_matches("test_");
        PlanExporter::export_all(test_name).unwrap();
        PlanExporter::compare_all(test_name).unwrap();
        fs::remove_dir_all(PlanExporter::get_results_base_dir_parent(test_name)).unwrap();
    }


    #[test]
    #[serial]
    #[named]
    fn test_two_level_with_resource() {
        clean_all_repositories();
        let path_to_test_settings_yml = "./config/settings.yml";
        if let Err(e) = supply::logger_config::configure_logger_from_path(path_to_test_settings_yml) {
            eprintln!("Failed to configure logger: {}", e);
        }
        let (car, tyre, body, car_capacity, _car_assembly) = create_2_level_car_supply_chain_with_resources();
        let mut specification = Specification::new(2, 0);

        // Set capacity using a single mutable reference
        let mut car_capacity_ref = car_capacity.lock();
        car_capacity_ref.set_capacity(create_date(2024, 1, 15), 100.0);
        car_capacity_ref.set_capacity(create_date(2024, 1, 16), 100.0);
        car_capacity_ref.set_capacity(create_date(2024, 1, 17), 200.0);
        car_capacity_ref.set_capacity(create_date(2024, 1, 18), 200.0);
        car_capacity_ref.set_capacity(create_date(2024, 1, 19), 200.0);
        car_capacity_ref.set_capacity(create_date(2024, 1, 20), 200.0);
        // 21s onwards there is no capacity
        car_capacity_ref.set_capacity(create_date(2024, 1, 21), 0.0);
        // Drop the mutable reference
        drop(car_capacity_ref);

        body.lock().add_inventory(create_date(2024, 1, 15), 1000.0);
        tyre.lock().add_inventory(create_date(2024, 1, 15), 4000.0);

        let dp = DemandPlanner::new();
        let demand = Demand::new("D1".to_string(), 300.0, NaiveDate::from_ymd_opt(2024, 1, 31).unwrap(), 0, car.clone());
        let result = dp.plan(demand.clone(), &mut specification);
        assert!(result.is_ok());

        let test_name = function_name!().trim_start_matches("test_");
        PlanExporter::export_all(test_name).unwrap();
        PlanExporter::compare_all(test_name).unwrap();
        fs::remove_dir_all(PlanExporter::get_results_base_dir_parent(test_name)).unwrap();
    }



    #[test]
    #[serial]
    #[named]
    fn test_lot_sized_car_sc_basic_1() {
        clean_all_repositories();
        // lot sized car assembly with no inventory on the car
        let path_to_test_settings_yml = "./config/settings.yml";
        TestUtils::setup_logger(Some(path_to_test_settings_yml));
        
        // Clear repository before test
        Demand::clear_repository();
        
        let (car, tyre, _body, engine, seat, car_assembly, _body_assembly) = create_car_supply_chain();
        let mut specification = Specification::new(2, 0);
        
        let jan_15 = create_date(2024, 1, 15);
        let jan_31 = create_date(2024, 1, 31);
        
        seat.lock().add_inventory(jan_15, 5000.0);
        tyre.lock().add_inventory(jan_15, 4000.0);
        engine.lock().add_inventory(jan_15, 1000.0);

        // Set lot size parameters
        car_assembly.lock().set_min_lot(50);
        car_assembly.lock().set_increment(20);

        let dp = DemandPlanner::new();
        let demand = Demand::new("D1".to_string(), 75.0, jan_31, 0, car.clone());
        let result = dp.plan(demand.clone(), &mut specification);
        assert!(result.is_ok());
        
        let demand_ref = demand.lock();
        let plans = &demand_ref.demand_plans;
        let demand_planned = plans.iter().map(|p| p.get_quantity()).sum::<f64>();
        assert!(demand_planned == 75.0);

        let car_inventory = car.lock().get_inventory_profile().get_net_inventory(&jan_31);
        assert!(car_inventory == 15.0);

        let car_assembly_ref = car_assembly.lock();
        let car_op_plans = car_assembly_ref.get_all_operation_plans();
        assert!(car_op_plans.len() == 1);
        assert!(car_op_plans[0].get_quantity() == 90.0);
        drop(car_assembly_ref);

        let test_name = function_name!().trim_start_matches("test_");
        PlanExporter::export_all(test_name).unwrap();
        PlanExporter::compare_all(test_name).unwrap();
        fs::remove_dir_all(PlanExporter::get_results_base_dir_parent(test_name)).unwrap();
    }


    #[test]
    #[serial]
    #[named]
    fn test_lot_sized_car_sc_basic_2() {
        clean_all_repositories();
        // lot sized car assembly with some incentory on the car
        let path_to_test_settings_yml = "./config/settings.yml";
        if let Err(e) = supply::logger_config::configure_logger_from_path(path_to_test_settings_yml) {
            eprintln!("Failed to configure logger: {}", e);
        }
        let (car, tyre, _body, engine, seat, car_assembly, _body_assembly) =   create_car_supply_chain();
        let mut specification = Specification::new(2, 0);
        seat.lock().add_inventory(create_date(2024, 1, 15), 5000.0);
        tyre.lock().add_inventory(create_date(2024, 1, 15), 4000.0);
        engine.lock().add_inventory(create_date(2024, 1, 15), 1000.0);
        car.lock().add_inventory(create_date(2024, 1, 15), 10.0);

        let mut car_assembly_ref = car_assembly.lock();
        car_assembly_ref.set_min_lot(50);
        car_assembly_ref.set_increment(20);
        drop(car_assembly_ref);

        let dp = DemandPlanner::new();
        let demand = Demand::new("D1".to_string(), 75.0, NaiveDate::from_ymd_opt(2024, 1, 31).unwrap(), 0, car.clone());
        let result = dp.plan(demand.clone(), &mut specification);
        assert!(result.is_ok());
        let demand_ref = demand.lock();
        let plans = &demand_ref.demand_plans;
        let demand_planned = plans.iter().map(|p| p.get_quantity()).sum::<f64>();
        assert!(demand_planned == 75.0);

        let car_inventory = car.lock().get_inventory_profile().get_net_inventory(&create_date(2024, 1, 31));
        assert!(car_inventory == 5.0);

        let car_assembly_ref = car_assembly.lock();
        let car_op_plans = car_assembly_ref.get_all_operation_plans();
        assert!(car_op_plans.len() == 1);
        assert!(car_op_plans[0].get_quantity() == 70.0);
        drop(car_assembly_ref);

        let test_name = function_name!().trim_start_matches("test_");
        PlanExporter::export_all(test_name).unwrap();
        PlanExporter::compare_all(test_name).unwrap();
        fs::remove_dir_all(PlanExporter::get_results_base_dir_parent(test_name)).unwrap();
    }


    #[test]
    #[serial]
    #[named]
    fn test_multiple_lot_sized_car_sc_with_capacity() {
        clean_all_repositories();
        // lot sized car assembly with some inventory on the car and a resource on body assembly with a lot size enabled
        let path_to_test_settings_yml = "./config/settings.yml";
        if let Err(e) = supply::logger_config::configure_logger_from_path(path_to_test_settings_yml) {
            eprintln!("Failed to configure logger: {}", e);
        }
        let (car, tyre, body, engine, seat, car_assembly, body_assembly) =   create_car_supply_chain();
        let mut specification = Specification::new(2, 0);
        seat.lock().add_inventory(create_date(2024, 1, 15), 5000.0);
        tyre.lock().add_inventory(create_date(2024, 1, 15), 4000.0);
        engine.lock().add_inventory(create_date(2024, 1, 15), 1000.0);
        car.lock().add_inventory(create_date(2024, 1, 15), 10.0);


        let mut car_assembly_ref = car_assembly.lock();
        car_assembly_ref.set_min_lot(50);
        car_assembly_ref.set_increment(20);
        drop(car_assembly_ref);

        let carcapacity = Resource::from_name("CarCapacity");
        carcapacity.lock().set_capacity(create_date(2024, 1, 19), 200.0);
        carcapacity.lock().set_capacity(create_date(2024, 1, 20), 200.0);
        carcapacity.lock().set_capacity(create_date(2024, 1, 21), 0.0);
        let car_capacity_flow = ResourceFlow::new(1.0, carcapacity.clone());
        body_assembly.lock().set_resource_flow(ResourceFlowVariant::SingleResource(car_capacity_flow));

        let mut body_assembly_ref = body_assembly.lock();
        body_assembly_ref.set_min_lot(150);
        body_assembly_ref.set_increment(20);
        drop(body_assembly_ref);


        let dp = DemandPlanner::new();
        let demand = Demand::new("D1".to_string(), 75.0, NaiveDate::from_ymd_opt(2024, 1, 31).unwrap(), 0, car.clone());
        let result = dp.plan(demand.clone(), &mut specification);
        assert!(result.is_ok());
        let demand_ref = demand.lock();
        let plans = &demand_ref.demand_plans;
        let demand_planned = plans.iter().map(|p| p.get_quantity()).sum::<f64>();
        assert!(demand_planned == 75.0);

        let car_inventory = car.lock().get_inventory_profile().get_net_inventory(&create_date(2024, 1, 31));
        assert!(car_inventory == 5.0);

        let mut body_inventory = body.lock().get_inventory_profile().get_net_inventory(&create_date(2024, 1, 23));
        assert!(body_inventory == 150.0);
        body_inventory = body.lock().get_inventory_profile().get_net_inventory(&create_date(2024, 1, 29));
        assert!(body_inventory == 80.0);

        let test_name = function_name!().trim_start_matches("test_");
        PlanExporter::export_all(test_name).unwrap();
        PlanExporter::compare_all(test_name).unwrap();
        fs::remove_dir_all(PlanExporter::get_results_base_dir_parent(test_name)).unwrap();
    }


    
}