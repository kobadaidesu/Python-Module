class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = 0.0
        self._age = 0
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: float) -> bool:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            return False
        self._height = height
        return True

    def set_age(self, age: int) -> bool:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            return False
        self._age = age
        return True

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def grow(self) -> None:
        self.set_height(self._height + 0.8)

    def age(self) -> None:
        self.set_age(self._age + 1)

    def show(self) -> None:
        print(f"{self._name}: {round(self._height, 1)}cm, {self._age} days old")


def main() -> None:
    print("=== Garden Security System ===")

    rose = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    rose.show()

    if rose.set_height(25.0):
        print(f"Height updated: {rose.get_height():.0f}cm")
    else:
        print("Height update rejected")

    if rose.set_age(30):
        print(f"Age updated: {rose.get_age()} days")
    else:
        print("Age update rejected")

    if not rose.set_height(-5.0):
        print("Height update rejected")

    if not rose.set_age(-10):
        print("Age update rejected")

    print("Current state: ", end="")
    rose.show()


if __name__ == "__main__":
    main()
