use log4rs::{
    append::console::ConsoleAppender,
    config::{Appender, Config, Root},
    encode::pattern::PatternEncoder,
};
use log::LevelFilter;
use serde::Deserialize;
use std::fs;


#[derive(Deserialize)]
pub struct SettingsConfig {
    pub pattern: String,
    pub level: String,
}


// used in tests
#[allow(dead_code)]
pub fn get_logger_config(path: &str) -> Result<SettingsConfig, Box<dyn std::error::Error>> {
    let config_str = fs::read_to_string(path)?;
    let config: SettingsConfig = serde_yaml::from_str(&config_str)?;
    Ok(config)
}

#[allow(dead_code)]
pub fn configure_logger_from_path(path: &str) -> Result<(), Box<dyn std::error::Error>> {
    // Read and parse configuration
    let log_settings = get_logger_config(path).unwrap();

    // Convert string level to LevelFilter
    let level = match log_settings.level.to_lowercase().as_str() {
        "info" => LevelFilter::Info,
        "debug" => LevelFilter::Debug,
        "trace" => LevelFilter::Trace,
        "warn" => LevelFilter::Warn,
        "error" => LevelFilter::Error,
        "off" => LevelFilter::Off,
        _ => LevelFilter::Info, // default to Info if invalid
    };

    // Create console appender with configured pattern
    let console = ConsoleAppender::builder()
        .encoder(Box::new(PatternEncoder::new(&log_settings.pattern)))
        .build();

    // Build configuration
    let config = Config::builder()
        .appender(Appender::builder().build("console", Box::new(console)))
        .build(Root::builder().appender("console").build(level))?;

    // Initialize the logger
    log4rs::init_config(config)?;

    Ok(())
} 

#[allow(dead_code)]
pub fn configure_logger() -> Result<(), Box<dyn std::error::Error>> {
    configure_logger_from_path("config/settings.yml")
}

// used in tests
#[allow(dead_code)]
pub fn set_log_level(level: LevelFilter) -> Result<(), Box<dyn std::error::Error>> {

    let pattern = "{m}{n}".to_string();
    // Create default console appender with a standard pattern
    let console = ConsoleAppender::builder()
        .encoder(Box::new(PatternEncoder::new(&pattern)))
        .build();

    // Build configuration with the specified level
    let config = Config::builder()
        .appender(Appender::builder().build("console", Box::new(console)))
        .build(Root::builder().appender("console").build(level))?;

    // Initialize the logger
    log4rs::init_config(config)?;

    Ok(())
}
