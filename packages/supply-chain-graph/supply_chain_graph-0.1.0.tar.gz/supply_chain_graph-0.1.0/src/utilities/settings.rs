use serde::Deserialize;
use std::fs;
use anyhow::Result;

#[derive(Debug, Deserialize)]
pub struct Settings {
    #[serde(default)]
    pub pattern: Option<String>,
    #[serde(default)]
    pub level: Option<String>,
    #[serde(default)]
    pub resize_plans: Option<bool>,
    #[serde(default)]
    pub trace_level: Option<i32>,
    #[serde(default)]
    pub trace_demands_ids: Option<String>,
}

impl Settings {
    pub fn load(config_path: &str) -> Result<Self> {
        let contents = fs::read_to_string(config_path)?;
        let settings: Settings = serde_yaml::from_str(&contents)?;
        Ok(settings)
    }

    pub fn load_settings() -> Result<Self> {
        let config_path = "config/settings.yml";
        Settings::load(config_path)
    }

    pub fn get_demands_to_trace(&self) -> Vec<i32> {
        if self.trace_level.is_none() {
            return vec![];
        }

        if self.trace_level.unwrap() < 1 {
            return vec![];
        }
        
        if let Some(trace_demands_ids) = &self.trace_demands_ids {
            trace_demands_ids.split(',').map(|s| s.parse().unwrap()).collect()
        } else {
            vec![]
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::fs;
    use tempfile::NamedTempFile;
    use log::info;

    #[test]
    fn test_load_settings() {
        if let Ok(settings) = Settings::load("config/settings.yml") {
            if let Some(pattern) = settings.pattern {
                info!("Pattern: {}", pattern);
            }
            if let Some(level) = settings.level {
                info!("Level: {}", level);
            }
            if let Some(resize_plans) = settings.resize_plans {
                info!("Resize plans: {}", resize_plans);
            }
            if let Some(trace_level) = settings.trace_level {
                info!("Trace level: {}", trace_level);
            }
        }
    }

    #[test]
    fn test_get_demands_to_trace_empty() {
        // Case 1: trace_level is None
        let settings = Settings {
            pattern: None,
            level: None,
            resize_plans: None,
            trace_level: None,
            trace_demands_ids: None,
        };
        assert_eq!(settings.get_demands_to_trace(), Vec::<i32>::new());

        // Case 2: trace_level is Some but trace_demands_ids is None
        let settings = Settings {
            pattern: None,
            level: None,
            resize_plans: None,
            trace_level: Some(1),
            trace_demands_ids: None,
        };
        assert_eq!(settings.get_demands_to_trace(), Vec::<i32>::new());
    }

    #[test]
    fn test_get_demands_to_trace_with_ids() {
        let settings = Settings {
            pattern: None,
            level: None,
            resize_plans: None,
            trace_level: Some(1),
            trace_demands_ids: Some("1,2,3".to_string()),
        };
        assert_eq!(settings.get_demands_to_trace(), vec![1, 2, 3]);
    }

    #[test]
    fn test_load_invalid_yaml() {
        let temp_file = NamedTempFile::new().unwrap();
        fs::write(temp_file.path(), "invalid: yaml: content: - ").unwrap();
        
        let result = Settings::load(temp_file.path().to_str().unwrap());
        assert!(result.is_err());
    }

    #[test]
    fn test_load_valid_yaml() {
        let temp_file = NamedTempFile::new().unwrap();
        let content = r#"
            pattern: "test_pattern"
            level: "error"
            resize_plans: true
            trace_level: 2
            trace_demands_ids: "1,2,3"
        "#;
        fs::write(temp_file.path(), content).unwrap();
        
        let result = Settings::load(temp_file.path().to_str().unwrap());
        assert!(result.is_ok());
        
        let settings = result.unwrap();
        assert_eq!(settings.pattern, Some("test_pattern".to_string()));
        assert_eq!(settings.level, Some("error".to_string()));
        assert_eq!(settings.resize_plans, Some(true));
        assert_eq!(settings.trace_level, Some(2));
        assert_eq!(settings.trace_demands_ids, Some("1,2,3".to_string()));
    }
}