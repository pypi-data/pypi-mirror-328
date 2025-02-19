use std::collections::{HashMap, HashSet};
use crate::sku::SKU;
use crate::operation::{OperationVariant, MaterialFlowVariant, ResourceFlowVariant};
use log::info;
use std::sync::Arc;
use parking_lot::Mutex;

#[derive(Debug, Clone, Copy)]
pub struct SKUCost {
    pub fixed_cost: f64,
}

impl SKUCost {
    pub fn new(fixed_cost: f64) -> Self {
        SKUCost { fixed_cost }
    }

    pub fn zero() -> Self {
        SKUCost { fixed_cost: 0.0 }
    }

    pub fn multiply(&self, quantity: f64) -> SKUCost {
        SKUCost { fixed_cost: self.fixed_cost * quantity }
    }
}

impl std::fmt::Display for SKUCost {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "Fixed Cost: {:.2}", self.fixed_cost)
    }
}

#[derive(Debug, Clone, Copy)]
pub struct OperationCost {
    pub fixed_cost: f64,
}

impl OperationCost {
    pub fn new(fixed_cost: f64) -> Self {
        OperationCost { fixed_cost }
    }

    pub fn zero() -> Self {
        OperationCost { fixed_cost: 0.0 }
    }

    pub fn multiply(&self, quantity: f64) -> OperationCost {
        OperationCost { fixed_cost: self.fixed_cost * quantity }
    }
}

impl std::fmt::Display for OperationCost {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "Fixed Cost: {:.2}", self.fixed_cost)
    }
}

#[derive(Debug, Clone, Copy)]
pub struct ResourceCost {
    pub fixed_cost: f64,
}

impl ResourceCost {
    pub fn new(fixed_cost: f64) -> Self {
        ResourceCost { fixed_cost }
    }

    pub fn zero() -> Self {
        ResourceCost { fixed_cost: 0.0 }
    }

    pub fn multiply(&self, quantity: f64) -> ResourceCost {
        ResourceCost { fixed_cost: self.fixed_cost * quantity }
    }
}

impl std::fmt::Display for ResourceCost {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "Fixed Cost: {:.2}", self.fixed_cost)
    }
}

#[derive(Debug, Clone, Copy)]
pub struct TotalCost {
    pub operation_cost: f64,
    pub sku_cost: f64,
    pub resource_cost: f64,
}

impl TotalCost {
    pub fn zero() -> Self {
        TotalCost { 
            operation_cost: 0.0,
            sku_cost: 0.0,
            resource_cost: 0.0,
        }
    }

    pub fn add_sku_cost(&mut self, sku_cost: &SKUCost) {
        self.sku_cost += sku_cost.fixed_cost;
    }

    pub fn add_operation_cost(&mut self, op_cost: &OperationCost) {
        self.operation_cost += op_cost.fixed_cost;
    }

    pub fn add_resource_cost(&mut self, resource_cost: &ResourceCost) {
        self.resource_cost += resource_cost.fixed_cost;
    }
}

impl std::fmt::Display for TotalCost {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "Total Operation Cost: {:.2}\nTotal SKU Cost: {:.2}\nTotal Resource Cost: {:.2}\nTotal Combined Cost: {:.2}", 
            self.operation_cost, 
            self.sku_cost,
            self.resource_cost,
            self.operation_cost + self.sku_cost + self.resource_cost)
    }
}

pub struct CostCalculator {
    operation_costs: HashMap<String, OperationCost>,
    sku_costs: HashMap<String, SKUCost>,
    resource_costs: HashMap<String, ResourceCost>,
}

impl CostCalculator {
    pub fn new() -> Self {
        Self {
            operation_costs: HashMap::new(),
            sku_costs: HashMap::new(),
            resource_costs: HashMap::new(),
        }
    }
    pub fn set_operation_cost(&mut self, operation_name: &str, cost: OperationCost) {
        self.operation_costs.insert(operation_name.to_string(), cost);
    }

    pub fn set_sku_cost(&mut self, sku_name: &str, cost: SKUCost) {
        self.sku_costs.insert(sku_name.to_string(), cost);
    }

    pub fn get_operation_cost(&self, operation_name: &str) -> Option<&OperationCost> {
        self.operation_costs.get(operation_name)
    }

    pub fn get_sku_cost(&self, sku_name: &str) -> Option<&SKUCost> {
        self.sku_costs.get(sku_name)
    }

    pub fn set_resource_cost(&mut self, resource_name: &str, cost: ResourceCost) {
        self.resource_costs.insert(resource_name.to_string(), cost);
    }

    pub fn get_resource_cost(&self, resource_name: &str) -> Option<&ResourceCost> {
        self.resource_costs.get(resource_name)
    }
}


#[derive(Debug)]
struct AlternateInfo {
    #[allow(dead_code)]
    name: String,
    basic_operations: HashSet<String>,
}

pub struct PathPrinter {
    // Maps alternate operation name to its basic operations
    alternates: HashMap<String, AlternateInfo>,
}

impl PathPrinter {
    pub fn new() -> Self {
        Self {
            alternates: HashMap::new(),
        }
    }

    pub fn print_alternates(&self) {
        info!("\nAlternate Operations Map:");
        for (alt_name, info) in &self.alternates {
            info!("{} -> {:?}", alt_name, info.basic_operations);
        }
    }

    pub fn collect_alternates(&mut self, sku: Arc<Mutex<SKU>>) {
        let mut visited = HashSet::new();
        self.collect_alternates_recursive(sku, &mut visited);
    }

    fn collect_alternates_recursive(
        &mut self,
        sku: Arc<Mutex<SKU>>,
        visited: &mut HashSet<String>
    ) {
        let sku_name = sku.lock().name().to_string();
        
        if !visited.insert(sku_name.clone()) {
            return;
        }

        let sku_ref = sku.lock();
        match sku_ref.get_top_producing_operation() {
            OperationVariant::Alternate(alt_op) => {
                let alt_op_ref = alt_op.lock();
                let alt_name = alt_op_ref.get_name().to_string();
                info!("Found Alternate Operation: {}", alt_name);
                
                // Collect basic operations from periods
                let mut basic_ops = HashSet::new();
                for period in alt_op_ref.get_period_effective_operation_map() {
                    for (op, _priority) in &period.operation_priority {
                        basic_ops.insert(op.lock().get_name().to_string());
                    }
                }

                self.alternates.insert(alt_name.clone(), AlternateInfo {
                    name: alt_name,
                    basic_operations: basic_ops,
                });
            },
            OperationVariant::Basic(op) => {
                // Process consume flows of basic operation
                match op.lock().get_consume_flow() {
                    MaterialFlowVariant::Single(flow) => {
                        let sku = flow.lock().get_sku();
                        self.collect_alternates_recursive(sku, visited);
                    },
                    MaterialFlowVariant::Simultaneous(sim_flow) => {
                        for flow in sim_flow.lock().get_flows() {
                            let sku = flow.lock().get_sku();
                            self.collect_alternates_recursive(sku, visited);
                        }
                    },
                    MaterialFlowVariant::None => {},
                }
            },
            OperationVariant::None => {},
        }

        visited.remove(&sku_name);
    }

    pub fn generate_combination_vector(&self) -> Vec<Vec<String>> {
        let mut result: Vec<Vec<String>> = vec![vec![]];
        
        // Convert alternates into a vector for consistent ordering
        let alternate_infos: Vec<&AlternateInfo> = self.alternates.values().collect();
        
        // For each alternate operation
        for alt_info in alternate_infos {
            let mut new_result = Vec::new();
            
            // For each existing combination
            for existing_combo in result {
                // For each basic operation in this alternate
                for basic_op in &alt_info.basic_operations {
                    // Create a new combination by adding this basic operation
                    let mut new_combo = existing_combo.clone();
                    new_combo.push(basic_op.clone());
                    new_result.push(new_combo);
                }
            }
            
            result = new_result;
        }
        
        result
    }

    pub fn traverse_selected_path(&self, sku: Arc<Mutex<SKU>>, combination: &[String]) {
        let mut visited = HashSet::new();
        self.traverse_selected_path_recursive(sku, combination, 0, &mut visited);
    }

    fn traverse_selected_path_recursive(
        &self,
        sku: Arc<Mutex<SKU>>, 
        combination: &[String],
        indent: usize,
        visited: &mut HashSet<String>,
    ) {
        let sku_name = sku.lock().name().to_string();
        
        // Check if we've already visited this SKU
        if !visited.insert(sku_name.clone()) {
            info!("{:indent$}└── 📦 SKU: {} (🔄 ❌ Cycle Detected 🔄 ❌)", "", sku_name, indent=indent);
            return;
        }

        info!("{:indent$}└── 📦 SKU: {}", "", sku_name, indent=indent);

        let sku_ref = sku.lock();
        let top_producing_operation = sku_ref.get_top_producing_operation().clone();
        drop(sku_ref);
        match top_producing_operation {
            OperationVariant::Basic(op) => {
                info!("{:indent$}    └── ⚙️ Operation: {}", "", op.lock().get_name(), indent=indent);
                
                // Process consume flows
                match op.lock().get_consume_flow() {
                    MaterialFlowVariant::Single(flow) => {
                        self.traverse_selected_path_recursive(
                            flow.lock().get_sku(), 
                            combination, 
                            indent + 8, 
                            visited
                        );
                    },
                    MaterialFlowVariant::Simultaneous(sim_flow) => {
                        for flow in sim_flow.lock().get_flows() {
                            self.traverse_selected_path_recursive(
                                flow.lock().get_sku(), 
                                combination, 
                                indent + 8, 
                                visited
                            );
                        }
                    },
                    MaterialFlowVariant::None => {
                        info!("{:indent$}        (no inputs)", "", indent=indent);
                    }
                }
            },
            OperationVariant::Alternate(alt_op) => {
                info!("{:indent$}    └── ⚙️⚙️ Alternate Operation: {}", "", alt_op.lock().get_name(), indent=indent);
                
                let alt_op_ref = alt_op.lock();
                for period in alt_op_ref.get_period_effective_operation_map() {
                    if let Some((op, priority)) = period.operation_priority
                        .iter()
                        .find(|(op, _)| combination.contains(&op.lock().get_name().to_string())) 
                    {
                        let period_info = match (period.from, period.till) {
                            (Some(from), Some(till)) => format!("{} to {}", from, till),
                            (Some(from), None) => format!("{} onwards", from),
                            (None, Some(till)) => format!("until {}", till),
                            (None, None) => "always effective".to_string(),
                        };
                        info!("{:indent$}        └── 📅 Period: {} (Priority: {})", "", period_info, priority, indent=indent);
                        info!("{:indent$}            └── ⚙️ Selected Operation: {}", "", op.lock().get_name(), indent=indent);
                        
                        // Process consume flows of selected operation
                        match op.lock().get_consume_flow() {
                            MaterialFlowVariant::Single(flow) => {
                                self.traverse_selected_path_recursive(
                                    flow.lock().get_sku(), 
                                    combination, 
                                    indent + 16, 
                                    visited
                                );
                            },
                            MaterialFlowVariant::Simultaneous(sim_flow) => {
                                for flow in sim_flow.lock().get_flows() {
                                    self.traverse_selected_path_recursive(
                                        flow.lock().get_sku(), 
                                        combination, 
                                        indent + 16, 
                                        visited
                                    );
                                }
                            },
                            MaterialFlowVariant::None => {
                                info!("{:indent$}                (no inputs)", "", indent=indent);
                            }
                        }
                        // Found a matching operation, break out of the period loop
                        break;
                    }
                }
            },
            OperationVariant::None => {}
        }

        visited.remove(&sku_name);
    }

    pub fn traverse_selected_path_with_cost(
        &self, 
        sku: Arc<Mutex<SKU>>, 
        combination: &[String],
        cost_calculator: &CostCalculator
    ) {
        let mut visited = HashSet::new();
        let mut total_cost = TotalCost::zero();
        info!("\nTraversing selected path with costs (base demand: 1.0):");
        self.traverse_selected_path_recursive_with_cost(
            sku, 
            combination, 
            0, 
            &mut visited,
            cost_calculator,
            &mut total_cost,
            1.0  // Base demand
        );
        info!("\n{}", total_cost);
    }

    fn traverse_selected_path_recursive_with_cost(
        &self,
        sku: Arc<Mutex<SKU>>, 
        combination: &[String],
        indent: usize,
        visited: &mut HashSet<String>,
        cost_calculator: &CostCalculator,
        total_cost: &mut TotalCost,
        cumulative_quantity: f64,
    ) {
        let sku_name = sku.lock().name().to_string();
        
        if !visited.insert(sku_name.clone()) {
            info!("{:indent$}└── 📦 SKU: {} (🔄 ❌ Cycle Detected 🔄 ❌) - Cumulative Qty: {:.2}", 
                "", sku_name, cumulative_quantity, indent=indent);
            return;
        }

        // Calculate and display SKU cost with cumulative quantity
        if let Some(sku_cost) = cost_calculator.get_sku_cost(&sku_name) {
            let total_sku_cost = sku_cost.multiply(cumulative_quantity);
            total_cost.add_sku_cost(&total_sku_cost);
            info!("{:indent$}└── 📦 SKU: {} - Cumulative Qty: {:.2} - Unit Cost: {:.2} - Total: {}", 
                "", sku_name, cumulative_quantity, sku_cost.fixed_cost, total_sku_cost, indent=indent);
        } else {
            info!("{:indent$}└── 📦 SKU: {} - Cumulative Qty: {:.2}", 
                "", sku_name, cumulative_quantity, indent=indent);
        }

        let sku_ref = sku.lock();
        let top_producing_operation = sku_ref.get_top_producing_operation().clone();
        drop(sku_ref);

        match top_producing_operation {
            OperationVariant::Basic(op) => {
                let op_ref = op.lock();
                let op_name = op_ref.get_name();

                // Calculate operation quantity based on produce flow
                let produce_qty_per = match op_ref.get_produce_flow() {
                    MaterialFlowVariant::Single(flow) => {
                        let qty = flow.lock().get_quantity_per();
                        info!("{:indent$}    └── 🔄 Produce Flow - Produces {:.2} SKU per run", 
                            "", qty, indent=indent);
                        qty
                    },
                    MaterialFlowVariant::Simultaneous(_) => {
                        info!("{:indent$}    └── 🔄 Produce Flow - Simultaneous flow (assumed 1.0)", 
                            "", indent=indent);
                        1.0
                    },
                    MaterialFlowVariant::None => {
                        info!("{:indent$}    └── 🔄 Produce Flow - No flow (assumed 1.0)", 
                            "", indent=indent);
                        1.0
                    },
                };

                // Operation runs needed = cumulative quantity needed / quantity produced per run
                let operation_runs = cumulative_quantity / produce_qty_per;

                if let Some(op_cost) = cost_calculator.get_operation_cost(op_name) {
                    let total_op_cost = op_cost.multiply(operation_runs);
                    total_cost.add_operation_cost(&total_op_cost);
                    info!("{:indent$}    └── ⚙️ Operation: {} - Runs: {:.2} - Unit Cost: {:.2} - Total: {}", 
                        "", op_name, operation_runs, op_cost.fixed_cost, total_op_cost, indent=indent);
                } else {
                    info!("{:indent$}    └── ⚙️ Operation: {} - Runs: {:.2}", 
                        "", op_name, operation_runs, indent=indent);
                }
                
                // Calculate resource cost if present
                if let ResourceFlowVariant::SingleResource(resource_flow) = op_ref.get_resource_flow() {
                    let resource_flow_ref = resource_flow.lock();
                    let resource = resource_flow_ref.get_resource().clone();
                    let resource_ref = resource.lock();   
                    let resource_name = resource_ref.get_name();
                    let resource_qty_per = resource_flow_ref.get_quantity_per();
                    
                    // Resource usage = operation runs * quantity per run
                    let resource_usage = operation_runs * resource_qty_per;

                    if let Some(resource_cost) = cost_calculator.get_resource_cost(resource_name) {
                        let total_resource_cost = resource_cost.multiply(resource_usage);
                        total_cost.add_resource_cost(&total_resource_cost);
                        info!("{:indent$}        └── 🛠️ Resource: {} - Usage: {:.2} - Unit Cost: {:.2} - Total: {}", 
                            "", resource_name, resource_usage, resource_cost.fixed_cost, total_resource_cost, indent=indent);
                    } else {
                        info!("{:indent$}        └── 🛠️ Resource: {} - Usage: {:.2}", 
                            "", resource_name, resource_usage, indent=indent);
                    }
                }
                
                // Process consume flows
                match op_ref.get_consume_flow() {
                    MaterialFlowVariant::Single(flow) => {
                        let flow_ref = flow.lock();
                        let consume_qty_per = flow_ref.get_quantity_per();
                        // Calculate required quantity for input: operation runs * quantity consumed per run
                        let required_input_qty = operation_runs * consume_qty_per;
                        info!("{:indent$}        └── 🔄 Consume Flow - Needs {:.2} per run - Total: {:.2}", 
                            "", consume_qty_per, required_input_qty, indent=indent);
                        self.traverse_selected_path_recursive_with_cost(
                            flow_ref.get_sku(), 
                            combination, 
                            indent + 8, 
                            visited,
                            cost_calculator,
                            total_cost,
                            required_input_qty
                        );
                    },
                    MaterialFlowVariant::Simultaneous(sim_flow) => {
                        for flow in sim_flow.lock().get_flows() {
                            let flow_ref = flow.lock();
                            let consume_qty_per = flow_ref.get_quantity_per();
                            let required_input_qty = operation_runs * consume_qty_per;
                            info!("{:indent$}        └── 🔄 Consume Flow - Needs {:.2} per run - Total: {:.2}", 
                                "", consume_qty_per, required_input_qty, indent=indent);
                            self.traverse_selected_path_recursive_with_cost(
                                flow_ref.get_sku(), 
                                combination, 
                                indent + 8, 
                                visited,
                                cost_calculator,
                                total_cost,
                                required_input_qty
                            );
                        }
                    },
                    MaterialFlowVariant::None => {
                        info!("{:indent$}        (no inputs)", "", indent=indent);
                    }
                }
            },
            OperationVariant::Alternate(alt_op) => {
                info!("{:indent$}    └── ⚙️⚙️ Alternate Operation: {}", 
                    "", alt_op.lock().get_name(), indent=indent);
                
                let alt_op_ref = alt_op.lock();
                for period in alt_op_ref.get_period_effective_operation_map() {
                    if let Some((op, priority)) = period.operation_priority
                        .iter()
                        .find(|(op, _)| combination.contains(&op.lock().get_name().to_string())) 
                    {
                        let period_info = match (period.from, period.till) {
                            (Some(from), Some(till)) => format!("{} to {}", from, till),
                            (Some(from), None) => format!("{} onwards", from),
                            (None, Some(till)) => format!("until {}", till),
                            (None, None) => "always effective".to_string(),
                        };
                        info!("{:indent$}        └── 📅 Period: {} (Priority: {})", 
                            "", period_info, priority, indent=indent);

                        let op_ref = op.lock();
                        let op_name = op_ref.get_name();

                        let produce_qty_per = match op_ref.get_produce_flow() {
                            MaterialFlowVariant::Single(flow) => {
                                let qty = flow.lock().get_quantity_per();
                                info!("{:indent$}            └── 🔄 Produce Flow - Produces {:.2} SKU per run", 
                                    "", qty, indent=indent);
                                qty
                            },
                            MaterialFlowVariant::Simultaneous(_) => {
                                info!("{:indent$}            └── 🔄 Produce Flow - Simultaneous flow (assumed 1.0)", 
                                    "", indent=indent);
                                1.0
                            },
                            MaterialFlowVariant::None => {
                                info!("{:indent$}            └── 🔄 Produce Flow - No flow (assumed 1.0)", 
                                    "", indent=indent);
                                1.0
                            },
                        };

                        let operation_runs = cumulative_quantity / produce_qty_per;

                        if let Some(op_cost) = cost_calculator.get_operation_cost(op_name) {
                            let total_op_cost = op_cost.multiply(operation_runs);
                            total_cost.add_operation_cost(&total_op_cost);
                            info!("{:indent$}            └── ⚙️ Selected Operation: {} - Runs: {:.2} - Unit Cost: {:.2} - Total: {}", 
                                "", op_name, operation_runs, op_cost.fixed_cost, total_op_cost, indent=indent);
                        } else {
                            info!("{:indent$}            └── ⚙️ Selected Operation: {} - Runs: {:.2}", 
                                "", op_name, operation_runs, indent=indent);
                        }
                        
                        // Add the same resource cost handling inside the alternate operation case
                        if let ResourceFlowVariant::SingleResource(resource_flow) = op_ref.get_resource_flow() {
                            let resource_flow_ref = resource_flow.lock();
                            let resource = resource_flow_ref.get_resource().clone();
                            let resource_ref = resource.lock();   
                            let resource_name = resource_ref.get_name();
                            let resource_qty_per = resource_flow_ref.get_quantity_per();
                            
                            let resource_usage = operation_runs * resource_qty_per;

                            if let Some(resource_cost) = cost_calculator.get_resource_cost(resource_name) {
                                let total_resource_cost = resource_cost.multiply(resource_usage);
                                total_cost.add_resource_cost(&total_resource_cost);
                                info!("{:indent$}                └── 🛠️ Resource: {} - Usage: {:.2} - Unit Cost: {:.2} - Total: {}", 
                                    "", resource_name, resource_usage, resource_cost.fixed_cost, total_resource_cost, indent=indent);
                            } else {
                                info!("{:indent$}                └── 🛠️ Resource: {} - Usage: {:.2}", 
                                    "", resource_name, resource_usage, indent=indent);
                            }
                        }

                        match op_ref.get_consume_flow() {
                            MaterialFlowVariant::Single(flow) => {
                                let flow_ref = flow.lock();
                                let consume_qty_per = flow_ref.get_quantity_per();
                                let required_input_qty = operation_runs * consume_qty_per;
                                info!("{:indent$}                └── 🔄 Consume Flow - Needs {:.2} per run - Total: {:.2}", 
                                    "", consume_qty_per, required_input_qty, indent=indent);
                                self.traverse_selected_path_recursive_with_cost(
                                    flow_ref.get_sku(), 
                                    combination, 
                                    indent + 16, 
                                    visited,
                                    cost_calculator,
                                    total_cost,
                                    required_input_qty
                                );
                            },
                            MaterialFlowVariant::Simultaneous(sim_flow) => {
                                for flow in sim_flow.lock().get_flows() {
                                    let flow_ref = flow.lock();
                                    let consume_qty_per = flow_ref.get_quantity_per();
                                    let required_input_qty = operation_runs * consume_qty_per;
                                    info!("{:indent$}                └── 🔄 Consume Flow - Needs {:.2} per run - Total: {:.2}", 
                                        "", consume_qty_per, required_input_qty, indent=indent);
                                    self.traverse_selected_path_recursive_with_cost(
                                        flow_ref.get_sku(), 
                                        combination, 
                                        indent + 16, 
                                        visited,
                                        cost_calculator,
                                        total_cost,
                                        required_input_qty
                                    );
                                }
                            },
                            MaterialFlowVariant::None => {
                                info!("{:indent$}                (no inputs)", "", indent=indent);
                            }
                        }
                        break;
                    }
                }
            },
            OperationVariant::None => {},
        }

        visited.remove(&sku_name);
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::supply_chains::sc_with_alternates::create_sc_with_alternates;
    use crate::logger_config;
    use log::LevelFilter;
    use serial_test::serial;

    #[test]
    #[serial]
    fn test_path_printing() {
        let _ = logger_config::set_log_level(LevelFilter::Off);
        // Create SKUs
        let final_product = create_sc_with_alternates();
        let mut path_printer = PathPrinter::new();
        
        // Phase 1: Collect all alternates
        path_printer.collect_alternates(final_product.clone());
        path_printer.print_alternates();

        let combinations = path_printer.generate_combination_vector();
        info!("\nAll possible combinations:");
        for (i, combo) in combinations.iter().enumerate() {
            info!("Combination {}: {:?}", i + 1, combo);
        }
    }

    #[test]
    #[serial]
    fn test_traverse_selected_path() {
        let _ = logger_config::set_log_level(LevelFilter::Off);
        // Create SKUs
        let final_product = create_sc_with_alternates();
        let mut path_printer = PathPrinter::new();

        
        // Phase 1: Collect all alternates
        path_printer.collect_alternates(final_product.clone());
        
        // Phase 2: Generate combinations
        let combinations = path_printer.generate_combination_vector();

        info!("\nTraversing each possible combination:");
        for (i, combo) in combinations.iter().enumerate() {
            info!("\nCombination {} path:", i + 1);
            path_printer.traverse_selected_path(final_product.clone(), combo);
        }
    }


    #[test]
    #[serial]
    fn test_cost_calculation() {
        let _ = logger_config::set_log_level(LevelFilter::Off);
        let final_product = create_sc_with_alternates();
        let mut cost_calculator = CostCalculator::new();
        cost_calculator.set_operation_cost("Make Component A1", OperationCost::new(1.0));
        cost_calculator.set_operation_cost("Make Component A2", OperationCost::new(1.0));
        cost_calculator.set_operation_cost("Make Component B1", OperationCost::new(1.0));
        cost_calculator.set_operation_cost("Make Component B2", OperationCost::new(1.0));
        cost_calculator.set_operation_cost("Main Assembly", OperationCost::new(1.0));
        cost_calculator.set_operation_cost("Direct Production", OperationCost::new(1.0));
        cost_calculator.set_operation_cost("Procure from Main Vendor", OperationCost::new(1.0));
        cost_calculator.set_operation_cost("Procure from Alt Vendor", OperationCost::new(1.0));
        
        cost_calculator.set_sku_cost("Raw Material A11", SKUCost::new(1.0));
        cost_calculator.set_sku_cost("Raw Material A12", SKUCost::new(1.0));
        cost_calculator.set_sku_cost("Raw Material A21", SKUCost::new(1.0));
        cost_calculator.set_sku_cost("Raw Material B11", SKUCost::new(1.0));
        cost_calculator.set_sku_cost("Raw Material B21", SKUCost::new(1.0));
        cost_calculator.set_sku_cost("Raw Material B22", SKUCost::new(1.0));

        // First collect all alternates to get possible combinations
        let mut path_printer = PathPrinter::new();
        path_printer.collect_alternates(final_product.clone());
        
        let combinations = path_printer.generate_combination_vector();
        
        info!("\nCost Analysis for Each Combination:");
        for (i, combo) in combinations.iter().enumerate() {
            info!("\nCombination {} - Operations: {:?}", i + 1, combo);
            path_printer.traverse_selected_path_with_cost(final_product.clone(), combo, &cost_calculator);
        }
    }

    #[test]
    #[serial]
    fn test_specific_combination() {
        let _ = logger_config::set_log_level(LevelFilter::Off);
        let final_product = create_sc_with_alternates();
        let mut cost_calculator = CostCalculator::new();

        // Set some example costs
        cost_calculator.set_operation_cost("Make Component A1", OperationCost::new(1.0));
        cost_calculator.set_operation_cost("Make Component A2", OperationCost::new(1.0));
        cost_calculator.set_operation_cost("Make Component B1", OperationCost::new(1.0));
        cost_calculator.set_operation_cost("Make Component B2", OperationCost::new(1.0));
        cost_calculator.set_operation_cost("Main Assembly", OperationCost::new(1.0));
        cost_calculator.set_operation_cost("Direct Production", OperationCost::new(1.0));
        cost_calculator.set_operation_cost("Procure from Main Vendor", OperationCost::new(1.0));
        cost_calculator.set_operation_cost("Procure from Alt Vendor", OperationCost::new(1.0));    
        
        cost_calculator.set_sku_cost("Raw Material A11", SKUCost::new(1.0));
        cost_calculator.set_sku_cost("Raw Material A12", SKUCost::new(1.0));
        cost_calculator.set_sku_cost("Raw Material A21", SKUCost::new(1.0));
        cost_calculator.set_sku_cost("Raw Material B11", SKUCost::new(1.0));
        cost_calculator.set_sku_cost("Raw Material B21", SKUCost::new(1.0));
        cost_calculator.set_sku_cost("Raw Material B22", SKUCost::new(1.0));
        
        cost_calculator.set_resource_cost("Assembly_Resource", ResourceCost::new(1.0));
        
        let combination = vec![
            "Procure from Main Vendor".to_string(), 
            "Direct Production".to_string()
        ];

        info!("\nAnalyzing specific combination: {:?}", combination);
        let path_printer = PathPrinter::new();

        path_printer.traverse_selected_path_with_cost(
            final_product.clone(), 
            &combination,
            &cost_calculator
        );
    }

    #[test]
    #[serial]
    fn test_cost_calculation_with_multiple_combinations() {
        let _ = logger_config::set_log_level(LevelFilter::Off);
        let final_product = create_sc_with_alternates();
        let mut cost_calculator = CostCalculator::new();

        cost_calculator.set_operation_cost("Make Component A1", OperationCost::new(1.0));
        cost_calculator.set_operation_cost("Make Component A2", OperationCost::new(1.0));
        cost_calculator.set_operation_cost("Make Component B1", OperationCost::new(1.0));
        cost_calculator.set_operation_cost("Make Component B2", OperationCost::new(1.0));
        cost_calculator.set_operation_cost("Main Assembly", OperationCost::new(1.0));
        cost_calculator.set_operation_cost("Direct Production", OperationCost::new(1.0));
        cost_calculator.set_operation_cost("Procure from Main Vendor", OperationCost::new(1.0));
        cost_calculator.set_operation_cost("Procure from Alt Vendor", OperationCost::new(1.0));
        
        cost_calculator.set_sku_cost("Raw Material A11", SKUCost::new(1.0));
        cost_calculator.set_sku_cost("Raw Material A12", SKUCost::new(1.0));
        cost_calculator.set_sku_cost("Raw Material A21", SKUCost::new(1.0));
        cost_calculator.set_sku_cost("Raw Material B11", SKUCost::new(1.0));
        cost_calculator.set_sku_cost("Raw Material B21", SKUCost::new(1.0));
        cost_calculator.set_sku_cost("Raw Material B22", SKUCost::new(1.0));

        cost_calculator.set_resource_cost("Assembly_Resource", ResourceCost::new(1.0));
        
        let mut path_printer = PathPrinter::new();
        path_printer.collect_alternates(final_product.clone());
        let combinations = path_printer.generate_combination_vector();

        info!("\nCost Analysis for Each Combination:");
        for (i, combo) in combinations.iter().enumerate() {
            info!("\nCombination {} - Operations: {:?}", i + 1, combo);
            path_printer.traverse_selected_path_with_cost(final_product.clone(), combo, &cost_calculator);
        }

    }
} 