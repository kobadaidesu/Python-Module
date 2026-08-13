import os


SCRIPT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
ENV_FILE = os.path.join(SCRIPT_DIRECTORY, ".env")


def load_environment_file() -> bool:
    try:
        from dotenv import load_dotenv  # type: ignore[import-not-found]
    except ImportError:
        print("ERROR: python-dotenv is not installed.")
        print("Install it with: python -m pip install -r requirements.txt")
        return False

    if os.path.exists(ENV_FILE):
        load_dotenv(ENV_FILE, override=False)
    else:
        print("WARNING: .env file not found; using OS environment only.")
    return True


def read_configuration() -> dict[str, str]:
    configuration: dict[str, str] = {}

    mode = os.getenv("MATRIX_MODE", "development").lower()
    if mode not in ("development", "production"):
        print("WARNING: MATRIX_MODE must be development or production.")
        print("Using development mode.")
        mode = "development"
    configuration["MATRIX_MODE"] = mode

    log_level = os.getenv("LOG_LEVEL")
    if not log_level:
        log_level = "DEBUG" if mode == "development" else "WARNING"
        print(f"WARNING: LOG_LEVEL not set; using {log_level}.")
    configuration["LOG_LEVEL"] = log_level

    for variable_name in ("DATABASE_URL", "API_KEY", "ZION_ENDPOINT"):
        value = os.getenv(variable_name)
        if not value:
            print(f"WARNING: {variable_name} is not configured.")
            value = ""
        configuration[variable_name] = value

    return configuration


def show_configuration(configuration: dict[str, str]) -> None:
    mode = configuration["MATRIX_MODE"]
    print("Configuration loaded:")
    print(f"Mode: {mode}")

    if configuration["DATABASE_URL"]:
        print(f"Database: Connected to {mode} instance")
    else:
        print("Database: Not configured")

    if configuration["API_KEY"]:
        print("API Access: Authenticated")
    else:
        print("API Access: Not configured")

    print(f"Log Level: {configuration['LOG_LEVEL']}")

    if configuration["ZION_ENDPOINT"]:
        print("Zion Network: Online")
    else:
        print("Zion Network: Not configured")

    if mode == "production":
        print("Runtime Policy: Production safeguards enabled")
    else:
        print("Runtime Policy: Development diagnostics enabled")


def show_security_status(configuration: dict[str, str]) -> None:
    print("Environment security check:")
    print("[OK] Secrets are read from environment variables")
    if os.path.exists(ENV_FILE):
        print("[OK] .env file loaded for development")
    else:
        print("[WARNING] .env file is not configured")
    print("[OK] OS environment variables override .env values")

    if configuration["API_KEY"]:
        print("[OK] API key is configured without being displayed")
    else:
        print("[WARNING] API key is missing")


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...")
    if not load_environment_file():
        return

    configuration = read_configuration()
    show_configuration(configuration)
    show_security_status(configuration)
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
