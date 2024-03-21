import sys
import ast


def list_inventory():
    if len(inventory) == 0:
        print("Inventory empty.")
    else:
        print("ID: Count")
        for id,value in sorted(inventory.items()):
            print(f"{id}: {value}")

def add_inventory():
    id = input("Enter the item ID: ").title()
    if id in inventory:
        inventory[id] = inventory[id] + int(input(f"How many more {id} items? "))
    else:
        print(f"Error! {id} not in inventory!")

try:
    with (
open("inventories.txt") as input_file,
open("update.txt", "w") as output_file,
open("changes.txt", "a") as changes
):
        for i,line in enumerate(input_file):
            line = line.strip()
            inventory = eval(line)
            print(f"Current Inventory {i+1}:")
            list_inventory()
            add_inventory()
            print("New Inventory:")
            list_inventory()
            if eval(line) == inventory:
                print(f"No changes were made to Inventory {i}", file=changes)
            else:
                print(line, end=" -> ", file=changes)
                print(inventory, file=changes)
            print(inventory, file=output_file)
        print("--------------------------------------------", file=changes)
        
    with (
open("update.txt") as update,
open("inventories.txt", "w") as original
):
        for line in update:
            line = line.strip()
            inventory = eval(line)
            print(inventory, file=original)


except OSError:
    print(f"Couldn't open {OSError}")
    sys.exit()
