from Gladiator import Gladiator
from Weapon import Weapon
import functions

# TODO: decide where to initialize the weapon stats

def show_main_menu():
    print('*** Main Menu ***\n')
    print(f'1. Fighter Stats\n' +
          f'2. TBD'
          )


def show_fighter_stats_menu():
    print(f'Fighter Stats\n' +
          f'-------------\n' +
          f'Name: {fighter1.name}\n' +
          f'Weapon: {fighter1.weapon_type}\n' +
          f'Attack Power: {fighter1.attack}\n' +
          f'Defense Power: {fighter1.defense}'
          )


def begin():
    show_main_menu()
    selection = input("Select an menu number\n")
    if selection == '1':
        print()
        show_fighter_stats_menu()
    go_back = input("Return to main menu? Y/N\n").lower()
    if go_back == "y":
        show_main_menu()
    else:
        exit()


fighter1 = Gladiator()
fighter1.get_weapon()
begin()

