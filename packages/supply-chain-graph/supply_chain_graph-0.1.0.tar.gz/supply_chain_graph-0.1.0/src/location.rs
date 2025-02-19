use std::collections::HashMap;
use crate::constants::LocationType;
use crate::location_group::LocationGroup;

#[derive(Debug)]
pub struct Location {
    name: String,
    location_type: LocationType,
    location_group: Option<LocationGroup>,
}

impl Location {
    pub fn new(name: String, location_type: LocationType, location_group: Option<LocationGroup>) -> Self {
        Location {
            name,
            location_type,
            location_group,
        }
    }

    pub fn get_name(&self) -> &String {
        &self.name
    }

    pub fn get_location_type(&self) -> &LocationType {
        &self.location_type
    }

    pub fn get_location_group(&self) -> Option<&LocationGroup> {
        self.location_group.as_ref()
    }
}

impl std::fmt::Display for Location {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        match &self.location_group {
            Some(group) => write!(
                f,
                "Location: {}, Location Group: {}, Location Type: {:?}",
                self.name, group, self.location_type
            ),
            None => write!(
                f,
                "Location: {}, Location Group: None, Location Type: {:?}",
                self.name, self.location_type
            ),
        }
    }
}
pub struct LocationRepository {
    locations: HashMap<String, Location>
}

impl LocationRepository {
    pub fn new() -> Self {
        LocationRepository {
            locations: HashMap::with_capacity(10000)
        }
    }

    pub fn add(&mut self, location: Location) -> &Location {
        let name = location.name.clone();
        self.locations.insert(name.clone(), location);
        self.locations.get(&name).unwrap()
    }

    pub fn add_from_name(&mut self, name: String) -> &Location {
        let location = Location::new(name, LocationType::Unspecified, None);
        self.add(location)
    }

    pub fn add_from_name_and_group(&mut self, name: String, location_group: Option<LocationGroup>) -> &Location {
        let location = Location::new(name, LocationType::Unspecified, location_group);
        self.add(location)
    }

    pub fn exists(&self, name: &str) -> bool {
        self.locations.contains_key(name)
    }

    pub fn find(&self, name: &str) -> Option<&Location> {
        self.locations.get(name)
    }
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_location_creation() {
        let location = Location::new(
            "Tokyo".to_string(),
            LocationType::Unspecified,
            None
        );
        assert_eq!(location.get_name(), "Tokyo");
    }

    #[test]
    fn test_location_repository_operations() {
        let mut repo = LocationRepository::new();
        
        // Test add_from_name
        repo.add_from_name("Paris".to_string());
        assert!(repo.exists("Paris"));
        
        // Test find
        let location = repo.find("Paris").unwrap();
        assert_eq!(location.get_name(), "Paris");
        
        // Test non-existent location
        assert!(!repo.exists("London"));
        assert!(repo.find("London").is_none());
    }

    #[test]
    fn test_location_with_group() {
        let group = LocationGroup::new("Europe".to_string());
        let mut repo = LocationRepository::new();
        
        repo.add_from_name_and_group("Rome".to_string(), Some(group.clone()));
        
        let location = repo.find("Rome").unwrap();
        assert_eq!(location.get_name(), "Rome");
        assert!(location.location_group.is_some());
        assert_eq!(location.location_group.as_ref().unwrap().get_name(), "Europe");
    }

    #[test]
    fn test_location_display() {
        let location = Location::new(
            "Berlin".to_string(),
            LocationType::Unspecified,
            None
        );
        assert_eq!(
            format!("{}", location),
            "Location: Berlin, Location Group: None, Location Type: Unspecified"
        );
    }
}
