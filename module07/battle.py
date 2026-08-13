from ex0 import AquaFactory, CreatureFactory, FlameFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base_creature = factory.create_base()
    evolved_creature = factory.create_evolved()

    print(base_creature.describe())
    print(base_creature.attack())
    print(evolved_creature.describe())
    print(evolved_creature.attack())


def test_battle(
    first_factory: CreatureFactory,
    second_factory: CreatureFactory,
) -> None:
    print("Testing battle")
    first_creature = first_factory.create_base()
    second_creature = second_factory.create_base()

    print(first_creature.describe())
    print("vs.")
    print(second_creature.describe())
    print("fight!")
    print(first_creature.attack())
    print(second_creature.attack())


def main() -> None:
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()

    test_factory(flame_factory)
    test_factory(aqua_factory)
    test_battle(flame_factory, aqua_factory)


if __name__ == "__main__":
    main()
