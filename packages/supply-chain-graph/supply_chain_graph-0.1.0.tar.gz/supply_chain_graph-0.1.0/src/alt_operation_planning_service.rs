use chrono::NaiveDate;
use log::info;
use std::sync::Arc;
use parking_lot::Mutex;

use crate::planning_service::PlanningService;
use crate::specification::Specification;
use crate::plan_proposal::ProposalStack;

use crate::constants::PRECISION;
use crate::planner::{choose_planner, PlannerType};
use crate::motivator::Motivator;
use crate::alternate_operation::AlternateOperation;

#[derive(Debug)]
pub struct AltOperationPlanningService {
    alternate_operation: Arc<Mutex<AlternateOperation>>,
}


impl PlanningService for AltOperationPlanningService {
    fn ask_internal(&self) -> String {
        "Alternate Operation Planning Service Response".to_string()
    }

    fn ask(&self, sku_quantity: f64, ask_date: NaiveDate, proposals: &mut ProposalStack, specification: &mut Specification, _motivator: &mut Motivator) -> f64 {
        let mut total_promised_qty = 0.0;
        let mut remaining_qty = sku_quantity;
        let mut alt_op = self.alternate_operation.lock();
        let op_name = alt_op.get_name().to_string();
        
        if specification.trace_current_demand() {
            info!("{}Need from Alternate Operation:{} Quantity:{} on {}", 
                specification.add_indent(), op_name, sku_quantity, ask_date);
        }

        // Get periods in reverse chronological order
        let periods: Vec<_> = alt_op.find_periods_reverse_iter(ask_date).collect();
        let mut op_proposals_across_alternates = ProposalStack::new();
        // Try each period in priority order
        for period in periods {
            if remaining_qty < PRECISION {
                break;
            }

            // Update specification with current period. priority is non needed here
            specification.set_effective_period(period.from, period.till);
            
            // Try each operation in the period. Note that operations are sorted by priority already. 
            // Lower priority number means higher precedence except if it is <= 0
            for op_priority in &period.operation_priority {
                if op_priority.1 <= 0 {
                    continue;
                }
                let _p1 = period.from;
                let alt_operation = op_priority.0.clone();
                let planner = choose_planner(PlannerType::Operation(alt_operation.clone()));
                let mut motivator = Motivator::AlternateMotive(self.alternate_operation.clone());
                
                let mut alt_op_proposals = ProposalStack::new();
                let promised_qty = planner.ask(remaining_qty,ask_date,&mut alt_op_proposals,specification,&mut motivator);

                total_promised_qty += promised_qty;
                remaining_qty -= promised_qty;

                if promised_qty > PRECISION {
                    op_proposals_across_alternates.merge_with_clear(&mut alt_op_proposals);
                }

                if remaining_qty < PRECISION {
                    break;
                }
            }
        }

        if specification.trace_current_demand() {
            info!("{}Promise from Alternate Operation: {} is {}", 
                specification.get_indent_string(), op_name, total_promised_qty);
            specification.remove_indent();
        }
        specification.reset_effective_period();

        proposals.merge_with_clear(&mut op_proposals_across_alternates);
        total_promised_qty
    }
}


impl AltOperationPlanningService {
    pub fn new(operation: Arc<Mutex<AlternateOperation>>) -> Self {
        AltOperationPlanningService { alternate_operation: operation }
    }
}