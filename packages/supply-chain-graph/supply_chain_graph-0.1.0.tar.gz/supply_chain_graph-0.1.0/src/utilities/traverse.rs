use std::collections::HashSet;
use chrono::NaiveDate;
use log::info;
use crate::sku::SKU;
use crate::operation::{OperationVariant, MaterialFlowVariant, ResourceFlowVariant};
use std::sync::Arc;
use parking_lot::Mutex;

pub fn print_supply_chain(sku: Arc<Mutex<SKU>>, indent: usize, effective_date: NaiveDate) {
    let mut visited = HashSet::new();
    print_supply_chain_recursive(sku, indent, &mut visited, effective_date);
}

fn print_supply_chain_recursive(
    sku: Arc<Mutex<SKU>>, 
    indent: usize, 
    visited: &mut HashSet<String>,
    effective_date: NaiveDate,
) {
    let sku_name = sku.lock().name().to_string();
    
    // Check if we've already visited this SKU
    if !visited.insert(sku_name.clone()) {
        info!("{:indent$}└── 📦 SKU: {} (🔄 ❌ Cycle Detected 🔄 ❌ )", "", sku_name, indent=indent);
        return;
    }

    info!("{:indent$}└── 📦 SKU: {}", "", sku_name, indent=indent);

    let sku_ref = sku.lock();
    let top_op = sku_ref.get_top_producing_operation().clone(); // Clone the enum to avoid holding the lock
    drop(sku_ref); // Release the lock before recursing

    match top_op {
        OperationVariant::Basic(op) => {
            let op_ref = op.lock();
            info!("{:indent$}    └── ⚙️ Operation: {}", "", op_ref.get_name(), indent=indent);
            
            // Print resource as a separate level
            match op_ref.get_resource_flow() {
                ResourceFlowVariant::SingleResource(resource_flow) => {
                    let resource_flow_ref = resource_flow.lock();
                    info!("{:indent$}        └── 🛠️ Resource: {}", 
                        "", 
                        resource_flow_ref.get_resource().lock().get_name(),
                        indent=indent
                    );
                },
                ResourceFlowVariant::None => {}
            }
            
            let consume_flow = op_ref.get_consume_flow();

            match consume_flow {
                MaterialFlowVariant::Single(flow) => {
                    print_supply_chain_recursive(flow.lock().get_sku(), indent + 8, visited, effective_date);
                },
                MaterialFlowVariant::Simultaneous(sim_flow) => {
                    let flows = sim_flow.lock().get_flows().clone(); // Clone to avoid holding lock
                    for flow in flows {
                        print_supply_chain_recursive(flow.lock().get_sku(), indent + 8, visited, effective_date);
                    }
                },
                MaterialFlowVariant::None => {
                    info!("{:indent$}        (no inputs)", "", indent=indent);
                }
            }
        },
        OperationVariant::Alternate(alt_op) => {
            let alt_op_ref = alt_op.lock();
            info!("{:indent$}    └── ⚙️⚙️ Alternate Operation: {}", "", alt_op_ref.get_name(), indent=indent);
            
            // Clone the periods to avoid holding the lock
            let periods = alt_op_ref.get_period_effective_operation_map().clone();
            drop(alt_op_ref); // Release the lock before iterating
            
            for (i, period) in periods.iter().enumerate() {
                // Skip periods that start after our effective date
                if let Some(from) = period.from {
                    if from > effective_date {
                        continue;
                    }
                }

                let period_info = match (period.from, period.till) {
                    (Some(from), Some(till)) => format!("Period {}: {} to {}", i + 1, from, till),
                    (Some(from), None) => format!("Period {}: {} onwards", i + 1, from),
                    (None, Some(till)) => format!("Period {}: until {}", i + 1, till),
                    (None, None) => format!("Period {}: always effective", i + 1),
                };
                info!("{:indent$}        └── 📅 {}", "", period_info, indent=indent);

                for (op, priority) in &period.operation_priority {
                    let op_ref = op.lock();
                    info!("{:indent$}            └── ⚙️ Operation: {} (Priority: {})", "", 
                        op_ref.get_name(), priority, indent=indent);
                    
                    // Print resource as a separate level
                    match op_ref.get_resource_flow() {
                        ResourceFlowVariant::SingleResource(resource_flow) => {
                            let resource_flow_ref = resource_flow.lock();
                            info!("{:indent$}                └── 🛠️ Resource: {}", 
                                "", 
                                resource_flow_ref.get_resource().lock().get_name(),
                                indent=indent
                            );
                        },
                        ResourceFlowVariant::None => {}
                    }
                    
                    let consume_flow = op_ref.get_consume_flow(); //

                    match consume_flow {
                        MaterialFlowVariant::Single(flow) => {
                            print_supply_chain_recursive(flow.lock().get_sku(), indent + 16, visited, effective_date);
                        },
                        MaterialFlowVariant::Simultaneous(sim_flow) => {
                            let flows = sim_flow.lock().get_flows().clone(); // Clone to avoid holding lock
                            for flow in flows {
                                print_supply_chain_recursive(flow.lock().get_sku(), indent + 16, visited, effective_date);
                            }
                        },
                        MaterialFlowVariant::None => {
                            info!("{:indent$}                (no inputs)", "", indent=indent);
                        }
                    }
                }
            }
        },
        OperationVariant::None => {}
    }

    visited.remove(&sku_name);
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::flow::Flow;
    use crate::operation::ResourceFlowVariant;
    use crate::simultaneous_flow::SimultaneousFlow;
    use chrono::NaiveDate;
    use crate::operation::Operation;
    use crate::supply_chains::sc_with_alternates::create_sc_with_alternates;
    use crate::logger_config;
    use log::LevelFilter;
    
    #[test]
    fn test_simple_supply_chain() {
        let _ = logger_config::set_log_level(LevelFilter::Off);
        // Create SKUs
        let final_product = SKU::from_name("FinalProduct");
        let component = SKU::from_name("Component");
        let raw_material = SKU::from_name("RawMaterial");

        // Create flows and operations
        // Operation 1: RawMaterial -> Component
        let op1_produce = MaterialFlowVariant::Single(Flow::new(false, 1.0, component.clone()));
        let op1_consume = MaterialFlowVariant::Single(Flow::new(true, 1.0, raw_material.clone()));
        let operation1 = Operation::new(
            "MakeComponent".to_string(),
            1, 0, 0,
            op1_produce,
            op1_consume,
            ResourceFlowVariant::None,
        );

        // Operation 2: Component -> FinalProduct
        let op2_produce = MaterialFlowVariant::Single(Flow::new(false, 1.0, final_product.clone()));
        let op2_consume = MaterialFlowVariant::Single(Flow::new(true, 1.0, component.clone()));
        let operation2 = Operation::new(
            "MakeFinal".to_string(),
            1, 0, 0,
            op2_produce,
            op2_consume,
            ResourceFlowVariant::None,
        );

        // Set up the relationships
        component.lock().set_top_producing_operation(OperationVariant::Basic(operation1));
        final_product.lock().set_top_producing_operation(OperationVariant::Basic(operation2));

        // Print the supply chain
        info!("Supply Chain for Finished Good:");
        print_supply_chain(final_product, 0, NaiveDate::from_ymd_opt(2024, 1, 1).unwrap());
    }

    #[test]
    fn test_complex_supply_chain_traversal() {

        let _ = logger_config::set_log_level(LevelFilter::Off);
        // Create a complex product structure:
        // Finished Good
        // ├── Sub-Assembly A (2 units)
        // │   ├── Component A1 (3 units)
        // │   │   ├── Raw Material A11 (2 units)
        // │   │   └── Raw Material A12 (4 units)
        // │   └── Component A2 (1 unit)
        // │       └── Raw Material A21 (3 units)
        // └── Sub-Assembly B (1 unit)
        //     ├── Component B1 (2 units)
        //     │   └── Raw Material B11 (2 units)
        //     └── Component B2 (3 units)
        //         ├── Raw Material B21 (1 unit)
        //         └── Raw Material B22 (2 units)

        // Create all SKUs
        let final_product = SKU::from_name("Finished Good");
        let sub_assembly_a = SKU::from_name("Sub-Assembly A");
        let sub_assembly_b = SKU::from_name("Sub-Assembly B");
        let component_a1 = SKU::from_name("Component A1");
        let component_a2 = SKU::from_name("Component A2");
        let component_b1 = SKU::from_name("Component B1");
        let component_b2 = SKU::from_name("Component B2");
        let raw_a11 = SKU::from_name("Raw Material A11");
        let raw_a12 = SKU::from_name("Raw Material A12");
        let raw_a21 = SKU::from_name("Raw Material A21");
        let raw_b11 = SKU::from_name("Raw Material B11");
        let raw_b21 = SKU::from_name("Raw Material B21");
        let raw_b22 = SKU::from_name("Raw Material B22");

        // Create operations for final assembly
        let final_assembly_op = Operation::new(
            "Final Assembly".to_string(),
            1, 0, 0,
            MaterialFlowVariant::Single(Flow::new(false, 1.0, final_product.clone())),
            MaterialFlowVariant::Simultaneous(SimultaneousFlow::new(vec![
                Flow::new(true, 2.0, sub_assembly_a.clone()),
                Flow::new(true, 1.0, sub_assembly_b.clone()),
            ])),
            ResourceFlowVariant::None,
        );

        // Create operations for sub-assemblies
        let sub_assembly_a_op = Operation::new(
            "Make Sub-Assembly A".to_string(),
            1, 0, 0,
            MaterialFlowVariant::Single(Flow::new(false, 1.0, sub_assembly_a.clone())),
            MaterialFlowVariant::Simultaneous(SimultaneousFlow::new(vec![
                Flow::new(true, 3.0, component_a1.clone()),
                Flow::new(true, 1.0, component_a2.clone()),
            ])),
            ResourceFlowVariant::None,
        );

        let sub_assembly_b_op = Operation::new(
            "Make Sub-Assembly B".to_string(),
            1, 0, 0,
            MaterialFlowVariant::Single(Flow::new(false, 1.0, sub_assembly_b.clone())),
            MaterialFlowVariant::Simultaneous(SimultaneousFlow::new(vec![
                Flow::new(true, 2.0, component_b1.clone()),
                Flow::new(true, 3.0, component_b2.clone()),
            ])),
            ResourceFlowVariant::None,
        );

        // Create operations for components
        let component_a1_op = Operation::new(
            "Make Component A1".to_string(),
            1, 0, 0,
            MaterialFlowVariant::Single(Flow::new(false, 1.0, component_a1.clone())),
            MaterialFlowVariant::Simultaneous(SimultaneousFlow::new(vec![
                Flow::new(true, 2.0, raw_a11.clone()),
                Flow::new(true, 4.0, raw_a12.clone()),
            ])),
            ResourceFlowVariant::None,
        );

        let component_a2_op = Operation::new(
            "Make Component A2".to_string(),
            1, 0, 0,
            MaterialFlowVariant::Single(Flow::new(false, 1.0, component_a2.clone())),
            MaterialFlowVariant::Single(Flow::new(true, 3.0, raw_a21.clone())),
            ResourceFlowVariant::None,
        );

        let component_b1_op = Operation::new(
            "Make Component B1".to_string(),
            1, 0, 0,
            MaterialFlowVariant::Single(Flow::new(false, 1.0, component_b1.clone())),
            MaterialFlowVariant::Single(Flow::new(true, 2.0, raw_b11.clone())),
            ResourceFlowVariant::None,
        );

        let component_b2_op = Operation::new(
            "Make Component B2".to_string(),
            1, 0, 0,
            MaterialFlowVariant::Single(Flow::new(false, 1.0, component_b2.clone())),
            MaterialFlowVariant::Simultaneous(SimultaneousFlow::new(vec![
                Flow::new(true, 1.0, raw_b21.clone()),
                Flow::new(true, 2.0, raw_b22.clone()),
            ])),
            ResourceFlowVariant::None,
        );

        // Set up the relationships
        final_product.lock().set_top_producing_operation(OperationVariant::Basic(final_assembly_op));
        sub_assembly_a.lock().set_top_producing_operation(OperationVariant::Basic(sub_assembly_a_op));
        sub_assembly_b.lock().set_top_producing_operation(OperationVariant::Basic(sub_assembly_b_op));
        component_a1.lock().set_top_producing_operation(OperationVariant::Basic(component_a1_op));
        component_a2.lock().set_top_producing_operation(OperationVariant::Basic(component_a2_op));
        component_b1.lock().set_top_producing_operation(OperationVariant::Basic(component_b1_op));
        component_b2.lock().set_top_producing_operation(OperationVariant::Basic(component_b2_op));

        // Test the traversal
        info!("\nTraversing complex supply chain:");
        print_supply_chain(final_product, 0, NaiveDate::from_ymd_opt(2024, 1, 1).unwrap());

        // Expected output should look like:
        // └── Finished Good
        //     └── Operation: Final Assembly
        //         └── Sub-Assembly A
        //             └── Operation: Make Sub-Assembly A
        //                 └── Component A1
        //                     └── Operation: Make Component A1
        //                         └── Raw Material A11
        //                         └── Raw Material A12
        //                 └── Component A2
        //                     └── Operation: Make Component A2
        //                         └── Raw Material A21
        //         └── Sub-Assembly B
        //             └── Operation: Make Sub-Assembly B
        //                 └── Component B1
        //                     └── Operation: Make Component B1
        //                         └── Raw Material B11
        //                 └── Component B2
        //                     └── Operation: Make Component B2
        //                         └── Raw Material B21
        //                         └── Raw Material B22
    }

    #[test]
    fn test_complex_supply_chain_with_alternates() {
        let _ = logger_config::set_log_level(LevelFilter::Off);
        let final_product = create_sc_with_alternates();
        // Test the traversal
        info!("\nTraversing complex supply chain with alternates:");
        print_supply_chain(final_product, 0, NaiveDate::from_ymd_opt(2025, 1, 1).unwrap());
    }
}