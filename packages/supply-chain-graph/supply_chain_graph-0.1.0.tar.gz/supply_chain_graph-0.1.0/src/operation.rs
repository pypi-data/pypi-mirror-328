use std::collections::HashMap;
use crate::flow::Flow;
use crate::simultaneous_flow::SimultaneousFlow;
use crate::ioperation::IOperation;
use crate::constants::OperationType;
use crate::operation_plan::OperationPlan;
use std::sync::Arc;
use parking_lot::Mutex;
use crate::resource_flow::ResourceFlow;
use chrono::NaiveDate;
use crate::constants::PRECISION;
use crate::alternate_operation::AlternateOperation;
use log::error;
use lazy_static::lazy_static;

lazy_static! {
    static ref OPERATION_REPOSITORY: Arc<Mutex<HashMap<String, Arc<Mutex<Operation>>>>> = 
        Arc::new(Mutex::new(HashMap::new()));
}

#[derive(Debug)]
pub enum MaterialFlowVariant {
    Single(Arc<Mutex<Flow>>),
    Simultaneous(Arc<Mutex<SimultaneousFlow>>),
    None,
}

#[derive(Debug)]
pub enum ResourceFlowVariant {
    None,
    SingleResource(Arc<Mutex<ResourceFlow>>),
}

#[derive(Debug, Clone)]
pub enum OperationVariant {
    None,
    Alternate(Arc<Mutex<AlternateOperation>>),
    Basic(Arc<Mutex<Operation>>),
    // MultiStepProcess(Rc<RefCell<MultiStepProcess>>),
}

#[derive(Debug, Clone)]
pub struct EffectivePeriod {
    pub from: Option<NaiveDate>,
    pub till: Option<NaiveDate>,
    pub priority: i32
}

#[derive(Debug)]
pub struct Operation {
    name: String, // this is the name with which this operation would be keyed into the repo. 
    // (For manufacturing: Potentially opname@process_name@bom_name)
    // (For tranportation: based on lane, source, destination, etc)
    internal_name: String, // this is the shorter name with which this operation would be referred in LSCO. for the
    // the given internal_name there could be multiple names since the same operation (internal_name/lsco name)
    // could be used with different boms. 
    lead_time: i32,
    min_lot: i32,
    increment: i32,
    produce_flow: MaterialFlowVariant,
    consume_flow: MaterialFlowVariant,
    resource_flow: ResourceFlowVariant,
    operation_plans: Vec<OperationPlan>,
    parent_operation: OperationVariant,
    // This is a list of periods that the operation is effective in. There is a priority defined for every periods.
    // that can help if this operation is a part of alternate operation. There is a utility function `split_into_non_overlapping_periods`
    // that can be used to split the operation into non overlapping periods.
    effective_periods: Vec<EffectivePeriod>,
    effectivity_processed: bool,
}

impl IOperation for Operation {
    fn operation_type(&self) -> OperationType {
        OperationType::Simple
    }
}

impl Operation {
    pub fn get_name(&self) -> &String {
        &self.name
    }

    pub fn get_lead_time(&self) -> i32 {
        self.lead_time
    }

    pub fn get_min_lot(&self) -> i32 {
        self.min_lot
    }

    pub fn set_min_lot(&mut self, min_lot: i32) {
        self.min_lot = min_lot;
    }

    pub fn get_increment(&self) -> i32 {
        self.increment
    }

    pub fn set_increment(&mut self, increment: i32) {
        self.increment = increment;
    }

    pub fn get_produce_flow(&self) -> &MaterialFlowVariant {
        &self.produce_flow
    }

    pub fn get_consume_flow(&self) -> &MaterialFlowVariant {
        &self.consume_flow
    }

    pub fn get_resource_flow(&self) -> &ResourceFlowVariant {
        &self.resource_flow
    }

    pub fn set_resource_flow(&mut self, resource_flow: ResourceFlowVariant) {
        self.resource_flow = resource_flow;
    }
    
    pub fn set_parent_operation(&mut self, parent_operation: OperationVariant) {
        self.parent_operation = parent_operation;
    }

    pub fn get_parent_operation(&self) -> &OperationVariant {
        &self.parent_operation
    }

    pub fn get_effective_periods(&self) -> &Vec<EffectivePeriod> {
        &self.effective_periods
    }
    
    pub fn is_effectivity_processed(&self) -> bool {
        self.effectivity_processed
    }

    pub fn set_effectivity_processed(&mut self, effectivity_processed: bool) {
        self.effectivity_processed = effectivity_processed;
    }

    pub fn get_operation_plans(&self) -> &Vec<OperationPlan> {
        &self.operation_plans
    }

    pub fn add_operation_plan(&mut self, plan: OperationPlan, resize_plan: bool) {
        if !resize_plan {
            self.operation_plans.push(plan);
        }
        else {
            self.resize_operation_plan(plan);
        }
    }

    pub fn is_lot_sized(&self) -> bool {
        self.min_lot > 0 || self.increment > 0
    }

    pub fn has_existing_op_plan_on_date(&self, date: NaiveDate) -> bool {
        // Check if there's an existing operation plan on the date
        let existing_plan_on_date = self.get_operation_plans()
            .iter()
            .any(|plan| plan.get_start_date() == date);
        existing_plan_on_date
    }

    pub fn scale_operation_plan_with_matching_start_date(&mut self, op_plan_qty: f64, start_date: NaiveDate) -> bool {
        if let Some(existing_plan) = self.operation_plans
            .iter_mut()
            .find(|p| p.get_start_date() == start_date) 
        {
            let new_qty = op_plan_qty + existing_plan.get_quantity();
            let ratio = new_qty / existing_plan.get_quantity();
            
            // Update main quantity
            existing_plan.set_quantity(new_qty);
            
            // Update in_flows
            for flow in existing_plan.get_in_flows() {
                let mut flow_ref = flow.lock();
                let new_qty = flow_ref.get_quantity() * ratio;
                flow_ref.set_quantity(new_qty);
            }

            // Update out_flows
            for flow in existing_plan.get_out_flows() {
                let mut flow_ref = flow.lock();
                let new_qty = flow_ref.get_quantity() * ratio;
                flow_ref.set_quantity(new_qty);
            }

            // Update resource_flows if they exist
            for resource_flow in existing_plan.get_in_resource_flows() {
                let mut flow_ref = resource_flow.lock();
                let new_qty = flow_ref.get_quantity() * ratio;
                flow_ref.set_quantity(new_qty);
            }
            return true;
        }
        return false;
    }

    pub fn resize_operation_plan(&mut self, plan: OperationPlan) {
        if let Some(existing_plan) = self.operation_plans
            .iter_mut()
            .find(|p| p.get_start_date() == plan.get_start_date()) 
        {
            // Merge quantities
            existing_plan.set_quantity(existing_plan.get_quantity() + plan.get_quantity());
            
            // Merge in_flows
            for new_flow in plan.get_in_flows() {
                if let Some(existing_flow) = existing_plan.get_in_flows()
                    .iter()
                    .find(|f| f.lock().get_sku().lock().name() == new_flow.lock().get_sku().lock().name()) 
                {
                    let mut existing_flow_ref = existing_flow.lock();
                    let current_qty = existing_flow_ref.get_quantity();
                    existing_flow_ref.set_quantity(current_qty + new_flow.lock().get_quantity());
                } else {
                    panic!("Flow not found in existing plan for operation {} and sku {}", 
                        self.name, new_flow.lock().get_sku().lock().name());
                }
            }

            // Merge out_flows
            for new_flow in plan.get_out_flows() {
                if let Some(existing_flow) = existing_plan.get_out_flows()
                    .iter()
                    .find(|f| f.lock().get_sku().lock().name() == new_flow.lock().get_sku().lock().name()) 
                {
                    let mut existing_flow_ref = existing_flow.lock();
                    let current_qty = existing_flow_ref.get_quantity();
                    existing_flow_ref.set_quantity(current_qty + new_flow.lock().get_quantity());
                } else {
                    panic!("Flow not found in existing plan for operation {} and sku {}", 
                        self.name, new_flow.lock().get_sku().lock().name());
                }
            }
        } else {
            // No matching plan found, add as new
            self.operation_plans.push(plan);
        }
    }

    // rounds down to the nearest increment if floor is true, rounds up if floor is false
    pub fn get_lot_sized_quantity(&self, quantity: f64, date: NaiveDate, floor: bool) -> f64 {
        if !self.is_lot_sized() {
            return quantity;
        }

        if quantity < PRECISION {
            return 0.0;
        }
        let min_lot = self.get_min_lot() as f64;
        let increment = self.get_increment() as f64;
        // Check if there's an existing operation plan on the date
        let existing_plan_on_date = self.has_existing_op_plan_on_date(date);
        let mut adjusted_quantity = quantity;
        if !existing_plan_on_date {
            // For new plans: must be at least min_lot and rounded to min_lot + n*increment
            if adjusted_quantity < min_lot {
                if floor {
                    adjusted_quantity = 0.0;
                } else {
                    adjusted_quantity = min_lot;
                }
            } else if increment > 0.0 {
                if floor {
                    adjusted_quantity = min_lot + ((adjusted_quantity - min_lot) / increment).floor() * increment;
                } else {
                    adjusted_quantity = min_lot + ((adjusted_quantity - min_lot) / increment).ceil() * increment;
                }
            }
        } else if increment > 0.0 {
            // For existing plans it is already assumed that they are already lot sized
            if floor {
                adjusted_quantity = (adjusted_quantity / increment).floor() * increment;
            } else {
                adjusted_quantity = (adjusted_quantity / increment).ceil() * increment;
            }
        }

        adjusted_quantity
    }

    pub fn new(
        name: String,
        lead_time: i32,
        min_lot: i32,
        increment: i32,
        produce_flow: MaterialFlowVariant,
        consume_flow: MaterialFlowVariant,
        resource_flow: ResourceFlowVariant,
    ) -> Arc<Mutex<Self>> {
        if name.is_empty() {
            // Handle empty name case
        }

        let repo = OPERATION_REPOSITORY.lock();
        if let Some(existing_op) = repo.get(&name) {
            return existing_op.clone();
        }
        drop(repo); // Release the lock before creating new Operation

        // for now just have this placeholder. When LSCO integration is done, this can be updated.
        let internal_name = name.split("@").last().unwrap().to_string();

        let operation = Arc::new(Mutex::new(Operation {
            name,
            internal_name,
            lead_time,
            min_lot,
            increment,
            produce_flow,
            consume_flow,
            resource_flow,
            operation_plans: Vec::new(),
            parent_operation: OperationVariant::None,
            effective_periods: Vec::new(),
            effectivity_processed: false,
        }));
        
        OPERATION_REPOSITORY.lock().insert(operation.lock().name.clone(), operation.clone());
        operation
    }

    pub fn find(name: &str) -> Option<Arc<Mutex<Operation>>> {
        OPERATION_REPOSITORY.lock()
            .get(name)
            .cloned()
    }

    pub fn exists(name: &str) -> bool {
        OPERATION_REPOSITORY.lock()
            .contains_key(name)
    }

    pub fn get_all_operations() -> Vec<Arc<Mutex<Operation>>> {
        OPERATION_REPOSITORY.lock()
            .values()
            .cloned()
            .collect()
    }

    pub fn get_all_operation_plans(&self) -> &Vec<OperationPlan> {
        &self.operation_plans
    }

    pub fn print_operation_plans(&self) {
        if !self.operation_plans.is_empty() {
            OperationPlan::print_operation_plan_header();
            for plan in self.get_operation_plans() {
                plan.print_operation_plan(&self.name);
            }
        }
    }

    pub fn clear_repository() {
        OPERATION_REPOSITORY.lock()
            .clear();
    }

    pub fn add_period(&mut self, from: Option<NaiveDate>, till: Option<NaiveDate>, priority: i32) {
        if till.is_some() && from.is_some() && till.unwrap() <= from.unwrap() {
            error!("Invalid period: till date {} is less than or equal to from date {} for Operation {}", till.unwrap(), from.unwrap(), self.name);
            return;
        }
        self.effective_periods.push(EffectivePeriod {
            from,
            till,
            priority,
        });
        self.effectivity_processed = false;
    }

    pub fn latest_effective_date(&mut self, ask_date: NaiveDate) -> Option<NaiveDate> {
        // Ensure periods are normalized and sorted
        self.split_into_non_overlapping_periods();
        self.get_latest_effective_date(ask_date)
    }

    pub fn get_latest_effective_date(&self, ask_date: NaiveDate) -> Option<NaiveDate> {
        if self.effective_periods.is_empty() {
            return Some(ask_date);
        }

        // Go backwards through periods
        for period in self.effective_periods.iter().rev() {
            match (period.from, period.till) {
                // For periods with both from and till dates
                (Some(from), Some(till)) => {
                    if ask_date >= till {
                        // Return one day before till
                        return till.pred_opt();
                    } else if ask_date >= from && ask_date < till {
                        return Some(ask_date);  // Return ask_date if it falls within period
                    }
                },
                // For periods with only till date
                (None, Some(till)) => {
                    if ask_date >= till {
                        return till.pred_opt();
                    } else {
                        return Some(ask_date);
                    }
                },
                // For periods with only from date
                (Some(from), None) => {
                    if ask_date >= from {
                        return Some(ask_date);
                    }
                },
                // For unbounded periods
                (None, None) => {
                    return Some(ask_date);
                }
            }
        }
        
        None // No valid effective date found
    }

    pub fn split_into_non_overlapping_periods(&mut self) {
        if self.effectivity_processed {
            return;
        }
        self.effectivity_processed = true;
        if self.effective_periods.is_empty() {
            return;
        }

        // Collect all unique dates
        let mut all_dates: Vec<NaiveDate> = Vec::new();
        for period in &self.effective_periods {
            if let Some(from) = period.from {
                all_dates.push(from);
            }
            if let Some(till) = period.till {
                all_dates.push(till);
            }
        }

        // Sort and deduplicate dates
        all_dates.sort();
        all_dates.dedup();

        if all_dates.is_empty() {
            return; // All periods are unbounded
        }

        let mut normalized_periods = Vec::new();

        // Handle period before first date if any periods are unbounded at start
        if let Some(first_date) = all_dates.first() {
            let effective_priority = self.effective_periods
                .iter()
                .filter(|p| p.from.is_none())
                .map(|p| p.priority)
                .max();

            if let Some(priority) = effective_priority {
                normalized_periods.push(EffectivePeriod {
                    from: None,
                    till: Some(*first_date),
                    priority,
                });
            }
        }

        // Process periods between dates
        for window in all_dates.windows(2) {
            let start_date = window[0];
            let end_date = window[1];
            
            // Find all periods that overlap this range
            let effective_priority = self.effective_periods
                .iter()
                .filter(|p| {
                    let after_start = match p.from {
                        Some(from) => from <= start_date,
                        None => true,
                    };
                    let before_end = match p.till {
                        Some(till) => till > start_date,
                        None => true,
                    };
                    after_start && before_end
                })
                .min_by_key(|p| {
                    // Prefer smaller periods when start dates match
                    match (p.from, p.till) {
                        (Some(from), Some(till)) if from == start_date => till - from,
                        _ => NaiveDate::MAX - start_date, // Place unbounded periods last
                    }
                })
                .map(|p| p.priority);

            if let Some(priority) = effective_priority {
                normalized_periods.push(EffectivePeriod {
                    from: Some(start_date),
                    till: Some(end_date),
                    priority,
                });
            }
        }

        // Handle period after last date if any periods are unbounded at end
        if let Some(last_date) = all_dates.last() {
            let effective_priority = self.effective_periods
                .iter()
                .filter(|p| p.till.is_none())
                .map(|p| p.priority)
                .max();

            if let Some(priority) = effective_priority {
                normalized_periods.push(EffectivePeriod {
                    from: Some(*last_date),
                    till: None,
                    priority,
                });
            }
        }

        // Sort periods by from date (None comes first)
        normalized_periods.sort_by(|a, b| {
            match (a.from, b.from) {
                (None, None) => std::cmp::Ordering::Equal,
                (None, Some(_)) => std::cmp::Ordering::Less,
                (Some(_), None) => std::cmp::Ordering::Greater,
                (Some(date_a), Some(date_b)) => date_a.cmp(&date_b),
            }
        });

        self.effective_periods = normalized_periods;
    }

    pub fn get_internal_name(&self) -> &str {
        &self.internal_name
    }

    pub fn set_produce_flow(&mut self, flow: MaterialFlowVariant) {
        self.produce_flow = flow;
    }

    pub fn set_consume_flow(&mut self, flow: MaterialFlowVariant) {
        self.consume_flow = flow;
    }

    pub fn reset(&mut self) {
        self.operation_plans.clear();
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use chrono::NaiveDate;
    use crate::sku::SKU;
    use serial_test::serial;
    
    fn setup() {
        Operation::clear_repository();
    }

    fn setup_test_flows() -> (MaterialFlowVariant, MaterialFlowVariant) {
        let sku1 = SKU::from_name("test_produce");
        let sku2 = SKU::from_name("test_consume");
        
        let produce_flow = Flow::new(false, 1.0, sku1);
        let consume_flow = Flow::new(true, 2.0, sku2);
        
        (
            MaterialFlowVariant::Single(produce_flow),
            MaterialFlowVariant::Single(consume_flow)
        )
    }

    fn create_test_operation() -> Arc<Mutex<Operation>> {
        let (produce_flow, consume_flow) = setup_test_flows();
        Operation::new(
            "test_op".to_string(),
            10,
            100,
            7,
            produce_flow,
            consume_flow,
            ResourceFlowVariant::None,
        )
    }

    #[test]
    #[serial]
    fn test_operation_creation() {
        setup();
        let operation = create_test_operation();
        let op = operation.lock();
        
        assert_eq!(op.get_name(), "test_op");
        assert_eq!(op.get_lead_time(), 10);
        assert_eq!(op.get_min_lot(), 100);
        assert_eq!(op.get_increment(), 7);
    }

    #[test]
    #[serial]
    fn test_operation_plans() {
        setup();
        let operation = create_test_operation();
        let date = NaiveDate::from_ymd_opt(2024, 1, 1).unwrap();
        
        let plan = OperationPlan::new(date, date, 50.0);
        operation.lock().add_operation_plan(plan, false);
        
        let binding = operation.lock();
        let plans = binding.get_operation_plans();
        assert_eq!(plans.len(), 1);
        assert_eq!(plans[0].get_quantity(), 50.0);
        assert_eq!(plans[0].get_start_date(), date);
        assert_eq!(plans[0].get_end_date(), date);
    }

    #[test]
    #[serial]
    fn test_operation_repository() {
        setup();
        // Create first operation
        let op1 = create_test_operation();
        
        // Create new flows for second operation
        let (produce_flow, consume_flow) = setup_test_flows();
        
        // Create second operation with same name but new flows
        let op2 = Operation::new(
            "test_op".to_string(),
            10,
            100,
            5,
            produce_flow,
            consume_flow,
            ResourceFlowVariant::None,
        );
        
        // Test that we get the same instance back
        assert!(Arc::ptr_eq(&op1, &op2));

        // Test finding operation
        let found_op = Operation::find("test_op");
        assert!(found_op.is_some());
        assert!(Arc::ptr_eq(&found_op.unwrap(), &op1));

        // Test exists
        assert!(Operation::exists("test_op"));
        assert!(!Operation::exists("nonexistent_op"));
    }

    #[test]
    #[serial]
    fn test_flow_wrappers() {
        setup();
        let operation = create_test_operation();
        let op = operation.lock();
        
        match op.get_produce_flow() {
            MaterialFlowVariant::Single(flow) => {
                assert!(!flow.lock().is_consume_flow());
                assert_eq!(flow.lock().get_quantity_per(), 1.0);
            },
            MaterialFlowVariant::Simultaneous(_) => panic!("Expected Single flow"),
            MaterialFlowVariant::None => panic!("Expected Single flow, got None"),
        }

        match op.get_consume_flow() {
            MaterialFlowVariant::Single(flow) => {
                assert!(flow.lock().is_consume_flow());
                assert_eq!(flow.lock().get_quantity_per(), 2.0);
            },
            MaterialFlowVariant::Simultaneous(_) => panic!("Expected Single flow"),
            MaterialFlowVariant::None => panic!("Expected Single flow, got None"),
        }
    }

    #[test]
    #[serial]
    fn test_operation_type() {
        setup();
        let operation = create_test_operation();
        assert_eq!(operation.lock().operation_type(), OperationType::Simple);
    }

    #[test]
    #[serial]
    fn test_mixed_flow_operation() {
        setup();
        let produce_sku = SKU::from_name("output_product");
        let consume_sku1 = SKU::from_name("input_material_1");
        let consume_sku2 = SKU::from_name("input_material_2");
        
        let produce_flow = MaterialFlowVariant::Single(Flow::new(false, 1.0, produce_sku));
        
        let consume_flow1 = Flow::new(true, 2.0, consume_sku1);
        let consume_flow2 = Flow::new(true, 3.0, consume_sku2);
        let consume_flows = SimultaneousFlow::new(vec![consume_flow1, consume_flow2]);
        let consume_flow = MaterialFlowVariant::Simultaneous(consume_flows);
        
        let operation = Operation::new(
            "mixed_flow_op".to_string(),
            5,
            50,
            10,
            produce_flow,
            consume_flow,
            ResourceFlowVariant::None,
        );
        
        let op = operation.lock();
        
        match op.get_produce_flow() {
            MaterialFlowVariant::Single(flow) => {
                assert!(!flow.lock().is_consume_flow());
                assert_eq!(flow.lock().get_quantity_per(), 1.0);
            },
            MaterialFlowVariant::Simultaneous(_) => panic!("Expected Single flow"),
            MaterialFlowVariant::None => panic!("Expected Single flow, got None"),
        }
        

        match op.get_consume_flow() {
            MaterialFlowVariant::Single(_) => panic!("Expected Simultaneous flow"),
            MaterialFlowVariant::Simultaneous(sim_flow) => {
                for flow in sim_flow.lock().get_flows() {
                    assert!(flow.lock().is_consume_flow());
                    println!("Simultaneous consume flow with quantity: {}", flow.lock().get_quantity_per());
                    let sku = flow.lock().get_sku();
                    println!("{}", sku.lock().name());
                }
            }
            MaterialFlowVariant::None => panic!("Expected Simultaneous flow, got None"),
        }
    }

    #[test]
    #[serial]
    fn test_operation_without_flows() {
        setup();
        let operation = Operation::new(
            "no_flow_op".to_string(),
            5,
            50,
            10,
            MaterialFlowVariant::None,
            MaterialFlowVariant::None,
            ResourceFlowVariant::None,
        );
        
        let op = operation.lock();
        match op.get_produce_flow() {
            MaterialFlowVariant::None => (),
            _ => panic!("Expected None produce flow"),
        }
        match op.get_consume_flow() {
            MaterialFlowVariant::None => (),
            _ => panic!("Expected None consume flow"),
        }
    }

    #[test]
    #[serial]
    fn test_get_lot_sized_quantity() {
        setup();
        let operation = create_test_operation(); // This has min_lot=100, increment=5
        let date = NaiveDate::from_ymd_opt(2024, 1, 1).unwrap();
        
        // Test cases for new plans (no existing plan on date)
        let op = operation.lock();

        // Below min_lot -ve should return 0
        assert_eq!(op.get_lot_sized_quantity(-2.0, date, true), 0.0);
        assert_eq!(op.get_lot_sized_quantity(-2.0, date, false), 0.0);

        // Below min_lot should return 0
        assert_eq!(op.get_lot_sized_quantity(50.0, date, true), 0.0);
        assert_eq!(op.get_lot_sized_quantity(50.0, date, false), 100.0);
        
        // Exact min_lot should return min_lot
        assert_eq!(op.get_lot_sized_quantity(100.0, date, true), 100.0);
        assert_eq!(op.get_lot_sized_quantity(100.0, date, false), 100.0);
        
        // Above min_lot should round to nearest increment
        assert_eq!(op.get_lot_sized_quantity(109.0, date, true), 107.0);  // Floor
        assert_eq!(op.get_lot_sized_quantity(109.0, date, false), 114.0); // Ceil

        drop(op);
        
        // Test with existing plan
        let plan = OperationPlan::new(date, date, 100.0);
        operation.lock().add_operation_plan(plan, false);
        
        // Now quantities should only round to increment
        let op = operation.lock();
        assert_eq!(op.get_lot_sized_quantity(112.0, date, true), 112.0);   // exact increment multiple
        assert_eq!(op.get_lot_sized_quantity(112.0, date, false), 112.0); 
        assert_eq!(op.get_lot_sized_quantity(114.0, date, true), 112.0); // not an increment multiple
        assert_eq!(op.get_lot_sized_quantity(114.0, date, false), 119.0); 
    }


    #[test]
    #[serial]
    fn test_multiple_effectivities_for_operation() {
        setup();
        let operation = create_test_operation();
        let mut op1 = operation.lock();
        
        // Create dates for testing
        let jan_1 = NaiveDate::from_ymd_opt(2024, 1, 1).unwrap();
        let mar_31 = NaiveDate::from_ymd_opt(2024, 3, 31).unwrap();
        let feb_1 = NaiveDate::from_ymd_opt(2024, 2, 1).unwrap();
        let may_1 = NaiveDate::from_ymd_opt(2024, 5, 1).unwrap();

        op1.add_period(
            Some(jan_1),
            Some(may_1),
            1
        );

        op1.add_period(
            Some(feb_1),
            Some(mar_31),
            3  // Higher priority period
        );
        
        
        // Test initial state
        assert_eq!(op1.effective_periods.len(), 2);
        assert_eq!(op1.effective_periods[0].priority, 1);
        assert_eq!(op1.effective_periods[1].priority, 3);
        
        // Test period normalization
        op1.split_into_non_overlapping_periods();
        
        // Should now have three distinct periods:
        // 1. Jan 1 - Feb 1 (priority 1)
        // 2. Feb 1 - Mar 31 (priority 3)
        // 3. Mar 31 - May 1 (priority 1)
        assert_eq!(op1.effective_periods.len(), 3);
        
        // Verify first period (before overlap)
        assert_eq!(op1.effective_periods[0].from, Some(jan_1));
        assert_eq!(op1.effective_periods[0].till, Some(feb_1));
        assert_eq!(op1.effective_periods[0].priority, 1);
        
        // Verify second period (during overlap - should have higher priority)
        assert_eq!(op1.effective_periods[1].from, Some(feb_1));
        assert_eq!(op1.effective_periods[1].till, Some(mar_31));
        assert_eq!(op1.effective_periods[1].priority, 3);
        
        // Verify third period (after overlap)
        assert_eq!(op1.effective_periods[2].from, Some(mar_31));
        assert_eq!(op1.effective_periods[2].till, Some(may_1));
        assert_eq!(op1.effective_periods[2].priority, 1);

    }

    #[test]
    #[serial]
    fn test_latest_effective_date() {
        setup();
        let operation = create_test_operation();
        let mut op = operation.lock();

        // Test with no periods
        let ask_date = NaiveDate::from_ymd_opt(2024, 1, 1).unwrap();
        assert_eq!(op.latest_effective_date(ask_date), Some(ask_date));

        // Add a single bounded period
        let period_from = NaiveDate::from_ymd_opt(2024, 1, 1).unwrap();
        let period_till = NaiveDate::from_ymd_opt(2024, 3, 1).unwrap();
        op.add_period(Some(period_from), Some(period_till), 1);

        // Test dates within the period
        let within_date = NaiveDate::from_ymd_opt(2024, 2, 1).unwrap();
        assert_eq!(op.latest_effective_date(within_date), Some(within_date));

        // Test date exactly on till date
        assert_eq!(op.latest_effective_date(period_till), 
            Some(NaiveDate::from_ymd_opt(2024, 2, 29).unwrap()));

        // Test date after till date
        let after_date = NaiveDate::from_ymd_opt(2024, 3, 15).unwrap();
        assert_eq!(op.latest_effective_date(after_date), 
            Some(NaiveDate::from_ymd_opt(2024, 2, 29).unwrap()));

        // Test date before period
        let before_date = NaiveDate::from_ymd_opt(2023, 12, 1).unwrap();
        assert_eq!(op.latest_effective_date(before_date), None);
    }

    #[test]
    #[serial]
    fn test_latest_effective_date_multiple_periods() {
        setup();
        let operation = create_test_operation();
        let mut op = operation.lock();

        // Add multiple non-overlapping periods
        op.add_period(
            Some(NaiveDate::from_ymd_opt(2024, 1, 1).unwrap()),
            Some(NaiveDate::from_ymd_opt(2024, 3, 1).unwrap()),
            1
        );
        op.add_period(
            Some(NaiveDate::from_ymd_opt(2024, 4, 1).unwrap()),
            Some(NaiveDate::from_ymd_opt(2024, 6, 1).unwrap()),
            1
        );

        // Test date in first period
        let date1 = NaiveDate::from_ymd_opt(2024, 2, 1).unwrap();
        assert_eq!(op.latest_effective_date(date1), Some(date1));

        // Test date at end of first period
        let date2 = NaiveDate::from_ymd_opt(2024, 3, 1).unwrap();
        assert_eq!(op.latest_effective_date(date2), 
            Some(NaiveDate::from_ymd_opt(2024, 2, 29).unwrap()));

        // Test date in gap between periods
        let date3 = NaiveDate::from_ymd_opt(2024, 3, 15).unwrap();
        assert_eq!(op.latest_effective_date(date3), 
            Some(NaiveDate::from_ymd_opt(2024, 2, 29).unwrap()));

        // Test date in second period
        let date4 = NaiveDate::from_ymd_opt(2024, 5, 1).unwrap();
        assert_eq!(op.latest_effective_date(date4), Some(date4));

        // Test date after all periods
        let date5 = NaiveDate::from_ymd_opt(2024, 7, 1).unwrap();
        assert_eq!(op.latest_effective_date(date5), 
            Some(NaiveDate::from_ymd_opt(2024, 5, 31).unwrap()));
    }

    #[test]
    #[serial]
    fn test_latest_effective_date_unbounded_periods() {
        setup();
        let operation = create_test_operation();
        let mut op = operation.lock();

        // Add period with only from date
        op.add_period(
            Some(NaiveDate::from_ymd_opt(2024, 1, 1).unwrap()),
            None,
            1
        );

        // Test date after from
        let date1 = NaiveDate::from_ymd_opt(2024, 2, 1).unwrap();
        assert_eq!(op.latest_effective_date(date1), Some(date1));

        // Test date before from
        let date2 = NaiveDate::from_ymd_opt(2023, 12, 1).unwrap();
        assert_eq!(op.latest_effective_date(date2), None);

        // Clear and add period with only till date
        op.effective_periods.clear();
        op.effectivity_processed = false;
        op.add_period(
            None,
            Some(NaiveDate::from_ymd_opt(2024, 3, 1).unwrap()),
            1
        );

        // Test date before till
        let date3 = NaiveDate::from_ymd_opt(2024, 2, 1).unwrap();
        assert_eq!(op.latest_effective_date(date3), Some(date3));

        // Test date at till
        let date4 = NaiveDate::from_ymd_opt(2024, 3, 1).unwrap();
        assert_eq!(op.latest_effective_date(date4), 
            Some(NaiveDate::from_ymd_opt(2024, 2, 29).unwrap()));

        // Test completely unbounded period
        op.effective_periods.clear();
        op.effectivity_processed = false;
        op.add_period(None, None, 1);

        // Test any date with unbounded period
        let date5 = NaiveDate::from_ymd_opt(2024, 1, 1).unwrap();
        assert_eq!(op.latest_effective_date(date5), Some(date5));
    }
}

