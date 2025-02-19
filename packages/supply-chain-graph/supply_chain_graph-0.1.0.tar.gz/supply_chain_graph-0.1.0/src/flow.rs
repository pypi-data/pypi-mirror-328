use crate::constants::FlowType;
use crate::iflow::IFlow;
use crate::sku::SKU;
use std::sync::Arc;
use parking_lot::Mutex;
use chrono::NaiveDate;

#[derive(Debug,Clone)]
pub struct FlowPlan {
    flow: Arc<Mutex<Flow>>,
    quantity: f64,
    // This date repesent the date of conumption/production depending on the flow type
    date: NaiveDate,
}

impl FlowPlan {
    pub fn new(flow: Arc<Mutex<Flow>>, quantity: f64, date: NaiveDate) -> Self {
        FlowPlan { flow, quantity, date }
    }

    pub fn get_flow(&self) -> Arc<Mutex<Flow>> {
        self.flow.clone()
    }

    pub fn get_quantity(&self) -> f64 {
        self.quantity
    }

    pub fn set_quantity(&mut self, quantity: f64) {
        self.quantity = quantity;
    }

    pub fn get_date(&self) -> NaiveDate {
        self.date
    }

    pub fn get_sku(&self) -> Arc<Mutex<SKU>> {
        self.flow.lock().get_sku()
    }

    pub fn print_flow_plan_header() {
        println!("{:<20}{:<15}{:<15}{:<30}{:<20}", " ", "Flow Qty", "Date", "SKU", "Type");
    }
    pub fn print_flow_plan(&self) {
        println!("{:<20}{:<15.2}{:<15}{:<30}{:<20}",
            " ",
            self.get_quantity(),
            self.get_date().format("%Y-%m-%d").to_string(),
            self.get_sku().lock().name().to_string(),
            if self.flow.lock().is_consume_flow() { "Consume" } else { "Produce" }
        );
    }
}

#[derive(Debug)]
pub struct Flow {
    is_consume_flow: bool,
    quantity_per: f64,
    sku: Arc<Mutex<SKU>>,
}

impl Flow {
    pub fn new(is_consume_flow: bool, quantity_per: f64, sku: Arc<Mutex<SKU>>) -> Arc<Mutex<Self>> {
        Arc::new(Mutex::new(Flow {
            is_consume_flow,
            quantity_per,
            sku,
        }))
    }

    pub fn is_consume_flow(&self) -> bool {
        self.is_consume_flow
    }

    pub fn is_produce_flow(&self) -> bool {
        !self.is_consume_flow
    }

    pub fn set_consume_flow(&mut self, is_consume_flow: bool) {
        self.is_consume_flow = is_consume_flow;
    }

    pub fn set_quantity_per(&mut self, quantity_per: f64) {
        self.quantity_per = quantity_per;
    }

    pub fn get_quantity_per(&self) -> f64 {
        self.quantity_per
    }

    pub fn get_sku(&self) -> Arc<Mutex<SKU>> {
        self.sku.clone()
    }

    pub fn get(&self) -> &Flow {
        return &self;
    } 

}

impl IFlow for Flow {
    fn flow_type(&self) -> FlowType {
        if self.is_consume_flow {
            FlowType::Consume
        } else {
            FlowType::Produce
        }
    }
}

impl IntoIterator for Flow {
    type Item = Flow;
    type IntoIter = std::iter::Once<Flow>;

    fn into_iter(self) -> Self::IntoIter {
        std::iter::once(self)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    fn setup_test_sku(name: &str) -> Arc<Mutex<SKU>> {
        SKU::new(name)
    }

    #[test]
    fn test_flow_creation() {
        let sku = setup_test_sku("Test SKU");
        let flow = Flow::new(true, 10.5, sku.clone());
        
        assert!(flow.lock().is_consume_flow());
        assert!(!flow.lock().is_produce_flow());
        assert_eq!(flow.lock().get_quantity_per(), 10.5);
        assert_eq!(flow.lock().get_sku().lock().name(), "Test SKU");
    }

    #[test]
    fn test_flow_type_transitions() {
        let sku = setup_test_sku("Test SKU");
        let flow = Flow::new(true, 1.0, sku);
        
        // Test initial state
        assert!(flow.lock().is_consume_flow());
        assert_eq!(flow.lock().flow_type(), FlowType::Consume);

        // Test transition to produce flow
        flow.lock().set_consume_flow(false);
        assert!(!flow.lock().is_consume_flow());
        assert!(flow.lock().is_produce_flow());
        assert_eq!(flow.lock().flow_type(), FlowType::Produce);
    }

    #[test]
    fn test_quantity_modifications() {
        let sku = setup_test_sku("Test SKU");
        let flow = Flow::new(true, 1.0, sku);
        
        assert_eq!(flow.lock().get_quantity_per(), 1.0);
        
        flow.lock().set_quantity_per(2.5);
        assert_eq!(flow.lock().get_quantity_per(), 2.5);
        
        flow.lock().set_quantity_per(0.0);
        assert_eq!(flow.lock().get_quantity_per(), 0.0);
        
        flow.lock().set_quantity_per(-1.0);
        assert_eq!(flow.lock().get_quantity_per(), -1.0);
    }

    #[test]
    fn test_sku_reference() {
        let sku = setup_test_sku("Test SKU");
        let flow = Flow::new(true, 10.5, sku.clone());
        
        assert_eq!(flow.lock().get_sku().lock().name(), "Test SKU");
    }

    #[test]
    fn test_flow_plan_print() {
        let sku = setup_test_sku("Test SKU");
        let flow = Flow::new(true, 10.5, sku.clone());
        let flow_plan = FlowPlan::new(flow, 10.5, NaiveDate::from_ymd_opt(2024, 1, 1).unwrap());
        flow_plan.print_flow_plan();
    }
} 

