import typing

from ex0 import AquaFactory, CreatureFactory, FlameFactory
from ex0.creatures import Creature
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import AggressiveStrategy, BattleStrategy, DefensiveStrategy
from ex2 import InvalidStrategyError, NormalStrategy

Opponent: typing.TypeAlias = tuple[CreatureFactory, BattleStrategy]
Competitor: typing.TypeAlias = tuple[Creature, BattleStrategy]


def perform_actions(
    creature: Creature,
    strategy: BattleStrategy,
) -> None:
    for action in strategy.act(creature):
        print(action)


def battle(opponents: list[Opponent]) -> None:
    competitors: list[Competitor] = []
    for factory, strategy in opponents:
        competitors.append((factory.create_base(), strategy))

    print("*** Tournament ***")
    print(f"{len(competitors)} opponents involved")

    try:
        for first_index in range(len(competitors)):
            for second_index in range(first_index + 1, len(competitors)):
                first_creature, first_strategy = competitors[first_index]
                second_creature, second_strategy = competitors[second_index]

                print("* Battle *")
                print(first_creature.describe())
                print("vs.")
                print(second_creature.describe())
                print("now fight!")
                perform_actions(first_creature, first_strategy)
                perform_actions(second_creature, second_strategy)
    except InvalidStrategyError as error:
        print(f"Battle error, aborting tournament: {error}")


def main() -> None:
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battle([
        (FlameFactory(), normal),
        (HealingCreatureFactory(), defensive),
    ])

    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([
        (FlameFactory(), aggressive),
        (HealingCreatureFactory(), defensive),
    ])

    print("Tournament 2 (multiple)")
    print(
        "[ (Aquabub+Normal), (Healing+Defensive), "
        "(Transform+Aggressive) ]"
    )
    battle([
        (AquaFactory(), normal),
        (HealingCreatureFactory(), defensive),
        (TransformCreatureFactory(), aggressive),
    ])


if __name__ == "__main__":
    main()
