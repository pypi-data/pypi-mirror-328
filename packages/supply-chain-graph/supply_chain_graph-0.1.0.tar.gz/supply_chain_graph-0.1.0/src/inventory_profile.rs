use std::collections::BTreeMap;
use chrono::{NaiveDate, Days};
use log::{info, debug};
use crate::constants::PRECISION;

#[derive(Debug, Default, Clone)]
pub struct InventoryProfile {
    profile: BTreeMap<NaiveDate, f64>,
}

impl InventoryProfile {
    pub fn new() -> Self {
        InventoryProfile {
            profile: BTreeMap::new(),
        }
    }

    pub fn add_inventory(&mut self, date: NaiveDate, quantity: f64) {
        if (quantity <= PRECISION) && (quantity >= -PRECISION) {
            return;
        }
        let entry = self.profile.entry(date).or_insert(0.0);
        *entry += quantity;
        if quantity >= 0.0 {
            debug!("Added inventory for {} -> {}. Available inventory is {}", date, quantity, self.get_available_inventory(&date));
        }
        else {
            debug!("Removed inventory for {} -> {}. Available inventory is {}", date, -quantity, self.get_available_inventory(&date));
        }
    }

    pub fn remove_inventory(&mut self, date: NaiveDate, quantity: f64) {
        self.add_inventory(date, -quantity);
    }

    pub fn get_net_inventory(&self, date: &NaiveDate) -> f64 {
        self.profile
            .range(..=date)
            .map(|(_, quantity)| *quantity)
            .sum()
    }

    pub fn get_available_inventory(&self, date: &NaiveDate) -> f64 {
        let net_inventory = self.get_net_inventory(date);
        let mut current_inventory = net_inventory;
        let mut min_inventory = net_inventory;

        let next_day = date.checked_add_days(Days::new(1))
            .unwrap_or(*date);

        for quantity in self.profile.range(next_day..).map(|(_, quantity)| *quantity) {
            current_inventory += quantity;
            min_inventory = min_inventory.min(current_inventory);
        }

        0f64.max(min_inventory)
    }

    pub fn print_inventory_profile(&self) {
        let mut prev_quantity = 0.0;
        println!("{:>15}{:>15}{:>15}", "Date", "Production", "OnHand");
        for (date, quantity) in &self.profile {
            let qty_now = quantity + prev_quantity;
            println!("{:>15}{:>15.2}{:>15.2}", date.format("%Y-%m-%d").to_string(), quantity, qty_now);
            prev_quantity = qty_now;
        }
    }

    pub fn get_profile(&self) -> &BTreeMap<NaiveDate, f64> {
        &self.profile
    }

    pub fn next_shortage_date(&self, from_date: &NaiveDate) -> Option<(NaiveDate, f64)> {
        let mut running_total = self.get_net_inventory(from_date);        
        
        // Get the next day after from_date
        let next_day = from_date.checked_add_days(Days::new(1))?;
        
        // Check all dates after from_date using proper range syntax
        for (date, quantity) in self.profile.range(next_day..) {
            running_total += quantity;
            if running_total < -PRECISION {
                return Some((*date, running_total));
            }
        }
        None
    }

    pub fn reset(&mut self) {
        self.profile.clear();
    }

}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_new_inventory_profile() {
        let profile = InventoryProfile::new();
        assert!(profile.profile.is_empty());
    }

    #[test]
    fn test_add_and_get_net_inventory() {
        let mut profile = InventoryProfile::new();
        let date = NaiveDate::from_ymd_opt(2024, 1, 1).unwrap();
        
        profile.add_inventory(date, 10.0);
        assert_eq!(profile.get_net_inventory(&date), 10.0);
        
        profile.add_inventory(date, 5.0);
        assert_eq!(profile.get_net_inventory(&date), 15.0);
    }

    #[test]
    fn test_remove_inventory() {
        let mut profile = InventoryProfile::new();
        let date = NaiveDate::from_ymd_opt(2024, 1, 1).unwrap();
        
        profile.add_inventory(date, 10.0);
        profile.remove_inventory(date, 3.0);
        assert_eq!(profile.get_net_inventory(&date), 7.0);
    }

    #[test]
    fn test_get_available_inventory() {
        let mut profile = InventoryProfile::new();
        let date1 = NaiveDate::from_ymd_opt(2024, 1, 1).unwrap();
        let date2 = NaiveDate::from_ymd_opt(2024, 1, 2).unwrap();
        let date3 = NaiveDate::from_ymd_opt(2024, 1, 3).unwrap();

        profile.add_inventory(date1, 10.0);
        profile.add_inventory(date2, -8.0);
        profile.add_inventory(date3, 5.0);

        assert_eq!(profile.get_available_inventory(&date1), 2.0); // 10 - 8 = 2 (minimum future balance)
        assert_eq!(profile.get_available_inventory(&date2), 2.0); // 2 + 5 = 7 (minimum future balance)
        assert_eq!(profile.get_available_inventory(&date3), 7.0); // Final balance
    }

    #[test]
    fn test_next_shortage_date() {
        let mut profile = InventoryProfile::new();
        let date1 = NaiveDate::from_ymd_opt(2024, 1, 1).unwrap();
        let date2 = NaiveDate::from_ymd_opt(2024, 1, 2).unwrap();
        let date3 = NaiveDate::from_ymd_opt(2024, 1, 3).unwrap();

        profile.add_inventory(date1, 10.0);
        profile.add_inventory(date2, -15.0);
        profile.add_inventory(date3, 5.0);

        // Should find shortage on date2
        let result = profile.next_shortage_date(&date1);
        assert!(result.is_some());
        let (shortage_date, quantity) = result.unwrap();
        assert_eq!(shortage_date, date2);
        assert_eq!(quantity, -5.0);

        // No shortage after date2
        assert!(profile.next_shortage_date(&date2).is_none());
    }
} 