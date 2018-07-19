import random


class Weapon:
    """
    This is the class to handle weapons.
    """

    weapon_types = ["sword", "spear", "club", "axe"]
    weapons_dict = {"sword": 7, "spear": 5, "club": 3, "axe": 6}
    weapon = ''

    def get_weapon(self):
        """
        This method determines which weapon the player will have by selecting randomly from a list
        Returns: the weapon as a string
        """
        weapon = random.choice(self.weapon_types)
        return weapon

    def get_weapon_damage(self):
        """
        This method determines how much damage the weapon will do by passing the weapon as a key into a dictionary
        and retrieving the value.
        Returns: A tuple with the string weapon name in index 0 and the integer weapon damage in index 1.gith
        """
        item = self.get_weapon()
        damage = self.weapons_dict[item]
        return item, damage

