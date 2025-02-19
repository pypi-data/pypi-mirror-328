use std::sync::Arc;
use parking_lot::Mutex;
use log::info;

use crate::demand::Demand;
use crate::quantity_date::QuantityDate;
use crate::plan_proposal::ProposalStack;
use crate::specification::Specification;
use crate::planner::{choose_planner, PlannerType};
use crate::motivator::Motivator;

pub struct DemandPlanner {
}

impl DemandPlanner {
    pub fn new() -> Self {
        DemandPlanner {}
    }

    pub fn plan_demand_list(&self, demands: Vec<Arc<Mutex<Demand>>>, specification: &mut Specification) -> Result<(), String> {
        let mut demand_id = 0;
        for demand in demands {
            specification.set_current_demand_id(demand_id);
            let _ = self.plan(demand, specification);
            demand_id += 1;
        }
        Ok(())
    }

    pub fn plan(&self, demand: Arc<Mutex<Demand>>, specification: &mut Specification) -> Result<(), String> {
        let demand_ref = demand.lock();

        if specification.get_trace_level() >= 1 {
            info!("Begin Planning Demand Id: {:?} for Quantity: {:?} on Date: {:?}", 
                demand_ref.get_id(), 
                demand_ref.get_quantity(), 
                demand_ref.get_request_date()
            );
        }
        
        // Check if SKU exists
        if demand_ref.get_sku().lock().name().is_empty() {
            return Err(format!("Demand {:?} does not have an associated SKU", demand_ref.get_id()));
        }
        
        let mut proposals = ProposalStack::new();
        let planner = choose_planner(PlannerType::SKU(demand_ref.get_sku().clone()));
        let request_date = *demand_ref.get_request_date();
        let mut demand_motivator = Motivator::DemandMotive(demand.clone());
        let available_qty = planner.ask(demand_ref.get_quantity(), request_date, &mut proposals, specification, &mut demand_motivator);
        
        drop(demand_ref); // Release the lock before modifying demand
        
        // Add the available quantity to demand plans
        let mut demand_ref = demand.lock();
        demand_ref.demand_plans.push(QuantityDate::new(available_qty, request_date));
        proposals.create_operation_plans();
        
        if specification.get_trace_level() >= 1 {
            info!("Planned Demand for: {}", available_qty);
        }
        
        Ok(())
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use chrono::NaiveDate;
    use crate::simultaneous_flow::SimultaneousFlow;
    use crate::sku::SKU;
    use crate::operation::Operation;
    use crate::flow::Flow;
    use crate::operation::MaterialFlowVariant;
    use crate::logger_config;
    use crate::operation::ResourceFlowVariant;
    use crate::operation::OperationVariant;
    use serial_test::serial;

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
        if let Err(e) = logger_config::configure_logger() {
            eprintln!("Failed to configure logger: {}", e);
        }

        let start_time = std::time::Instant::now();

        // Create products
        let car = SKU::from_name("Car");
        let tyre = SKU::from_name("Tyre");
        let body = SKU::from_name("Body");
        let engine = SKU::from_name("Engine");
        let seat = SKU::from_name("Seat");

        // Create dates
        let jan_15 = NaiveDate::from_ymd_opt(2024, 1, 15).unwrap();
        let jan_27 = NaiveDate::from_ymd_opt(2024, 1, 27).unwrap();
        let jan_31 = NaiveDate::from_ymd_opt(2024, 1, 31).unwrap();

        // Create demand
        let demand = Demand::new(
            "D1".to_string(),
            250.0,
            jan_31,
            0,
            car.clone()
        );

        // Setup flows and operations
        {
            let mut car_ref = car.lock();
            let mut tyre_ref = tyre.lock();
            let mut body_ref = body.lock();
            let mut seat_ref = seat.lock();
            let mut engine_ref = engine.lock();

            // Add inventory
            car_ref.add_inventory(jan_27, 150.0);
            tyre_ref.add_inventory(jan_15, 2000.0);
            body_ref.add_inventory(jan_15, 100.0);
            seat_ref.add_inventory(jan_15, 1000000.0);
            engine_ref.add_inventory(jan_15, 200.0);
        }

        // Create planner and specification
        let dp = DemandPlanner::new();
        let mut specification = Specification::new(2, 0);

        // Plan demand
        let result = dp.plan(demand.clone(), &mut specification);
        assert!(result.is_ok());

        // Log duration
        let duration = start_time.elapsed();
        info!("Time taken to create model and plan demands: {:?}", duration);
        info!("End of planning");
        clean_all_repositories();
    }

    #[test]
    #[serial]
    fn test_planning_with_operations() {
        clean_all_repositories();
        if let Err(e) = logger_config::configure_logger() {
            eprintln!("Failed to configure logger: {}", e);
        }

        let start_time = std::time::Instant::now();

        // Create products
        let car = SKU::from_name("Car");
        let tyre = SKU::from_name("Tyre");
        let body = SKU::from_name("Body");

        // Create dates
        let jan_15 = NaiveDate::from_ymd_opt(2024, 1, 15).unwrap();
        let jan_31 = NaiveDate::from_ymd_opt(2024, 1, 31).unwrap();

        // Create flows
        let tyre_flow = Flow::new(true, 4.0, tyre.clone()); // 4 tyres per car
        let body_flow = Flow::new(true, 1.0, body.clone()); // 1 body per car
        let car_flow = Flow::new(false, 1.0, car.clone()); // 1 car produced

        // Create simultaneous flow for consuming components
        let sim_flow = SimultaneousFlow::new(vec![tyre_flow, body_flow]);
        
        // Create car assembly operation with simultaneous consuming flow
        let car_assembly = Operation::new(
            "Car Assembly".to_string(),
            2,
            1,
            1,
            MaterialFlowVariant::Single(car_flow),
            MaterialFlowVariant::Simultaneous(sim_flow),
            ResourceFlowVariant::None
        );

        // Add operation to car SKU
        {
            let mut car_ref = car.lock();
            car_ref.set_top_producing_operation(OperationVariant::Basic(car_assembly.clone()));

            // Add effectivity period to car SKU
            let jan_26 = NaiveDate::from_ymd_opt(2024, 1, 26).unwrap();
            car_assembly.lock().add_period(Some(jan_15), Some(jan_26), 1);
        }

        // Create demand for 100 cars
        let demand_qty = 200.0;
        let demand = Demand::new("D2".to_string(), demand_qty, jan_31, 0, car.clone());

        // Add inventory for components
        {
            let mut tyre_ref = tyre.lock();
            let mut body_ref = body.lock();
            let mut car_ref = car.lock();

            tyre_ref.inventory_profile().add_inventory(jan_15, 500.0);
            body_ref.inventory_profile().add_inventory(jan_15, 150.0);
            car_ref.inventory_profile().add_inventory(jan_15, 100.0);
        }

        // Create planner and specification
        let dp = DemandPlanner::new();
        let mut specification = Specification::new(2, 0);

        // Plan demand
        let result = dp.plan(demand.clone(), &mut specification);
        assert!(result.is_ok());

        // Log duration
        let duration = start_time.elapsed();
        info!("Time taken to create model and plan demands: {:?}", duration);

        // Verify the results
        let demand_ref = demand.lock();
        let plans = &demand_ref.demand_plans;
        assert!(!plans.is_empty(), "Should have created at least one plan");
        
        // The planned quantity should be limited by either tyres/4 or bodies
        let total_planned = plans.iter().map(|p| p.get_quantity()).sum::<f64>();
        assert!(total_planned == demand_qty, "Should not plan more than demanded");
        assert!(total_planned > 0.0, "Should plan some quantity");

        let jan_25 = NaiveDate::from_ymd_opt(2024, 1, 25).unwrap();
        let op_ref = car_assembly.lock();
        let op_plans = op_ref.get_operation_plans();
        
        let has_jan_25_plan = op_plans.iter().any(|plan| {
            plan.get_start_date() == jan_25
        });
        assert!(has_jan_25_plan, "Should have created an operation plan on January 25");

        info!("End of planning with operations");
        clean_all_repositories();
    }

    #[test]
    #[serial]
    fn test_planning_3_levels() {
        clean_all_repositories();
        if let Err(e) = logger_config::configure_logger() {
            eprintln!("Failed to configure logger: {}", e);
        }

        let start_time = std::time::Instant::now();

        // Create products
        let car = SKU::from_name("Car");
        let tyre = SKU::from_name("Tyre");
        let body = SKU::from_name("Body");
        let engine = SKU::from_name("Engine");
        let seat = SKU::from_name("Seat");

        // Create dates
        let jan_15 = NaiveDate::from_ymd_opt(2024, 1, 15).unwrap();
        let jan_31 = NaiveDate::from_ymd_opt(2024, 1, 31).unwrap();

        // Create flows for car assembly
        let tyre_flow = Flow::new(true, 4.0, tyre.clone()); // 4 tyres per car
        let body_flow = Flow::new(true, 1.0, body.clone()); // 1 body per car
        let car_flow = Flow::new(false, 1.0, car.clone()); // 1 car produced

        // Create flows for body assembly
        let engine_flow = Flow::new(true, 1.0, engine.clone()); // 1 engine per body
        let seat_flow = Flow::new(true, 5.0, seat.clone());   // 5 seats per body
        let body_output_flow = Flow::new(false, 1.0, body.clone()); // 1 body produced

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
        {
            let mut car_ref = car.lock();
            let mut body_ref = body.lock();
            car_ref.set_top_producing_operation(OperationVariant::Basic(car_assembly));
            body_ref.set_top_producing_operation(OperationVariant::Basic(body_assembly));
        }

        // Create demand for cars
        let demand_qty = 200.0;
        let demand = Demand::new("D3".to_string(), demand_qty, jan_31, 0, car.clone());

        // Add initial inventory
        {
            let mut tyre_ref = tyre.lock();
            let mut body_ref = body.lock();
            let mut engine_ref = engine.lock();
            let mut seat_ref = seat.lock();
            let mut car_ref = car.lock();

            tyre_ref.add_inventory(jan_15, 1000.0);
            body_ref.add_inventory(jan_15, 50.0);
            engine_ref.add_inventory(jan_15, 50.0);
            seat_ref.add_inventory(jan_15, 500.0);
            car_ref.add_inventory(jan_15, 50.0);
        }

        // Create planner and specification
        let dp = DemandPlanner::new();
        let mut specification = Specification::new(2, 0);

        // Plan demand
        let result = dp.plan(demand.clone(), &mut specification);
        assert!(result.is_ok());

        // Log duration
        let duration = start_time.elapsed();
        info!("Time taken to create model and plan demands: {:?}", duration);

        // Verify the results
        let demand_ref = demand.lock();
        let plans = &demand_ref.demand_plans;
        assert!(!plans.is_empty(), "Should have created at least one plan");
        
        let total_planned = plans.iter().map(|p| p.get_quantity()).sum::<f64>();
        assert!(total_planned == 150.0, "Should not plan more than demanded");
        assert!(total_planned > 0.0, "Should plan some quantity");

        info!("End of planning with 3 levels");
        clean_all_repositories();
    }
 

    #[test]
    #[serial]
    fn test_planning_3_levels_mt() {
        clean_all_repositories();
        if let Err(e) = logger_config::configure_logger() {
            eprintln!("Failed to configure logger: {}", e);
        }

        let start_time = std::time::Instant::now();

        // Create products
        let car = SKU::from_name("Car");
        let tyre = SKU::from_name("Tyre");
        let body = SKU::from_name("Body");
        let engine = SKU::from_name("Engine");
        let seat = SKU::from_name("Seat");

        // Create dates
        let jan_15 = NaiveDate::from_ymd_opt(2024, 1, 15).unwrap();
        let jan_31 = NaiveDate::from_ymd_opt(2024, 1, 31).unwrap();

        // Create flows for car assembly
        let tyre_flow = Flow::new(true, 4.0, tyre.clone()); // 4 tyres per car
        let body_flow = Flow::new(true, 1.0, body.clone()); // 1 body per car
        let car_flow = Flow::new(false, 1.0, car.clone()); // 1 car produced

        // Create flows for body assembly
        let engine_flow = Flow::new(true, 1.0, engine.clone()); // 1 engine per body
        let seat_flow = Flow::new(true, 5.0, seat.clone());   // 5 seats per body
        let body_output_flow = Flow::new(false, 1.0, body.clone()); // 1 body produced

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
        {
            let mut car_ref = car.lock();
            let mut body_ref = body.lock();
            car_ref.set_top_producing_operation(OperationVariant::Basic(car_assembly));
            body_ref.set_top_producing_operation(OperationVariant::Basic(body_assembly));
        }


        {
            let mut tyre_ref = tyre.lock();
            let mut body_ref = body.lock();
            let mut engine_ref = engine.lock();
            let mut seat_ref = seat.lock();
            let mut car_ref = car.lock();

            tyre_ref.add_inventory(jan_15, 10000000.0);
            body_ref.add_inventory(jan_15, 50.0);
            engine_ref.add_inventory(jan_15, 5000000.0);
            seat_ref.add_inventory(jan_15, 50000000.0);
            car_ref.add_inventory(jan_15, 50.0);
        }
        // Create 100 demands for each thread
        let demand_qty = 200.0;
        let demands1: Vec<Arc<Mutex<Demand>>> = (0..100)
            .map(|i| Demand::new(format!("D3_{}", i), demand_qty, jan_31, i, car.clone()))
            .collect();
        let demands2: Vec<Arc<Mutex<Demand>>> = (0..100)
            .map(|i| Demand::new(format!("D4_{}", i), demand_qty, jan_31, i, car.clone()))
            .collect();

        // Create planner and specification
        let dp = Arc::new(DemandPlanner::new());
        let specification = Arc::new(Mutex::new(Specification::new(2, 0)));

        // Clone data for threads
        let dp_clone1 = dp.clone();
        let dp_clone2 = dp.clone();
        let spec_clone1 = specification.clone();
        let spec_clone2 = specification.clone();
        let demands1_clone = demands1.clone();
        let demands2_clone = demands2.clone();


        let thread1 = std::thread::spawn(move || {
            for demand in demands1_clone {
                let result = dp_clone1.plan(demand.clone(), &mut spec_clone1.lock());
                assert!(result.is_ok(), "Planning failed for demand {:?}", demand.lock().get_id());
            }
        });

        let thread2 = std::thread::spawn(move || {
            for demand in demands2_clone {
                let result = dp_clone2.plan(demand.clone(), &mut spec_clone2.lock());
                assert!(result.is_ok(), "Planning failed for demand {:?}", demand.lock().get_id());
            }
        });

        // Wait for both threads to complete
        thread1.join().expect("Thread 1 panicked");
        thread2.join().expect("Thread 1 panicked");

        // Log duration
        let duration = start_time.elapsed();
        info!("Time taken to create model and plan 200 demands in parallel: {:?}", duration);

        // Verify some results from each thread
        let sample_demand1 = &demands1[0];
        let sample_demand2 = &demands2[0];
        let plans1 = &sample_demand1.lock().demand_plans;
        let plans2 = &sample_demand2.lock().demand_plans;
        
        assert!(!plans1.is_empty(), "Should have created at least one plan for first D3 demand");
        assert!(!plans2.is_empty(), "Should have created at least one plan for first D4 demand");

        info!("End of planning with 3 levels Multi Threaded (200 demands total)");
        clean_all_repositories();
    }
} 
