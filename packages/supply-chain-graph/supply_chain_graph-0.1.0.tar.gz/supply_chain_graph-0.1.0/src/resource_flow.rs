use crate::constants::FlowType;
use crate::iflow::IFlow;
use crate::resource::Resource;
use std::sync::Arc;
use parking_lot::Mutex;
use chrono::NaiveDate;

#[derive(Debug, Clone)]
pub struct ResourceFlowPlan {
    flow_ref: Arc<Mutex<ResourceFlow>>,
    quantity: f64,
    date: NaiveDate,
}

impl ResourceFlowPlan {
    pub fn new(flow_ref: Arc<Mutex<ResourceFlow>>, quantity: f64, date: NaiveDate) -> Self {
        ResourceFlowPlan { flow_ref, quantity, date }
    }

    pub fn get_flow_ref(&self) -> Arc<Mutex<ResourceFlow>> {
        self.flow_ref.clone()
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

    pub fn get_resource(&self) -> Arc<Mutex<Resource>> {
        self.flow_ref.lock().get_resource()
    }

    pub fn print_flow_plan_header() {
        println!("{:<20}{:<20}{:<15}{:<20}{:<20}", " ", "Flow Quantity", "Date", "Resource", "Type");
    }

    pub fn print_flow_plan(&self) {
        println!("{:<20}{:<20.2}{:<15}{:<20}{:<20}",
            " ",
            self.get_quantity(),
            self.get_date().format("%Y-%m-%d").to_string(),
            self.get_resource().lock().get_name().to_string(),
            "Consume"
        );
    }
}

#[derive(Debug)]
pub struct ResourceFlow {
    quantity_per: f64,
    resource: Arc<Mutex<Resource>>,
}

impl ResourceFlow {
    pub fn new(quantity_per: f64, resource: Arc<Mutex<Resource>>) -> Arc<Mutex<Self>> {
        Arc::new(Mutex::new(ResourceFlow {
            quantity_per,
            resource,
        }))
    }

    pub fn set_quantity_per(&mut self, quantity_per: f64) {
        self.quantity_per = quantity_per;
    }

    pub fn get_quantity_per(&self) -> f64 {
        self.quantity_per
    }

    pub fn get_resource(&self) -> Arc<Mutex<Resource>> {
        self.resource.clone()
    }

    pub fn get(&self) -> &ResourceFlow {
        return &self;
    }
}

impl IFlow for ResourceFlow {
    fn flow_type(&self) -> FlowType {
        FlowType::Consume
    }
}

impl IntoIterator for ResourceFlow {
    type Item = ResourceFlow;
    type IntoIter = std::iter::Once<ResourceFlow>;

    fn into_iter(self) -> Self::IntoIter {
        std::iter::once(self)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    fn setup_test_resource(name: &str) -> Arc<Mutex<Resource>> {
        Resource::from_name(name)
    }

    #[test]
    fn test_flow_creation() {
        let resource = setup_test_resource("Test Resource");
        let flow = ResourceFlow::new(10.5, resource.clone());
        
        assert_eq!(flow.lock().get_quantity_per(), 10.5);
        assert_eq!(flow.lock().get_resource().lock().get_name(), "Test Resource");
    }

    #[test]
    fn test_flow_type_transitions() {
        let resource = setup_test_resource("Test Resource");
        let flow = ResourceFlow::new(1.0, resource);
        assert_eq!(flow.lock().flow_type(), FlowType::Consume);
    }

    #[test]
    fn test_quantity_modifications() {
        let resource = setup_test_resource("Test Resource");
        let flow = ResourceFlow::new(1.0, resource);
        
        assert_eq!(flow.lock().get_quantity_per(), 1.0);
        
        flow.lock().set_quantity_per(2.5);
        assert_eq!(flow.lock().get_quantity_per(), 2.5);
        
        flow.lock().set_quantity_per(0.0);
        assert_eq!(flow.lock().get_quantity_per(), 0.0);
        
        flow.lock().set_quantity_per(-1.0);
        assert_eq!(flow.lock().get_quantity_per(), -1.0);
    }

    #[test]
    fn test_resource_reference() {
        let resource = setup_test_resource("Test Resource");
        let flow = ResourceFlow::new(10.5, resource.clone());
        
        assert_eq!(flow.lock().get_resource().lock().get_name(), "Test Resource");
    }

    #[test]
    fn test_flow_plan_print() {
        let resource = setup_test_resource("Test Resource");
        let flow = ResourceFlow::new(10.5, resource.clone());
        let flow_plan = ResourceFlowPlan::new(flow, 10.5, NaiveDate::from_ymd_opt(2024, 1, 1).unwrap());
        flow_plan.print_flow_plan();
    }
} 