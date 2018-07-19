import random
from Weapon import Weapon


class Gladiator:

    health = 50
    weapon_bonus = 0
    armor_bonus = 0
    weapon_type = ''

    def __init__(self):
        self.attack = random.randint(1, 10)
        self.defense = random.randint(1, 10)
        self.name = input("Enter your fighter's name.\n")

    def print_stats(self):
        print(f'{self.name} Stats\n' +
              f'----------------------\n' +
              f'Health: {self.health}\n' +
              f'Weapon: {self.weapon_type}'
              )

    def get_weapon(self):
        """
        This method determines the weapon type and damage of the fighter, and then assigns each one to its relevant
        field.
        """
        item = Weapon()
        weapon_item_damage = item.get_weapon_damage()
        self.weapon_type = weapon_item_damage[0]
        self.weapon_bonus = weapon_item_damage[1]
        print('gladiator.get_weapon() called; weapon selected')
        self.determine_attack()
        print('gladiator.determine_attack() called; attack determined')

    def determine_attack(self):
        """
        This determines the players attack damage.
        """
        self.attack += random.randint(1, 5)
        number = random.randint(1, 10)
        weapon_bonus = Gladiator.weapon_bonus
        final_attack = (self.attack + weapon_bonus) // 2 + number
        # print(f'Initial attack: {self.attack}')
        # print(f'random number: {number}')
        # print(f'weapon_bonus: {weapon_bonus}')
        # print(f'Final attack: {final_attack}')

