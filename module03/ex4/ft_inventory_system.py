import sys


def arg_inventory() -> dict[str, int]:
    inventory: dict[str, int] = {}
    index: int = 1
    while index < len(sys.argv):
        param: str = sys.argv[index]
        j: int = 0
        while j < len(param) and param[j] != ":":
            j += 1
        if j == len(param) or j == 0:
            print(f"Error - invalid parameter '{param}'")
        else:
            item_name: str = param[:j]
            quantity_text: str = param[j + 1:]
            if item_name in inventory:
                print(f"Redundant item '{item_name}' - discarding")
            else:
                try:
                    quantity: int = int(quantity_text)
                    inventory.update({item_name: quantity})
                except ValueError as error:
                    print(f"Quantity error for '{item_name}': {error}")
        index += 1
    return inventory


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = arg_inventory()
    item_list: list[str] = list(inventory.keys())
    total_quantity: int = sum(list(inventory.values()))
    print(f"Got inventory: {inventory}")
    print(f"Item list: {item_list}")
    print(f"Total quantity of the {len(item_list)} items: {total_quantity}")
    if len(item_list) > 0:
        most_item: str = item_list[0]
        least_item: str = item_list[0]
        index: int = 0
        while index < len(item_list):
            item_name: str = item_list[index]
            if total_quantity != 0:
                percentage: float = inventory[item_name] / total_quantity * 100
                print(f"Item {item_name} represents {round(percentage, 1)}%")
            if inventory[item_name] > inventory[most_item]:
                most_item = item_name
            if inventory[item_name] < inventory[least_item]:
                least_item = item_name
            index += 1
        print(
            f"Item most abundant: {most_item} "
            f"with quantity {inventory[most_item]}"
        )
        print(
            f"Item least abundant: {least_item} "
            f"with quantity {inventory[least_item]}"
        )
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
