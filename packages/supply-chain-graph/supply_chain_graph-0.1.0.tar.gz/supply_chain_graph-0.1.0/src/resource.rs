use std::collections::BTreeMap;
use std::collections::HashMap;
use std::fmt;
use chrono::NaiveDate;
use chrono::Days;
use crate::operation::EffectivePeriod;
use parking_lot::Mutex;
use lazy_static;
use std::sync::Arc;


use crate::constants::PRECISION;

const MAX_DATE: NaiveDate = NaiveDate::from_ymd_opt(9999, 12, 31).unwrap();

lazy_static::lazy_static! {
    static ref RESOURCE_REPOSITORY: Mutex<HashMap<String, Arc<Mutex<Resource>>>> = Mutex::new(HashMap::new());
}

// START

#[derive(Debug, Clone)]
pub struct CapacityBucket {
    start_date: NaiveDate,
    end_date: NaiveDate,
    capacity: f64,
    original_capacity: f64,
}

impl CapacityBucket {
    pub fn new(start_date: NaiveDate, end_date: NaiveDate, capacity: f64) -> Self {
        Self {
            start_date,
            end_date,
            capacity,
            original_capacity: capacity,
        }
    }

    pub fn new_with_updated_capacity(start_date: NaiveDate, end_date: NaiveDate, capacity: f64, original_capacity: f64) -> Self {
        Self {
            start_date,
            end_date,
            capacity,
            original_capacity,
        }
    }

    pub fn get_start_date(&self) -> NaiveDate {
        self.start_date
    }

    pub fn get_end_date(&self) -> NaiveDate {
        self.end_date
    }

    pub fn get_capacity(&self) -> f64 {
        self.capacity
    }

    pub fn get_original_capacity(&self) -> f64 {
        self.original_capacity
    }
}

impl fmt::Display for CapacityBucket {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(
            f,
            "{:<12} {:<12} {:<17.2} {:<17.2}",
            self.start_date,
            if self.end_date == MAX_DATE { "INF FUTURE".to_string() } else { self.end_date.to_string() },
            self.capacity,
            self.original_capacity
        )
    }
}

#[derive(Debug)]
pub struct Resource {
    resource_name: String,
    is_constrained: bool,
    capacities: BTreeMap<NaiveDate, (f64, f64)>,
}

impl Resource {
    pub fn from_name(resource_name: &str) -> Arc<Mutex<Self>> {
        let key = format!("{}", resource_name);
        let mut repo = RESOURCE_REPOSITORY.lock();
        
        if let Some(existing_resource) = repo.get(&key) {
            return existing_resource.clone();
        }

        let resource = Arc::new(Mutex::new(Resource {
            resource_name: resource_name.to_string(),
            is_constrained: true,
            capacities: BTreeMap::new(),
        }));

        repo.insert(key, resource.clone());
        resource
    }

    pub fn get_name(&self) -> &str {
        &self.resource_name
    }

    pub fn is_constrained(&self) -> bool {
        self.is_constrained
    }

    pub fn set_constrained(&mut self, is_constrained: bool) {
        self.is_constrained = is_constrained;
    }

    pub fn set_capacity(&mut self, date: NaiveDate, capacity: f64) {
        self.capacities.insert(date, (capacity, capacity));
    }

    pub fn get_capacity_bucket(&self, date: NaiveDate) -> Option<CapacityBucket> {
        let (&start_date, &(capacity, original_capacity)) = self.capacities.range(..=date).next_back()?;
        
        let end_date = self.capacities
            .range((start_date + Days::new(1))..)
            .next()
            .map(|(&next_date, _)| next_date)
            .unwrap_or(MAX_DATE);
        
        Some(CapacityBucket {
            start_date,
            end_date,
            capacity,
            original_capacity,
        })
    }

    pub fn print_all_capacity_buckets(&self) {
        println!("{:<12} {:<12} {:<17} {:<17}", 
            "Start Date", "End Date", "Avail Capacity", "Orig Capacity");
        println!("{}", "-".repeat(58));

        for (&date, _) in self.capacities.iter() {
            if let Some(bucket) = self.get_capacity_bucket(date) {
                println!("{}", bucket);
            }
        }
    }

    pub fn get_latest_bucket_with_capacity(&self, date: NaiveDate) -> Option<CapacityBucket> {
        // Find the latest entry on or before the date with positive capacity
        let (&start_date, &capacity) = self.capacities
            .range(..=date)
            .rev()  // Iterate in reverse order to find the latest first
            .find(|(_, &(capacity, _))| capacity >= PRECISION)?;
        
        // Find the next entry's date after our found start_date
        let end_date = self.capacities
            .range((start_date + Days::new(1))..)
            .next()
            .map(|(&next_date, _)| next_date)
            .unwrap_or(MAX_DATE);
        
        Some(CapacityBucket::new_with_updated_capacity(start_date, end_date, capacity.0, capacity.1))
    }

    pub fn find_day_and_bucket_with_available_capacity(&self, ask_date: NaiveDate, effective_period: &Vec<EffectivePeriod>) -> Option<(NaiveDate, CapacityBucket)> {
        // If no effective periods, all dates are effective
        if effective_period.is_empty() {
            if let Some(bucket) = self.get_latest_bucket_with_capacity(ask_date) {
                let date = if ask_date >= bucket.end_date {
                    bucket.end_date.pred_opt()?
                } else {
                    ask_date
                };
                return Some((date, bucket));
            }
            return None;
        }

        // Start with the latest bucket on or before ask_date and work backwards
        let mut current_date = ask_date;
        while let Some(bucket) = self.get_latest_bucket_with_capacity(current_date) {
            // Check dates from min(ask_date, bucket.end_date - 1) down to bucket.start_date
            let start_check = if ask_date >= bucket.end_date {
                bucket.end_date.pred_opt()?
            } else {
                ask_date
            };
            
            let mut check_date = start_check;
            while check_date >= bucket.start_date {
                // Check if check_date falls within any effective period
                for period in effective_period {
                    if (period.from.is_none() || check_date >= period.from.unwrap()) &&
                       (period.till.is_none() || check_date < period.till.unwrap()) {
                        return Some((check_date, bucket.clone()));
                    }
                }
                check_date = check_date.pred_opt()?;
            }
            
            // If we didn't find a date in this bucket, move to the previous bucket
            current_date = bucket.start_date.pred_opt()?;
        }
        
        None
    }

    pub fn add_capacity(&mut self, date: NaiveDate, amount: f64) -> Result<(), String> {
        if amount >= -PRECISION && amount <= PRECISION {
            return Ok(());
        }
        if let Some(bucket) = self.get_capacity_bucket(date) {
            let (current_capacity, original_capacity) = self.capacities.get(&bucket.start_date).unwrap();
            self.capacities.insert(bucket.start_date, (current_capacity + amount, *original_capacity));
            Ok(())
        } else {
            Err("No capacity bucket found for the given date".to_string())
        }
    }

    pub fn remove_capacity(&mut self, date: NaiveDate, amount: f64) -> Result<(), String> {
        self.add_capacity(date, -amount)
    }

    pub fn get_all_resources() -> Vec<Arc<Mutex<Self>>> {
        RESOURCE_REPOSITORY.lock().values().cloned().collect()
    }

    pub fn clear_repository() {
        RESOURCE_REPOSITORY.lock().clear();
    }

    pub fn get_capacity_profile(&self) -> &BTreeMap<NaiveDate, (f64, f64)> {
        &self.capacities
    }

    // dont call this in isolation. This is a utility function used with resetin operation
    // and skus for their plans
    pub fn reset(&mut self) {
        // resets the available capacity to the original capacity
        for (date, (capacity, original_capacity)) in self.capacities.iter_mut() {
            *capacity = *original_capacity;
        }
    }

}

#[cfg(test)]
mod tests {
    use super::*;
    use chrono::NaiveDate;

    fn create_test_date(year: i32, month: u32, day: u32) -> NaiveDate {
        NaiveDate::from_ymd_opt(year, month, day).unwrap()
    }

    #[test]
    fn test_resource_creation_and_singleton() {
        let resource1 = Resource::from_name("R1");
        let resource2 = Resource::from_name("R1");
        
        assert_eq!(resource1.lock().get_name(), "R1");
        assert!(Arc::ptr_eq(&resource1, &resource2), "Same named resources should return same instance");
    }

    #[test]
    fn test_capacity_buckets() {
        let resource = Resource::from_name("TestResource");
        let mut r = resource.lock();
        
        // Set up test data
        r.set_capacity(create_test_date(2024, 1, 1), 100.0);
        r.set_capacity(create_test_date(2024, 1, 15), 150.0);
        r.set_capacity(create_test_date(2024, 2, 1), 200.0);

        // Test date before first capacity entry - should return None
        let before_first = r.get_capacity_bucket(create_test_date(2023, 12, 31));
        assert!(before_first.is_none(), "Date before first capacity should return None");

        // Test getting capacity bucket for specific dates
        let bucket1 = r.get_capacity_bucket(create_test_date(2024, 1, 10)).unwrap();
        assert_eq!(bucket1.get_start_date(), create_test_date(2024, 1, 1));
        assert_eq!(bucket1.get_end_date(), create_test_date(2024, 1, 15));
        assert_eq!(bucket1.get_capacity(), 100.0);

        let bucket2 = r.get_capacity_bucket(create_test_date(2024, 1, 15)).unwrap();
        assert_eq!(bucket2.get_capacity(), 150.0);

        // Test date after last capacity entry - should return last bucket with MAX_DATE
        let after_last = r.get_capacity_bucket(create_test_date(2024, 3, 1)).unwrap();
        assert_eq!(after_last.get_start_date(), create_test_date(2024, 2, 1));
        assert_eq!(after_last.get_end_date(), MAX_DATE);
        assert_eq!(after_last.get_capacity(), 200.0);

        let after_last = r.get_capacity_bucket(create_test_date(2024, 2, 1)).unwrap();
        assert_eq!(after_last.get_start_date(), create_test_date(2024, 2, 1));
        assert_eq!(after_last.get_end_date(), MAX_DATE);
        assert_eq!(after_last.get_capacity(), 200.0);

    }

    #[test]
    fn test_latest_bucket_with_capacity() {
        let resource = Resource::from_name("CapacityTest");
        let mut r = resource.lock();
        
        // check before creating capacity buckets
        let bucket = r.get_latest_bucket_with_capacity(create_test_date(2024, 1, 1));
        assert!(bucket.is_none(), "No capacity buckets were modelled");

        // Set up test data with zero and positive capacities
        r.set_capacity(create_test_date(2024, 1, 1), 100.0);
        r.set_capacity(create_test_date(2024, 1, 15), 0.0);
        r.set_capacity(create_test_date(2024, 2, 1), 200.0);

        // Test date before first capacity entry - should return None
        let before_first = r.get_latest_bucket_with_capacity(create_test_date(2023, 12, 31));
        assert!(before_first.is_none(), "Date before first capacity should return None");

        // Test exactly on first date
        let first_date = r.get_latest_bucket_with_capacity(create_test_date(2024, 1, 1)).unwrap();
        assert_eq!(first_date.get_start_date(), create_test_date(2024, 1, 1));
        assert_eq!(first_date.get_end_date(), create_test_date(2024, 1, 15));
        assert_eq!(first_date.get_capacity(), 100.0);

        // Test finding latest bucket with positive capacity
        let bucket = r.get_latest_bucket_with_capacity(create_test_date(2024, 1, 20)).unwrap();
        assert_eq!(bucket.get_start_date(), create_test_date(2024, 1, 1));
        assert_eq!(bucket.get_end_date(), create_test_date(2024, 1, 15));
        assert_eq!(bucket.get_capacity(), 100.0);

        // Test finding bucket after zero capacity period
        let bucket = r.get_latest_bucket_with_capacity(create_test_date(2024, 2, 15)).unwrap();
        assert_eq!(bucket.get_start_date(), create_test_date(2024, 2, 1));
        assert_eq!(bucket.get_capacity(), 200.0);
    }

    #[test]
    fn test_capacity_modifications() {
        let resource = Resource::from_name("CapacityModTest");
        let mut r = resource.lock();
        
        // Set up initial capacity
        r.set_capacity(create_test_date(2024, 1, 1), 100.0);
        r.set_capacity(create_test_date(2024, 2, 1), 200.0);

        // Test adding zero capacity (should succeed)
        assert!(r.add_capacity(create_test_date(2024, 1, 15), 0.0).is_ok());
        
        // Test removing zero capacity (should succeed)
        assert!(r.remove_capacity(create_test_date(2024, 1, 15), 0.0).is_ok());

        // Test multiple modifications to same bucket
        r.add_capacity(create_test_date(2024, 1, 15), 50.0).unwrap();
        r.add_capacity(create_test_date(2024, 1, 20), 30.0).unwrap();
        let bucket = r.get_capacity_bucket(create_test_date(2024, 1, 15)).unwrap();
        assert_eq!(bucket.get_capacity(), 180.0); // 100 + 50 + 30

        // Test removing capacity in steps
        r.remove_capacity(create_test_date(2024, 1, 15), 20.0).unwrap();
        r.remove_capacity(create_test_date(2024, 1, 20), 40.0).unwrap();
        let bucket = r.get_capacity_bucket(create_test_date(2024, 1, 15)).unwrap();
        assert_eq!(bucket.get_capacity(), 120.0); // 180 - 20 - 40

        // Test removing capacity exactly to zero
        r.remove_capacity(create_test_date(2024, 1, 15), 120.0).unwrap();
        let bucket = r.get_capacity_bucket(create_test_date(2024, 1, 15)).unwrap();
        assert_eq!(bucket.get_capacity(), 0.0);

        // Test removing capacity when at zero (should pass)
        assert!(r.remove_capacity(create_test_date(2024, 1, 15), 0.1).is_ok());

        // Test that other buckets were unaffected
        let bucket = r.get_capacity_bucket(create_test_date(2024, 2, 15)).unwrap();
        assert_eq!(bucket.get_capacity(), 200.0);
    }

    #[test]
    fn test_find_day_and_bucketwith_available_capacity() {
        let resource = Resource::from_name("CapacityTest1");
        let mut r = resource.lock();
        
        // Set up multiple capacity buckets
        r.set_capacity(create_test_date(2024, 1, 1), 100.0);
        r.set_capacity(create_test_date(2024, 1, 10), 200.0);
        r.set_capacity(create_test_date(2024, 1, 20), 0.0);
        r.set_capacity(create_test_date(2024, 1, 25), 300.0);
        
        // Test with no effective periods
        let result = r.find_day_and_bucket_with_available_capacity(
            create_test_date(2024, 1, 15),
            &vec![]
        );
        assert!(result.is_some());
        let (date, bucket) = result.unwrap();
        assert_eq!(date, create_test_date(2024, 1, 15));
        assert_eq!(bucket.get_capacity(), 200.0);
        
        // Test with effective periods
        let effective_periods = vec![
            EffectivePeriod {
                from: Some(create_test_date(2024, 1, 5)),
                till: Some(create_test_date(2024, 1, 8)),
                priority: 1
            }
        ];
        
        // Test finding date in first available bucket
        let result = r.find_day_and_bucket_with_available_capacity(
            create_test_date(2024, 1, 15),
            &effective_periods
        );
        assert!(result.is_some());
        let (date, bucket) = result.unwrap();
        assert_eq!(date, create_test_date(2024, 1, 7));
        assert_eq!(bucket.get_capacity(), 100.0);
        
        // Test with effective period spanning multiple buckets
        let effective_periods = vec![
            EffectivePeriod {
                from: Some(create_test_date(2024, 1, 8)),
                till: Some(create_test_date(2024, 1, 12)),
                priority: 1
            }
        ];
        
        let result = r.find_day_and_bucket_with_available_capacity(
            create_test_date(2024, 1, 15),
            &effective_periods
        );
        assert!(result.is_some());
        let (date, bucket) = result.unwrap();
        assert_eq!(date, create_test_date(2024, 1, 11));
        assert_eq!(bucket.get_capacity(), 200.0);
        
        // Test when no intersection is possible in current bucket but exists in previous bucket
        let effective_periods = vec![
            EffectivePeriod {
                from: Some(create_test_date(2024, 1, 3)),
                till: Some(create_test_date(2024, 1, 4)),
                priority: 1
            }
        ];
        
        let result = r.find_day_and_bucket_with_available_capacity(
            create_test_date(2024, 1, 31),
            &effective_periods
        );
        assert!(result.is_some());
        let (date, bucket) = result.unwrap();
        assert_eq!(date, create_test_date(2024, 1, 3));
        assert_eq!(bucket.get_capacity(), 100.0);

        // Test when no intersection is not possible since effective period is later
        let effective_periods = vec![
            EffectivePeriod {
                from: Some(create_test_date(2024, 1, 29)),
                till: Some(create_test_date(2024, 1, 31)),
                priority: 1
            }
        ];
        
        let result = r.find_day_and_bucket_with_available_capacity(
            create_test_date(2024, 1, 26),
            &effective_periods
        );
        assert!(result.is_none());

        // ask on effectivity start boundary
        let result = r.find_day_and_bucket_with_available_capacity(
            create_test_date(2024, 1, 29),
            &effective_periods
        );
        assert!(result.is_some());
        let (date, bucket) = result.unwrap();
        assert_eq!(date, create_test_date(2024, 1, 29));
        assert_eq!(bucket.get_capacity(), 300.0);
    }
} 