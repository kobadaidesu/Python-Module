from __future__ import annotations

from typing import Any


def artifact_sorter(
    artifacts: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    return sorted(
        artifacts,
        key=lambda artifact: artifact["power"],
        reverse=True,
    )


def power_filter(
    mages: list[dict[str, Any]], min_power: int
) -> list[dict[str, Any]]:
    return list(
        filter(lambda mage: mage["power"] >= min_power, mages)
    )


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, int | float]:
    strongest = max(mages, key=lambda mage: mage["power"])
    weakest = min(mages, key=lambda mage: mage["power"])
    total_power = sum(mage["power"] for mage in mages)
    avg_power = round(total_power / len(mages), 2)
    return {
        "max_power": strongest["power"],
        "min_power": weakest["power"],
        "avg_power": avg_power,
    }


def main() -> None:
    artifacts: list[dict[str, Any]] = [
        {"name": "Crystal Orb", "power": 75},
        {"name": "Fire Staff", "power": 92},
        {"name": "Magic Shield", "power": 80},
    ]
    spells = ["fireball", "heal", "shield"]

    print("Sorted artifacts:", artifact_sorter(artifacts))
    print("Powerful artifacts:", power_filter(artifacts, 80))
    print("Transformed spells:", spell_transformer(spells))
    print("Mage statistics:", mage_stats(artifacts))


if __name__ == "__main__":
    main()
