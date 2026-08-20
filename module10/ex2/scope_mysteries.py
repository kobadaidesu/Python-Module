from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable[[], int]:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    total_power = initial_power

    def accumulate(power: int) -> int:
        nonlocal total_power
        total_power += power
        return total_power

    return accumulate


def enchantment_factory(
    enchantment_type: str,
) -> Callable[[str], str]:
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchant


def memory_vault() -> dict[str, Callable[..., Any]]:
    memories: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        memories[key] = value

    def recall(key: str) -> Any:
        return memories.get(key, "Memory not found")

    return {"store": store, "recall": recall}


def main() -> None:
    first_counter = mage_counter()
    second_counter = mage_counter()
    print("First counter:", first_counter(), first_counter())
    print("Second counter:", second_counter())

    accumulator = spell_accumulator(100)
    print("Accumulated power:", accumulator(20), accumulator(30))

    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print("Enchantments:", flaming("Sword"), frozen("Shield"))

    vault = memory_vault()
    vault["store"]("secret", 42)
    print("Stored memory:", vault["recall"]("secret"))
    print("Missing memory:", vault["recall"]("unknown"))


if __name__ == "__main__":
    main()
