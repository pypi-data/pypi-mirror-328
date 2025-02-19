use crate::constants::FlowType;
use crate::iflow::IFlow;
use crate::flow::Flow;
use log::error;
use std::sync::Arc;
use parking_lot::Mutex;

// Note: This class is not used anywhere. It is a placeholder for future use.
// LSCO does not support alternate material flows. The construct supported is ALternateBOM
// So we could potentially use either:
// 1) another consume_flow to model the alternate BOM
// 2) create a different operation to model the alternate BOM. (The operation could then have an internal name)


#[derive(Debug)]
pub struct AlternateMaterialFlow {
    // Stores all flows that could be used
    all_flows: Vec<Arc<Mutex<Flow>>>,
    // Vec<alternatives_set<primary_flows_indices>>
    // Example: [[[0,1], [2,3]], [[4], [5,6]]] means:
    // - First alternative set: primary flows 0,1 can be replaced by flows 2,3
    // - Second alternative set: primary flow 4 can be replaced by flows 5,6
    alternate_indices: Vec<Vec<Vec<usize>>>,
}

impl AlternateMaterialFlow {
    pub fn new(flows: Vec<Arc<Mutex<Flow>>>) -> Arc<Mutex<Self>> {
        Arc::new(Mutex::new(AlternateMaterialFlow {
            all_flows: flows,
            alternate_indices: Vec::new(),
        }))
    }

    /// Adds a new set of alternative flows
    /// primary_indices: indices of the primary flows
    /// alternate_indices: indices of the alternate flows that can replace the primary flows
    pub fn add_alternative_set(&mut self, primary_indices: Vec<usize>, alternate_indices: Vec<usize>) {
        // Validate indices
        let max_index = self.all_flows.len();
        let all_indices: Vec<usize> = primary_indices.iter()
            .chain(alternate_indices.iter())
            .cloned()
            .collect();

        // Check if any index is out of bounds
        if let Some(&invalid_index) = all_indices.iter().find(|&&i| i >= max_index) {
            error!("Invalid flow index: {}. Max allowed index: {}", invalid_index, max_index - 1);
            return;
        }

        // Check for duplicates within primary and alternate sets
        if has_duplicates(&primary_indices) || has_duplicates(&alternate_indices) {
            error!("Duplicate indices found in primary or alternate flows");
            return;
        }

        self.alternate_indices.push(vec![primary_indices, alternate_indices]);
    }

    pub fn get_all_flows(&self) -> &Vec<Arc<Mutex<Flow>>> {
        &self.all_flows
    }

    pub fn get_alternate_indices(&self) -> &Vec<Vec<Vec<usize>>> {
        &self.alternate_indices
    }

    /// Adds a new flow to the all_flows vector
    /// Returns the index of the newly added flow
    /// Returns None if the flow is not a consume flow
    pub fn add_flow(&mut self, flow: Arc<Mutex<Flow>>) -> Option<usize> {
        if !flow.lock().is_consume_flow() {
            error!("Only consume flows are allowed in AlternateMaterialFlow");
            return None;
        }
        self.all_flows.push(flow);
        Some(self.all_flows.len() - 1)
    }
}

impl IFlow for AlternateMaterialFlow {
    fn flow_type(&self) -> FlowType {
        FlowType::AlternateMaterial
    }
}

// Helper function to check for duplicates in a vector
fn has_duplicates(indices: &[usize]) -> bool {
    let mut seen = std::collections::HashSet::new();
    !indices.iter().all(|item| seen.insert(item))
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::sku::SKU;

    fn create_consume_flow(name: &str, quantity: f64) -> Arc<Mutex<Flow>> {
        Flow::new(true, quantity, SKU::from_name(name))
    }

    fn create_produce_flow(name: &str, quantity: f64) -> Arc<Mutex<Flow>> {
        Flow::new(false, quantity, SKU::from_name(name))
    }

    #[test]
    fn test_new_alternate_material_flow() {
        let alt_flow = AlternateMaterialFlow::new(vec![]);
        assert_eq!(alt_flow.lock().get_all_flows().len(), 0);
        assert_eq!(alt_flow.lock().get_alternate_indices().len(), 0);
    }

    #[test]
    fn test_add_flow() {
        let alt_flow = AlternateMaterialFlow::new(vec![]);
        let consume_index = alt_flow.lock().add_flow(create_consume_flow("test1", 1.0));
        assert_eq!(consume_index, Some(0));
        assert_eq!(alt_flow.lock().get_all_flows().len(), 1);

        let produce_index = alt_flow.lock().add_flow(create_produce_flow("test2", 1.0));
        assert_eq!(produce_index, None);
        assert_eq!(alt_flow.lock().get_all_flows().len(), 1);
    }

    #[test]
    fn test_add_valid_alternative_set() {
        let flows = vec![
            create_consume_flow("primary1", 1.0),
            create_consume_flow("primary2", 1.0),
            create_consume_flow("alt1", 1.0),
            create_consume_flow("alt2", 1.0),
        ];
        let alt_flow = AlternateMaterialFlow::new(flows);
        
        alt_flow.lock().add_alternative_set(vec![0, 1], vec![2, 3]);
        assert_eq!(alt_flow.lock().get_alternate_indices().len(), 1);
    }

    #[test]
    fn test_invalid_indices() {
        let alt_flow = AlternateMaterialFlow::new(vec![create_consume_flow("test1", 1.0)]);
        alt_flow.lock().add_alternative_set(vec![0], vec![1]); // 1 is invalid index
        assert_eq!(alt_flow.lock().get_alternate_indices().len(), 0);
    }

    #[test]
    fn test_incompatible_flow_types() {
        let alt_flow = AlternateMaterialFlow::new(vec![]);
        let consume1_idx = alt_flow.lock().add_flow(create_consume_flow("consume1", 1.0));
        let produce_idx = alt_flow.lock().add_flow(create_produce_flow("produce1", 1.0));
        let consume2_idx = alt_flow.lock().add_flow(create_consume_flow("consume2", 1.0));

        assert_eq!(consume1_idx, Some(0));
        assert_eq!(produce_idx, None);
        assert_eq!(consume2_idx, Some(1));
        
        assert_eq!(alt_flow.lock().get_all_flows().len(), 2);
    }

    #[test]
    fn test_duplicate_indices() {
        let flows = vec![
            create_consume_flow("test1", 1.0),
            create_consume_flow("test2", 1.0),
        ];
        let alt_flow = AlternateMaterialFlow::new(flows);
        
        alt_flow.lock().add_alternative_set(vec![0, 0], vec![1]); // Duplicate in primary
        assert_eq!(alt_flow.lock().get_alternate_indices().len(), 0);
    }
} 