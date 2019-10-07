import random
import time


class Player:
    def __init__(self, name, hp, mp, phys_attack, accuracy, defense):
        self.name = name
        self.level = 1
        self.dream_level = 1
        self.hp = hp
        self.mp = mp
        self.phys_attack = phys_attack
        self.accuracy = accuracy
        self.defense = defense
        self.inventory = {}
        self.equipped = {"head": None, "neck": None, "chest": None,
                         "arm_r": None, "arm_l": None, "hands": None,
                         "hand_r": None, "hand_l": None, "waist": None,
                         "legs": None, "feet": None}

    def adjust_stats(self, item, remove=False):
        is_weapon = isinstance(item, Weapon)
        if remove is True:
            if is_weapon:
                self.phys_attack -= item.attack_boost
                self.accuracy -= item.accuracy_boost
            else:
                self.hp -= item.hp_boost
                self.mp -= item.mp_boost
                self.defense -= item.defense_boost
        else:
            if is_weapon:
                self.phys_attack += item.attack_boost
                self.accuracy += item.accuracy_boost
            else:
                self.hp += item.hp_boost
                self.mp += item.mp_boost
                self.defense += item.defense_boost

    def equip_item(self, item):
        equippable = self.can_equip(item)
        if item not in self.inventory.keys():
            print("You don't have that item.")
        if equippable is True:
            slot = item.slot
            equipment = self.equipped[slot]
            if equipment is not None:
                while True:
                    inp = input(
                        f"Would you like to replace {equipment} with {item}? y/n:\n")
                    if inp == "y":
                        self.adjust_stats(equipment, True)
                    elif inp == "n":
                        print("The item stays in your inventory.")
                        break
                    else:
                        print("Please answer with \"y\" or \"n\".")
                        continue
            else:
                self.equipped[slot] = item
                del self.inventory[item]
                self.adjust_stats(item)

        else:
            print(equippable)

    def can_equip(self, item):
        equippable = None
        if item.function == "equip":
            equippable = True
        else:
            equippable = "That item cannot be equipped."
        if equippable is True and self.level >= item.level:
            equippable = True
        elif equippable is True:
            equippable = "You are not a high enough level to equip that item."
        return equippable

    def display_stats(self):
        print(f"{self.name}'s stats:")
        print(f"Level: {self.level}")
        print(f"Dream Level: {self.dream_level}")
        print(f"Hit Points: {self.hp}")
        print(f"Magic Points: {self.mp}")
        print(f"Physical Attack: {self.phys_attack}")
        print(f"Accuracy: {self.accuracy}")
        print(f"Defense: {self.defense}")
        print(f"Inventory:", end=" ")

    def display_inventory(self):
        inv_list = []
        for key, value in self.inventory.items():
            inv_list.append(f"{key.name.title()} x {value}")
        if not inv_list:
            print("You have nothing in your inventory.")
        else:
            for item in inv_list:
                if inv_list[-1] == item:
                    print(f"{item}.")
                else:
                    print(f"{item}, ", end="")

    def display_equipped(self):
        print("Equipped items:")
        for key, value in self.equipped.items():
            if value is None:
                print(f"{key.title()}: Empty")
            else:
                print(f"{key.title()}: {value.name.title()}")


class Item:
    def __init__(self, name, description, location, function="use"):
        self.name = name
        self.description = description
        self. location = location
        self.function = function
        self.equippable = False


class Weapon(Item):
    def __init__(self, name, description, location, function="equip",
                 slot="hand_r", level=1, accuracy_boost=0, attack_boost=0):
        super().__init__(name, description, location, function)
        self.slot = slot
        self.level = level
        self.accuracy_boost = accuracy_boost
        self.attack_boost = attack_boost
        self.equippable = True


class Armor(Item):
    def __init__(self, name, description, location, function="equip",
                 slot="chest", level=1, hp_boost=0, mp_boost=0,
                 defense_boost=0):
        super().__init__(name, description, location, function)
        self.slot = slot
        self.level = level
        self.hp_boost = hp_boost
        self.mp_boost = mp_boost
        self.defense_boost = defense_boost


# This is only a test

humperdink = Player("Humperdink", 30, 27, 50, 35, 40)
breastplate = Armor("Breastplate", "A sturdy bronze breastplate that protects the wearer from physical attacks.", "forest", hp_boost=20, defense_boost=10)
shiny_sword = Weapon("Shiny Sword", "A polished sword ready to be stained by the blood of your enemies", "forest", accuracy_boost=15, attack_boost=20)
dark_helmet = Armor("Dark Helmet", "A giant helmet, recommended for short heroes.", "forest", slot="head", hp_boost=5, defense_boost=5)
potion = Item("Potion", "A tonic that instantly heals wounds", "forest")

humperdink.inventory[breastplate] = 1
humperdink.inventory[shiny_sword] = 1
humperdink.inventory[dark_helmet] = 1
humperdink.inventory[potion] = 5
humperdink.display_inventory()
humperdink.display_equipped()
humperdink.display_stats()
humperdink.equip_item(breastplate)
humperdink.equip_item(shiny_sword)
humperdink.equip_item(dark_helmet)
humperdink.display_inventory()
humperdink.display_equipped()
humperdink.display_stats()

