import os


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...")

    try:
        from dotenv import load_dotenv  # type: ignore[import-not-found]
    except ImportError:
        print("ERROR: python-dotenv is not installed.")
        print("Install it with: python -m pip install -r requirements.txt")
        return

    env_loaded = load_dotenv(override=False)

    mode = os.getenv("MATRIX_MODE", "development").lower()
    if mode not in ("development", "production"):
        print("WARNING: Invalid MATRIX_MODE; using development.")
        mode = "development"

    database_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL")
    if not log_level:
        log_level = "DEBUG" if mode == "development" else "WARNING"
    zion_endpoint = os.getenv("ZION_ENDPOINT")

    print("Configuration loaded:")
    print(f"Mode: {mode}")
    if database_url:
        print(f"Database: Configured for {mode}")
    else:
        print("Database: Not configured")
    if api_key:
        print("API Access: Configured")
    else:
        print("API Access: Not configured")
    print(f"Log Level: {log_level}")
    if zion_endpoint:
        print("Zion Network: Configured")
    else:
        print("Zion Network: Not configured")
    if mode == "production":
        print("Runtime Policy: Production safeguards enabled")
    else:
        print("Runtime Policy: Development diagnostics enabled")

    missing_settings: list[str] = []
    for name, value in (
        ("DATABASE_URL", database_url),
        ("API_KEY", api_key),
        ("ZION_ENDPOINT", zion_endpoint),
    ):
        if not value:
            missing_settings.append(name)

    print("Environment security check:")
    if env_loaded:
        print("[OK] .env file loaded")
    else:
        print("[WARNING] .env file not found or empty")
    print("[OK] OS environment variables override .env values")
    print("[OK] Secret values are not displayed")

    if missing_settings:
        missing = ", ".join(missing_settings)
        print(f"[WARNING] Missing configuration: {missing}")
    else:
        print("[OK] All required configuration is present")

    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
