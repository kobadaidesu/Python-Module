import random


players: list[str] = [
    "Alice", "bob", "Charlie", "dylan", "Emma",
    "Gregory", "john", "kevin", "Liam",
]


def main() -> None:
    capitalized_players: list[str] = [
        name.capitalize() for name in players
    ]
    capitalized_only: list[str] = [
        name for name in players if name == name.capitalize()
    ]
    score_dict: dict[str, int] = {
        name: random.randint(0, 1000) for name in capitalized_players
    }
    score_total: int = sum([score_dict[name] for name in score_dict])
    score_average: float = score_total / len(score_dict)
    high_scores: dict[str, int] = {
        name: score_dict[name]
        for name in score_dict
        if score_dict[name] > score_average
    }

    print("=== Game Data Alchemist ===")
    print(f"Initial list of players: {players}")
    print(f"New list with all names capitalized: {capitalized_players}")
    print(f"New list of capitalized names only: {capitalized_only}")
    print(f"Score dict: {score_dict}")
    print(f"Score average is {round(score_average, 2)}")
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
