use crate::alternate_operation::AlternateOperation;
use crate::sku::SKU;
use chrono::NaiveDate;
use crate::operation::{Operation, OperationVariant, MaterialFlowVariant, ResourceFlowVariant};
use crate::flow::Flow;
use crate::simultaneous_flow::SimultaneousFlow;
use crate::resource::Resource;
use crate::resource_flow::ResourceFlow;
use std::sync::Arc;
use parking_lot::Mutex;

/*** 
                                Finished Good (FG)
                                      [*]
                                       |
                    +------------------+------------------+
                    |                  |                  |
                    v                  v                  v
     Main Assembly (P1)     Direct Production (P2)    Alt Assembly (P3)
    [Jan-Jul]  {AR}         [Apr+]    {AR}            [Jan+]
         |                        |                        |
    +----+----+              +----+----+            +-----+-----+
    |         |              |         |            |     |     |
    v         v              v         v            v     v     |
   MA        MB            RA11      RB22         CA1   CB2    +-> FG
    |         |             [*]                     ^     ^
    |         |         +----+----+                |     |
+---+---+  +--+--+     |         |                |     |
|       |  |     |     v         v                |     |
CA1    CA2 CB1  CB2   MV        AV               |     |
 |      |   |     |                              |     |
 |      |   |     +----+----+                    |     +----+----+
 |      |   |          |    |                    |          |    |
 v      v   v          v    v                    |          v    v
RA11   RA21 RB11     RB21 RB22                  |         RB21 RB22
RA12              

Legend:
[*]     = Alternate paths available
{AR}    = Assembly Resource required
->      = Material flow
P1/P2/P3= Priority levels
MA      = Make Component A
MB      = Make Component B
CA1/CA2 = Component A1/A2
CB1/CB2 = Component B1/B2
RA11    = Raw Material A11
MV/AV   = Main/Alt Vendor

                Raw A11
                 [*]
            +-----+-----+
            |           |
            v           v
    Main Vendor    Alt Vendor
    (Priority 1)   (Priority 2)
         ^              ^
         |              |
    Raw A11@Main    Raw A11@Alt

***/

pub fn create_sc_with_alternates() -> Arc<Mutex<SKU>> {
        // First create the same complex supply chain as in test_complex_supply_chain_traversal
        let final_product = SKU::from_name("Finished Good");
        let sub_assembly_a = SKU::from_name("Intermediate A");
        let sub_assembly_b = SKU::from_name("Intermediate B");
        let component_a1 = SKU::from_name("Component A1");
        let component_a2 = SKU::from_name("Component A2");
        let component_b1 = SKU::from_name("Component B1");
        let component_b2 = SKU::from_name("Component B2");
        let raw_a11 = SKU::from_name("Raw Material A11");
        let raw_a11_vendor_main = SKU::from_name("Raw A11@MainVendor");
        let raw_a11_vendor_alt = SKU::from_name("Raw A11@AltVendor");
        let raw_a12 = SKU::from_name("Raw Material A12");
        let raw_a21 = SKU::from_name("Raw Material A21");
        let raw_b11 = SKU::from_name("Raw Material B11");
        let raw_b21 = SKU::from_name("Raw Material B21");
        let raw_b22 = SKU::from_name("Raw Material B22");

        // Create assembly resource
        let assembly_resource = Resource::from_name("Assembly_Resource");

        assembly_resource.lock().set_capacity(
            NaiveDate::from_ymd_opt(2024, 1, 1).unwrap(),
            1000.0
        );

        let assembly_resource_flow = ResourceFlow::new(1.0, assembly_resource.clone());

        // Create the complex final assembly operation with resource
        let final_assembly_op = Operation::new(
            "Main Assembly".to_string(),
            1, 0, 0,
            MaterialFlowVariant::Single(Flow::new(false, 1.0, final_product.clone())),
            MaterialFlowVariant::Simultaneous(SimultaneousFlow::new(vec![
                Flow::new(true, 2.0, sub_assembly_a.clone()),
                Flow::new(true, 1.0, sub_assembly_b.clone()),
            ])),
            ResourceFlowVariant::SingleResource(assembly_resource_flow.clone()),
        );

        // Create direct production operation with resource
        let direct_production_op = Operation::new(
            "Direct Production".to_string(),
            2, 0, 0,
            MaterialFlowVariant::Single(Flow::new(false, 2.0, final_product.clone())),
            MaterialFlowVariant::Simultaneous(SimultaneousFlow::new(vec![
                Flow::new(true, 4.0, raw_a11.clone()),
                Flow::new(true, 3.0, raw_b22.clone()),
            ])),
            ResourceFlowVariant::SingleResource(assembly_resource_flow.clone()),
        );

        // Create a third alternative that uses different sub-assemblies.
        // Have one of the components to be a Finished Good to make a Cycle. 
        let alternative_assembly_op = Operation::new(
            "Alternative Assembly".to_string(),
            1, 0, 0,
            MaterialFlowVariant::Single(Flow::new(false, 1.0, final_product.clone())),
            MaterialFlowVariant::Simultaneous(SimultaneousFlow::new(vec![
                Flow::new(true, 3.0, component_a1.clone()),
                Flow::new(true, 2.0, component_b2.clone()),
                Flow::new(true, 1.0, final_product.clone()),  // ⚠️ Circular dependency: final_product requires itself

            ])),
            ResourceFlowVariant::None,
        );

        // Create and configure the alternate operation
        let alt_operation = AlternateOperation::new("Finished Good Production".to_string());
        
        // Add periods to operations
        let jan_1 = NaiveDate::from_ymd_opt(2024, 1, 1).unwrap();
        let apr_1 = NaiveDate::from_ymd_opt(2024, 4, 1).unwrap();
        let jul_1 = NaiveDate::from_ymd_opt(2024, 7, 1).unwrap();
        
        final_assembly_op.lock().add_period(Some(jan_1), Some(jul_1), 1);      // Priority 1, Jan-Jul
        direct_production_op.lock().add_period(Some(apr_1), None, 2);          // Priority 2, Apr onwards
        alternative_assembly_op.lock().add_period(Some(jan_1), None, 3);       // Priority 3, Jan onwards

        // Set up the alternate operation
        {
            let mut alt_op = alt_operation.lock();
            alt_op.add_operation_as_alternate(final_assembly_op.clone(), OperationVariant::Alternate(alt_operation.clone()));
            alt_op.add_operation_as_alternate(direct_production_op, OperationVariant::Alternate(alt_operation.clone()));
            alt_op.add_operation_as_alternate(alternative_assembly_op, OperationVariant::Alternate(alt_operation.clone()));
            alt_op.generate_period_to_effective_operation_map();
        }

        // Set up the rest of the complex supply chain (same as before)
        let sub_assembly_a_op = Operation::new(
            "Make Intermediate A".to_string(),
            1, 0, 0,
            MaterialFlowVariant::Single(Flow::new(false, 1.0, sub_assembly_a.clone())),
            MaterialFlowVariant::Simultaneous(SimultaneousFlow::new(vec![
                Flow::new(true, 3.0, component_a1.clone()),
                Flow::new(true, 1.0, component_a2.clone()),
            ])),
            ResourceFlowVariant::None,
        );

        let sub_assembly_b_op = Operation::new(
            "Make Intermediate B".to_string(),
            1, 0, 0,
            MaterialFlowVariant::Single(Flow::new(false, 1.0, sub_assembly_b.clone())),
            MaterialFlowVariant::Simultaneous(SimultaneousFlow::new(vec![
                Flow::new(true, 2.0, component_b1.clone()),
                Flow::new(true, 3.0, component_b2.clone()),
            ])),
            ResourceFlowVariant::None,
        );

        // Create operations for components
        let component_a1_op = Operation::new(
            "Make Component A1".to_string(),
            1, 0, 0,
            MaterialFlowVariant::Single(Flow::new(false, 1.0, component_a1.clone())),
            MaterialFlowVariant::Simultaneous(SimultaneousFlow::new(vec![
                Flow::new(true, 2.0, raw_a11.clone()),
                Flow::new(true, 4.0, raw_a12.clone()),
            ])),
            ResourceFlowVariant::None,
        );

        let component_a2_op = Operation::new(
            "Make Component A2".to_string(),
            1, 0, 0,
            MaterialFlowVariant::Single(Flow::new(false, 1.0, component_a2.clone())),
            MaterialFlowVariant::Single(Flow::new(true, 3.0, raw_a21.clone())),
            ResourceFlowVariant::None,
        );

        let component_b1_op = Operation::new(
            "Make Component B1".to_string(),
            1, 0, 0,
            MaterialFlowVariant::Single(Flow::new(false, 1.0, component_b1.clone())),
            MaterialFlowVariant::Single(Flow::new(true, 2.0, raw_b11.clone())),
            ResourceFlowVariant::None,
        );

        let component_b2_op = Operation::new(
            "Make Component B2".to_string(),
            1, 0, 0,
            MaterialFlowVariant::Single(Flow::new(false, 1.0, component_b2.clone())),
            MaterialFlowVariant::Simultaneous(SimultaneousFlow::new(vec![
                Flow::new(true, 1.0, raw_b21.clone()),
                Flow::new(true, 2.0, raw_b22.clone()),
            ])),
            ResourceFlowVariant::None,
        );

        // Set up all the relationships
        final_product.lock().set_top_producing_operation(OperationVariant::Alternate(alt_operation));
        sub_assembly_a.lock().set_top_producing_operation(OperationVariant::Basic(sub_assembly_a_op));
        sub_assembly_b.lock().set_top_producing_operation(OperationVariant::Basic(sub_assembly_b_op));
        component_a1.lock().set_top_producing_operation(OperationVariant::Basic(component_a1_op));
        component_a2.lock().set_top_producing_operation(OperationVariant::Basic(component_a2_op));
        component_b1.lock().set_top_producing_operation(OperationVariant::Basic(component_b1_op));
        component_b2.lock().set_top_producing_operation(OperationVariant::Basic(component_b2_op));

        // Add procurement operations for raw_a11
        let procure_main_op = Operation::new(
            "Procure from Main Vendor".to_string(),
            1, 0, 0,
            MaterialFlowVariant::Single(Flow::new(false, 2.0, raw_a11.clone())),
            MaterialFlowVariant::Single(Flow::new(true, 1.0, raw_a11_vendor_main.clone())),
            ResourceFlowVariant::None,
        );

        let procure_alt_op = Operation::new(
            "Procure from Alt Vendor".to_string(),
            1, 0, 0,
            MaterialFlowVariant::Single(Flow::new(false, 1.0, raw_a11.clone())),
            MaterialFlowVariant::Single(Flow::new(true, 1.0, raw_a11_vendor_alt.clone())),
            ResourceFlowVariant::None,
        );

        // Create and configure alternate operation for procurement
        let procurement_alt_operation = AlternateOperation::new("Raw A11 Procurement".to_string());
        
        // Add periods to procurement operations
        procure_main_op.lock().add_period(None, None, 1); 
        procure_alt_op.lock().add_period(None, None, 2);

        // Set up the procurement alternate operation
        {
            let mut alt_op = procurement_alt_operation.lock();
            alt_op.add_operation_as_alternate(procure_main_op, OperationVariant::Alternate(procurement_alt_operation.clone()));
            alt_op.add_operation_as_alternate(procure_alt_op, OperationVariant::Alternate(procurement_alt_operation.clone()));
            alt_op.generate_period_to_effective_operation_map();
        }

        raw_a11.lock().set_top_producing_operation(OperationVariant::Alternate(procurement_alt_operation));

        return final_product;
}