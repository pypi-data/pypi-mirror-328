use std::fmt::Debug;
use std::collections::HashMap;
use std::sync::Arc;
use parking_lot::Mutex;
use lazy_static::lazy_static;

use crate::InventoryProfile;
use crate::operation::Operation;
use chrono::NaiveDate;
use log::info;
use crate::operation::OperationVariant;
use crate::alternate_operation::AlternateOperation;

lazy_static! {
    static ref SKU_REPOSITORY: Arc<Mutex<HashMap<String, Arc<Mutex<SKU>>>>> = 
        Arc::new(Mutex::new(HashMap::new()));
}

#[derive(Debug)]
pub struct SKU {
    name: String,
    product_name: String,
    location_name: String,
    inventory_profile: InventoryProfile,
    top_producing_operation: OperationVariant,
    producing_operations: Vec<Arc<Mutex<Operation>>>,
    consuming_operations: Vec<Arc<Mutex<Operation>>>,
}

impl SKU {
    pub fn new(name: &str) -> Arc<Mutex<Self>> {
        if name.is_empty() {
            panic!("SKU name cannot be empty");
        }

        let repo = SKU_REPOSITORY.lock();
        if let Some(existing_sku) = repo.get(name) {
            return existing_sku.clone();
        }
        drop(repo); // Release the lock before creating new SKU

        let sku = Arc::new(Mutex::new(SKU {
            name: name.to_string(),
            product_name: "".to_string(),
            location_name: "".to_string(),
            inventory_profile: InventoryProfile::new(),
            top_producing_operation: OperationVariant::None,
            producing_operations: Vec::new(),
            consuming_operations: Vec::new(),
        }));
        
        SKU_REPOSITORY.lock().insert(name.to_string(), sku.clone());
        sku
    }

    pub fn create(product_name: &str, location_name: &str) -> Arc<Mutex<Self>> {
        let name = format!("{}{}{}", product_name, "@", location_name);
        SKU::from_name(&name)
    }

    pub fn from_name(name: &str) -> Arc<Mutex<Self>> {
        SKU::new(name)
    }

    pub fn find(name: &str) -> Option<Arc<Mutex<SKU>>> {
        SKU_REPOSITORY.lock()
            .get(name)
            .cloned()
    }

    pub fn exists(name: &str) -> bool {
        SKU_REPOSITORY.lock()
            .contains_key(name)
    }

    pub fn set_top_producing_operation(&mut self, operation: OperationVariant) {
        self.top_producing_operation = operation;
    }

    pub fn get_top_producing_operation(&self) -> &OperationVariant {
        &self.top_producing_operation
    }

    pub fn add_producing_operation(&mut self, operation: Arc<Mutex<Operation>>) {
        let op_name = operation.lock().get_name().to_string();
        if !self.producing_operations.iter().any(|op| *op.lock().get_name() == op_name) {
            self.producing_operations.push(operation);
        }
    }

    pub fn add_consuming_operation(&mut self, operation: Arc<Mutex<Operation>>) {
        let op_name = operation.lock().get_name().to_string();
        if !self.consuming_operations.iter().any(|op| *op.lock().get_name() == op_name) {
            self.consuming_operations.push(operation);
        }   
    }

    pub fn get_producing_operations(&self) -> &Vec<Arc<Mutex<Operation>>> {
        &self.producing_operations
    }

    pub fn get_consuming_operations(&self) -> &Vec<Arc<Mutex<Operation>>> {
        &self.consuming_operations
    }   

    pub fn generate_top_producing_operation(&mut self) {
        // If there are no producing operations, return early
        if self.producing_operations.is_empty() {
            return;
        }

        // If there's only one producing operation, set it directly as top producing operation
        if self.producing_operations.len() == 1 {
            self.top_producing_operation = OperationVariant::Basic(self.producing_operations[0].clone());
            return;
        }

        // Create a new alternate operation with name based on SKU
        let alt_op = AlternateOperation::new(format!("{}_alt", self.name));
        
        // Add each producing operation as an alternate
        {
            let mut alt_op_ref = alt_op.lock();
            for op in &self.producing_operations {
                alt_op_ref.add_operation_as_alternate(
                    op.clone(),
                    OperationVariant::Alternate(alt_op.clone())
                );
            }
            
            // Generate the period to effective operation map
            alt_op_ref.generate_period_to_effective_operation_map();
        }
        
        // Set this alternate operation as the top producing operation
        self.top_producing_operation = OperationVariant::Alternate(alt_op);
    }

    pub fn name(&self) -> &str {
        &self.name
    }

    pub fn inventory_profile(&mut self) -> &mut InventoryProfile {
        &mut self.inventory_profile
    }

    pub fn get_inventory_profile(&self) -> &InventoryProfile {
        &self.inventory_profile
    }

    pub fn add_inventory(&mut self, date: NaiveDate, quantity: f64) {
        self.inventory_profile.add_inventory(date, quantity);
    }

    pub fn remove_inventory(&mut self, date: NaiveDate, quantity: f64) {
        self.inventory_profile.remove_inventory(date, quantity);
    }

    pub fn print_inventory_profile(&self) {
        info!("Inventory Profile for {}", self.name);
        self.inventory_profile.print_inventory_profile();
    }

    pub fn get_all_skus() -> Vec<Arc<Mutex<SKU>>> {
        SKU_REPOSITORY.lock()
            .values()
            .cloned()
            .collect()
    }

    pub fn clear_repository() {
        SKU_REPOSITORY.lock()
            .clear();
    }

    pub fn product_name(&self) -> &str {
        &self.product_name
    }

    pub fn location_name(&self) -> &str {
        &self.location_name
    }

    pub fn reset(&mut self) {
        self.inventory_profile.reset();
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::operation::Operation;
    use crate::operation::MaterialFlowVariant;
    use crate::flow::Flow;
    use crate::operation::ResourceFlowVariant;
    use serial_test::serial;

    // Helper function to clean up before/after tests
    fn clean_repository() {
        SKU::clear_repository();
    }

    #[test]
    #[serial]
    fn test_sku_creation() {
        let sku = SKU::from_name("test_sku");
        let sku_ref = sku.lock();  // MutexGuard gives direct access to SKU
        assert_eq!(sku_ref.name(), "test_sku");
    }

    #[test]
    #[serial]
    fn test_sku_creation_with_product_and_location() {
        clean_repository();  // Clear repository before test
        
        let sku = SKU::create("test_product", "test_location");
        assert_eq!(sku.lock().name(), "test_product@test_location");
        
        let sku2 = SKU::create("test_product", "test_location");
        assert!(Arc::ptr_eq(&sku, &sku2));
        
        assert_eq!(SKU::get_all_skus().len(), 1);
        assert_eq!(
            SKU::find("test_product@test_location").unwrap().lock().name(),
            "test_product@test_location"
        );
        
        clean_repository();  // Clean up after test
    }

    #[test]
    #[serial]
    fn test_top_producing_operation() {
        let sku = SKU::from_name("test_sku");
        let produce_flow = MaterialFlowVariant::Single(Flow::new(false, 1.0, sku.clone()));
        let consume_flow = MaterialFlowVariant::Single(Flow::new(true, 1.0, SKU::from_name("input")));
        
        let operation = Operation::new(
            "test_operation".to_string(),
            1,
            10,
            1,
            produce_flow,
            consume_flow,
            ResourceFlowVariant::None,
        );
        
        // Get operation name first
        let op_name = operation.lock().get_name().to_string();
        
        {
            let mut sku_ref = sku.lock();
            sku_ref.set_top_producing_operation(OperationVariant::Basic(operation.clone()));
            
            // Test getting the operation back
            let retrieved_op = sku_ref.get_top_producing_operation();
            match retrieved_op {
                OperationVariant::Basic(op) => {
                    assert_eq!(*op.lock().get_name(), *op_name);
                },
                _ => panic!("Expected a Basic operation variant"),
            }
        }
        clean_repository()
    }

    #[test]
    #[serial]
    fn test_sku_repository() {
        let sku1 = SKU::from_name("test_repo_sku");
        let sku2 = SKU::from_name("test_repo_sku");
        assert!(Arc::ptr_eq(&sku1, &sku2));

        let found_sku = SKU::find("test_repo_sku");
        assert!(found_sku.is_some());
        assert!(Arc::ptr_eq(&found_sku.unwrap(), &sku1));

        assert!(SKU::exists("test_repo_sku"));
        assert!(!SKU::exists("nonexistent_sku"));
        clean_repository()
    }
}

