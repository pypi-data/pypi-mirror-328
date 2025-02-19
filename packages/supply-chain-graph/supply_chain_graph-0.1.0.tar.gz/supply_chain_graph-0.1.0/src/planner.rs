use std::sync::Arc;
use parking_lot::Mutex;

use crate::sku::SKU;
use crate::operation::Operation;
use crate::planning_service::PlanningService;
use crate::basic_sku_planning_service::BasicSKUPlanningService;
use crate::basic_operation_planning_service::BasicOperationPlanningService;
use crate::alt_operation_planning_service::AltOperationPlanningService;
use crate::alternate_operation::AlternateOperation;

#[derive(Debug)]
pub enum PlannerType {
    SKU(Arc<Mutex<SKU>>),
    Operation(Arc<Mutex<Operation>>),
    AlternateOperation(Arc<Mutex<AlternateOperation>>),
}

// TODO:
// This call and subsequent call to ask() is costly. Can we so sometihng to avoid this dynamism
// They increase the time taken by 25%
pub fn choose_planner(planner_type: PlannerType) -> Box<dyn PlanningService> {
    match planner_type {
        PlannerType::SKU(sku) => Box::new(BasicSKUPlanningService::new(sku)),
        PlannerType::Operation(operation) => Box::new(BasicOperationPlanningService::new(operation)),
        PlannerType::AlternateOperation(operation) => Box::new(AltOperationPlanningService::new(operation)),
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::operation::MaterialFlowVariant;
    use crate::flow::Flow;
    use crate::operation::ResourceFlowVariant;
    use crate::sku::SKU;
    use crate::operation::Operation;
    use crate::alternate_operation::AlternateOperation;
    use crate::operation::OperationVariant;

    #[test]
    fn test_choose_planner() {
        // Create test SKU
        let sku = SKU::from_name("test_sku");
        let planner = choose_planner(PlannerType::SKU(sku));
        assert_eq!(planner.ask_internal(), "Basic SKU Planning Service Response");

        // Create test Operation
        let output_sku = SKU::from_name("output");
        let input_sku = SKU::from_name("input");
        let _produce_flow = MaterialFlowVariant::Single(Flow::new(false, 1.0, output_sku));
        let _consume_flow = MaterialFlowVariant::Single(Flow::new(true, 1.0, input_sku));
        
        let operation1 = Operation::new(
            "test_operation".to_string(),
            1,
            10,
            1,
            MaterialFlowVariant::None,
            MaterialFlowVariant::None,
            ResourceFlowVariant::None
        );
        
        let planner = choose_planner(PlannerType::Operation(operation1.clone()));
        assert_eq!(planner.ask_internal(), "Operation Planning Service Response");

        let operation2 = Operation::new(
            "test_operation2".to_string(),
            1,
            10,
            1,
            MaterialFlowVariant::None,
            MaterialFlowVariant::None,
            ResourceFlowVariant::None
        );

        let alt_operation = AlternateOperation::new("test_alternate".to_string());
        {
            let mut alt_op_guard = alt_operation.lock();
            alt_op_guard.add_alternate(operation1.clone());
            alt_op_guard.add_alternate(operation2.clone());
        }
        
        {
            operation1.lock().set_parent_operation(OperationVariant::Alternate(alt_operation.clone()));
            operation2.lock().set_parent_operation(OperationVariant::Alternate(alt_operation.clone()));
        }

        let planner = choose_planner(PlannerType::AlternateOperation(alt_operation));
        assert_eq!(planner.ask_internal(), "Alternate Operation Planning Service Response");
    }
} 