use std::sync::Arc;
use parking_lot::Mutex;
use chrono::NaiveDate;
use chrono::Duration;
use log::{info, error};

use crate::operation::Operation;
use crate::planning_service::PlanningService;
use crate::specification::Specification;
use crate::plan_proposal::ProposalStack;
use crate::sku::SKU;
use crate::operation::MaterialFlowVariant;
use crate::operation::ResourceFlowVariant;

use crate::constants::PRECISION;
use crate::plan_proposal::Proposal;
use crate::planner::{choose_planner, PlannerType};
use crate::motivator::Motivator;
use crate::utilities::unique::generate_unique_id;
use crate::flow::Flow;
use crate::operation::EffectivePeriod;


#[derive(Debug)]
pub struct BasicOperationPlanningService {
    operation: Arc<Mutex<Operation>>,
}


impl PlanningService for BasicOperationPlanningService {
    fn ask_internal(&self) -> String {
        "Operation Planning Service Response".to_string()
    }


    fn ask(&self, sku_quantity: f64, ask_date: NaiveDate, proposals: &mut ProposalStack, specification: &mut Specification, motivator: &mut Motivator) -> f64 {
        let operation = self.operation.lock();
        let mut total_promised_op_plan_qty = 0.0; // across all capacity pre builds
        let mut q_per = 1.0;
        let mut op_plan_quantity = sku_quantity;
        let op_name = operation.get_name().clone();

        // Adjust date for lead time
        let lead_time = operation.get_lead_time();
        let ask_date = ask_date - Duration::days(lead_time as i64);

        match operation.get_produce_flow() {
            MaterialFlowVariant::Single(flow) => {
                q_per = flow.lock().get_quantity_per();
                op_plan_quantity = sku_quantity / q_per;
                // lotsize above
                op_plan_quantity = operation.get_lot_sized_quantity(op_plan_quantity, ask_date, false);
            },
            MaterialFlowVariant::Simultaneous(_) => {
                error!("Co-product flows not yet supported");
                return 0.0;
            },
            MaterialFlowVariant::None => (),
        }

        if specification.trace_current_demand() {
            info!("{}Need to Operation:{} Quantity:{} on {} q_per:{},minlot:{},increment:{}", specification.add_indent(), op_name.clone(), op_plan_quantity, ask_date, q_per, operation.get_min_lot(), operation.get_increment());
        }

        drop(operation);

        let mut resource_proposals = ProposalStack::new();
        let  (mut promised_op_plan_qty_from_resource, mut capacity_available_date) = self.ask_capacity(op_plan_quantity, ask_date, &mut resource_proposals, specification, &motivator);

        let mut capacity_is_available = promised_op_plan_qty_from_resource > PRECISION;
        let mut material_is_available = true;
        let mut ask_satisfied = false;

        while capacity_is_available && material_is_available && !ask_satisfied {
            // Check promise from SKUs now given that we have a promise of promised_op_plan_qty_from_resource from resources
            let mut sku_proposals = Vec::new();
            let promised_op_plan_qty = self.ask_material(promised_op_plan_qty_from_resource, capacity_available_date, &mut sku_proposals, specification);

            if promised_op_plan_qty < promised_op_plan_qty_from_resource - PRECISION {
                material_is_available = false;
            }

            total_promised_op_plan_qty += promised_op_plan_qty;

            // Add all SKU proposals to the main proposal stack
            let id = generate_unique_id();
            for (_sku, mut proposal) in sku_proposals {
                proposal.set_top_proposal_id(id); // only one proposal per SKU is returned at max and this sets the id on it
                proposals.merge_with_clear(&mut proposal);
            }

            if !material_is_available && !resource_proposals.is_empty() {
                Proposal::adjust_resource_proposals(&mut resource_proposals, promised_op_plan_qty, id);
            }
            resource_proposals.play_all(); // now reduce capacity
            resource_proposals.set_top_proposal_id(id);
            proposals.merge_with_clear(&mut resource_proposals);

            if promised_op_plan_qty > 0.0 {
                let inner_oper = self.operation.lock();
                match inner_oper.get_produce_flow() {
                    MaterialFlowVariant::Single(flow) => {
                        q_per = flow.lock().get_quantity_per();
                        let sku_quantity = promised_op_plan_qty * q_per;
                        let mut op_proposal = Proposal::new_flow(flow.clone(), sku_quantity, capacity_available_date + Duration::days(lead_time as i64));
                        op_proposal.play();
                        op_proposal.set_id(id);
                        proposals.push(op_proposal);
                        
                        // Op Plan placeholder to bind all flow plans into an operation plan
                        let mut op_plan_proposal = Proposal::new_operation_plan(self.operation.clone(), promised_op_plan_qty, capacity_available_date, capacity_available_date + Duration::days(lead_time as i64));
                        op_plan_proposal.set_id(id);
                        proposals.push(op_plan_proposal);
                    },
                    MaterialFlowVariant::Simultaneous(_) => {
                        error!("Co-product flows not yet supported");
                        return 0.0;
                    },
                    MaterialFlowVariant::None => (),
                }
            }
            if total_promised_op_plan_qty < op_plan_quantity - PRECISION {
                if material_is_available {
                    let remaining_ask_op_quantity = op_plan_quantity - total_promised_op_plan_qty;
                    (promised_op_plan_qty_from_resource, capacity_available_date) = self.ask_capacity(remaining_ask_op_quantity, capacity_available_date, &mut resource_proposals, specification, &motivator);
                    capacity_is_available = promised_op_plan_qty_from_resource > PRECISION;
                }
            }
            else {
                ask_satisfied = true;
            }
        }

        if specification.trace_current_demand() {
            info!("{}Promise from Operation: {} is {}", specification.get_indent_string(),op_name.clone(),total_promised_op_plan_qty);
            specification.remove_indent();
        }
        total_promised_op_plan_qty * q_per

    }
}


impl BasicOperationPlanningService {
    pub fn new(operation: Arc<Mutex<Operation>>) -> Self {
        BasicOperationPlanningService { operation }
    }

    // returns the lot sized quantity of op plans that can be created on the available date
    // op_quantity is already lot sized. This function also checks for capacity during the effective period.
    // If the resource is not attached it still checks for operation effectivity to return the date
    fn ask_capacity(&self, op_quantity: f64, ask_date: NaiveDate, resource_proposals: &mut ProposalStack, specification: &mut Specification, motivator: &Motivator) -> (f64, NaiveDate) {
        let mut available_op_qty = op_quantity;
        let mut available_date = ask_date;

        let operation = self.operation.lock();
        match operation.get_resource_flow() {
            ResourceFlowVariant::None => {
                // if no effectivities modelled, this would still return the ask date
                if let Some(date) = operation.get_latest_effective_date(ask_date) {
                    available_date = date;
                }
                else {
                    available_op_qty = 0.0;
                }
            }
            ResourceFlowVariant::SingleResource(flow) => {
                let flow_ref = flow.lock();
                let resource = flow_ref.get_resource();
                let resource_ref = resource.lock();
                let quantity_per = flow_ref.get_quantity_per();
                let resource_name = resource_ref.get_name();

                // assume sku motive and initializr to operatiom effective periods
                let mut effective_periods: &Vec<EffectivePeriod> = operation.get_effective_periods();
                if specification.trace_current_demand() {
                    info!("{}Capacity required from: {} amount: {} on: {}", specification.add_indent(), resource_name, op_quantity*quantity_per, ask_date);
                    if effective_periods.len() > 0 {    
                        info!("{}Effectivity: {:?}",specification.get_indent_string(),effective_periods);
                    }
                }

                let is_alternate_motive = match motivator {
                    Motivator::AlternateMotive(_) => true,
                    _ => false,
                };
                if is_alternate_motive {
                    // for alternate motive, effective periods are not used
                    effective_periods = specification.get_effective_periods();
                }

                available_op_qty = 0.0;
                while available_op_qty < PRECISION {
                    // Get the latest bucket with capacity on or before passed date ensuring effectivity checks are applied
                    if let Some((date, bucket)) = resource_ref.find_day_and_bucket_with_available_capacity(available_date, effective_periods) {
                        available_date = date;
                        // Calculate how much op plan we can actually create based on resource capacity
                        let op_quantity_capacity = bucket.get_capacity() / quantity_per;

                        available_op_qty = if op_quantity_capacity < op_quantity {
                            // lotsize below if the remaining capacity is not sufficient
                            operation.get_lot_sized_quantity(op_quantity_capacity, available_date, true)
                        } else {
                            op_quantity
                        };

                        if available_op_qty >= PRECISION {
                            resource_proposals.push(Proposal::new_resource_flow_plan_with_id(flow.clone(), available_op_qty, available_date, 0));
                            break;
                        }
                        // Move to the day before this bucket's start date to check previous buckets
                        available_date = bucket.get_start_date() - Duration::days(1);
                    } else {
                        // No more buckets with capacity available
                        break;
                    }
                }

                if specification.trace_current_demand() {
                    info!("{}Capacity Promised by {} on {}, is {}", specification.get_indent_string(), resource_name, available_date, available_op_qty*quantity_per);
                    specification.remove_indent();
                }
            }
        }
        (available_op_qty, available_date)
    }
    
    fn ask_material_flows<'a>(
        &self,
        flows: impl Iterator<Item = &'a Arc<Mutex<Flow>>>,
        op_quantity: f64,
        ask_date: NaiveDate,
        sku_proposals: &mut Vec<(Arc<Mutex<SKU>>, ProposalStack)>,
        specification: &mut Specification,
    ) -> f64 {
        let mut min_available_op_qty = op_quantity;
        
        for flow in flows {
            let flow_ref = flow.lock();
            let sku = flow_ref.get_sku();
            let mut proposals = ProposalStack::new();
            let sku_quantity = op_quantity * flow_ref.get_quantity_per();
            
            let planner = choose_planner(PlannerType::SKU(sku.clone()));
            let mut motivator = Motivator::FlowMotive(flow.clone());
            drop(flow_ref);
            let available_sku_quantity = planner.ask(sku_quantity, ask_date, &mut proposals, specification, &mut motivator);
            let flow_ref = flow.lock();
            let sku = flow_ref.get_sku();
            if available_sku_quantity < (min_available_op_qty * flow_ref.get_quantity_per() - PRECISION) {
                min_available_op_qty = available_sku_quantity / flow_ref.get_quantity_per();
            }
            sku_proposals.push((sku, proposals));
        }
        
        min_available_op_qty
    }

    fn ask_material(&self, op_quantity: f64, ask_date: NaiveDate, 
        sku_proposals: &mut Vec<(Arc<Mutex<SKU>>, ProposalStack)>,
        specification: &mut Specification
    ) -> f64 {
        let operation = self.operation.lock();
        let mut min_available_op_qty : f64;
        match operation.get_consume_flow() {
            MaterialFlowVariant::Single(flow) => {
                min_available_op_qty = self.ask_material_flows(std::iter::once(flow), op_quantity, ask_date, sku_proposals, specification);
                //let operation = self.operation.lock();
                if min_available_op_qty <= op_quantity - PRECISION {
                    if operation.is_lot_sized() {
                        min_available_op_qty = operation.get_lot_sized_quantity(min_available_op_qty, ask_date, true);
                    }
                    drop(operation);
                    Proposal::undo_sku_proposals(sku_proposals);
                    if min_available_op_qty >= PRECISION {
                        let promised_op_plan_qty = self.ask_material(min_available_op_qty, ask_date, sku_proposals, specification);
                        if promised_op_plan_qty <= min_available_op_qty - PRECISION {
                            error!("Error: The promised quantity {} is less than minAvailableQty: {}", promised_op_plan_qty, min_available_op_qty);
                            Proposal::undo_sku_proposals(sku_proposals);
                            min_available_op_qty = 0.0;
                        }
                    }
                }
                min_available_op_qty
            },
            MaterialFlowVariant::Simultaneous(sim_flow) => {
                min_available_op_qty = self.ask_material_flows(sim_flow.lock().get_flows().iter(), op_quantity, ask_date, sku_proposals, specification);
                if min_available_op_qty <= op_quantity - PRECISION {
                    if operation.is_lot_sized() {
                        min_available_op_qty = operation.get_lot_sized_quantity(min_available_op_qty, ask_date, true);
                    }
                    drop(operation);
                    Proposal::undo_sku_proposals(sku_proposals);
                    if min_available_op_qty >= PRECISION {
                        let promised_op_plan_qty = self.ask_material(min_available_op_qty, ask_date, sku_proposals, specification);
                        if promised_op_plan_qty <= min_available_op_qty - PRECISION {
                            error!("Error: The promised quantity {} is less than minAvailableQty: {}", promised_op_plan_qty, min_available_op_qty);
                            Proposal::undo_sku_proposals(sku_proposals);
                            min_available_op_qty = 0.0;
                        }
                    }
                }
                min_available_op_qty
            },
            MaterialFlowVariant::None => op_quantity,
        }
    }

}

#[cfg(test)]
mod tests {
    use super::*;
    use chrono::NaiveDate;
    use crate::resource::Resource;
    use crate::resource_flow::ResourceFlow;
    use crate::specification::Specification;
    use crate::motivator::Motivator;

    #[test]
    fn test_ask_capacity_with_lot_sizing_and_effective_periods() {
        // Create a resource with capacity
        let resource = Resource::from_name("TestResource");
        let jan_1 = NaiveDate::from_ymd_opt(2024, 1, 1).unwrap();
        
        // Remove borrow_mut() - just use the MutexGuard directly
        let mut res = resource.lock();
        res.set_capacity(jan_1, 98.0);

        // Create operation with lot sizing rules (min_lot = 20, increment = 5)
        let operation = Operation::new(
            "LotSizedOp".to_string(),
            0,  // lead time
            20, // min lot
            5,  // increment
            MaterialFlowVariant::None,
            MaterialFlowVariant::None,
            ResourceFlowVariant::SingleResource(ResourceFlow::new(1.0, resource.clone())),
        );

        let planning_service = BasicOperationPlanningService::new(operation.clone());
        let mut proposals = ProposalStack::new();
        let mut spec = Specification::new(2, 0);
        let motivator = Motivator::None;
        drop(res);  // Explicitly drop the MutexGuard before next use

        // Test cases:
        // 1. Ask for quantity below min lot
        let (qty1, date1) = planning_service.ask_capacity(15.0, jan_1, &mut proposals, &mut spec, &motivator);
        assert_eq!(qty1, 15.0, "Quantity below min lot is not checked for lot sizing");

        // 2. Ask for quantity above lot
        let (qty2, date2) = planning_service.ask_capacity(22.0, jan_1, &mut proposals, &mut spec, &motivator);
        assert_eq!(qty2, 22.0, "Quantity should round down to nearest increment above min lot");

        // 3. Ask for quantity limited by resource capacity
        let (qty3, date3) = planning_service.ask_capacity(110.0, jan_1, &mut proposals, &mut spec, &motivator);
        assert_eq!(qty3, 95.0, "Quantity should be limited by resource capacity and rounded to increment");

        // Verify dates weren't changed
        assert_eq!(date1, jan_1);
        assert_eq!(date2, jan_1);
        assert_eq!(date3, jan_1);

        let feb_1 = NaiveDate::from_ymd_opt(2024, 2, 1).unwrap();
        // capacity lower than min lot
        {
            let mut res = resource.lock();  // New scope for MutexGuard
            res.set_capacity(jan_1, 98.0);
            res.set_capacity(feb_1, 5.0);
        }  // MutexGuard is dropped here

        let (qty, avail_date) = planning_service.ask_capacity(110.0, feb_1, &mut proposals, &mut spec, &motivator);
        assert_eq!(qty, 95.0, "Previous bucket is used");
        assert_eq!(avail_date, feb_1 - Duration::days(1), "Available date now in previous bucket than ends on feb_1");

        // Test with effective periods
        {
            let mut oper = operation.lock();
            oper.add_period(Some(jan_1), Some(jan_1 + Duration::days(5)), 1);
            oper.add_period(Some(jan_1 + Duration::days(10)), Some(jan_1 + Duration::days(15)), 1);
        }

        let (qty, avail_date) = planning_service.ask_capacity(110.0, feb_1, &mut proposals, &mut spec, &motivator);
        assert_eq!(qty, 95.0, "Available date now in previous bucket than ends on feb_1");
        assert_eq!(avail_date, jan_1 + Duration::days(14), "Available date now in previous bucket than ends on feb_1");
    }
}


