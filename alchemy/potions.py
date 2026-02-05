from .elements import create_water, create_earth, create_air
from alchemy.elements import create_fire


def healing_potion() -> str:
    return f'Healing potion brewed with {create_fire()} ' + \
           f'and {create_water()}'


def strength_potion() -> str:
    return f'Strength potion brewed with {create_fire()} ' + \
           f'and {create_earth()}'


def invisibility_potion() -> str:
    return f'Invisibility potion brewed with {create_air()} ' + \
           f'and {create_water()}'


def wisdom_potion() -> str:
    return 'Wisdom potion brewed with ' + \
           ', '.join([
                    create_fire(),
                    create_air(),
                    create_earth(),
                    create_water()
                ])
