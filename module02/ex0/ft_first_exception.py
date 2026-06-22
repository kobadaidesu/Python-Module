def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    for temp_str in ("25", "abc"):
        try:
            temp_int = input_temperature(temp_str)
            print(f"Temperature is now {temp_int}°C")
        except ValueError as error:
            print(f"Caught input_temperature error: {error}")


if __name__ == "__main__":
    print("=== Garden Temperature ===\n")
    test_temperature()
    print("All tests completed - program didn't crash!")
