// This will be our main library file that exports all modules
pub mod constants;
pub mod product;
pub mod location;
pub mod sku;
pub mod inventory_profile;
pub mod flow;
pub mod resource;
pub mod location_group;
pub mod quantity_date;
pub mod simultaneous_flow;
pub mod operation_plan;
pub mod operation;
pub mod specification;
pub mod plan_proposal;
pub mod demand;
pub mod planning_service;
pub mod basic_operation_planning_service;
pub mod basic_sku_planning_service;
pub mod alt_operation_planning_service;
pub mod alternate_material_flow;
pub mod logger_config;
pub mod iflow;
pub mod ioperation;
pub mod flow_types;
pub mod demand_planner;
pub mod utilities {
    pub mod memory;  // This tells Rust to look for memory.rs in the utils/ directory
    pub mod unique;
    pub mod settings;
    pub mod traverse;
    pub mod upstream_traverse;
    pub mod cost_calculator;
}

pub mod scale {
    pub mod laptop_sc_scaled;
}

pub mod web {
    pub mod supply_plan_service;
}

// sample supply chains
pub mod supply_chains {
    pub mod sc_with_alternates;
}

pub mod reports {
    pub mod plan_exporter;
}

pub mod planner;
pub mod motivator;
pub mod resource_flow;
pub mod alternate_operation;

// Re-export commonly used items
pub use constants::*;
pub use product::Product;
pub use location::Location;
pub use operation::Operation;
pub use simultaneous_flow::SimultaneousFlow;
pub use operation_plan::OperationPlan; 
pub use specification::Specification; 
pub use demand::Demand;
pub use logger_config::configure_logger;
pub use iflow::IFlow;
pub use ioperation::IOperation;
pub use location_group::LocationGroup;
pub use sku::SKU;   
pub use flow::Flow;
pub use inventory_profile::InventoryProfile;
pub use flow_types::{ConsumeFlow, ProduceFlow};
pub use plan_proposal::Proposal;
pub use planning_service::PlanningService;
pub use basic_operation_planning_service::BasicOperationPlanningService;
pub use basic_sku_planning_service::BasicSKUPlanningService;
pub use alt_operation_planning_service::AltOperationPlanningService;
pub use demand_planner::DemandPlanner;

pub use planner::{choose_planner, PlannerType};
pub use motivator::Motivator;
pub use utilities::settings::Settings;
//pub use reports::plan_exporter::PlanExporter;
pub use resource::Resource;
pub use alternate_operation::AlternateOperation;

// Declare the module
pub mod py_interface {
    pub mod network_objects;
}
