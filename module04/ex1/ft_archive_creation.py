import sys
import typing


def close_file(file: typing.IO[str], file_name: str) -> None:
    try:
        file.close()
    except Exception as error:
        print(f"Error closing file '{file_name}': {error}")
    else:
        print(f"File '{file_name}' closed.")


def transform_content(content: str) -> str:
    lines: list[str] = content.splitlines()
    new_content: str = ""
    index: int = 0

    while index < len(lines):
        new_content += lines[index] + "#\n"
        index += 1
    return new_content


def save_content(content: str) -> None:
    new_file_name: str = input("Enter new file name (or empty): ")
    new_file: typing.IO[str]

    if new_file_name == "":
        print("Not saving data.")
        return
    print(f"Saving data to '{new_file_name}'")
    new_file = open(new_file_name, "w")
    new_file.write(content)
    new_file.close()
    print(f"Data saved in file '{new_file_name}'.")


def print_file(file_name: str) -> None:
    file: typing.IO[str]
    content: str
    new_content: str

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{file_name}'")
    try:
        file = open(file_name, "r")
    except Exception as error:
        print(f"Error opening file '{file_name}': {error}")
        return
    try:
        content = file.read()
    except Exception as error:
        print(f"Error reading file '{file_name}': {error}")
        close_file(file, file_name)
        return
    print("---")
    print(content, end="")
    print("---")
    close_file(file, file_name)
    new_content = transform_content(content)
    print("Transform data:")
    print("---")
    print(new_content, end="")
    print("---")
    save_content(new_content)


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return
    print_file(sys.argv[1])


if __name__ == "__main__":
    main()
