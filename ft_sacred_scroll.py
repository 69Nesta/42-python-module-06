import alchemy


def main() -> None:
    print('\n=== Sacred Scroll Mastery ===\n')

    demo_functions = [
        alchemy.elements.create_fire,
        alchemy.elements.create_water,
        alchemy.elements.create_earth,
        alchemy.elements.create_air
    ]

    print('Testing direct module access:')
    for func in demo_functions:
        print(f'alchemy.element.{func.__name__}(): {func()}')
    print('')

    print('Testing direct module access:')
    try:
        print('alchemy.create_fire(): ', end=' ')
        print(alchemy.create_fire())
    except AttributeError:
        print('AttributeError - not exposed')
    try:
        print('alchemy.create_water(): ', end=' ')
        print(alchemy.create_water())
    except AttributeError:
        print('AttributeError - not exposed')
    try:
        print('alchemy.create_earth(): ', end=' ')
        print(alchemy.create_earth())
    except AttributeError:
        print('AttributeError - not exposed')
    try:
        print('alchemy.create_air(): ', end=' ')
        print(alchemy.create_air())
    except AttributeError:
        print('AttributeError - not exposed')

    print('\nPackage Metadata:')
    print(f'Name: {alchemy.__name__}')
    print(f'Version: {alchemy.__version__}')


if __name__ == "__main__":
    main()
