class Plant:
    name: str
    height: float
    age: int

    def grow(self) -> None:
        self.height += 0.8

    def get_age(self) -> None:
        self.age += 1

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")


def main() -> None:
    Rose = Plant()
    Rose.name = "Rose"
    Rose.height = 25.0
    Rose.age = 30
    start_height = Rose.height
    Rose.show()
    print("=== Garden Plant Growth ===")
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        Rose.grow()
        Rose.get_age()
        Rose.show()
    total_growth = Rose.height - start_height
    print(f"Growth this week: {round(total_growth, 1)}cm")


if __name__ == "__main__":
    main()
