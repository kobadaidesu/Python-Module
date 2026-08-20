from collections.abc import Callable


Spell = Callable[[str, int], str]
Condition = Callable[[str, int], bool]


def spell_combiner(
    spell1: Spell, spell2: Spell
) -> Callable[[str, int], tuple[str, str]]:
    def combined_spell(target: str, power: int) -> tuple[str, str]:
        return spell1(target, power), spell2(target, power)

    return combined_spell


def power_amplifier(
    base_spell: Spell, multiplier: int
) -> Spell:
    def amplified_spell(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    return amplified_spell


def conditional_caster(
    condition: Condition, spell: Spell
) -> Spell:
    def conditional_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"

    return conditional_spell


def spell_sequence(spells: list[Spell]) -> Callable[[str, int], list[str]]:
    def sequence_spell(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]

    return sequence_spell


def main() -> None:
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} with {power} damage"

    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power} HP"

    def has_enough_power(target: str, power: int) -> bool:
        return power >= 50

    combined = spell_combiner(fireball, heal)
    amplified = power_amplifier(fireball, 3)
    conditional = conditional_caster(has_enough_power, fireball)
    sequence = spell_sequence([fireball, heal])

    print("Combined:", combined("Dragon", 40))
    print("Amplified:", amplified("Dragon", 20))
    print("Conditional success:", conditional("Dragon", 60))
    print("Conditional failure:", conditional("Dragon", 30))
    print("Sequence:", sequence("Dragon", 50))


if __name__ == "__main__":
    main()
