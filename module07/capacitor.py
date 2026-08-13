from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_healing_creatures() -> None:
    factory = HealingCreatureFactory()
    base_creature = factory.create_base()
    evolved_creature = factory.create_evolved()

    print("Testing Creature with healing capability")
    print("base:")
    print(base_creature.describe())
    print(base_creature.attack())
    print(base_creature.heal())
    print("evolved:")
    print(evolved_creature.describe())
    print(evolved_creature.attack())
    print(evolved_creature.heal())


def test_transform_creatures() -> None:
    factory = TransformCreatureFactory()
    base_creature = factory.create_base()
    evolved_creature = factory.create_evolved()

    print("Testing Creature with transform capability")
    print("base:")
    print(base_creature.describe())
    print(base_creature.attack())
    print(base_creature.transform())
    print(base_creature.attack())
    print(base_creature.revert())
    print("evolved:")
    print(evolved_creature.describe())
    print(evolved_creature.attack())
    print(evolved_creature.transform())
    print(evolved_creature.attack())
    print(evolved_creature.revert())


def main() -> None:
    test_healing_creatures()
    test_transform_creatures()


if __name__ == "__main__":
    main()
