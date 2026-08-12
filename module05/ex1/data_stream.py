import abc
import typing


class DataProcessor(abc.ABC):
    name: str = "Processor"

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

    def get_total(self) -> int:
        return self._next_rank

    def get_remaining(self) -> int:
        return len(self._data)


class NumericProcessor(DataProcessor):
    name: str = "Numeric Processor"

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
    name: str = "Text Processor"

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
    name: str = "Log Processor"

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


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for element in stream:
            for proc in self._processors:
                if proc.validate(element):
                    proc.ingest(element)
                    break
            else:
                print(
                    "DataStream error - "
                    f"Can't process element in stream: {element}"
                )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return
        for proc in self._processors:
            print(
                f"{proc.name}: total {proc.get_total()} items processed, "
                f"remaining {proc.get_remaining()} on processor"
            )


def main() -> None:
    print("=== Code Nexus - Data Stream ===")
    print("Initialize DataStream")
    stream = DataStream()
    stream.print_processors_stats()

    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    print("Register NumericProcessor")
    stream.register_processor(numeric)

    batch: list[typing.Any] = [
        "hello",
        [3.5, -1, 2.0],
        [
            {
                "log_level": "INFO",
                "log_message": "Server started",
            },
            {
                "log_level": "ERROR",
                "log_message": "Request failed",
            },
        ],
        42,
        ["red", "blue"],
    ]
    print(f"First batch: {batch}")
    stream.process_stream(batch)
    stream.print_processors_stats()

    print("Register TextProcessor and LogProcessor")
    stream.register_processor(text)
    stream.register_processor(log)

    print("Process first batch again")
    stream.process_stream(batch)
    stream.print_processors_stats()

    print("Consume: Numeric=3, Text=2, Log=1")
    for _ in range(3):
        numeric.output()
    for _ in range(2):
        text.output()
    log.output()
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
