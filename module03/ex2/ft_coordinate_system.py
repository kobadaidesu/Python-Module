import math


def get_player_pos() -> tuple[float, float, float]:
    prompt: str = "Enter new coordinates as floats in format 'x,y,z': "
    while True:
        text: str = input(prompt)
        try:
            x_text, y_text, z_text = text.split(",")
        except ValueError:
            print("Invalid syntax")
            continue
        try:
            bad_value: str = x_text
            x: float = float(x_text)
            bad_value = y_text
            y: float = float(y_text)
            bad_value = z_text
            z: float = float(z_text)
        except ValueError as error:
            print(f"Error on parameter '{bad_value}': {error}")
            continue
        return (x, y, z)


def get_distance(first_pos: tuple[float, float, float], second_pos: tuple[float, float, float],) -> float:
    x1, y1, z1 = first_pos
    x2, y2, z2 = second_pos
    return math.sqrt((x2 - x1) ** 2  + (y2 - y1) ** 2  + (z2 - z1) ** 2)


def main() -> None:
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    first_pos: tuple[float, float, float] = get_player_pos()
    print(f"Got a first tuple: {first_pos}")
    print(f"It includes: X={first_pos[0]}, "f"Y={first_pos[1]}, Z={first_pos[2]}")
    center_pos: tuple[float, float, float] = (0.0, 0.0, 0.0)
    center_distance: float = get_distance(center_pos, first_pos)
    print(f"Distance to center: {round(center_distance, 4)}")
    print("Get a second set of coordinates")
    second_pos: tuple[float, float, float] = get_player_pos()
    distance: float = get_distance(first_pos, second_pos)
    print(f"Distance between the 2 sets of coordinates: {round(distance, 4)}")


if __name__ == "__main__":
    main()
