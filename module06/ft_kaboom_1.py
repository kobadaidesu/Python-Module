def main() -> None:
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print(
        "Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION",
        flush=True,
    )

    from alchemy.grimoire.dark_spellbook import dark_spell_record

    result = dark_spell_record("Forbidden", "Bats and arsenic")
    print(f"Testing record dark spell: {result}")


if __name__ == "__main__":
    main()
