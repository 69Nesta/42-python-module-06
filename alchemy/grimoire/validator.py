def validate_ingredients(ingredients: str) -> str:
    valid_ingredients = ['fire', 'water', 'earth', 'air']

    for ingredient in ingredients.split(' '):
        if ingredient.lower().strip() not in valid_ingredients:
            return f'{ingredients} - INVALID'
    return f'{ingredients} - VALID'
