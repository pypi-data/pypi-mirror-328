use std::f64;

pub const PRECISION: f64 = 0.000001;

#[derive(Debug, Clone, PartialEq)]
pub enum LocationType {
    Customer,
    DC,
    Plant,
    Warehouse,
    Store,
    Unspecified,
}

#[derive(Debug, Clone, PartialEq)]
pub enum FlowType {
    Produce,
    Consume,
    Simultaneous,
    AlternateMaterial,
    AltConsume,
    CoProduce,
    Resource,
    Default, // 
}

#[derive(Debug, Clone, PartialEq)]
pub enum OperationType {
    Simple,
    MultiStep,
    Alternate,
    EffectiveAlternate,
}

#[derive(Debug, Clone, PartialEq)]
pub enum SKUType {
    Simple,
    Optimal,
    Unlimited,
    Supply,
} 