use crate::flow::Flow;
use crate::demand::Demand;
use std::sync::Arc;
use parking_lot::Mutex;
use crate::sku::SKU;
use crate::alternate_operation::AlternateOperation;

#[derive(Debug)]
pub enum Motivator {
    DemandMotive(Arc<Mutex<Demand>>), // Demand can motivate FG SKU
    FlowMotive(Arc<Mutex<Flow>>), // Produced Flow from Operation can motivate SKU
    SKUMotive(Arc<Mutex<SKU>>), // SKU can motivate Operation/Alternate Operation
    AlternateMotive(Arc<Mutex<AlternateOperation>>), // Alternate Operation can motivate SKU
    None,
}
