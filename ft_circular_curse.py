from alchemy.grimoire import validate_ingredients, record_spell


def test_validate_ingredients(ingredients: str):
    print(f'validate_ingredients({ingredients}): '
          f'{validate_ingredients(ingredients)}')


def test_record_spell(spell_name: str, ingredients: str):
    print(f'record_spell({spell_name}, {ingredients}): '
          f'{record_spell(spell_name, ingredients)}')


def main():
    print('=== Circular Curse Breaking ===')

    print('\nTesting ingredient validation:')
    test_validate_ingredients('fire air')
    test_validate_ingredients('dragon scales')

    print('\nTesting spell recording with validation:')
    test_record_spell('Fireball', 'fire air')
    test_record_spell('Dark Magic', 'shadow')

    print('\nTesting late import technique:')
    test_record_spell('Lightning', 'air')

    print('\nCircular dependency curse avoided using late imports!')
    print('All spells processed safely')


if __name__ == '__main__':
    main()
