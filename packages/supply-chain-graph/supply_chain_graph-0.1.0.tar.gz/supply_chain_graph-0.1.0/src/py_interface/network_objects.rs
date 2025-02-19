use pyo3::prelude::*;
use crate::sku::SKU;
use std::sync::Arc;
use parking_lot::Mutex;
use crate::operation::Operation;
use crate::flow::Flow;
use crate::operation::MaterialFlowVariant;
use crate::operation::ResourceFlowVariant;
use crate::simultaneous_flow::SimultaneousFlow;
use chrono::NaiveDate;
use crate::utilities::upstream_traverse::get_supply_chain;
use crate::demand::Demand;
use crate::demand_planner::DemandPlanner;
use crate::specification::Specification;
use pyo3::types::PySequence;
use crate::logger_config;
use log::LevelFilter;
use crate::resource::Resource;
use crate::resource_flow::ResourceFlow;

#[pyclass]
pub struct PySKU {
    #[pyo3(get)]
    name: String,
    inner: Arc<Mutex<SKU>>,
}

#[pymethods]
impl PySKU {
    #[new]
    pub fn new(name: &str) -> Self {
        let inner = SKU::new(name);
        PySKU {
            name: name.to_string(),
            inner,
        }
    }

    #[staticmethod]
    pub fn create(product_name: &str, location_name: &str) -> Self {
        let inner = SKU::create(product_name, location_name);
        let name = inner.lock().name().to_string();
        PySKU {
            name,
            inner,
        }
    }

    #[getter]
    pub fn product_name(&self) -> String {
        self.inner.lock().product_name().to_string()
    }

    #[getter]
    pub fn location_name(&self) -> String {
        self.inner.lock().location_name().to_string()
    }

    /// Get the upstream supply chain for this SKU
    /// 
    /// Args:
    ///     effective_date (str): The date in 'YYYY-MM-DD' format to evaluate the supply chain
    /// 
    /// Returns:
    ///     list[str]: A formatted list of strings representing the supply chain
    /// 
    /// Example:
    ///     >>> sku = PySKU.create("product", "location")
    ///     >>> supply_chain = sku.get_supply_chain("2024-01-01")
    ///     >>> for line in supply_chain:
    ///     ...     print(line)
    pub fn get_supply_chain(&self, effective_date: &str) -> PyResult<Vec<String>> {
        // Parse the date string
        let date = NaiveDate::parse_from_str(effective_date, "%Y-%m-%d")
            .map_err(|e| PyErr::new::<pyo3::exceptions::PyValueError, _>(
                format!("Invalid date format. Expected YYYY-MM-DD, got: {}. Error: {}", effective_date, e)
            ))?;

        // Call the upstream traverse function
        Ok(get_supply_chain(self.inner.clone(), 0, date))
    }

    /// Generate the top producing operation for this SKU
    /// 
    /// This method will create an alternate operation if there are multiple producing operations,
    /// or set the single producing operation as the top producer.
    pub fn generate_top_producing_operation(&mut self) {
        self.inner.lock().generate_top_producing_operation();
    }

    /// Add a producing operation for this SKU
    /// 
    /// Args:
    ///     operation (PyOperation): The operation that produces this SKU
    pub fn add_producing_operation(&mut self, operation: &PyOperation) {
        self.inner.lock().add_producing_operation(operation.inner.clone());
    }

    /// Add a consuming operation for this SKU
    /// 
    /// Args:
    ///     operation (PyOperation): The operation that consumes this SKU
    pub fn add_consuming_operation(&mut self, operation: &PyOperation) {
        self.inner.lock().add_consuming_operation(operation.inner.clone());
    }

    /// Add inventory for this SKU at a specific date
    /// 
    /// Args:
    ///     date (str): Date in 'YYYY-MM-DD' format
    ///     quantity (float): Quantity to add
    pub fn add_inventory(&self, date: &str, quantity: f64) -> PyResult<()> {
        let parsed_date = NaiveDate::parse_from_str(date, "%Y-%m-%d")
            .map_err(|e| PyErr::new::<pyo3::exceptions::PyValueError, _>(
                format!("Invalid date format. Expected YYYY-MM-DD, got: {}. Error: {}", date, e)
            ))?;

        self.inner.lock().add_inventory(parsed_date, quantity);
        Ok(())
    }

    /// Print the inventory profile for this SKU
    pub fn print_inventory_profile(&self) {
        self.inner.lock().print_inventory_profile();
    }
}

#[pyclass]
pub struct PyOperation {
    #[pyo3(get)]
    name: String,
    inner: Arc<Mutex<Operation>>,
}

#[pymethods]
impl PyOperation {
    #[new]
    pub fn new(name: &str, lead_time: i32, min_lot: i32, increment: i32) -> Self {
        let inner = Operation::new(
            name.to_string(),
            lead_time,
            min_lot,
            increment,
            MaterialFlowVariant::None,
            MaterialFlowVariant::None,
            ResourceFlowVariant::None,
        );
        PyOperation {
            name: name.to_string(),
            inner,
        }
    }

    pub fn add_produce_flow(&mut self, sku: &PySKU, quantity_per: f64) -> PyResult<()> {
        let flow = Flow::new(false, quantity_per, sku.inner.clone());
        let mut op = self.inner.lock();
        op.set_produce_flow(MaterialFlowVariant::Single(flow));
        Ok(())
    }

    pub fn add_consume_flow(&mut self, sku: &PySKU, quantity_per: f64) -> PyResult<()> {
        let flow = Flow::new(true, quantity_per, sku.inner.clone());
        let mut op = self.inner.lock();
        op.set_consume_flow(MaterialFlowVariant::Single(flow));
        Ok(())
    }

    pub fn add_simultaneous_consume_flow(&mut self, sku: &PySKU, quantity_per: f64) -> PyResult<()> {
        let flow = Flow::new(true, quantity_per, sku.inner.clone());
        let mut op = self.inner.lock();
        
        match &op.get_consume_flow() {
            MaterialFlowVariant::None => {
                let sim_flow = SimultaneousFlow::new(vec![flow]);
                op.set_consume_flow(MaterialFlowVariant::Simultaneous(sim_flow));
            },
            MaterialFlowVariant::Simultaneous(existing_sim_flow) => {
                existing_sim_flow.lock().add_flow(flow);
            },
            MaterialFlowVariant::Single(_) => {
                return Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    "Cannot add simultaneous flow to operation with single flow"
                ));
            }
        }
        Ok(())
    }

    #[getter]
    pub fn lead_time(&self) -> i32 {
        self.inner.lock().get_lead_time()
    }

    #[getter]
    pub fn min_lot(&self) -> i32 {
        self.inner.lock().get_min_lot()
    }

    #[getter]
    pub fn increment(&self) -> i32 {
        self.inner.lock().get_increment()
    }

    /// Add an effective period for this operation
    /// 
    /// Args:
    ///     priority (int): Priority level for this period (lower number means higher priority)
    ///     from_date (str, optional): Start date in 'YYYY-MM-DD' format. None means unbounded start.
    ///     till_date (str, optional): End date in 'YYYY-MM-DD' format. None means unbounded end.
    #[pyo3(signature = (priority, from_date=None, till_date=None))]
    pub fn add_period(&mut self, priority: i32, from_date: Option<&str>, till_date: Option<&str>) -> PyResult<()> {
        // Parse the dates if they exist
        let from = if let Some(date_str) = from_date {
            Some(NaiveDate::parse_from_str(date_str, "%Y-%m-%d")
                .map_err(|e| PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("Invalid from_date format. Expected YYYY-MM-DD, got: {}. Error: {}", date_str, e)
                ))?)
        } else {
            None
        };

        let till = if let Some(date_str) = till_date {
            Some(NaiveDate::parse_from_str(date_str, "%Y-%m-%d")
                .map_err(|e| PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("Invalid till_date format. Expected YYYY-MM-DD, got: {}. Error: {}", date_str, e)
                ))?)
        } else {
            None
        };

        // Validate that till date is after from date if both exist
        if let (Some(from_date), Some(till_date)) = (from, till) {
            if till_date <= from_date {
                return Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("till_date ({}) must be after from_date ({})", till_date, from_date)
                ));
            }
        }

        self.inner.lock().add_period(from, till, priority);
        Ok(())
    }

    /// Get the latest effective date for this operation
    /// 
    /// Args:
    ///     ask_date (str): The date in 'YYYY-MM-DD' format to check effectivity
    /// 
    /// Returns:
    ///     str: The latest effective date in 'YYYY-MM-DD' format, or None if not effective
    pub fn get_latest_effective_date(&mut self, ask_date: &str) -> PyResult<Option<String>> {
        let date = NaiveDate::parse_from_str(ask_date, "%Y-%m-%d")
            .map_err(|e| PyErr::new::<pyo3::exceptions::PyValueError, _>(
                format!("Invalid date format. Expected YYYY-MM-DD, got: {}. Error: {}", ask_date, e)
            ))?;

        let result = self.inner.lock().latest_effective_date(date);
        Ok(result.map(|d| d.format("%Y-%m-%d").to_string()))
    }

    /// Add a resource requirement to this operation
    /// 
    /// Args:
    ///     resource (PyResource): The resource required by this operation
    ///     quantity_per (float): The amount of resource required per unit of operation
    pub fn add_resource(&mut self, resource: &PyResource, quantity_per: f64) -> PyResult<()> {
        let resource_flow = ResourceFlow::new(quantity_per, resource.inner.clone());
        let mut op = self.inner.lock();
        op.set_resource_flow(ResourceFlowVariant::SingleResource(resource_flow));
        Ok(())
    }

    /// Print all operation plans for this operation
    pub fn print_operation_plans(&self) {
        self.inner.lock().print_operation_plans();
    }
}

#[pyclass]
pub struct PyDemand {
    inner: Arc<Mutex<Demand>>,
}

#[pymethods]
impl PyDemand {
    #[new]
    pub fn new(id: String, quantity: f64, request_date: &str, max_lateness: i32, sku: &PySKU) -> PyResult<Self> {
        // Parse the date
        let date = NaiveDate::parse_from_str(request_date, "%Y-%m-%d")
            .map_err(|e| PyErr::new::<pyo3::exceptions::PyValueError, _>(
                format!("Invalid date format. Expected YYYY-MM-DD, got: {}. Error: {}", request_date, e)
            ))?;

        // Create the demand
        let demand = Demand::new(id, quantity, date, max_lateness, sku.inner.clone());
        
        Ok(PyDemand {
            inner: demand
        })
    }

    /// Get the demand ID
    #[getter]
    pub fn id(&self) -> String {
        self.inner.lock().get_id().to_string()
    }

    /// Get the demand quantity
    #[getter]
    pub fn quantity(&self) -> f64 {
        self.inner.lock().get_quantity()
    }

    /// Get the request date
    #[getter]
    pub fn request_date(&self) -> String {
        self.inner.lock().get_request_date().format("%Y-%m-%d").to_string()
    }

    /// Get the max lateness
    #[getter]
    pub fn max_lateness(&self) -> i32 {
        self.inner.lock().get_max_lateness()
    }

    /// Set the priority of the demand
    pub fn set_priority(&mut self, priority: i32) {
        self.inner.lock().set_priority(priority);
    }

    /// Get the priority of the demand
    #[getter]
    pub fn priority(&self) -> i32 {
        self.inner.lock().get_priority()
    }

    /// Get the planned quantity for this demand
    pub fn get_planned_quantity(&self) -> f64 {
        self.inner.lock().demand_plans.iter().map(|p| p.get_quantity()).sum()
    }

    /// Print all demand plans for this demand
    pub fn print_demand_plans(&self) {
        Demand::print_demand_plan_header();
        self.inner.lock().print_demand_plan();
    }
}

#[pyclass]
pub struct PyDemandPlanner {
    inner: DemandPlanner,
}

#[pymethods]
impl PyDemandPlanner {
    #[new]
    pub fn new() -> Self {
        PyDemandPlanner {
            inner: DemandPlanner::new()
        }
    }

    /// Plan a list of demands
    /// 
    /// Args:
    ///     demands (list[PyDemand]): List of demands to plan
    ///     trace_level (int): Level of trace output (0-2)
    pub fn plan_demand_list(&self, py: Python, demands: &PySequence, trace_level: i32) -> PyResult<()> {
        if let Err(e) = logger_config::set_log_level(LevelFilter::Info) {
            eprintln!("Failed to configure logger: {}", e);
        }

        let mut specification = Specification::new(2, trace_level);
        
        let rust_demands: Vec<Arc<Mutex<Demand>>> = demands.iter()?
            .filter_map(|item| item.ok())
            .filter_map(|obj| obj.extract::<PyRef<PyDemand>>().ok())
            .map(|demand| demand.inner.clone())
            .collect();

        self.inner.plan_demand_list(rust_demands, &mut specification)
            .map_err(|e| PyErr::new::<pyo3::exceptions::PyRuntimeError, _>(e))?;

        Ok(())
    }

}

#[pyclass]
pub struct PyResource {
    #[pyo3(get)]
    name: String,
    inner: Arc<Mutex<Resource>>,
}

#[pymethods]
impl PyResource {
    #[new]
    pub fn new(name: &str) -> Self {
        let inner = Resource::from_name(name);
        PyResource {
            name: name.to_string(),
            inner,
        }
    }

    /// Set capacity for a specific date
    /// 
    /// Args:
    ///     date (str): Date in 'YYYY-MM-DD' format
    ///     capacity (float): Capacity value
    pub fn set_capacity(&mut self, date: &str, capacity: f64) -> PyResult<()> {
        let parsed_date = NaiveDate::parse_from_str(date, "%Y-%m-%d")
            .map_err(|e| PyErr::new::<pyo3::exceptions::PyValueError, _>(
                format!("Invalid date format. Expected YYYY-MM-DD, got: {}. Error: {}", date, e)
            ))?;

        self.inner.lock().set_capacity(parsed_date, capacity);
        Ok(())
    }

    /// Set whether the resource is constrained
    pub fn set_constrained(&mut self, is_constrained: bool) {
        self.inner.lock().set_constrained(is_constrained);
    }

    #[getter]
    pub fn is_constrained(&self) -> bool {
        self.inner.lock().is_constrained()
    }

    /// Print all capacity buckets for this resource
    pub fn print_all_capacity_buckets(&self) {
        self.inner.lock().print_all_capacity_buckets();
    }
}

/// Reset all SKUs, Operations and Resources in the system
#[pyfunction]
pub fn reset_network() {
    // Reset all SKUs
    for sku in SKU::get_all_skus() {
        sku.lock().reset();
    }

    // Reset all Operations
    for operation in Operation::get_all_operations() {
        operation.lock().reset();
    }

    // Reset all Resources
    for resource in Resource::get_all_resources() {
        resource.lock().reset();
    }

    // Reset all demands
    for demand in Demand::get_all_demands() {
        demand.lock().reset();
    }
}

/// Get all SKUs in the system
#[pyfunction]
pub fn get_all_skus() -> Vec<PySKU> {
    SKU::get_all_skus()
        .into_iter()
        .map(|sku| {
            let name = sku.lock().name().to_string();
            PySKU {
                name,
                inner: sku,
            }
        })
        .collect()
}

/// Get all Operations in the system
#[pyfunction]
pub fn get_all_operations() -> Vec<PyOperation> {
    Operation::get_all_operations()
        .into_iter()
        .map(|op| {
            let name = op.lock().get_name().to_string();
            PyOperation {
                name,
                inner: op,
            }
        })
        .collect()
}

/// Get all Resources in the system
#[pyfunction]
pub fn get_all_resources() -> Vec<PyResource> {
    Resource::get_all_resources()
        .into_iter()
        .map(|resource| {
            let name = resource.lock().get_name().to_string();
            PyResource {
                name,
                inner: resource,
            }
        })
        .collect()
}

/// Get all demands
#[pyfunction]
pub fn get_all_demands() -> Vec<PyDemand> {
    Demand::get_all_demands()
        .into_iter()
        .map(|demand| PyDemand { inner: demand })
        .collect()
}

#[pymodule]
fn supply(py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<PySKU>()?;
    m.add_class::<PyOperation>()?;
    m.add_class::<PyDemand>()?;
    m.add_class::<PyDemandPlanner>()?;
    m.add_class::<PyResource>()?;
    m.add_function(wrap_pyfunction!(reset_network, m)?)?;
    m.add_function(wrap_pyfunction!(get_all_skus, m)?)?;
    m.add_function(wrap_pyfunction!(get_all_operations, m)?)?;
    m.add_function(wrap_pyfunction!(get_all_resources, m)?)?;
    m.add_function(wrap_pyfunction!(get_all_demands, m)?)?;
    Ok(())
}