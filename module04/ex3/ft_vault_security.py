def secure_archive(
        fiel_name: str, option: str = "read", content: str = ""
) -> tuple[bool, str]:
    try:
        if option == "read":
            with open(fiel_name, "r") as file:
                return open(True, file.read())
        elif option == "write":
            with open(fiel_name, "w") as file:
                file.write(content)
                return (True, "Content successfully written to file")
        else:
            return (False, "Invalid option")
    except OSError as error:
        return (False, str(error))
    
    
if __name__ == "__main__":
    print("=== Cyber Archives Security ===")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "read"))

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd", "read"))

    print("Using 'secure_archive' to read from a regular file:")
    result: tuple[bool, str] = secure_archive("ancient_fragment.txt", "read")
    print(result)

    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_archive.txt", "write", result[1]))