use std::fs::File;
use std::io::Write;
use crate::sku::SKU;
use crate::operation::Operation;
use crate::Resource;
use std::fs;
use std::io::BufReader;
use std::io::BufRead;

pub struct PlanExporter;

impl PlanExporter {
    // Folder where a new expect can be created. Not to be checked in.
    pub fn get_results_base_dir(test_name: &str) -> String {
        format!("tests/data/run_result/{}/expects", test_name)
    }
    pub fn get_results_base_dir_parent(test_name: &str) -> String {
        format!("tests/data/run_result/{}", test_name)
    }
    // Folder where expect files are manually moved and stored (for comparison during integration test runs).
    pub fn get_expects_base_dir(test_name: &str) -> String {
        format!("tests/data/{}/expects", test_name)
    }

    pub fn get_inventory_profiles_file() -> String {
        "inventory_profiles.csv".to_string()
    }
    pub fn get_resource_profiles_file() -> String {
        "resource_profiles.csv".to_string()
    }

    pub fn get_operation_plans_file() -> String {
        "operation_plans.csv".to_string()
    }

    pub fn export_inventory_profiles(test_name: &str) -> std::io::Result<()> {
        // Create directory if it doesn't exist
        let result_dir = format!("{}", PlanExporter::get_results_base_dir(test_name));
        fs::create_dir_all(result_dir.clone())?;
        let test_file = format!("{}/{}", result_dir, PlanExporter::get_inventory_profiles_file());
        let mut file = File::create(test_file)?;
        // Write header
        writeln!(file, "# SKU Name,Date,Quantity,Total Quantity")?;
        // Get all SKUs and sort them by name
        let mut skus = SKU::get_all_skus();
        skus.sort_by(|a, b| a.lock().name().cmp(b.lock().name()));
        
        // Export each SKU's inventory profile
        for sku in skus {
            let sku_ref = sku.lock();
            let sku_name = sku_ref.name();
            let profile = sku_ref.get_inventory_profile();
            // Get the inventory profile data
            let mut total_quantity = 0.0;
            for (date, quantity) in profile.get_profile() {
                total_quantity += quantity;
                writeln!(file, "{},{},{:.2},{:.2}", sku_name, date, quantity, total_quantity)?;
            }
        }
        
        Ok(())
    }

    pub fn export_resource_profiles(test_name: &str) -> std::io::Result<()> {
        // Create directory if it doesn't exist
        let mut resources = Resource::get_all_resources();
        if !resources.is_empty() {
            let result_dir = format!("{}", PlanExporter::get_results_base_dir(test_name));
            fs::create_dir_all(result_dir.clone())?;
            let test_file = format!("{}/{}", result_dir, PlanExporter::get_resource_profiles_file());
            let mut file = File::create(test_file)?;
            // Write header
            writeln!(file, "# Resource Name,Date,Available Capacity,Original Capacity")?;

            resources.sort_by(|a, b| a.lock().get_name().cmp(b.lock().get_name()));
            
            // Export each Resource's capacity profile
            for resource in resources {
                let resource_ref = resource.lock();
                let resource_name = resource_ref.get_name();
                for (&date, &capacity) in resource_ref.get_capacity_profile().iter() {
                    writeln!(file, "{},{},{:.2},{:.2}", resource_name, date, capacity.0, capacity.1)?;
                }
            }
        }
        Ok(())
    }


    fn compare_csv_files(expect_path: &str, actual_path: &str) -> std::io::Result<()> {
        let expect_file = File::open(expect_path)?;
        let actual_file = File::open(actual_path)?;
        
        // Create BufReaders to read the files line by line
        let expect_reader = BufReader::new(expect_file);
        let actual_reader = BufReader::new(actual_file);
        
        // Collect all lines into vectors
        let mut expect_lines: Vec<String> = expect_reader.lines().collect::<Result<_, _>>()?;
        let mut actual_lines: Vec<String> = actual_reader.lines().collect::<Result<_, _>>()?;
        
        // Keep the header (first line) separate and sort the rest
        let expect_header = expect_lines.remove(0);
        let actual_header = actual_lines.remove(0);
        // Sort the remaining lines
        expect_lines.sort();
        actual_lines.sort();
        // Compare headers first
        assert_eq!(expect_header, actual_header, "Headers don't match");
        // Then compare sorted content
        assert_eq!(expect_lines, actual_lines, "File contents don't match");

        Ok(())
    }

    pub fn compare_inventory_profiles(test_name: &str) -> std::io::Result<()> {
        let expect_file = format!("{}/{}", PlanExporter::get_expects_base_dir(test_name), "inventory_profiles.csv");
        let actual_file = format!("{}/{}", PlanExporter::get_results_base_dir(test_name), "inventory_profiles.csv");
        PlanExporter::compare_csv_files(&expect_file, &actual_file)
    }

    pub fn compare_operation_plans(test_name: &str) -> std::io::Result<()> {
        let expect_file = format!("{}/{}", PlanExporter::get_expects_base_dir(test_name), "operation_plans.csv");
        let actual_file = format!("{}/{}", PlanExporter::get_results_base_dir(test_name), "operation_plans.csv");
        PlanExporter::compare_csv_files(&expect_file, &actual_file)
    }

    pub fn compare_resource_profiles(test_name: &str) -> std::io::Result<()> {
        let expect_file = format!("{}/{}", PlanExporter::get_expects_base_dir(test_name), "resource_profiles.csv");
        let actual_file = format!("{}/{}", PlanExporter::get_results_base_dir(test_name), "resource_profiles.csv");
        if fs::metadata(actual_file.clone()).is_ok() {
            PlanExporter::compare_csv_files(&expect_file, &actual_file)
        }
        else {
            Ok(())
        }
    }

    pub fn export_operation_plans(test_name: &str) -> std::io::Result<()> {
        let result_dir = format!("{}", PlanExporter::get_results_base_dir(test_name));
        fs::create_dir_all(result_dir.clone())?;
        let test_file = format!("{}/{}", result_dir, PlanExporter::get_operation_plans_file());
        let mut file = File::create(test_file)?;
        
        // Updated header to include flow information
        writeln!(file, "# Operation,Start Date,End Date,Quantity")?;
        writeln!(file, "#   Operation,FlowDate,FlowQuantity,FlowType,Item")?;

        let operations = Operation::get_all_operations();
        for operation in operations {
            let operation_ref = operation.lock();
            let operation_plans = Operation::get_all_operation_plans(&operation_ref);
            for operation_plan in operation_plans {
                let operation_name = operation_ref.get_name();  
                let start_date = operation_plan.get_start_date();   
                let end_date = operation_plan.get_end_date();
                let quantity = operation_plan.get_quantity();
                
                // Write the base operation plan
                writeln!(file, "{},{},{},{:.2}", 
                    operation_name, start_date, end_date, quantity)?;
                
                // Export in_flows (consuming flows)
                for flow_plan in operation_plan.get_in_flows() {
                    let flow = flow_plan.lock();
                    let sku = flow.get_sku();
                    let sku_ref = sku.lock();
                    let sku_name = sku_ref.name();
                    writeln!(file, "  {},{},{:.2},Consuming,{}", 
                        operation_name, flow.get_date(), flow.get_quantity(), sku_name)?;
                }
                
                // Export out_flows (producing flows)
                for flow_plan in operation_plan.get_out_flows() {
                    let flow = flow_plan.lock();
                    let sku = flow.get_sku();
                    let sku_ref = sku.lock();
                    let sku_name = sku_ref.name();
                    writeln!(file, "  {},{},{:.2},Producing,{}",
                        operation_name, flow.get_date(), flow.get_quantity(), sku_name)?;
                }
                
                // Export resource flows
                for resource_flow_plan in operation_plan.get_in_resource_flows() {
                    let flow = resource_flow_plan.lock();
                    let resource = flow.get_resource();
                    let resource_ref = resource.lock();
                    let resource_name = resource_ref.get_name();
                    writeln!(file, "  {},{},{:.2},LoadResource,{}",
                        operation_name, flow.get_date(), flow.get_quantity(), resource_name)?;
                }
            }
        }
        Ok(())
    }

    pub fn export_all(test_name: &str) -> std::io::Result<()> {
        PlanExporter::export_inventory_profiles(test_name)?;
        PlanExporter::export_operation_plans(test_name)?;
        PlanExporter::export_resource_profiles(test_name)?;
        Ok(())
    }

    pub fn compare_all(test_name: &str) -> std::io::Result<()> {
        PlanExporter::compare_inventory_profiles(test_name)?;
        PlanExporter::compare_operation_plans(test_name)?;
        PlanExporter::compare_resource_profiles(test_name)?;
        Ok(())
    }

}

#[cfg(test)]
mod tests {
    use super::*;
    use serial_test::serial;
    use crate::sku::SKU;
    use std::fs;
    use std::io::BufReader;
    use std::io::BufRead;
    use chrono::NaiveDate;
    use crate::operation::Operation;
    use crate::flow::Flow;
    use crate::operation_plan::OperationPlan; 
    use crate::operation::MaterialFlowVariant;
    use crate::operation::ResourceFlowVariant;
    use std::sync::Arc;
    use parking_lot::Mutex;
    use crate::resource::Resource;

    fn setup_test_data() {
        // Clear any existing SKUs
        SKU::clear_repository();
        
        // Create test SKUs with inventory
        let sku1 = SKU::new("SKU_A");
        let sku2 = SKU::new("SKU_B");
        
        let date1 = NaiveDate::from_ymd_opt(2024, 1, 1).unwrap();
        let date2 = NaiveDate::from_ymd_opt(2024, 1, 2).unwrap();
        
        sku1.lock().add_inventory(date1, 100.0);
        sku1.lock().add_inventory(date2, -50.0);
        
        sku2.lock().add_inventory(date1, 200.0);
        sku2.lock().add_inventory(date2, 75.0);
    }

    fn setup_test_flows() -> (MaterialFlowVariant, MaterialFlowVariant) {
        let sku1 = SKU::from_name("test_produce");
        let sku2 = SKU::from_name("test_consume");
        
        let produce_flow = Flow::new(false, 1.0, sku1);
        let consume_flow = Flow::new(true, 2.0, sku2);
        
        (
            MaterialFlowVariant::Single(produce_flow),
            MaterialFlowVariant::Single(consume_flow)
        )
    }

    fn create_test_operation(name: &str) -> Arc<Mutex<Operation>> {
        let (produce_flow, consume_flow) = setup_test_flows();
        Operation::new(
            name.to_string(),
            10,
            100,
            5,
            produce_flow,
            consume_flow,
            ResourceFlowVariant::None,
        )
    }

    fn setup_test_operation_plans() {
        let operation = create_test_operation("test_op");
        let date = NaiveDate::from_ymd_opt(2024, 1, 1).unwrap();
        let plan = OperationPlan::new(date, date, 50.0);
        operation.lock().add_operation_plan(plan, false);
    }

    fn setup_test_resources() {
        Resource::clear_repository();
        
        let resource1 = Resource::from_name("Machine_A");
        let resource2 = Resource::from_name("Machine_B");
        
        let date1 = NaiveDate::from_ymd_opt(2024, 1, 1).unwrap();
        let date2 = NaiveDate::from_ymd_opt(2024, 1, 2).unwrap();
        
        resource1.lock().set_capacity(date1, 80.0);
        resource1.lock().set_capacity(date2, 90.0);
        
        resource2.lock().set_capacity(date1, 150.0);
        resource2.lock().set_capacity(date2, 180.0);
    }

    #[test]
    #[serial]
    fn test_export_inventory_profiles() {
        setup_test_data();
        
        let test_name = "case_2";
        let ouput_file = "inventory_profiles.csv";
        let result_dir = PlanExporter::get_results_base_dir(test_name);  
        let test_file = format!("{}/{}", result_dir, ouput_file);
        PlanExporter::export_inventory_profiles(test_name).unwrap();
        
        // Read the exported file in the results folder.
        let expect_file = test_file.clone();
        let file = File::open(expect_file).unwrap();
        let reader = BufReader::new(file);
        let actual_lines: Vec<String> = reader.lines().map(|l| l.unwrap()).collect();
        
        // Create expected CSV content
        let expected_lines = vec![
            "# SKU Name,Date,Quantity,Total Quantity".to_string(),
            "SKU_A,2024-01-01,100.00,100.00".to_string(),
            "SKU_A,2024-01-02,-50.00,50.00".to_string(),
            "SKU_B,2024-01-01,200.00,200.00".to_string(),
            "SKU_B,2024-01-02,75.00,275.00".to_string(),
        ];

        // Compare actual vs expected
        assert_eq!(actual_lines, expected_lines, "CSV content doesn't match expected output");
        
        fs::remove_dir_all(PlanExporter::get_results_base_dir_parent(test_name)).unwrap();

    }

    #[test]
    #[serial]
    fn test_compare_all() {
        SKU::clear_repository();
        Operation::clear_repository();
        Resource::clear_repository();
        setup_test_data();
        setup_test_operation_plans();
        let test_name = "exporter_sample";
        PlanExporter::export_all(test_name).unwrap();
        PlanExporter::compare_all(test_name).unwrap();
        fs::remove_dir_all(PlanExporter::get_results_base_dir_parent(test_name)).unwrap();
    }

    #[test]
    #[serial]
    fn test_export_resource_profiles() {
        setup_test_resources();
        
        let test_name = "case_4";
        let output_file = "resource_profiles.csv";
        let result_dir = PlanExporter::get_results_base_dir(test_name);  
        let test_file = format!("{}/{}", result_dir, output_file);

        PlanExporter::export_resource_profiles(test_name).unwrap();

        // Read the exported file
        let file = File::open(test_file.clone()).unwrap();
        let reader = BufReader::new(file);
        let actual_lines: Vec<String> = reader.lines().map(|l| l.unwrap()).collect();

        // Create expected CSV content
        let expected_lines = vec![
            "# Resource Name,Date,Available Capacity,Original Capacity".to_string(),
            "Machine_A,2024-01-01,80.00,80.00".to_string(),
            "Machine_A,2024-01-02,90.00,90.00".to_string(),
            "Machine_B,2024-01-01,150.00,150.00".to_string(),
            "Machine_B,2024-01-02,180.00,180.00".to_string(),
        ];

        // Compare actual vs expected
        assert_eq!(actual_lines, expected_lines, "CSV content doesn't match expected output");

        // Clean up test file
        fs::remove_dir_all(PlanExporter::get_results_base_dir_parent(test_name)).unwrap();
    }
}