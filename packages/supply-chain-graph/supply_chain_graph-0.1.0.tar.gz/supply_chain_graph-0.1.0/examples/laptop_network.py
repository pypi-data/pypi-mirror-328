from supply import PySKU
from supply import PyOperation
from supply import PyDemand
from supply import PyDemandPlanner
from supply import reset_network
from supply import get_all_skus
from supply import get_all_operations
from supply import get_all_resources
from supply import get_all_demands
from supply import PyResource

#===============================================

# Create a realistic laptop supply chain with alternate manufacturing locations
# SKUs at different locations
laptop_dc = PySKU.create("Laptop", "DC")
laptop_plant1 = PySKU.create("Laptop", "Plant1")
laptop_plant2 = PySKU.create("Laptop", "Plant2")

# Components at Plant1
disk_plant1 = PySKU.create("Disk", "Plant1")
cpu_plant1 = PySKU.create("CPU", "Plant1")
memory_plant1 = PySKU.create("Memory", "Plant1")

# Components at Plant2
disk_plant2 = PySKU.create("Disk", "Plant2")
cpu_plant2 = PySKU.create("CPU", "Plant2")
memory_plant2 = PySKU.create("Memory", "Plant2")

# Create assembly resources
assembly_resource_plant1 = PyResource("Assembly_Resource_Plant1")
assembly_resource_plant2 = PyResource("Assembly_Resource_Plant2")

# Set daily capacity for the resources (e.g., 100 units per day)
for day in range(15, 32):  # Jan 15-31
    date = f"2024-01-{day}"
    assembly_resource_plant1.set_capacity(date, 100.0)
    assembly_resource_plant2.set_capacity(date, 100.0)

# Create assembly operations for both plants with resources
laptop_assembly_plant1 = PyOperation("Make_Laptop_Plant1", lead_time=2, min_lot=1, increment=1)
laptop_assembly_plant1.add_produce_flow(laptop_plant1, quantity_per=1.0)
laptop_assembly_plant1.add_simultaneous_consume_flow(disk_plant1, quantity_per=1.0)
laptop_assembly_plant1.add_simultaneous_consume_flow(cpu_plant1, quantity_per=1.0)
laptop_assembly_plant1.add_simultaneous_consume_flow(memory_plant1, quantity_per=2.0)
laptop_assembly_plant1.add_resource(assembly_resource_plant1, quantity_per=1.0)  # Add resource requirement

laptop_assembly_plant2 = PyOperation("Make_Laptop_Plant2", lead_time=3, min_lot=1, increment=1)
laptop_assembly_plant2.add_produce_flow(laptop_plant2, quantity_per=1.0)
laptop_assembly_plant2.add_simultaneous_consume_flow(disk_plant2, quantity_per=1.0)
laptop_assembly_plant2.add_simultaneous_consume_flow(cpu_plant2, quantity_per=1.0)
laptop_assembly_plant2.add_simultaneous_consume_flow(memory_plant2, quantity_per=2.0)
laptop_assembly_plant2.add_resource(assembly_resource_plant2, quantity_per=1.0)  # Add resource requirement

# Create transport operations from plants to DC
move_laptop_plant1_to_dc = PyOperation("Move_Laptop_Plant1_to_DC", lead_time=1, min_lot=1, increment=1)
move_laptop_plant1_to_dc.add_produce_flow(laptop_dc, quantity_per=1.0)
move_laptop_plant1_to_dc.add_consume_flow(laptop_plant1, quantity_per=1.0)

move_laptop_plant2_to_dc = PyOperation("Move_Laptop_Plant2_to_DC", lead_time=1, min_lot=1, increment=1)
move_laptop_plant2_to_dc.add_produce_flow(laptop_dc, quantity_per=1.0)
move_laptop_plant2_to_dc.add_consume_flow(laptop_plant2, quantity_per=1.0)

# Link operations to SKUs
laptop_plant1.add_producing_operation(laptop_assembly_plant1)
laptop_plant1.generate_top_producing_operation()

laptop_plant2.add_producing_operation(laptop_assembly_plant2)
laptop_plant2.generate_top_producing_operation()

laptop_dc.add_producing_operation(move_laptop_plant1_to_dc)
laptop_dc.add_producing_operation(move_laptop_plant2_to_dc)
laptop_dc.generate_top_producing_operation()

# Add initial inventory
disk_plant1.add_inventory("2024-01-15", 1000.0)
cpu_plant1.add_inventory("2024-01-15", 250.0)
memory_plant1.add_inventory("2024-01-15", 500.0)
disk_plant2.add_inventory("2024-01-15", 1000.0)
cpu_plant2.add_inventory("2024-01-15", 250.0)
memory_plant2.add_inventory("2024-01-15", 500.0)

# Create and plan a demand
demand1 = PyDemand(id="D1",quantity=100.0,request_date="2024-01-31",max_lateness=0,sku=laptop_dc)
demand2 = PyDemand(id="D2",quantity=200.0,request_date="2024-01-30",max_lateness=0,sku=laptop_dc)


# Create planner and plan demand
planner = PyDemandPlanner()
planner.plan_demand_list([demand1, demand2], trace_level=2)

# Print results
print("\nDemand Plans:")
for demand in get_all_demands():
    demand.print_demand_plans()

print("\nInventory Profiles:")
for sku in get_all_skus():
    sku.print_inventory_profile()

print("\nOperation Plans:")
for op in get_all_operations():
    op.print_operation_plans()

print("\nResources:")
for res in get_all_resources():
    #if res.name == "Assembly_Resource_Plant1":
    res.print_all_capacity_buckets()

print("\nSupply Chain:")
sc = laptop_dc.get_supply_chain("2024-01-31")
for line in sc:
    print(line)


