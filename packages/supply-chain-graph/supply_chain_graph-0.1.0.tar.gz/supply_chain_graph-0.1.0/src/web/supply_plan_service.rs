use actix_web::{web, App, HttpResponse, HttpServer, Responder};
use serde::{Deserialize, Serialize};
use crate::utilities::upstream_traverse::get_supply_chain;
use crate::sku::SKU;
use crate::operation::Operation;

#[derive(Debug, Serialize, Deserialize)]
pub struct RetrieveSKURequest {
    sku_name: String,
}

#[derive(Debug, Serialize)]
pub struct SKUInfoResponse {
    success: bool,
    message: String,
}

#[derive(Debug, Serialize)]
pub struct SKUListResponse {
    success: bool,
    skus: Vec<String>,
}

#[derive(Debug, Serialize)]
pub struct OperationListResponse {
    success: bool,
    operations: Vec<String>,
}

#[derive(Debug, Serialize)]
pub struct SupplyChainResponse {
    success: bool,
    supply_chain: Vec<String>,
}

async fn retrieve_sku_info(request: web::Json<RetrieveSKURequest>) -> impl Responder {
    HttpResponse::Ok().json(SKUInfoResponse {
        success: true,
        message: format!("SKU info retrieved for: {}", request.sku_name),
    })
}

async fn health_check() -> impl Responder {
    HttpResponse::Ok().json(SKUInfoResponse {
        success: true,
        message: "Service is healthy".to_string(),
    })
}

async fn list_skus() -> impl Responder {
    let skus = SKU::get_all_skus();
    let sku_names: Vec<String> = skus.iter()
        .map(|sku| sku.lock().name().to_string())
        .collect();

    HttpResponse::Ok().json(SKUListResponse {
        success: true,
        skus: sku_names,
    })
}

async fn list_operations() -> impl Responder {
    let operations = Operation::get_all_operations();
    let operation_names: Vec<String> = operations.iter()
        .map(|operation| operation.lock().get_name().to_string())
        .collect();

    HttpResponse::Ok().json(OperationListResponse {
        success: true,
        operations: operation_names,
    })
}


async fn upstream_supply_chain(request: web::Json<RetrieveSKURequest>) -> impl Responder {
    // Find the SKU
    let skus = SKU::get_all_skus();
    let target_sku = skus.iter()
        .find(|sku| sku.lock().name() == request.sku_name);
    
    match target_sku {
        Some(sku) => {
            let current_date = chrono::Local::now().date_naive();
            // Get the supply chain path directly
            println!("Current date: {}", current_date);
            let supply_chain_output = get_supply_chain(sku.clone(), 0, current_date);
            println!("Supply chain output");
            // Return the supply chain elements as separate strings in the vector
            HttpResponse::Ok().json(SupplyChainResponse {
                success: true,
                supply_chain: supply_chain_output,  // Use the vector directly without joining
            })
        },
        None => HttpResponse::NotFound().json(SupplyChainResponse {
            success: false,
            supply_chain: vec![format!("SKU '{}' not found", request.sku_name)],
        })
    }
}

pub async fn start_server() -> std::io::Result<()> {
    println!("Starting server at http://127.0.0.1:8080");
    
    HttpServer::new(|| {
        App::new()
            .route("/health", web::get().to(health_check))
            .route("/retrieve", web::post().to(retrieve_sku_info))
            .route("/skus", web::get().to(list_skus))
            .route("/operations", web::get().to(list_operations))
            .route("/upstream-supply-chain", web::post().to(upstream_supply_chain))
    })
    .bind("127.0.0.1:8080")?
    .run()
    .await
} 