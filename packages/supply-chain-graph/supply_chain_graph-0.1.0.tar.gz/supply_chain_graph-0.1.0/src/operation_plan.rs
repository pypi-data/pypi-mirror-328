use chrono::NaiveDate;
use crate::flow::FlowPlan;
use std::sync::Arc;
use parking_lot::Mutex;
use crate::resource_flow::ResourceFlowPlan;

#[derive(Debug)]
pub struct OperationPlan {
    start_date: NaiveDate,
    end_date: NaiveDate,
    quantity: f64,
    in_flows: Vec<Arc<Mutex<FlowPlan>>>,
    out_flows: Vec<Arc<Mutex<FlowPlan>>>,
    in_resource_flows: Vec<Arc<Mutex<ResourceFlowPlan>>>,
    // capacity plans to be added
}

impl OperationPlan {
    pub fn new(
        start_date: NaiveDate,
        end_date: NaiveDate,
        quantity: f64,
    ) -> Self {
        OperationPlan {
            start_date,
            end_date,
            quantity,
            in_flows: vec![],
            out_flows: vec![],
            in_resource_flows: vec![],
        }
    }

    pub fn get_start_date(&self) -> NaiveDate {
        self.start_date
    }

    pub fn set_start_date(&mut self, start_date: NaiveDate) {
        self.start_date = start_date;
    }

    pub fn get_end_date(&self) -> NaiveDate {
        self.end_date
    }

    pub fn set_end_date(&mut self, end_date: NaiveDate) {
        self.end_date = end_date;
    }

    pub fn get_quantity(&self) -> f64 {
        self.quantity
    }

    pub fn set_quantity(&mut self, quantity: f64) {
        self.quantity = quantity;
    }

    pub fn add_in_flow(&mut self, flow: Arc<Mutex<FlowPlan>>) {
        self.in_flows.push(flow);
    }

    pub fn add_out_flow(&mut self, flow: Arc<Mutex<FlowPlan>>) {
        self.out_flows.push(flow);
    }

    pub fn add_in_resource_flow(&mut self, flow: Arc<Mutex<ResourceFlowPlan>>) {
        self.in_resource_flows.push(flow);
    }

    pub fn get_in_flows(&self) -> &Vec<Arc<Mutex<FlowPlan>>> {
        &self.in_flows
    }

    pub fn get_out_flows(&self) -> &Vec<Arc<Mutex<FlowPlan>>> {
        &self.out_flows
    }

    pub fn get_in_resource_flows(&self) -> &Vec<Arc<Mutex<ResourceFlowPlan>>> {
        &self.in_resource_flows
    }

    pub fn print_operation_plan_header() {
        println!("{:<20}{:<15}{:<15}{:<30}", "Quantity", "Start Date", "End Date", "Operation");
    }

    pub fn print_operation_plan(&self, operation_name: &str ) {
        println!("{:<20}{:<15}{:<15}{:<30}", 
            self.quantity, 
            self.get_start_date().format("%Y-%m-%d").to_string(), 
            self.get_end_date().format("%Y-%m-%d").to_string(), 
            operation_name
        );
        FlowPlan::print_flow_plan_header();
        for in_flow in self.get_in_flows() {
            in_flow.lock().print_flow_plan();
        }
        for out_flow in self.get_out_flows() {
            out_flow.lock().print_flow_plan();
        }
    }

}