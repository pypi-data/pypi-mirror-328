mod logger_config;
use supply::web::supply_plan_service;
use log::info;
use supply::supply_chains::sc_with_alternates::create_sc_with_alternates;

#[tokio::main]
async fn main() {
    info!("Starting Supply Plan Service");
    let _final_product = create_sc_with_alternates();
    // Start the web service
    if let Err(e) = supply_plan_service::start_server().await {
        eprintln!("Server error: {}", e);
        std::process::exit(1);
    }
}

