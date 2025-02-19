use crate::constants::OperationType;

pub trait IOperation {
    fn operation_type(&self) -> OperationType;
} 