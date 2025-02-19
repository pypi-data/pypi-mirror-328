use crate::constants::FlowType;
use crate::iflow::IFlow;
use crate::flow::Flow;
use log::error;
use std::sync::Arc;
use parking_lot::Mutex;

#[derive(Debug)]
pub struct SimultaneousFlow {
    flows: Vec<Arc<Mutex<Flow>>>,
}

impl SimultaneousFlow {
    fn validate_flows(flows: &[Arc<Mutex<Flow>>]) -> bool {
        if flows.is_empty() {
            return true;
        }
        let first_is_consume = flows[0].lock().is_consume_flow();
        flows.iter().all(|flow| flow.lock().is_consume_flow() == first_is_consume)
    }

    pub fn new(flows: Vec<Arc<Mutex<Flow>>>) -> Arc<Mutex<Self>> {
        if !Self::validate_flows(&flows) {
            panic!("All flows must be of the same type");
        }
        Arc::new(Mutex::new(SimultaneousFlow { flows }))
    }

    pub fn add_flow(&mut self, flow: Arc<Mutex<Flow>>) {
        // If this is the first flow, accept it
        if self.flows.is_empty() {
            self.flows.push(flow);
            return;
        }

        // Check if new flow matches the type of existing flows
        let existing_is_consume = self.flows[0].lock().is_consume_flow();
        let flow_is_consume = flow.lock().is_consume_flow();
        if flow_is_consume != existing_is_consume {
            error!(
                "Flow type mismatch. Expected {}, got {}",
                if existing_is_consume { "consume" } else { "produce" },
                if flow_is_consume { "consume" } else { "produce" }
            );
            return;
        }

        // Check if flow with this SKU already exists
        let flow_clone = flow.clone();
        let flow_ref = flow_clone.lock();
        let sku = flow_ref.get_sku().clone();
        let sku_ref = sku.lock();
        let new_sku_name = sku_ref.name().to_string();
        let quantity_per = flow_ref.get_quantity_per();
        drop(flow_ref);
        drop(sku_ref);
        
        if let Some(existing_flow) = self.flows.iter().find(|existing_flow| 
            existing_flow.lock().get_sku().lock().name().to_string() == new_sku_name
        ) {
            error!(
                "Flow with SKU {} already exists in simultaneous flow",
                new_sku_name
            );
            existing_flow.lock().set_quantity_per(quantity_per);
            return;
        }

        self.flows.push(flow);
    }

    pub fn get_flows(&self) -> &Vec<Arc<Mutex<Flow>>> {
        &self.flows
    }
}

impl IFlow for SimultaneousFlow {
    fn flow_type(&self) -> FlowType {
        FlowType::Simultaneous
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::sku::SKU;

    fn create_consume_flow() -> Arc<Mutex<Flow>> {
        Flow::new(true, 1.0, SKU::from_name("test_consume"))
    }

    fn create_produce_flow() -> Arc<Mutex<Flow>> {
        Flow::new(false, 1.0, SKU::from_name("test_produce"))
    }

    fn create_consume_flow_with_same_sku_name() -> Arc<Mutex<Flow>> {
        Flow::new(true, 2.0, SKU::from_name("test_consume"))
    }

    #[test]
    fn test_new_empty_simultaneous_flow() {
        let sim_flow = SimultaneousFlow::new(vec![]);
        assert_eq!(sim_flow.lock().get_flows().len(), 0);
    }

    #[test]
    fn test_add_first_flow() {
        let sim_flow = SimultaneousFlow::new(vec![]);
        sim_flow.lock().add_flow(create_consume_flow());
        assert_eq!(sim_flow.lock().get_flows().len(), 1);
        assert!(sim_flow.lock().get_flows()[0].lock().is_consume_flow());
    }

    #[test]
    fn test_add_same_flow() {
        let sim_flow = SimultaneousFlow::new(vec![create_consume_flow()]);
        sim_flow.lock().add_flow(create_consume_flow());
        assert_eq!(sim_flow.lock().get_flows().len(), 1);
    }

    #[test]
    fn test_add_incompatible_flows() {
        let sim_flow = SimultaneousFlow::new(vec![create_consume_flow()]);
        sim_flow.lock().add_flow(create_produce_flow());
        // Should not add incompatible flow
        assert_eq!(sim_flow.lock().get_flows().len(), 1);
    }

    #[test]
    #[should_panic(expected = "All flows must be of the same type")]
    fn test_new_with_incompatible_flows() {
        SimultaneousFlow::new(vec![
            create_consume_flow(),
            create_produce_flow(),
        ]);
    }

    #[test]
    fn test_flow_type() {
        let sim_flow = SimultaneousFlow::new(vec![]);
        let flow = sim_flow.lock();
        assert_eq!(flow.flow_type(), FlowType::Simultaneous);
    }

    #[test]
    fn test_add_flow_with_duplicate_sku() {
        let sim_flow = SimultaneousFlow::new(vec![create_consume_flow()]);
        let duplicate_flow = create_consume_flow_with_same_sku_name();
        sim_flow.lock().add_flow(duplicate_flow);
        // Should not add flow with duplicate SKU
        assert_eq!(sim_flow.lock().get_flows().len(), 1);
    }

    #[test]
    fn test_add_flow_with_different_sku() {
        let sim_flow = SimultaneousFlow::new(vec![create_consume_flow()]);
        let different_sku_flow = Flow::new(true, 1.0, SKU::from_name("different_sku"));
        sim_flow.lock().add_flow(different_sku_flow);
        // Should add flow with different SKU
        assert_eq!(sim_flow.lock().get_flows().len(), 2);
    }

    #[test]
    fn test_update_flow() {
        let sim_flow = SimultaneousFlow::new(vec![create_consume_flow()]);
        assert_eq!(sim_flow.lock().get_flows()[0].lock().get_quantity_per(), 1.0);
        sim_flow.lock().add_flow(create_consume_flow_with_same_sku_name());
        assert_eq!(sim_flow.lock().get_flows().len(), 1);
        assert!(sim_flow.lock().get_flows()[0].lock().is_consume_flow());
        assert_eq!(sim_flow.lock().get_flows()[0].lock().get_quantity_per(), 2.0);
    }
}
