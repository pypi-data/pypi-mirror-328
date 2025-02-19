from supply import PySKU
from supply import PyOperation
from supply import PyDemand
from supply import PyDemandPlanner
from supply import reset_network
from supply import get_all_skus
from supply import get_all_operations
from supply import get_all_resources

# Create SKUs
body_sku = PySKU.create("Body", "Plant1")
output_sku = PySKU.create("Car", "Plant1")
print(type(body_sku))

# Example of simultaneous flows
engine_sku = PySKU.create("Engine", "Plant1")
op = PyOperation("AssembleCarInPlant2", lead_time=1, min_lot=100, increment=10)
op.add_produce_flow(output_sku, quantity_per=1.0)
op.add_simultaneous_consume_flow(body_sku, quantity_per=1.0)
op.add_simultaneous_consume_flow(engine_sku, quantity_per=1.0)
op.add_simultaneous_consume_flow(body_sku, quantity_per=1.0)

# Add the operations to the SKUs
output_sku.add_producing_operation(op)
output_sku.generate_top_producing_operation()
# Print operation details
print(f"Operation: {op.name}")
print(f"Lead Time: {op.lead_time}")
print(f"Min Lot: {op.min_lot}")
print(f"Increment: {op.increment}")


print("Supply Chain:")
sc = output_sku.get_supply_chain("2024-01-01")
for line in sc:
    print(line)



# Real life example - Complex Supply Chain with Alternates
# Create SKUs for finished good and components
fg = PySKU.create("Finished_Good", "Plant1")
sub_assy_a = PySKU.create("Subassembly_A", "Plant1")
sub_assy_b = PySKU.create("Subassembly_B", "Plant1")
comp_a1 = PySKU.create("Component_A1", "Plant1")
comp_b1 = PySKU.create("Component_B1", "Plant1")
raw_a11 = PySKU.create("Raw_A11", "Plant1")
raw_a11_main = PySKU.create("Raw_A11", "MainVendor")
raw_a11_alt = PySKU.create("Raw_A11", "AltVendor")

# Create main assembly operation with two effective periods
main_assembly = PyOperation("Main_Assembly", lead_time=1, min_lot=100, increment=10)
main_assembly.add_produce_flow(fg, quantity_per=1.0)
main_assembly.add_simultaneous_consume_flow(sub_assy_a, quantity_per=2.0)
main_assembly.add_simultaneous_consume_flow(sub_assy_b, quantity_per=1.0)

# Add effective periods for main assembly:
# Jan-Mar with priority 1 (high priority)
main_assembly.add_period(1, from_date="2024-01-01", till_date="2024-04-01")
# May-Dec with priority 3 (low priority)
main_assembly.add_period(3, from_date="2024-05-01", till_date="2024-12-31")

# Create direct production with one effective period
direct_prod = PyOperation("Direct_Production", lead_time=2, min_lot=200, increment=20)
direct_prod.add_produce_flow(fg, quantity_per=1.0)
direct_prod.add_simultaneous_consume_flow(raw_a11, quantity_per=4.0)

# Add effective period for direct production:
# Jan-Dec with priority 2 (medium priority)
direct_prod.add_period(2, from_date="2024-01-01", till_date="2024-12-31")
#direct_prod.add_period(2, from_date=None, till_date=None)

# Add both operations to finished good
fg.add_producing_operation(main_assembly)
fg.add_producing_operation(direct_prod)
fg.generate_top_producing_operation()

# Create subassembly operations
sub_a_op = PyOperation("Make_Subassembly_A", lead_time=1, min_lot=50, increment=10)
sub_a_op.add_produce_flow(sub_assy_a, quantity_per=1.0)
sub_a_op.add_consume_flow(comp_a1, quantity_per=2.0)
sub_assy_a.add_producing_operation(sub_a_op)
sub_assy_a.generate_top_producing_operation()

# Create procurement operations with alternates
procure_main = PyOperation("Procure_Main_Vendor", lead_time=3, min_lot=1000, increment=100)
procure_main.add_produce_flow(raw_a11, quantity_per=1.0)
procure_main.add_consume_flow(raw_a11_main, quantity_per=1.0)

procure_alt = PyOperation("Procure_Alt_Vendor", lead_time=2, min_lot=500, increment=50)
procure_alt.add_produce_flow(raw_a11, quantity_per=1.0)
procure_alt.add_consume_flow(raw_a11_alt, quantity_per=1.0)

raw_a11.add_producing_operation(procure_main)
raw_a11.add_producing_operation(procure_alt)
raw_a11.generate_top_producing_operation()

# Print the supply chain at different dates to see the effect of priorities
print("\nSupply Chain in February (Main Assembly Priority 1):")
sc = fg.get_supply_chain("2024-02-15")
for line in sc:
    print(line)

print("\nSupply Chain As seen from 2025-06-11:")
sc = fg.get_supply_chain("2025-06-11")
for line in sc:
    print(line)

# Create a demand for 100 units of finished good
demand1 = PyDemand(
    id="D1",
    quantity=1000.0,
    request_date="2024-03-31",
    max_lateness=0,
    sku=fg
)

# Create another demand with different priority
demand2 = PyDemand(
    id="D2",
    quantity=2000.0,
    request_date="2024-04-30",
    max_lateness=7,
    sku=fg
)

# Set priorities (lower number means higher priority)
demand1.set_priority(1)  # High priority
demand2.set_priority(2)  # Lower priority

# Create a list of demands
demands = [demand1, demand2]
# After planning (if you implement planning functionality)
print(f"Planned Quantity: {demand1.get_planned_quantity()}")

# Add inventory to SKUs
raw_a11.add_inventory("2024-01-15", 10000.0)
# Print inventory profiles
print("\nInitial Inventory Profiles:")
raw_a11.print_inventory_profile()


# Create planner and plan demands
planner = PyDemandPlanner()


# Plan list of demands
print("\nPlanning multiple demands:")
planner.plan_demand_list([demand1, demand2], trace_level=2)


print("\nAfter First Planning:")
for demand in [demand1, demand2]:
    demand.print_demand_plans()

# Print final inventory profiles
print("\nFinal Inventory Profiles:")
for sku in get_all_skus():
    sku.print_inventory_profile()
print("\nFinal Resource Profiles:")    
for res in get_all_resources():
    res.print_all_capacity_buckets()
print("\nFinal Operation Plans:")
for op in get_all_operations():
    op.print_operation_plans()

reset_network()
print("\nAfter Reset:")
for sku in get_all_skus():
    sku.print_inventory_profile()
print("\nAfter Reset Resource Profiles:")    
for res in get_all_resources():
    res.print_all_capacity_buckets()
print("\nAfter Reset Operation Plans:")
for op in get_all_operations():
    op.print_operation_plans()

raw_a11.add_inventory("2024-01-15", 10000.0)
# sort in reverse order of request date
demands = sorted(demands, key=lambda x: x.request_date, reverse=True)
planner.plan_demand_list(demands, trace_level=2)

print("\nAfter Second Planning:")
for demand in demands:
    demand.print_demand_plans()
