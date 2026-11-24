import sys


def parse_inventory(arguments: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}
    for argument in arguments:
        try:
            name, quantity_text = argument.split(":")
        except ValueError:
            print(f"Error - invalid parameter '{argument}'")
            continue
        name = name.strip()
        if not name:
            print(f"Error - invalid parameter '{argument}'")
            continue
        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue
        try:
            quantity = int(quantity_text)
            if quantity < 0:
                raise ValueError("quantity cannot be negative")
        except ValueError as error:
            print(f"Quantity error for '{name}': {error}")
            continue
        inventory.update({name: quantity})
    return inventory


def show_inventory(inventory: dict[str, int]) -> None:
    print(f"Got inventory: {inventory}")
    items = list(inventory.keys())
    print(f"Item list: {items}")
    total = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total}")
    if not items:
        print("Inventory is empty; no most or least abundant item.")
        return
    most = items[0]
    least = items[0]
    for item in inventory:
        percentage = inventory[item] / total * 100 if total else 0.0
        print(f"Item {item} represents {round(percentage, 1):.1f}%")
        if inventory[item] > inventory[most]:
            most = item
        if inventory[item] < inventory[least]:
            least = item
    print(f"Item most abundant: {most} with quantity {inventory[most]}")
    print(f"Item least abundant: {least} with quantity {inventory[least]}")


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory = parse_inventory(sys.argv[1:])
    show_inventory(inventory)
    new_item = "magic_item"
    suffix = 1
    while new_item in inventory:
        new_item = f"magic_item_{suffix}"
        suffix += 1
    inventory.update({new_item: 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
