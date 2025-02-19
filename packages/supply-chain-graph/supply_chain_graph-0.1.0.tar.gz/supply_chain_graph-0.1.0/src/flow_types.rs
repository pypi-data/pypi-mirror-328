use crate::constants::FlowType;
use crate::iflow::IFlow;
use crate::flow::Flow;
use crate::simultaneous_flow::SimultaneousFlow;
use std::sync::Arc;
use parking_lot::Mutex;


#[derive(Debug)]
pub enum ConsumeFlow {
    Single(Arc<Mutex<Flow>>),
    Simultaneous(Arc<Mutex<SimultaneousFlow>>),
}

impl ConsumeFlow {
    pub fn new_single(flow: Arc<Mutex<Flow>>) -> Self {
        assert!(flow.lock().is_consume_flow(), "Flow must be a consume flow");
        ConsumeFlow::Single(flow)
    }

    pub fn new_simultaneous(flows: Vec<Arc<Mutex<Flow>>>) -> Self {
        ConsumeFlow::Simultaneous(SimultaneousFlow::new(flows))
    }
}

impl IFlow for ConsumeFlow {
    fn flow_type(&self) -> FlowType {
        match self {
            ConsumeFlow::Single(_) => FlowType::Consume,
            ConsumeFlow::Simultaneous(_) => FlowType::Simultaneous,
        }
    }
}

#[derive(Debug)]
pub enum ProduceFlow {
    Single(Arc<Mutex<Flow>>),
    CoProduct(Arc<Mutex<SimultaneousFlow>>),
}

impl ProduceFlow {
    pub fn new_single(flow: Arc<Mutex<Flow>>) -> Self {
        assert!(!flow.lock().is_consume_flow(), "Flow must be a produce flow");
        ProduceFlow::Single(flow)
    }

    pub fn new_coproduct(flows: Vec<Arc<Mutex<Flow>>>) -> Self {
        assert!(flows.iter().all(|f| !f.lock().is_consume_flow()), 
            "All flows must be produce flows");
        ProduceFlow::CoProduct(SimultaneousFlow::new(flows))
    }
}

impl IFlow for ProduceFlow {
    fn flow_type(&self) -> FlowType {
        match self {
            ProduceFlow::Single(_) => FlowType::Produce,
            ProduceFlow::CoProduct(_) => FlowType::CoProduce,
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::sku::SKU;

    #[test]
    fn test_consume_flow_enum() {
        let sku1 = SKU::from_name("test1");
        let flow = Flow::new(true, 1.0, sku1);  // Already returns Arc<Mutex<Flow>>
        
        let single = ConsumeFlow::new_single(flow);
        assert_eq!(single.flow_type(), FlowType::Consume);
        
        let sku2 = SKU::from_name("test2");
        let sku3 = SKU::from_name("test3");
        let flows = vec![
            Flow::new(true, 1.0, sku2),
            Flow::new(true, 2.0, sku3),
        ];
        let simultaneous = ConsumeFlow::new_simultaneous(flows);
        assert_eq!(simultaneous.flow_type(), FlowType::Simultaneous);
    }

    #[test]
    fn test_produce_flow_enum() {
        let sku1 = SKU::from_name("test1");
        let flow = Flow::new(false, 1.0, sku1);  // Already returns Arc<Mutex<Flow>>
        
        let single = ProduceFlow::new_single(flow);
        assert_eq!(single.flow_type(), FlowType::Produce);
        
        let sku2 = SKU::from_name("test2");
        let sku3 = SKU::from_name("test3");
        let flows = vec![
            Flow::new(false, 1.0, sku2),
            Flow::new(false, 2.0, sku3),
        ];
        let coproduct = ProduceFlow::new_coproduct(flows);
        assert_eq!(coproduct.flow_type(), FlowType::CoProduce);
    }

    #[test]
    #[should_panic(expected = "Flow must be a consume flow")]
    fn test_invalid_consume_flow() {
        let sku = SKU::from_name("test");
        let flow = Flow::new(false, 1.0, sku); // produce flow
        ConsumeFlow::new_single(flow); // should panic
    }

    #[test]
    #[should_panic(expected = "Flow must be a produce flow")]
    fn test_invalid_produce_flow() {
        let sku = SKU::from_name("test");
        let flow = Flow::new(true, 1.0, sku); // consume flow
        ProduceFlow::new_single(flow); // should panic
    }
} 