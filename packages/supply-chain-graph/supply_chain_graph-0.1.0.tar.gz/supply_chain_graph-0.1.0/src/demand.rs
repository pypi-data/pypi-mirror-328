use chrono::NaiveDate;
use std::sync::Arc;
use parking_lot::Mutex;
use std::collections::HashMap;
use crate::sku::SKU;
use crate::quantity_date::QuantityDate;

lazy_static::lazy_static! {
    static ref DEMAND_REPOSITORY: Mutex<HashMap<String, Arc<Mutex<Demand>>>> = Mutex::new(HashMap::new());
}

#[derive(Debug)]
pub struct Demand {
    id: String,
    quantity: f64,
    request_date: NaiveDate,
    max_lateness: i32,
    sku: Arc<Mutex<SKU>>,
    pub priority: i32,
    pub demand_plans: Vec<QuantityDate>,
}

impl Demand {
    pub fn new(
        id: String,
        quantity: f64,
        request_date: NaiveDate,
        max_lateness: i32,
        sku: Arc<Mutex<SKU>>,
    ) -> Arc<Mutex<Self>> {
        let mut repo = DEMAND_REPOSITORY.lock();
        if let Some(existing_demand) = repo.get(&id) {
            return existing_demand.clone();
        }

        let demand = Arc::new(Mutex::new(Demand {
            id: id.clone(),
            quantity,
            request_date,
            max_lateness,
            sku,
            priority: i32::MAX,
            demand_plans: Vec::with_capacity(1),
        }));

        repo.insert(id, demand.clone());
        demand
    }

    // Repository methods
    pub fn find(id: &str) -> Option<Arc<Mutex<Demand>>> {
        DEMAND_REPOSITORY.lock().get(id).cloned()
    }

    pub fn exists(id: &str) -> bool {
        DEMAND_REPOSITORY.lock().contains_key(id)
    }

    pub fn get_all_demands() -> Vec<Arc<Mutex<Demand>>> {
        DEMAND_REPOSITORY.lock().values().cloned().collect()
    }

    pub fn clear_repository() {
        DEMAND_REPOSITORY.lock().clear();
    }

    // Getters
    pub fn get_id(&self) -> &str {
        &self.id
    }

    pub fn get_quantity(&self) -> f64 {
        self.quantity
    }

    pub fn get_request_date(&self) -> &NaiveDate {
        &self.request_date
    }

    pub fn get_max_lateness(&self) -> i32 {
        self.max_lateness
    }

    pub fn get_sku(&self) -> Arc<Mutex<SKU>> {
        self.sku.clone()
    }

    pub fn get_priority(&self) -> i32 {
        self.priority
    }

    pub fn set_priority(&mut self, priority: i32) {
        self.priority = priority;
    }

    pub fn reset(&mut self) {
        self.demand_plans.clear();
    }

    pub fn print_demand_plan_header() {
        println!("{:<20}{:<20}{:<20}{:<15}{:<20}{:<15}", "Demand ID", "SKU","Request Date", "Request Qty", "Satisfied Date", "Planned Qty");
    }

    pub fn print_demand_plan(&self) {
        for demand_plan in self.demand_plans.iter() {
            println!("{:<20}{:<20}{:<20}{:<15.2}{:<20}{:<15.2}", 
                self.id, 
                self.sku.lock().name(),
                self.request_date.format("%Y-%m-%d").to_string(), 
                self.quantity, 
                demand_plan.get_date().format("%Y-%m-%d").to_string(), 
                demand_plan.get_quantity()
            );
        }
    }

}

#[cfg(test)]
mod tests {
    use super::*;

    fn setup_test_sku() -> Arc<Mutex<SKU>> {
        SKU::new("TEST_SKU_001")
    }

    fn setup_test_environment() {
        Demand::clear_repository();
    }

    fn create_test_date() -> NaiveDate {
        NaiveDate::from_ymd_opt(2024, 1, 1).unwrap()
    }

    #[test]
    fn test_sku_helper() {
        let sku = setup_test_sku();
        assert_eq!(sku.lock().name(), "TEST_SKU_001");
    }

    #[test]
    fn test_individual_getters() {
        setup_test_environment();
        let sku = setup_test_sku();
        let request_date = NaiveDate::from_ymd_opt(2024, 3, 15).unwrap();
        let quantity = 175.5;
        let max_lateness = 7;

        let demand = Demand::new(
            "D1".to_string(),
            quantity,
            request_date,
            max_lateness,
            sku
        );

        let demand_ref = demand.lock();
        // Test each getter individually
        assert_eq!(demand_ref.get_quantity(), 175.5);
        assert_eq!(demand_ref.get_request_date(), &request_date);
        assert_eq!(demand_ref.get_max_lateness(), 7);
    }

    #[test]
    fn test_zero_values() {
        setup_test_environment();
        let sku = setup_test_sku();
        let request_date = create_test_date();
        
        let demand = Demand::new(
            "D2".to_string(),
            0.0,
            request_date,
            0,
            sku
        );

        let demand_ref = demand.lock();
        assert_eq!(demand_ref.get_quantity(), 0.0);
        assert_eq!(demand_ref.get_max_lateness(), 0);
    }

    #[test]
    fn test_negative_values() {
        setup_test_environment();
        let sku = setup_test_sku();
        let request_date = create_test_date();
        
        let demand = Demand::new(
            "D3".to_string(),
            -100.0,
            request_date,
            -5,
            sku
        );

        let demand_ref = demand.lock();
        assert_eq!(demand_ref.get_quantity(), -100.0);
        assert_eq!(demand_ref.get_max_lateness(), -5);
    }

    #[test]
    fn test_large_values() {
        setup_test_environment();
        let sku = setup_test_sku();
        let request_date = create_test_date();
        
        let demand = Demand::new(
            "D4".to_string(),
            f64::MAX / 2.0,
            request_date,
            i32::MAX / 2,
            sku
        );

        let demand_ref = demand.lock();
        assert_eq!(demand_ref.get_quantity(), f64::MAX / 2.0);
        assert_eq!(demand_ref.get_max_lateness(), i32::MAX / 2);
    }

    #[test]
    fn test_same_date_different_demands() {
        setup_test_environment();
        let sku = setup_test_sku();
        let same_date = create_test_date();

        let demands = vec![
            ("D10", 100.0, 5),
            ("D11", 200.0, 3),
            ("D12", 300.0, 7),
        ];

        for (id, qty, lateness) in demands {
            let demand = Demand::new(
                id.to_string(),
                qty,
                same_date.clone(),
                lateness,
                sku.clone()
            );

            let demand_ref = demand.lock();
            assert_eq!(demand_ref.get_request_date(), &same_date);
            assert_eq!(demand_ref.get_quantity(), qty);
            assert_eq!(demand_ref.get_max_lateness(), lateness);

            let same_date2 = create_test_date();
            assert_eq!(demand_ref.get_request_date(), &same_date2);

        }
    }   

    // ... existing tests ...
}

