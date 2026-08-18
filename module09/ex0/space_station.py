from datetime import datetime

from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime = Field(...)
    is_operational: bool = Field(default=True)
    notes: str | None = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("=" * 40)

    station = SpaceStation.model_validate(
        {
            "station_id": "ISS001",
            "name": "International Space Station",
            "crew_size": 6,
            "power_level": 85.5,
            "oxygen_level": 92.3,
            "last_maintenance": "2024-05-20T15:30:00",
        }
    )

    print("Valid station created:")
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    status = "Operational" if station.is_operational else "Offline"
    print(f"Status: {status}")
    print(f"Last maintenance: {station.last_maintenance}")

    print()
    print("=" * 40)
    print("Expected validation error:")
    try:
        SpaceStation.model_validate(
            {
                "station_id": "ISS002",
                "name": "Overcrowded Station",
                "crew_size": 25,
                "power_level": 75.0,
                "oxygen_level": 90.0,
                "last_maintenance": "2024-05-20T15:30:00",
            }
        )
    except ValidationError as error:
        print(error)


if __name__ == "__main__":
    main()
