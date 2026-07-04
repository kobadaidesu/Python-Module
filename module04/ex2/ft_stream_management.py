import sys
import typing


def write_error(message: str) -> None:
    sys.stdout.flush()
    sys.stderr.write(f"[STDERR] {message}\n")
    sys.stderr.flush()


def close_file(file: typing.IO[str], file_name: str) -> None:
    try:
        file.close()
    except Exception as error:
        write_error(f"Error closing file '{file_name}': {error}")
    else:
        print(f"File '{file_name}' closed.")


def print_content(content: str) -> None:
    print("---")
    print(content, end="")
    print("---")


def transform_content(content: str) -> str:
    transformed: str = ""
    lines: list[str] = content.splitlines()

    for line in lines:
        transformed += line + "#\n"
    return transformed


def read_output_name() -> str:
    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    return sys.stdin.readline().rstrip("\n")


def save_content(content: str) -> None:
    saved: int = 0
    output_file: typing.IO[str]

    try:
        output_name: str = read_output_name()
    except Exception as error:
        write_error(f"Error reading file name: {error}")
        return
    if output_name == "":
        print("Not saving data.")
        return
    print(f"Saving data to '{output_name}'")
    try:
        output_file = open(output_name, "w")
    except Exception as error:
        write_error(f"Error opening file '{output_name}': {error}")
        print("Data not saved.")
        return
    try:
        output_file.write(content)
        saved = 1
    except Exception as error:
        write_error(f"Error writing file '{output_name}': {error}")
    finally:
        try:
            output_file.close()
        except Exception as error:
            saved = 0
            write_error(f"Error closing file '{output_name}': {error}")
    if saved == 1:
        print(f"Data saved in file '{output_name}'.")
    else:
        print("Data not saved.")


def process_file(file_name: str) -> None:
    file: typing.IO[str]
    content: str = ""
    transformed: str

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{file_name}'")
    try:
        file = open(file_name, "r")
    except Exception as error:
        write_error(f"Error opening file '{file_name}': {error}")
        return
    try:
        content = file.read()
        print_content(content)
    except Exception as error:
        write_error(f"Error reading file '{file_name}': {error}")
        return
    finally:
        close_file(file, file_name)
    transformed = transform_content(content)
    print("Transform data:")
    print_content(transformed)
    save_content(transformed)


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
        return
    process_file(sys.argv[1])


if __name__ == "__main__":
    main()
