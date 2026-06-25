import random


ACHIEVEMENTS: list[str] = [
    "Crafting Genius",
    "World Savior",
    "Master Explorer",
    "Collector Supreme",
    "Untouchable",
    "Boss Slayer",
    "Strategist",
    "Unstoppable",
    "Speed Runner",
    "Survivor",
    "Treasure Hunter",
    "First Steps",
    "Sharp Mind",
    "Hidden Path Finder",
]


def gen_player_achievements() -> set[str]:
    achievement_count: int = random.randint(5, len(ACHIEVEMENTS) - 3)
    return set(random.sample(ACHIEVEMENTS, achievement_count))


def main() -> None:
    alice: set[str] = gen_player_achievements()
    bob: set[str] = gen_player_achievements()
    charlie: set[str] = gen_player_achievements()
    dylan: set[str] = gen_player_achievements()
    achievement_catalog: set[str] = set(ACHIEVEMENTS)

    all_distinct: set[str] = alice.union(bob, charlie, dylan)
    common: set[str] = alice.intersection(bob, charlie, dylan)

    print("=== Achievement Tracker System ===")
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")
    print(f"All distinct achievements: {all_distinct}")
    print(f"Common achievements: {common}")
    print(f"Only Alice has: {alice.difference(bob, charlie, dylan)}")
    print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
    print(f"Only Charlie has: {charlie.difference(alice, bob, dylan)}")
    print(f"Only Dylan has: {dylan.difference(alice, bob, charlie)}")
    print(f"Alice is missing: {achievement_catalog.difference(alice)}")
    print(f"Bob is missing: {achievement_catalog.difference(bob)}")
    print(f"Charlie is missing: {achievement_catalog.difference(charlie)}")
    print(f"Dylan is missing: {achievement_catalog.difference(dylan)}")


if __name__ == "__main__":
    main()
