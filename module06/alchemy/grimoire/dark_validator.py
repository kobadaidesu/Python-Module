from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    lowered_ingredients = ingredients.lower()
    is_valid = any(
        allowed in lowered_ingredients
        for allowed in dark_spell_allowed_ingredients()
    )
    result = "VALID" if is_valid else "INVALID"
    return f"{ingredients} - {result}"
