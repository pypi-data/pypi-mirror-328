use std::collections::HashMap;

#[derive(Debug, Clone)]
pub struct Product {
    name: String,
    cost: f64,
}

impl Product {
    // Constructor for creating a new Product
    pub fn new(name: String, cost: f64) -> Self {
        Product { name, cost }
    }

    pub fn get_name(&self) -> &String {
        &self.name
    }

    pub fn get_cost(&self) -> f64 {
        self.cost
    }
}

pub struct ProductRepository {
    products: HashMap<String, Product>,
}

impl ProductRepository {
    // Constructor for creating a new ProductRepository
    pub fn new() -> Self {
        ProductRepository {
            products: HashMap::new(),
        }
    }

    // Add a product to the repository
    pub fn add(&mut self, product: Product) -> &Product {
        let name = product.name.clone();    
        self.products.insert(name.clone(), product);
        self.products.get(&name).unwrap()
    }

    // Find a product by name, returns a reference to the product if found
    pub fn find(&self, name: &str) -> Option<&Product> {
        self.products.get(name)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_product_creation() {
        let product = Product::new(String::from("Test Product"), 99.99);
        assert_eq!(product.name, "Test Product");
        assert_eq!(product.cost, 99.99);
    }

    #[test]
    fn test_repository_add_and_find() {
        let mut repo = ProductRepository::new();
        let product = Product::new(String::from("Test Product"), 99.99);
        
        repo.add(product);
        
        let found_product = repo.find("Test Product");
        assert!(found_product.is_some());
        
        let found_product = found_product.unwrap();
        assert_eq!(found_product.name, "Test Product");
        assert_eq!(found_product.cost, 99.99);
    }

    #[test]
    fn test_repository_find_nonexistent() {
        let repo = ProductRepository::new();
        let found_product = repo.find("Nonexistent Product");
        assert!(found_product.is_none());
    }
}

