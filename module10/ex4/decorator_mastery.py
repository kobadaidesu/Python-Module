import functools
from collections.abc import Callable
from time import perf_counter
from typing import Any, TypeVar, cast
from time import sleep


F = TypeVar("F", bound=Callable[..., Any])


def spell_timer(func: F) -> F:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start = perf_counter()
        result = func(*args, **kwargs)
        elapsed = perf_counter() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result

    return cast(F, wrapper)


def power_validator(min_power: int) -> Callable[[F], F]:
    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power = kwargs.get("power")
            if power is None and args:
                power = args[-1]
            if not isinstance(power, int) or power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)

        return cast(F, wrapper)

    return decorator


def retry_spell(max_attempts: int) -> Callable[[F], F]:
    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            "Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )
            return (
                "Spell casting failed after "
                f"{max_attempts} attempts"
            )

        return cast(F, wrapper)

    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        return all(
            character.isalpha() or character.isspace()
            for character in name
        )

    @power_validator(min_power=10)
    def cast_spell(
        self: "MageGuild", spell_name: str, power: int
    ) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    @spell_timer
    def fireball() -> str:
        sleep(0.1)
        return "Fireball cast!"

    @power_validator(min_power=20)
    def empowered_spell(target: str, power: int) -> str:
        return f"Empowered spell hits {target} with {power} power"

    attempts = 0

    @retry_spell(max_attempts=3)
    def unstable_spell() -> str:
        nonlocal attempts
        attempts += 1
        if attempts < 3:
            raise RuntimeError("Spell failed")
        return "Unstable spell cast!"

    print("Timer result:", fireball())
    print("Validated:", empowered_spell("Dragon", power=20))
    print("Rejected:", empowered_spell("Dragon", 19))
    print("Retry result:", unstable_spell())
    print("Valid mage name:", MageGuild.validate_mage_name("Merlin"))
    print("Invalid mage name:", MageGuild.validate_mage_name("M3"))

    guild = MageGuild()
    print("Guild cast:", guild.cast_spell("Lightning", 10))
    print("Guild rejection:", guild.cast_spell("Lightning", 9))


if __name__ == "__main__":
    main()
