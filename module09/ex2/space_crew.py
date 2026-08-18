from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank = Field(...)
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime = Field(...)
    duration_days: int = Field(..., ge=1, le=3650)
    crew: list[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        leadership_ranks = {Rank.COMMANDER, Rank.CAPTAIN}
        if not any(member.rank in leadership_ranks for member in self.crew):
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        if self.duration_days > 365:
            experienced_count = sum(
                member.years_experience >= 5 for member in self.crew
            )
            if experienced_count * 2 < len(self.crew):
                raise ValueError(
                    "Long missions (> 365 days) require at least 50% "
                    "experienced crew (5+ years)"
                )

        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")

        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=" * 41)

    mission = SpaceMission.model_validate(
        {
            "mission_id": "M2024_MARS",
            "mission_name": "Mars Colony Establishment",
            "destination": "Mars",
            "launch_date": "2025-07-15T09:00:00",
            "duration_days": 900,
            "budget_millions": 2500.0,
            "crew": [
                {
                    "member_id": "CM01",
                    "name": "Sarah Connor",
                    "rank": "commander",
                    "age": 45,
                    "specialization": "Mission Command",
                    "years_experience": 15,
                },
                {
                    "member_id": "CM02",
                    "name": "John Smith",
                    "rank": "lieutenant",
                    "age": 32,
                    "specialization": "Navigation",
                    "years_experience": 8,
                },
                {
                    "member_id": "CM03",
                    "name": "Alice Johnson",
                    "rank": "officer",
                    "age": 28,
                    "specialization": "Engineering",
                    "years_experience": 3,
                },
            ],
        }
    )

    print("Valid mission created:")
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions:.1f}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(
            f"- {member.name} ({member.rank.value}) "
            f"- {member.specialization}"
        )

    print()
    print("=" * 41)
    print("Expected validation error:")
    try:
        SpaceMission(
            mission_id="M2024_TEST",
            mission_name="Mars Survey Test",
            destination="Mars",
            launch_date=mission.launch_date,
            duration_days=900,
            budget_millions=500.0,
            crew=[mission.crew[1], mission.crew[2]],
        )
    except ValidationError as error:
        print(error)


if __name__ == "__main__":
    main()
