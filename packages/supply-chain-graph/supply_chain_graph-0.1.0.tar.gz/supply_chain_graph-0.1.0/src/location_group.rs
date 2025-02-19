use std::collections::HashMap;
use std::sync::Mutex;
use lazy_static::lazy_static;

lazy_static! {
    pub static ref LOCATION_GROUPS: Mutex<HashMap<String, LocationGroup>> = Mutex::new(HashMap::new());
}

#[derive(Debug, Clone)]
pub struct LocationGroup {
    name: String,
}

impl LocationGroup {
    pub fn new(name: String) -> Self {
        let group = LocationGroup {
            name: name.clone(),
        };
        LOCATION_GROUPS.lock().unwrap().insert(name, group.clone());
        group
    }

    pub fn get_name(&self) -> &String {
        &self.name
    }
}

impl std::fmt::Display for LocationGroup {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "{}", self.name)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_location_group_creation() {
        let group = LocationGroup::new("Test Group".to_string());
        assert_eq!(group.get_name(), "Test Group");
    }

    #[test]
    fn test_location_group_display() {
        let group = LocationGroup::new("Display Test".to_string());
        assert_eq!(format!("{}", group), "Display Test");
    }

    #[test]
    fn test_location_groups_storage() {
        let group_name = "Storage Test".to_string();
        let _group = LocationGroup::new(group_name.clone());
        let stored_group = LOCATION_GROUPS.lock().unwrap().get(&group_name).cloned();
        assert!(stored_group.is_some());
        assert_eq!(stored_group.unwrap().get_name(), &group_name);
    }
} 