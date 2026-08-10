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

    @property
    def total(self) -> int:
        return self._next_rank

    @property
    def remaining(self) -> int:
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
            isinstance(key, str) and isinstance(item, str)
            for key, item in value.items()
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


class ExportPlugin(typing.Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVExportPlugin:
    @staticmethod
    def _escape(value: str) -> str:
        escaped = value.replace('"', '""')
        if any(mark in value for mark in (",", '"', "\n", "\r")):
            return f'"{escaped}"'
        return escaped

    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = [self._escape(value) for _, value in data]
        print("CSV Output:")
        print(",".join(values))


class JSONExportPlugin:
    @staticmethod
    def _escape(value: str) -> str:
        return (
            value.replace("\\", "\\\\")
            .replace('"', '\\"')
            .replace("\b", "\\b")
            .replace("\f", "\\f")
            .replace("\n", "\\n")
            .replace("\r", "\\r")
            .replace("\t", "\\t")
        )

    def process_output(self, data: list[tuple[int, str]]) -> None:
        items = [
            f'"item_{rank}": "{self._escape(value)}"'
            for rank, value in data
        ]
        print("JSON Output:")
        print("{" + ", ".join(items) + "}")


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
                f"{proc.name}: total {proc.total} items processed, "
                f"remaining {proc.remaining} on processor"
            )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self._processors:
            output_data: list[tuple[int, str]] = []
            for _ in range(min(nb, proc.remaining)):
                output_data.append(proc.output())
            if output_data:
                plugin.process_output(output_data)


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===")
    print("Initialize DataStream")
    stream = DataStream()
    stream.print_processors_stats()

    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    print("Register processors")
    stream.register_processor(numeric)
    stream.register_processor(text)
    stream.register_processor(log)

    first_batch: list[typing.Any] = [
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
    print(f"First batch: {first_batch}")
    stream.process_stream(first_batch)
    stream.print_processors_stats()

    print("CSV plugin: 3 items per processor")
    stream.output_pipeline(3, CSVExportPlugin())
    stream.print_processors_stats()

    second_batch: list[typing.Any] = [
        21,
        ["apple", "banana", "orange"],
        [
            {"log_level": "ERROR", "log_message": "Server stopped"},
            {
                "log_level": "INFO",
                "log_message": "Server restarted",
            },
        ],
        [10, 20, 30],
        "goodbye",
    ]
    print(f"Second batch: {second_batch}")
    stream.process_stream(second_batch)
    stream.print_processors_stats()

    print("JSON plugin: 5 items per processor")
    stream.output_pipeline(5, JSONExportPlugin())
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
