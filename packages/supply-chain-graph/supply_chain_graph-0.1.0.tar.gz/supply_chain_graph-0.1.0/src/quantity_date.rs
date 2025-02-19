use chrono::NaiveDate;
use std::fmt;

#[derive(Debug, Clone)]
pub struct QuantityDate {
    quantity: f64,
    date: NaiveDate,
}

impl QuantityDate {
    pub fn new(quantity: f64, date: NaiveDate) -> Self {
        QuantityDate {
            quantity,
            date,
        }
    }

    pub fn get_quantity(&self) -> f64 {
        self.quantity
    }

    pub fn get_date(&self) -> NaiveDate {
        self.date
    }

    pub fn set_quantity(&mut self, quantity: f64) {
        self.quantity = quantity;
    }

    pub fn set_date(&mut self, date: NaiveDate) {
        self.date = date;
    }

    pub fn unschedule(&self) -> Result<(), String> {
        Err("This method 'unschedule' should not be called.".to_string())
    }

    pub fn create(&self) -> Result<(), String> {
        Err("This method 'create' should not be called.".to_string())
    }
}

impl fmt::Display for QuantityDate {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "QuantityDate{{quantity: {}, date: {}}}", self.quantity, self.date)
    }
} 