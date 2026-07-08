class Plant:
    name: str
    height: float
    _age: int

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self._age += 1

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self._age} days old")


def main() -> None:
    Rose = Plant()
    Rose.name = "Rose"
    Rose.height = 25.0
    Rose._age = 30
    start_height = Rose.height
    print("=== Garden Plant Growth ===")
    Rose.show()
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        Rose.grow()
        Rose.age()
        Rose.show()
    total_growth = Rose.height - start_height
    print(f"Growth this week: {round(total_growth, 1)}cm")


if __name__ == "__main__":
    main()
