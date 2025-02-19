#[cfg(target_os = "linux")]
pub fn get_memory_usage() -> String {
    let mut result = String::new();
    if let Ok(status) = std::fs::read_to_string("/proc/self/status") {
        for line in status.lines() {
            if line.starts_with("VmRSS:") || line.starts_with("VmSize:") {
                result.push_str(&format!("{}\n", line.trim()));
            }
        }
    }
    result
}

#[cfg(target_os = "macos")]
pub fn get_memory_usage() -> String {
    use std::process::Command;
    
    // Use ps command to get memory information
    let output = Command::new("ps")
        .args(["-o", "rss=,vsz=", "-p", &std::process::id().to_string()])
        .output();

    match output {
        Ok(output) => {
            if output.status.success() {
                // Convert output bytes to string and trim whitespace
                if let Ok(info) = String::from_utf8(output.stdout) {
                    // Split the output into RSS and VSZ values
                    let values: Vec<&str> = info.split_whitespace().collect();
                    if values.len() >= 2 {
                        if let (Ok(rss), Ok(vsz)) = (values[0].parse::<u64>(), values[1].parse::<u64>()) {
                            // ps outputs in KB, convert to MB
                            return format!(
                                "Memory used: {} MB, Virtual memory: {} MB \n{}",
                                rss / 1024,
                                vsz / 1024,
                                "================================================"
                            );
                        }
                    }
                }
            }
            "Failed to parse memory info".to_string()
        }
        Err(_) => "Failed to get memory info".to_string()
    }
}

#[cfg(not(any(target_os = "linux", target_os = "macos", target_os = "windows")))]
pub fn get_memory_usage() -> String {
    "Memory usage not implemented for this platform".to_string()
} 
