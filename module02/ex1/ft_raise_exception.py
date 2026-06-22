def input_temperature(temp_str: str) -> int:
    temp_int = int(temp_str)
    if temp_int > 40:
        raise ValueError(f"{temp_int}°C is too hot for plants (max 40°C)")
    if temp_int < 0:
        raise ValueError(f"{temp_int}°C is too cold for plants (min 0°C)")
    return temp_int


def test_temperature() -> None:
    for temp_str in ("25", "abc", "100", "-50"):
        print(f"Input data is '{temp_str}'")
        try:
            temp_int = input_temperature(temp_str)
            print(f"Temperature is now {temp_int}°C")
        except ValueError as error:
            print(f"Caught input_temperature error: {error}")
        print()


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_temperature()
    print("All tests completed - program didn't crash!")
