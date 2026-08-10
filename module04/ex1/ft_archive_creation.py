import sys
import typing


def close_file(file: typing.IO[str], file_name: str) -> None:
    try:
        file.close()
    except OSError as error:
        print(f"Error closing file '{file_name}': {error}")
    else:
        print(f"File '{file_name}' closed.")


def transform_content(content: str) -> str:
    lines: list[str] = content.splitlines()
    new_content: str = ""

    for line in lines:
        new_content += line + "#\n"
    return new_content


def print_content(content: str) -> None:
    print("---")
    print(content, end="")
    print("---")


def save_content(content: str) -> None:
    saved: int = 0

    try:
        new_file_name: str = input("Enter new file name (or empty): ")
    except EOFError as error:
        print(f"Error reading file name: {error}")
        return
    new_file: typing.IO[str]

    if new_file_name == "":
        print("Not saving data.")
        return
    print(f"Saving data to '{new_file_name}'")
    try:
        new_file = open(new_file_name, "w")
    except OSError as error:
        print(f"Error opening file '{new_file_name}': {error}")
        return
    try:
        new_file.write(content)
        saved = 1
    except OSError as error:
        print(f"Error writing file '{new_file_name}': {error}")
    finally:
        try:
            new_file.close()
        except OSError as error:
            saved = 0
            print(f"Error closing file '{new_file_name}': {error}")
    if saved == 1:
        print(f"Data saved in file '{new_file_name}'.")


def process_file(file_name: str) -> None:
    file: typing.IO[str]
    content: str = ""
    new_content: str

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{file_name}'")
    try:
        file = open(file_name, "r")
    except OSError as error:
        print(f"Error opening file '{file_name}': {error}")
        return
    try:
        content = file.read()
        print_content(content)
    except (OSError, UnicodeDecodeError) as error:
        print(f"Error reading file '{file_name}': {error}")
        return
    finally:
        close_file(file, file_name)
    new_content = transform_content(content)
    print("Transform data:")
    print_content(new_content)
    save_content(new_content)


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return
    process_file(sys.argv[1])


if __name__ == "__main__":
    main()
