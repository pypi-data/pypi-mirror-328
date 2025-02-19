use std::sync::Arc;
use parking_lot::Mutex;
use std::collections::HashSet;
use chrono::NaiveDate;
use crate::sku::SKU;
use crate::operation::{OperationVariant, MaterialFlowVariant, ResourceFlowVariant};

pub fn get_supply_chain(sku: Arc<Mutex<SKU>>, indent: usize, effective_date: NaiveDate) -> Vec<String> {
    let mut output = Vec::new();
    let mut visited = HashSet::new();
    get_supply_chain_recursive(sku, indent, &mut visited, effective_date, &mut output);
    output
}

fn get_supply_chain_recursive(
    sku: Arc<Mutex<SKU>>, 
    indent: usize, 
    visited: &mut HashSet<String>,
    effective_date: NaiveDate,
    output: &mut Vec<String>,
) {
    let sku_name = sku.lock().name().to_string();
    
    // Check if we've already visited this SKU
    if !visited.insert(sku_name.clone()) {
        output.push(format!("{:indent$}└── 📦 SKU: {} (🔄 ❌ Cycle Detected 🔄 ❌ )", "", sku_name, indent=indent));
        return;
    }

    output.push(format!("{:indent$}└── 📦 SKU: {}", "", sku_name, indent=indent));

    let sku_ref = sku.lock();
    let top_op = sku_ref.get_top_producing_operation().clone();
    drop(sku_ref);

    match top_op {
        OperationVariant::Basic(op) => {
            let op_ref = op.lock();
            output.push(format!("{:indent$}    └── ⚙️ Operation: {}", "", op_ref.get_name(), indent=indent));
            
            match op_ref.get_resource_flow() {
                ResourceFlowVariant::SingleResource(resource_flow) => {
                    let resource_flow_ref = resource_flow.lock();
                    output.push(format!("{:indent$}        └── 🛠️ Resource: {}", 
                        "", 
                        resource_flow_ref.get_resource().lock().get_name(),
                        indent=indent
                    ));
                },
                ResourceFlowVariant::None => {}
            }
            
            let consume_flow = op_ref.get_consume_flow();

            match consume_flow {
                MaterialFlowVariant::Single(flow) => {
                    get_supply_chain_recursive(flow.lock().get_sku(), indent + 8, visited, effective_date, output);
                },
                MaterialFlowVariant::Simultaneous(sim_flow) => {
                    let flows = sim_flow.lock().get_flows().clone();
                    for flow in flows {
                        get_supply_chain_recursive(flow.lock().get_sku(), indent + 8, visited, effective_date, output);
                    }
                },
                MaterialFlowVariant::None => {
                    output.push(format!("{:indent$}        (no inputs)", "", indent=indent));
                }
            }
        },
        OperationVariant::Alternate(alt_op) => {
            let alt_op_ref = alt_op.lock();
            output.push(format!("{:indent$}    └── ⚙️⚙️ Alternate Operation: {}", "", alt_op_ref.get_name(), indent=indent));
            
            let periods = alt_op_ref.get_period_effective_operation_map().clone();
            drop(alt_op_ref);
            
            for (i, period) in periods.iter().enumerate() {
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
                output.push(format!("{:indent$}        └── 📅 {}", "", period_info, indent=indent));

                for (op, priority) in &period.operation_priority {
                    let op_ref = op.lock();
                    output.push(format!("{:indent$}            └── ⚙️ Operation: {} (Priority: {})", "", 
                        op_ref.get_name(), priority, indent=indent));
                    
                    match op_ref.get_resource_flow() {
                        ResourceFlowVariant::SingleResource(resource_flow) => {
                            let resource_flow_ref = resource_flow.lock();
                            output.push(format!("{:indent$}                └── 🛠️ Resource: {}", 
                                "", 
                                resource_flow_ref.get_resource().lock().get_name(),
                                indent=indent
                            ));
                        },
                        ResourceFlowVariant::None => {}
                    }
                    
                    let consume_flow = op_ref.get_consume_flow();

                    match consume_flow {
                        MaterialFlowVariant::Single(flow) => {
                            get_supply_chain_recursive(flow.lock().get_sku(), indent + 16, visited, effective_date, output);
                        },
                        MaterialFlowVariant::Simultaneous(sim_flow) => {
                            let flows = sim_flow.lock().get_flows().clone();
                            for flow in flows {
                                get_supply_chain_recursive(flow.lock().get_sku(), indent + 16, visited, effective_date, output);
                            }
                        },
                        MaterialFlowVariant::None => {
                            output.push(format!("{:indent$}                (no inputs)", "", indent=indent));
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
    use crate::supply_chains::sc_with_alternates::create_sc_with_alternates;
    use log::info;

    #[test]
    fn test_complex_supply_chain_with_alternates() {
        let sku = create_sc_with_alternates();
        let effective_date = NaiveDate::from_ymd_opt(2025, 1, 1).unwrap();
        let supply_chain = get_supply_chain(sku, 0, effective_date);
        for line in supply_chain {
            info!("{}", line); 
        }
    }
}