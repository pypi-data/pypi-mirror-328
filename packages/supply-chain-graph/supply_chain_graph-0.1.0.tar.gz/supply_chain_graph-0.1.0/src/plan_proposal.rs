use chrono::NaiveDate;
use crate::flow::Flow;
use crate::sku::SKU;
use crate::flow::FlowPlan;
use crate::operation::Operation;
use std::collections::HashMap;
use crate::operation_plan::OperationPlan;
use crate::resource_flow::ResourceFlowPlan;
use crate::resource_flow::ResourceFlow;
use log::info;
use crate::constants::PRECISION;
use std::sync::Arc;
use parking_lot::Mutex;

#[derive(Debug)]
pub enum Proposal {
    OperationPlanType {
        operation: Arc<Mutex<Operation>>,
        id: u32, // same id tells that flow plans can be tied together into an operation plan
        quantity: f64,
        start_date: NaiveDate,
        end_date: NaiveDate,
    },
    FlowPlanType {
        flow_plan: FlowPlan,
        id: u32, // same id tells that flow plans can be tied together into an operation plan
    },
    ResourceFlowPlanType {
        flow_plan: ResourceFlowPlan,
        id: u32, 
    },
    DeliveryPlanType {
        sku: Arc<Mutex<SKU>>,
        quantity: f64,
        date: NaiveDate,
        id: u32,
    },
}

// id here helps with understanding which flow plans can be tied together into an operation plan
impl Proposal {
    pub fn new_flow(flow: Arc<Mutex<Flow>>, quantity: f64, date: NaiveDate) -> Self {
        Proposal::FlowPlanType {
            flow_plan: FlowPlan::new(flow, quantity, date),
            id: 0,
        }
    }

    pub fn new_flow_with_id(flow: Arc<Mutex<Flow>>, quantity: f64, date: NaiveDate, id: u32) -> Self {
        Proposal::FlowPlanType {
            flow_plan: FlowPlan::new(flow, quantity, date),
            id,
        }
    }

    pub fn new_delivery(sku: Arc<Mutex<SKU>>, quantity: f64, date: NaiveDate) -> Self {
        Proposal::DeliveryPlanType { sku, quantity, date, id: 0 }
    }

    pub fn new_delivery_with_id(sku: Arc<Mutex<SKU>>, quantity: f64, date: NaiveDate, id: u32) -> Self {
        Proposal::DeliveryPlanType { sku, quantity, date, id }
    }

    pub fn new_operation_plan(operation: Arc<Mutex<Operation>>, quantity: f64, start_date: NaiveDate, end_date: NaiveDate) -> Self {
        Proposal::OperationPlanType { operation, id: 0, quantity, start_date, end_date }
    }

    pub fn new_operation_plan_with_id(operation: Arc<Mutex<Operation>>, quantity: f64, start_date: NaiveDate, end_date: NaiveDate, id: u32) -> Self {
        Proposal::OperationPlanType { operation, id, quantity, start_date, end_date }
    }

    pub fn new_resource_flow_plan(resource_flow: Arc<Mutex<ResourceFlow>>, quantity: f64, date: NaiveDate) -> Self {
        Proposal::ResourceFlowPlanType { flow_plan: ResourceFlowPlan::new(resource_flow, quantity, date), id: 0 }
    }

    pub fn new_resource_flow_plan_with_id(resource_flow: Arc<Mutex<ResourceFlow>>, quantity: f64, date: NaiveDate, id: u32) -> Self {
        Proposal::ResourceFlowPlanType { flow_plan: ResourceFlowPlan::new(resource_flow, quantity, date), id }
    }

    pub fn play(&self) {
        match self {
            Proposal::FlowPlanType { flow_plan, ..} => {
                let flow = flow_plan.get_flow();
                let flow_guard = flow.lock();
                let sku = flow_guard.get_sku();
                let quantity = flow_plan.get_quantity();
                
                let mut sku_guard = sku.lock();
                if flow_guard.is_produce_flow() {
                    sku_guard.inventory_profile().add_inventory(flow_plan.get_date(), quantity);
                } else {
                    sku_guard.inventory_profile().remove_inventory(flow_plan.get_date(), quantity);
                }
            },
            Proposal::DeliveryPlanType {sku, quantity, date, ..} => {
                sku.lock().inventory_profile().remove_inventory(*date, *quantity);
            },
            Proposal::ResourceFlowPlanType {flow_plan, ..} => {
                let flow = flow_plan.get_flow_ref();
                let flow_ref = flow.lock();
                let resource = flow_ref.get_resource();
                let quantity = flow_plan.get_quantity();
                let _ = resource.lock().remove_capacity(flow_plan.get_date(), quantity);
            },
            Proposal::OperationPlanType { .. } => {
                // do nothing
            }
        }
    }

    pub fn reset(&self) {
        match self {
            Proposal::FlowPlanType { flow_plan, .. } => {
                let flow = flow_plan.get_flow();
                let flow_guard = flow.lock();
                let sku = flow_guard.get_sku();
                let quantity = flow_plan.get_quantity();

                let mut sku_guard = sku.lock();
                if flow_guard.is_produce_flow() {
                    sku_guard.inventory_profile().remove_inventory(flow_plan.get_date(), quantity);
                } else {
                    sku_guard.inventory_profile().add_inventory(flow_plan.get_date(), quantity);
                }
            },
            Proposal::DeliveryPlanType { sku, quantity, date, .. } => {
                sku.lock().inventory_profile().add_inventory(*date, *quantity);
            },
            Proposal::ResourceFlowPlanType {flow_plan, ..} => {
                let flow = flow_plan.get_flow_ref();
                let flow_ref = flow.lock();
                let resource = flow_ref.get_resource();
                let quantity = flow_plan.get_quantity();
                let _ = resource.lock().add_capacity(flow_plan.get_date(), quantity);
            },
            Proposal::OperationPlanType { ..} => {
                // do nothing
            }
        }
    }

    pub fn get_quantity(&self) -> f64 {
        match self {
            Proposal::FlowPlanType { flow_plan, .. } => flow_plan.get_quantity(),
            Proposal::DeliveryPlanType { quantity, .. } => *quantity,
            Proposal::OperationPlanType { quantity, .. } => *quantity,
            Proposal::ResourceFlowPlanType {flow_plan, ..} => flow_plan.get_quantity(),
        }
    }

    pub fn print(&self) {
        match self {
            Proposal::FlowPlanType { flow_plan, id } => {
                let flow_ref_rc = flow_plan.get_flow();
                let flow_guard = flow_ref_rc.lock();
                let flow_type = if flow_guard.is_consume_flow() { "Consume" } else { "Produce" };
                info!("Id: {} {} {:?} of {:?} on {:?}", id, flow_type, flow_plan.get_quantity(), flow_guard.get_sku().lock().name(), flow_plan.get_date());
            },
            Proposal::ResourceFlowPlanType {flow_plan, id} => {
                let flow_ref_rc = flow_plan.get_flow_ref();
                let flow_ref = flow_ref_rc.lock();
                let flow_type = "Consume";
                info!("Id: {} {} {:?} of {:?} on {:?}", id, flow_type, flow_plan.get_quantity(), (*flow_ref).get_resource().lock().get_name(), flow_plan.get_date());
            },
            Proposal::DeliveryPlanType { sku, quantity, date, id } => info!("Id: {} Delivery: {:?} of {:?} on {:?}", id, quantity, sku.lock().name(), date),
            Proposal::OperationPlanType { operation, id, quantity, start_date, end_date } => {
                info!("Id: {} Operation: {:?} of {:?} from {:?} to {:?}", id, quantity, operation.lock().get_name(), start_date, end_date);
            }
        }
    }

    pub fn set_id(&mut self, new_id: u32) {
        match self {
            Proposal::FlowPlanType { id, .. } => *id = new_id,
            Proposal::DeliveryPlanType { id, .. } => *id = new_id,
            Proposal::OperationPlanType { id, .. } => *id = new_id,
            Proposal::ResourceFlowPlanType {id, ..} => *id = new_id,
        }
    }

    pub fn undo_sku_proposals(sku_proposals: &mut Vec<(Arc<Mutex<SKU>>, ProposalStack)>) {
        for (_sku, ref mut proposal) in sku_proposals.iter_mut() {
            proposal.reset_all();
        }
        sku_proposals.clear();
    }

    pub fn undo_resource_proposals(resource_proposals: &mut ProposalStack) {
        resource_proposals.reset_all();
    }

    pub fn adjust_resource_proposals(resource_proposals: &mut ProposalStack, op_quantity: f64, id: u32) {
        // if op_quantity is less than PRECISION then we need to undo the resource consumption proposal
        if op_quantity < PRECISION {
            resource_proposals.proposals.clear();
        }
        for proposal in &mut resource_proposals.proposals {
            if let Proposal::ResourceFlowPlanType { flow_plan, .. } = proposal {
                let flow = flow_plan.get_flow_ref();
                let quantity_per = flow.lock().get_quantity_per();
                flow_plan.set_quantity(op_quantity * quantity_per);
                proposal.set_id(id);
            }
        }

    }
}



#[derive(Debug)]
pub struct ProposalStack {
    proposals: Vec<Proposal>,
}

impl ProposalStack {
    pub fn new() -> Self {
        ProposalStack {
            proposals: Vec::new(),
        }
    }

    pub fn push(&mut self, proposal: Proposal) {
        self.proposals.push(proposal);
    }

    pub fn pop(&mut self) -> Option<Proposal> {
        self.proposals.pop()
    }

    pub fn play_all(&self) {
        for proposal in self.proposals.iter() {
            proposal.play();
        }
    }

    pub fn reset_all(&self) {
        for proposal in self.proposals.iter() {
            proposal.reset();
        }
    }

    pub fn len(&self) -> usize {
        self.proposals.len()
    }

    pub fn is_empty(&self) -> bool {
        self.proposals.is_empty()
    }

    pub fn merge(&mut self, other: ProposalStack) {
        self.proposals.extend(other.proposals);
    }

    pub fn merge_with_clear(&mut self, other: &mut  ProposalStack) {
        self.proposals.extend(other.proposals.drain(..));
    }

    pub fn clear(&mut self) {
        self.proposals.clear();
    }

    pub fn print(&self) {
        for proposal in self.proposals.iter() {
            proposal.print();
        }
    }

    pub fn set_top_proposal_id(&mut self, id: u32) -> bool {
        if let Some(proposal) = self.proposals.last_mut() {
            proposal.set_id(id);
            true
        } else {
            false
        }
    }


    pub fn create_operation_plans(&self) {
        // Create a map to store proposals by their IDs
        let mut id_groups: HashMap<u32, Vec<&Proposal>> = HashMap::new();
        let resize_plan = true;

        // Group proposals by their IDs
        for proposal in &self.proposals {
            match proposal {
                Proposal::OperationPlanType { id, .. } => {
                    id_groups.entry(*id).or_default().push(proposal);
                },
                Proposal::FlowPlanType { id, .. } => {
                    id_groups.entry(*id).or_default().push(proposal);
                },
                Proposal::ResourceFlowPlanType { id, .. } => {
                    id_groups.entry(*id).or_default().push(proposal);
                },
                _ => {} // Skip delivery plans
            }
        }

        // Process each group of proposals
        for (_id, proposals) in id_groups {
            // Find the operation plan proposal in the group
            if let Some(op_proposal) = proposals.iter().find(|p| matches!(p, Proposal::OperationPlanType { .. })) {
                if let Proposal::OperationPlanType { operation, quantity, start_date, end_date, .. } = op_proposal {
                    let mut scaled = false;
                    if resize_plan {
                        scaled = operation.lock().scale_operation_plan_with_matching_start_date(*quantity, *start_date);
                    }
                    if scaled {
                        continue;
                    }
                    
                    // Create new operation plan
                    let mut op_plan = OperationPlan::new(*start_date, *end_date, *quantity);

                    // Add flow plans
                    for proposal in proposals {
                        match proposal {
                            Proposal::FlowPlanType { flow_plan, .. } => {
                                let flow = flow_plan.get_flow();
                                let flow_plan = Arc::new(Mutex::new(flow_plan.clone()));
                                
                                if flow.lock().is_consume_flow() {
                                    op_plan.add_in_flow(flow_plan);
                                } else {
                                    op_plan.add_out_flow(flow_plan);
                                }
                            },
                            Proposal::ResourceFlowPlanType { flow_plan, .. } => {
                                let flow_plan = Arc::new(Mutex::new(flow_plan.clone()));
                                op_plan.add_in_resource_flow(flow_plan);
                            },
                            _ => {} // Skip other proposal types
                        }
                    }

                    // Add operation plan to the operation since scaling was unsucessful
                    operation.lock().add_operation_plan(op_plan, false);

                }
            }
        }
    } 
    
}

#[cfg(test)]
mod tests {
    use super::*;
    use chrono::NaiveDate;

    fn setup_test_date() -> NaiveDate {
        NaiveDate::from_ymd_opt(2024, 1, 1).unwrap()
    }

    fn setup_test_sku(name: &str) -> Arc<Mutex<SKU>> {
        SKU::from_name(name)
    }

    fn setup_test_flow(is_consume: bool, qty: f64, sku: Arc<Mutex<SKU>>) -> Arc<Mutex<Flow>> {
        Flow::new(is_consume, qty, sku)
    }

    fn setup_test_resource_flow(quantity_per: f64) -> Arc<Mutex<ResourceFlow>> {
        use crate::resource::Resource;
        let resource = Resource::from_name("Test Resource");
        ResourceFlow::new(quantity_per, resource)
    }

    #[test]
    fn test_proposal_flow_creation() {
        let sku = setup_test_sku("Test SKU");
        let flow = setup_test_flow(true, 10.0, sku);
        let date = setup_test_date();
        
        let proposal = Proposal::new_flow(flow, 5.0, date);
        
        match proposal {
            Proposal::FlowPlanType { flow_plan, id } => {
                assert_eq!(flow_plan.get_quantity(), 5.0);
                assert_eq!(id, 0);
            },
            _ => panic!("Expected FlowPlanType proposal"),
        }
    }

    #[test]
    fn test_proposal_delivery_creation() {
        let sku = setup_test_sku("Test SKU");
        let date = setup_test_date();
        
        let proposal = Proposal::new_delivery(sku.clone(), 15.0, date);
        
        match proposal {
            Proposal::DeliveryPlanType { quantity, .. } => {
                assert_eq!(quantity, 15.0);
            },
            _ => panic!("Expected DeliveryPlanType proposal"),
        }
    }

    #[test]
    fn test_proposal_play_and_reset() {
        let sku = setup_test_sku("Test SKU");
        let flow = setup_test_flow(true, 2.0, sku.clone());
        let date = setup_test_date();
        
        let proposal = Proposal::new_flow(flow, 5.0, date);
        
        // Initial inventory should be 0
        assert_eq!(sku.lock().inventory_profile().get_net_inventory(&date), 0.0);
        
        // Play should remove 5.0 from inventory
        proposal.play();
        assert_eq!(sku.lock().inventory_profile().get_net_inventory(&date), -5.0);
        
        // Reset should add back 5.0
        proposal.reset();
        assert_eq!(sku.lock().inventory_profile().get_net_inventory(&date), 0.0);
    }

    #[test]
    fn test_proposal_stack_operations() {
        let mut stack = ProposalStack::new();
        let sku = setup_test_sku("Test SKU");
        let date = setup_test_date();
        
        let proposal1 = Proposal::new_delivery(sku.clone(), 5.0, date);
        let proposal2 = Proposal::new_delivery(sku.clone(), 3.0, date);
        
        assert!(stack.is_empty());
        
        stack.push(proposal1);
        assert_eq!(stack.len(), 1);
        
        stack.push(proposal2);
        assert_eq!(stack.len(), 2);
        
        let popped = stack.pop();
        assert!(popped.is_some());
        assert_eq!(stack.len(), 1);
    }

    #[test]
    fn test_proposal_stack_merge() {
        let mut stack1 = ProposalStack::new();
        let mut stack2 = ProposalStack::new();
        let mut stack3 = ProposalStack::new();
        let sku = setup_test_sku("Test SKU");
        let date = setup_test_date();
        
        stack1.push(Proposal::new_delivery(sku.clone(), 5.0, date));
        stack2.push(Proposal::new_delivery(sku.clone(), 3.0, date));
        stack3.push(Proposal::new_delivery(sku.clone(), 6.0, date));
        
        assert_eq!(stack1.len(), 1);
        assert_eq!(stack2.len(), 1);
        
        stack1.merge(stack2);
        assert_eq!(stack1.len(), 2);

        stack1.merge_with_clear(&mut stack3);
        assert_eq!(stack1.len(), 3);
        assert_eq!(stack3.len(), 0);

    }

    #[test]
    fn test_adjust_resource_proposals() {
        let date = setup_test_date();
        let resource_flow = setup_test_resource_flow(2.0);
        let mut proposal_stack = ProposalStack::new();

        // Add a resource flow proposal
        proposal_stack.push(Proposal::new_resource_flow_plan(
            resource_flow.clone(),
            10.0,  // initial quantity
            date
        ));

        // Test case 1: Adjust with valid quantity
        Proposal::adjust_resource_proposals(&mut proposal_stack, 5.0, 42);
        
        // Check that quantity was adjusted (5.0 * 2.0 quantity_per = 10.0)
        if let Proposal::ResourceFlowPlanType { flow_plan, id } = &proposal_stack.proposals[0] {
            assert_eq!(flow_plan.get_quantity(), 10.0);
            assert_eq!(*id, 42);
        } else {
            panic!("Expected ResourceFlowPlanType");
        }

        assert!(proposal_stack.proposals.len() == 1);

        // Test case 2: Quantity below PRECISION should clear proposals
        Proposal::adjust_resource_proposals(&mut proposal_stack, PRECISION / 2.0, 42);
        assert!(proposal_stack.proposals.is_empty());
    }
}