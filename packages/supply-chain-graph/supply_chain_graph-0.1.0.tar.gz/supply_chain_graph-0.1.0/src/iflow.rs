use std::fmt::Debug;
use crate::constants::FlowType;

pub trait IFlow: Debug {
    fn flow_type(&self) -> FlowType;
} 