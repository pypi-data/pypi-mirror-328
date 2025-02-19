use crate::utilities::settings::Settings;
use chrono::NaiveDate;
use crate::operation::EffectivePeriod;

#[derive(Debug)]
pub struct Specification {
    indent: i32,
    trace_level: i32,
    indent_string: String,
    spaces: String,
    resize_plans: bool,
    trace_demands_ids: Vec<i32>,
    current_demand_id: i32,
    effective_periods: Vec<EffectivePeriod>,
}

impl Specification {
    pub fn new(indent: i32, trace_level: i32) -> Self {
        let spaces = " ".repeat(indent as usize);
        Self {
            indent,
            trace_level,
            indent_string: String::new(),
            spaces,
            resize_plans: false,
            trace_demands_ids: vec![],
            current_demand_id: -1,
            effective_periods: vec![],
        }
    }

    pub fn new_from_settings(indent: i32, path_to_settings_yml: &str) -> Self {
        let spaces = " ".repeat(indent as usize);
        let settings = Settings::load(path_to_settings_yml)
            .expect("Failed to load settings file");
        Self {
            indent,
            trace_level: settings.trace_level.unwrap_or(0),
            indent_string: String::new(),
            spaces,
            resize_plans: settings.resize_plans.unwrap_or(true),
            trace_demands_ids: settings.get_demands_to_trace(),
            current_demand_id: -1,
            effective_periods: vec![],
        }
    }


    pub fn set_trace_demands_ids(&mut self, trace_demands_ids: Vec<i32>) {
        self.trace_demands_ids = trace_demands_ids;
    }

    pub fn set_current_demand_id(&mut self, current_demand_id: i32) {
        self.current_demand_id = current_demand_id;
    }

    pub fn trace_current_demand(&self) -> bool {
        if self.trace_level >= 1 {
            self.trace_demands_ids.contains(&self.current_demand_id) || self.trace_demands_ids.is_empty()
        } else {
            false
        }
    }

    pub fn set_resize_plans(&mut self, resize_plans: bool) {
        self.resize_plans = resize_plans;
    }

    pub fn get_indent(&self) -> i32 {
        self.indent
    }

    pub fn set_indent(&mut self, indent: i32) {
        self.indent = indent;
    }

    pub fn get_trace_level(&self) -> i32 {
        self.trace_level
    }

    pub fn set_trace_level(&mut self, trace_level: i32) {
        self.trace_level = trace_level;
    }

    pub fn add_indent(&mut self) -> &String {
        self.indent_string.push_str(&self.spaces);
        &self.indent_string
    }

    pub fn remove_indent(&mut self) -> &String {
        let new_length = self.indent_string.len().saturating_sub(self.indent as usize);
        self.indent_string.truncate(new_length);
        &self.indent_string
    }

    pub fn get_indent_string(&self) -> &String {
        &self.indent_string
    }

    pub fn get_latest_effective_date(&self, ask_date: NaiveDate) -> Option<NaiveDate> {
        if self.effective_periods.len() != 1 {
            panic!("Exactly one effective period must be defined in specification when Alternate motive is used");
        }
        
        let period = &self.effective_periods[0];
        let from = period.from.expect("From date must be set");
        let till = period.till.expect("Till date must be set");

        if ask_date < from {
            None
        } else if ask_date >= till {
            Some(till.pred_opt().expect("Date underflow when subtracting one day"))
        } else {
            Some(ask_date)
        }
    }
    
    pub fn set_effective_period(&mut self, from: Option<NaiveDate>, till: Option<NaiveDate>) {
        self.effective_periods.push(EffectivePeriod { from, till, priority: i32::MAX });
    }

    pub fn reset_effective_period(&mut self) {
        self.effective_periods.clear();
    }

    pub fn get_effective_periods(&self) -> &Vec<EffectivePeriod> {
        &self.effective_periods
    }


}

#[cfg(test)]
mod tests {
    use super::*;
    use chrono::NaiveDate;

    #[test]
    fn test_get_latest_effective_date() {
        let mut spec = Specification::new(2, 0);
        
        // Set effective period
        let period_start = NaiveDate::from_ymd_opt(2024, 1, 1).unwrap();
        let period_end = NaiveDate::from_ymd_opt(2024, 2, 1).unwrap();
        spec.set_effective_period(Some(period_start), Some(period_end));

        // Test date within effective period
        let within_period = NaiveDate::from_ymd_opt(2024, 1, 15).unwrap();
        assert_eq!(spec.get_latest_effective_date(within_period), Some(within_period));

        // Test date before effective period
        let before_period = NaiveDate::from_ymd_opt(2023, 12, 31).unwrap();
        assert_eq!(spec.get_latest_effective_date(before_period), None);

        // Test date equal to end date
        let end_date = NaiveDate::from_ymd_opt(2024, 2, 1).unwrap();
        let expected_end = NaiveDate::from_ymd_opt(2024, 1, 31).unwrap();
        assert_eq!(spec.get_latest_effective_date(end_date), Some(expected_end));

        // Test date after effective period
        let after_period = NaiveDate::from_ymd_opt(2024, 2, 2).unwrap();
        assert_eq!(spec.get_latest_effective_date(after_period), Some(expected_end));
    }

    #[test]
    #[should_panic(expected = "Exactly one effective period must be defined in specification when Alternate motive is used")]
    fn test_get_latest_effective_date_no_period() {
        let spec = Specification::new(2, 0);
        let test_date = NaiveDate::from_ymd_opt(2024, 1, 15).unwrap();
        spec.get_latest_effective_date(test_date);
    }

    #[test]
    #[should_panic(expected = "Exactly one effective period must be defined in specification when Alternate motive is used")]
    fn test_get_latest_effective_date_multiple_periods() {
        let mut spec = Specification::new(2, 0);
        
        // Add two periods
        let period_start = NaiveDate::from_ymd_opt(2024, 1, 1).unwrap();
        let period_end = NaiveDate::from_ymd_opt(2024, 2, 1).unwrap();
        spec.set_effective_period(Some(period_start), Some(period_end));
        spec.set_effective_period(Some(period_start), Some(period_end));

        let test_date = NaiveDate::from_ymd_opt(2024, 1, 15).unwrap();
        spec.get_latest_effective_date(test_date);
    }
} 
