import abc
import typing


class DataProcessor(abc.ABC):
    def __init__(self) -> None:
        # FIFO: (rank, str化した値)
        self._data: list[tuple[int, str]] = []
        self._total: int = 0

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        ...

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        ...

    def _store(self, value: str) -> None:
        self._data.append((self._total, value))
        self._total += 1

    def output(self) -> tuple[int, str]:
        if not self._data:
            raise IndexError("No data available in processor")
        return self._data.pop(0)


class NumericProcessor(DataProcessor):
    @staticmethod
    def _is_number(value: typing.Any) -> bool:
        # bool は int の派生型なので明示的に除外する
        return isinstance(value, (int, float)) and not isinstance(value, bool)

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, list):
            if not data:  
                return False
            return all(self._is_number(item) for item in data)
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
            if not data:
                return False
            return all(isinstance(item, str) for item in data)
        return isinstance(data, str)

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise TypeError("Improper text data")
        values = data if isinstance(data, list) else [data]
        for value in values:
            self._store(value)  # 既に str → 変換なしでそのまま


class LogProcessor(DataProcessor):
    @staticmethod
    def _is_log(value: typing.Any) -> bool:
        return isinstance(value, dict) and all(
            isinstance(k, str) and isinstance(v, str)
            for k, v in value.items()
        )

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, list):
            if not data:
                return False
            return all(self._is_log(item) for item in data)
        return self._is_log(data)

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise TypeError("Improper log data")
        values = data if isinstance(data, list) else [data]
        for entry in values:
            self._store(": ".join(entry.values()))


def print_validation(proc: DataProcessor, sample: typing.Any) -> None:
    print(f"Trying to validate input '{sample}': {proc.validate(sample)}")


def extract_and_print(proc: DataProcessor, count: int, label: str) -> None:
    unit = "value" if count == 1 else "values"
    print(f"Extracting {count} {unit}...")
    for _ in range(count):
        rank, value = proc.output()
        print(f"{label} {rank}: {value}")


def main() -> None:
    print("=== Code Nexus - Data Processor ===")

    print("Testing Numeric Processor...")
    numeric = NumericProcessor()
    print_validation(numeric, 42)
    print_validation(numeric, "Hello")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        # 意図的に型違反の不正データを渡す(subject 記載の mypy 警告が出る)
        numeric.ingest("foo")
    except TypeError as error:
        print(f"Got exception: {error}")
    numbers: list[int | float] = [1, 2, 3, 4, 5]
    print(f"Processing data: {numbers}")
    numeric.ingest(numbers)
    extract_and_print(numeric, 3, "Numeric value")

    print("Testing Text Processor...")
    text = TextProcessor()
    print_validation(text, 42)
    words = ["Hello", "Nexus", "World"]
    print(f"Processing data: {words}")
    text.ingest(words)
    extract_and_print(text, 1, "Text value")

    print("Testing Log Processor...")
    log = LogProcessor()
    print_validation(log, "Hello")
    logs = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]
    print(f"Processing data: {logs}")
    log.ingest(logs)
    extract_and_print(log, 2, "Log entry")


if __name__ == "__main__":
    main()
