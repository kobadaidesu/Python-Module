from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    lowered_ingredients = ingredients.lower()
    is_valid = any(
        allowed in lowered_ingredients
        for allowed in light_spell_allowed_ingredients()
    )
    result = "VALID" if is_valid else "INVALID"
    return f"{ingredients} - {result}"
