def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients as validate
    validation_result = validate(ingredients)
    is_valid = 'INVALID' not in validation_result

    if is_valid:
        return f'Spell recorded: {spell_name} ({validation_result})'
    else:
        return f'Spell rejected: {spell_name} ({validation_result})'
