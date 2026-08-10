import abc
import typing


class DataProcessor(abc.ABC):
    def __init__(self) -> None:
        self._data: list[tuple[int, str]] = []
        self._next_rank: int = 0

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        ...

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        ...

    def _store(self, value: str) -> None:
        self._data.append((self._next_rank, value))
        self._next_rank += 1

    def output(self) -> tuple[int, str]:
        if not self._data:
            raise IndexError("No data available in processor")
        return self._data.pop(0)


class NumericProcessor(DataProcessor):
    @staticmethod
    def _is_number(value: typing.Any) -> bool:
        return isinstance(value, (int, float)) and not isinstance(value, bool)

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, list):
            return bool(data) and all(
                self._is_number(item) for item in data
            )
        return self._is_number(data)

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise TypeError("Improper numeric data")
        values = data if isinstance(data, list) else [data]
        for value in values:
            self._store(str(value))


class TextProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, list):
            return bool(data) and all(isinstance(item, str) for item in data)
        return isinstance(data, str)

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise TypeError("Improper text data")
        values = data if isinstance(data, list) else [data]
        for value in values:
            self._store(value)


class LogProcessor(DataProcessor):
    @staticmethod
    def _is_log(value: typing.Any) -> bool:
        return isinstance(value, dict) and all(
            isinstance(k, str) and isinstance(v, str)
            for k, v in value.items()
        )

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, list):
            return bool(data) and all(self._is_log(item) for item in data)
        return self._is_log(data)

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise TypeError("Improper log data")
        values = data if isinstance(data, list) else [data]
        for entry in values:
            self._store(": ".join(entry.values()))


def print_validation(proc: DataProcessor, sample: typing.Any) -> None:
    print(f"validate({sample!r}) -> {proc.validate(sample)}")


def print_outputs(proc: DataProcessor, count: int) -> None:
    for _ in range(count):
        print(f"output() -> {proc.output()}")


def main() -> None:
    print("=== Code Nexus - Data Processor ===")

    print("NumericProcessor")
    numeric = NumericProcessor()
    print_validation(numeric, 42)
    print_validation(numeric, "hello")
    print("ingest('foo') without validate()")
    try:
        # Intentional invalid call required by the subject.
        numeric.ingest("foo")
    except TypeError as error:
        print(f"TypeError: {error}")
    numbers: list[int | float] = [1, 2.5, 3]
    print(f"ingest({numbers!r})")
    numeric.ingest(numbers)
    print_outputs(numeric, 3)

    print("TextProcessor")
    text = TextProcessor()
    print_validation(text, "hello")
    print_validation(text, 42)
    words = ["red", "green", "blue"]
    print(f"ingest({words!r})")
    text.ingest(words)
    print_outputs(text, 1)

    print("LogProcessor")
    log = LogProcessor()
    logs = [
        {"log_level": "INFO", "log_message": "Server started"},
        {"log_level": "ERROR", "log_message": "Request failed"},
    ]
    print_validation(log, logs[0])
    print_validation(log, "hello")
    print(f"ingest({logs!r})")
    log.ingest(logs)
    print_outputs(log, 2)


if __name__ == "__main__":
    main()
