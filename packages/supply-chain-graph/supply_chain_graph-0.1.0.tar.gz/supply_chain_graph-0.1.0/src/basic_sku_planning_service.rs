use std::sync::Arc;
use parking_lot::Mutex;
use crate::sku::SKU;
use crate::planning_service::PlanningService;
use crate::specification::Specification;
use crate::plan_proposal::ProposalStack;
use chrono::NaiveDate;
use crate::plan_proposal::Proposal;

use crate::constants::PRECISION;
use log::info;
use crate::planner::{choose_planner, PlannerType};
use crate::motivator::Motivator;
use crate::operation::OperationVariant;

#[derive(Debug)]
pub struct BasicSKUPlanningService {
    sku: Arc<Mutex<SKU>>,
}


impl PlanningService for BasicSKUPlanningService {
    fn ask_internal(&self) -> String {
        "Basic SKU Planning Service Response".to_string()
    }

    fn ask(&self, sku_quantity: f64, ask_date: NaiveDate, proposals: &mut ProposalStack, specification: &mut Specification, motivator: &mut Motivator) -> f64 {
        let sku_guard = self.sku.lock();
        let sku_name = sku_guard.name().to_string();
        let inventory_profile = sku_guard.get_inventory_profile();
        let available_qty = inventory_profile.get_available_inventory(&ask_date);
        let mut sku_motivator = Motivator::SKUMotive(self.sku.clone());

        if specification.trace_current_demand() {
            info!("{}Material required from: {} : {} on {} available: {}", specification.add_indent(), sku_name, sku_quantity, ask_date, available_qty);
        }

        let mut total_promised_sku_qty = 0.0;
        let top_producing_operation = sku_guard.get_top_producing_operation().clone();
        drop(sku_guard);

        if available_qty >= sku_quantity - PRECISION {
            total_promised_sku_qty = sku_quantity;
        } else {
            if available_qty >= PRECISION {
                total_promised_sku_qty = available_qty;
            }
            let remaining_qty = sku_quantity - total_promised_sku_qty;
            
            match top_producing_operation {
                OperationVariant::Basic(operation) => {
                    let planner = choose_planner(PlannerType::Operation(operation.clone()));
                    let mut op_promise = planner.ask(remaining_qty, ask_date, proposals, specification, &mut sku_motivator);
                    if op_promise >= remaining_qty {
                        op_promise = remaining_qty;
                    }
                    total_promised_sku_qty = total_promised_sku_qty + op_promise;
                },
                OperationVariant::Alternate(operation) => {
                    let planner = choose_planner(PlannerType::AlternateOperation(operation.clone()));
                    let mut op_promise = planner.ask(remaining_qty, ask_date, proposals, specification, &mut sku_motivator);
                    if op_promise >= remaining_qty {
                        op_promise = remaining_qty;
                    }
                    total_promised_sku_qty = total_promised_sku_qty + op_promise;
                },
                OperationVariant::None => {
                    // No operation available to produce more
                }
            }
        }

        let proposal = match motivator {
            Motivator::FlowMotive(flow) => { 
                Proposal::new_flow(flow.clone(), total_promised_sku_qty, ask_date)
            },
            _ => {
                Proposal::new_delivery(self.sku.clone(), total_promised_sku_qty, ask_date)
            }
        };

        proposal.play();
        proposals.push(proposal);

        if specification.trace_current_demand() {
            info!("{}Material Promised by {} is {}", specification.get_indent_string(), sku_name, total_promised_sku_qty);
            specification.remove_indent();
        }
        total_promised_sku_qty
    }
}

impl BasicSKUPlanningService {
    pub fn new(sku: Arc<Mutex<SKU>>) -> Self {
        BasicSKUPlanningService { sku }
    }



} 
