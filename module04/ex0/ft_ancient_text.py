import sys
import typing


def close_file(file: typing.IO[str], file_name: str) -> None:
    try:
        file.close()
    except OSError as error:
        print(f"Error closing file '{file_name}': {error}")
    else:
        print(f"File '{file_name}' closed.")


def print_file(file_name: str) -> None:
    file: typing.IO[str]
    content: str

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{file_name}'")
    try:
        file = open(file_name, "r")
    except OSError as error:
        print(f"Error opening file '{file_name}': {error}")
        return
    try:
        content = file.read()
        print("---")
        print(content, end="")
        print("---")
    except OSError as error:
        print(f"Error reading file '{file_name}': {error}")
        return
    finally:
        close_file(file, file_name)


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    print_file(sys.argv[1])


if __name__ == "__main__":
    main()
