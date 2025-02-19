use std::sync::Arc;
use parking_lot::Mutex;
use crate::sku::SKU;
use crate::resource::Resource;
use crate::operation::{Operation, MaterialFlowVariant, ResourceFlowVariant};
use crate::flow::Flow;
use crate::simultaneous_flow::SimultaneousFlow;
use crate::resource_flow::ResourceFlow;
use chrono::NaiveDate;
use crate::demand::Demand;
use crate::specification::Specification;
use crate::demand_planner::DemandPlanner;
use log::info;

#[allow(dead_code)]
fn create_laptop_supply_chain(count: u32) -> Arc<Mutex<SKU>> {
    // Create SKUs with count suffix
    let laptop_dc = SKU::from_name(&format!("Laptop@DC_{}", count));
    let laptop_plant1 = SKU::from_name(&format!("Laptop@Plant1_{}", count));
    let laptop_plant2 = SKU::from_name(&format!("Laptop@Plant2_{}", count));
    
    // Create component SKUs for each plant with count suffix
    let disk_plant1 = SKU::from_name(&format!("Disk@Plant1_{}", count));
    let cpu_plant1 = SKU::from_name(&format!("CPU@Plant1_{}", count));
    let memory_plant1 = SKU::from_name(&format!("Memory@Plant1_{}", count));
    
    let disk_plant2 = SKU::from_name(&format!("Disk@Plant2_{}", count));
    let cpu_plant2 = SKU::from_name(&format!("CPU@Plant2_{}", count));
    let memory_plant2 = SKU::from_name(&format!("Memory@Plant2_{}", count));

    // Create assembly resources with count suffix
    let assembly_resource_plant1 = Resource::from_name(&format!("Assemble_Laptop@Plant1_{}", count));
    let assembly_resource_plant2 = Resource::from_name(&format!("Assemble_Laptop@Plant2_{}", count));
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
        format!("Make_Laptop@Plant1_{}", count),
        0, // lead time
        1, // min batch
        1, // batch multiple
        MaterialFlowVariant::Single(laptop_plant1_output),
        MaterialFlowVariant::Simultaneous(laptop_plant1_components),
        ResourceFlowVariant::SingleResource(assembly_resource_flow_plant1)
    );

    let laptop_assembly_plant2 = Operation::new(
        format!("Make_Laptop@Plant2_{}", count),
        0, // lead time
        1, // min batch
        1, // batch multiple
        MaterialFlowVariant::Single(laptop_plant2_output),
        MaterialFlowVariant::Simultaneous(laptop_plant2_components),
        ResourceFlowVariant::SingleResource(assembly_resource_flow_plant2)
    );

    // Create transport operation (from either plant to DC)
    let move_laptop_plant1_to_dc = Operation::new(
        format!("Move_Laptop@Plant1-to-DC_{}", count),
        0, // lead time
        1, // min batch
        1, // batch multiple
        MaterialFlowVariant::Single(Flow::new(false, 1.0, laptop_dc.clone())),
        MaterialFlowVariant::Single(Flow::new(true, 1.0, laptop_plant1.clone())), // Can consume from Plant1
        ResourceFlowVariant::None
    );

    let move_laptop_plant2_to_dc = Operation::new(
        format!("Move_Laptop@Plant2-to-DC_{}", count),
        0, // lead time
        1, // min batch
        1, // batch multiple
        MaterialFlowVariant::Single(Flow::new(false, 1.0, laptop_dc.clone())),
        MaterialFlowVariant::Single(Flow::new(true, 1.0, laptop_plant2.clone())), // Can consume from Plant1
        ResourceFlowVariant::None
    );

    // Add inventory to components (1000 units each)
    let jan_15 = NaiveDate::from_ymd_opt(2024, 1, 15).unwrap();
    
    // Plant 1 components
    disk_plant1.lock().add_inventory(jan_15, 1000.0);
    cpu_plant1.lock().add_inventory(jan_15, 1000.0);
    memory_plant1.lock().add_inventory(jan_15, 2000.0);
    
    // Plant 2 components
    disk_plant2.lock().add_inventory(jan_15, 1000.0);
    cpu_plant2.lock().add_inventory(jan_15, 1000.0);
    memory_plant2.lock().add_inventory(jan_15, 2000.0);

    // Add daily capacity of 100 units from Jan 15 to Jan 30
    let jan_30 = NaiveDate::from_ymd_opt(2024, 1, 30).unwrap();
    let mut current_date = jan_15;
    
    while current_date <= jan_30 {
        assembly_resource_plant1.lock().set_capacity(current_date, 100.0);
        assembly_resource_plant2.lock().set_capacity(current_date, 100.0);
        current_date = current_date.succ_opt().unwrap();
    }

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

    laptop_dc
}

#[allow(dead_code)]
fn plan_laptop_demands(specification: &mut Specification) -> Result<(), String> {
    let dp = DemandPlanner::new();
    
    // Get all demands and sort by priority
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
        
        let result = dp.plan(demand.clone(), specification);
        if let Err(e) = result {
            return Err(format!("Failed to plan demand {}: {}", i + 1, e));
        }

        // Track planned quantity
        let demand_ref = demand.lock();
        let plans = &demand_ref.demand_plans;
        let demand_planned = plans.iter().map(|p| p.get_quantity()).sum::<f64>();
        total_planned_quantity += demand_planned;
    }

    info!("Total quantity planned across all demands: {}", total_planned_quantity);
    info!("Average quantity planned per demand: {}", 
          total_planned_quantity / all_demands.len() as f64);

    Ok(())
}

// Not being used at the moment. But it ran in 1/6th the time of the single thread version.
#[allow(dead_code)]
fn plan_laptop_demands_parallel() -> Result<(), String> {
    use std::thread;
    use std::sync::mpsc;

    let dp = Arc::new(DemandPlanner::new());
    //let specification = Arc::new(Mutex::new(specification.clone()));
    
    // Get all demands and sort by priority
    let mut all_demands = Demand::get_all_demands();
    all_demands.sort_by(|a, b| {
        let a_priority = a.lock().get_priority();
        let b_priority = b.lock().get_priority();
        a_priority.cmp(&b_priority)
    });

    let chunk_size = (all_demands.len() + 9) / 10; // Ceiling division
    let (tx, rx) = mpsc::channel();

    // Spawn 10 threads
    let mut handles = vec![];
    
    for thread_id in 0..10 {
        let start = thread_id * chunk_size;
        let end = std::cmp::min((thread_id + 1) * chunk_size, all_demands.len());
        
        if start >= all_demands.len() {
            break;
        }

        let thread_demands = all_demands[start..end].to_vec();
        let thread_dp = dp.clone();
        let mut thread_spec = Specification::new(2, 0);
        let thread_tx = tx.clone();

        let handle = thread::spawn(move || {
            let mut thread_total = 0.0;
            
            for (i, demand) in thread_demands.iter().enumerate() {
                let demand_index = start + i;
                //thread_spec.lock().set_current_demand_id(demand_index as i32);
                //thread_spec.set_current_demand_id(demand_index as i32);
                if let Err(e) = thread_dp.plan(demand.clone(), &mut thread_spec) {
                    thread_tx.send(Err(format!("Thread {} failed to plan demand {}: {}", 
                        thread_id, demand_index + 1, e))).unwrap();
                    return;
                }

                let demand_ref = demand.lock();
                let plans = &demand_ref.demand_plans;
                let demand_planned = plans.iter().map(|p| p.get_quantity()).sum::<f64>();
                thread_total += demand_planned;
            }
            
            thread_tx.send(Ok(thread_total)).unwrap();
        });

        handles.push(handle);
    }

    drop(tx); // Drop original sender so channel closes when all threads complete

    let mut total_planned_quantity = 0.0;
    for result in rx {
        match result {
            Ok(thread_total) => total_planned_quantity += thread_total,
            Err(e) => return Err(e),
        }
    }

    // Wait for all threads to complete
    for handle in handles {
        handle.join().map_err(|_| "Thread panicked")?;
    }

    info!("Total quantity planned across all demands: {}", total_planned_quantity);
    info!("Average quantity planned per demand: {}", 
             total_planned_quantity / all_demands.len() as f64);

    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::specification::Specification;
    use log::info;
    use crate::logger_config;
    use crate::utilities::memory::get_memory_usage;

    #[test]
    fn test_plan_laptop_demands() {
        // Clear repositories
        SKU::clear_repository();
        Operation::clear_repository();
        Demand::clear_repository();

        // Configure logging
        if let Err(e) = logger_config::configure_logger() {
            eprintln!("Failed to configure logger: {}", e);
        }

        let mut start_time = std::time::Instant::now();
        let num_chains = 100000;

        // Create supply chains
        let mut supply_chains = Vec::with_capacity(num_chains);
        for i in 1..=num_chains {
            let fg_product = create_laptop_supply_chain(i as u32);
            supply_chains.push(fg_product);
        }

        let mut elapsed = start_time.elapsed();
        info!("Time taken for creation of supply chains: {:?}", elapsed);
        let sku_count = SKU::get_all_skus().len();
        info!("SKU count: {}", sku_count);
        let operation_count = Operation::get_all_operations().len();
        info!("Operation count: {}", operation_count);

        start_time = std::time::Instant::now();

        // Create demands
        let demands_on_fg = 10;
        for (chain_idx, laptop_dc) in supply_chains.iter().enumerate() {
            for day in 1..=demands_on_fg {
                let demand_date = NaiveDate::from_ymd_opt(2024, 2, day).unwrap();
                let demand = Demand::new(
                    format!("D{}_{}", chain_idx + 1, day),
                    125.0,
                    demand_date,
                    0,
                    laptop_dc.clone()
                );
                demand.lock().set_priority((chain_idx * 10 + day as usize) as i32);
            }
        }
        let demand_count = Demand::get_all_demands().len();
        info!("Demand count: {}", demand_count);
        elapsed = start_time.elapsed();
        info!("Time taken for creation of demands: {:?}", elapsed);

        start_time = std::time::Instant::now();

        info!("Before planning Memory usage:\n{}", get_memory_usage());
        // Create specification and plan demands
        let mut specification = Specification::new(2, 0);
        let result = plan_laptop_demands(&mut specification);
        assert!(result.is_ok(), "Failed to plan demands: {:?}", result.err());
        
        elapsed = start_time.elapsed();
        info!("Time taken for planning all demands: {:?}", elapsed);
        // Verify results
        let all_demands = Demand::get_all_demands();
        for demand in &all_demands {
            let demand_ref = demand.lock();
            let plans = &demand_ref.demand_plans;
            assert!(!plans.is_empty(), "Demand {} has no plans", demand_ref.get_id());
        }

        // Analyze operation plans
        let all_operations = Operation::get_all_operations();
        let mut total_op_plans = 0;
        let mut total_op_plan_quantity = 0.0;

        for operation in all_operations {
            let op = operation.lock();
            let plans = op.get_all_operation_plans();

            let plan_count = plans.len();
            total_op_plans += plan_count;
            let plan_quantity_sum_on_op: f64 = plans.iter().map(|p| p.get_quantity()).sum();
            total_op_plan_quantity += plan_quantity_sum_on_op;
        }

        // Print summary
        info!("\nOperation Plan Statistics:");
        info!("Total Operation Plans: {}", total_op_plans);
        info!("Total Operation Plan Quantity: {:.2}", total_op_plan_quantity);
    

        info!("\nDemand Statistics:");
        info!("Total Demands: {}", all_demands.len());
        let total_demand_planned: f64 = all_demands.iter()
            .map(|d| d.lock().demand_plans.iter().map(|p| p.get_quantity()).sum::<f64>())
            .sum();
        info!("Total Planned Quantity: {:.2}", total_demand_planned);
        info!("Average Quantity per Demand: {:.2}", 
              total_demand_planned / all_demands.len() as f64);

        info!("Final Memory usage:\n{}", get_memory_usage());

        
    }
}