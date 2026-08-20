import functools
import operator
from collections.abc import Callable
from typing import Any


Enchantment = Callable[[int, str, str], str]


def spell_reducer(spells: list[int], operation: str) -> int:
    operations: dict[str, Callable[[int, int], int]] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min,
    }
    if operation not in operations:
        raise ValueError(f"Unknown operation: {operation}")
    if not spells:
        return 0
    return functools.reduce(operations[operation], spells)


def partial_enchanter(
    base_enchantment: Enchantment,
) -> dict[str, Callable[[str], str]]:
    return {
        "fire_enchant": functools.partial(
            base_enchantment, 50, "fire"
        ),
        "ice_enchant": functools.partial(base_enchantment, 50, "ice"),
        "lightning_enchant": functools.partial(
            base_enchantment, 50, "lightning"
        ),
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def dispatch(spell: Any) -> str:
        return "Unknown spell type"

    @dispatch.register(int)
    def dispatch_int(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatch.register(str)
    def dispatch_str(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispatch.register(list)
    def dispatch_list(spell: list[Any]) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return dispatch


def main() -> None:
    spells = [10, 20, 30]
    print("Sum:", spell_reducer(spells, "add"))
    print("Product:", spell_reducer(spells, "multiply"))
    print("Maximum:", spell_reducer(spells, "max"))
    print("Minimum:", spell_reducer(spells, "min"))

    def base_enchantment(power: int, element: str, target: str) -> str:
        return f"{element} enchantment on {target} with {power} power"

    enchanters = partial_enchanter(base_enchantment)
    print(enchanters["fire_enchant"]("Sword"))
    print(enchanters["ice_enchant"]("Shield"))
    print(enchanters["lightning_enchant"]("Axe"))

    print("Fibonacci(10):", memoized_fibonacci(10))

    dispatch = spell_dispatcher()
    print(dispatch(42))
    print(dispatch("Fire Shield"))
    print(dispatch(["fireball", "heal", "shield"]))
    print(dispatch(3.14))


if __name__ == "__main__":
    main()
