from collections import namedtuple, OrderedDict
from random import randint

from enums import Ability, Ancestry, Backgrounds, Class
from menus import Menu


class Character:
    def __init__(self, player):
        self.player = player
        self.name = ""
        self.ancestry = ""
        self.class_ = None
        self.level = 0
        self.background = ""
        self.stats = OrderedDict({
            "Strength": 0,
            "Dexterity": 0,
            "Constitution": 0,
            "Intelligence": 0,
            "Wisdom": 0,
            "Charisma": 0
        })
        self.saves = OrderedDict({
            "Fortitude": 0,
            "Reflex": 0,
            "Will": 0
        })
        self.languages = list()
        self.hit_points = 0
        self.alignment = ""
        self.age = 0
        self.gender = None
        self.armor_class = 0
        self.touch = 0  # touch armor class
        self.feats = OrderedDict({
            "ancestry": list(),
            "background": list(),
            "class": list(),
            "skill": list()
        })
        self.class_features = list()
        self.speed = 0
        self.strikes = {
            "melee": list(),
            "ranged": list()
        }
        self.skills = OrderedDict({
            "Acrobatics": "",
            "Athletics": "",
            "Intimidation": "",
            "Lore [Farming]": "",
            "Lore [Warfare]": "",
            "Perception": ""
        })
        self.gear = {
            "gear": list(),
            "ready": list(),
            "stowed": list(),
            "coins": namedtuple("coins", ["cp", "sp", "gp", "pp"])
        }
        self.bulk = namedtuple("bulk", ["bulk", "light", "encumbered", "max"])
        self.resonance_points = 0
        self.experience_points = 0
        self.senses = {"Perception": self.skills["Perception"]}
        self.hero_points = 0
        self.bonuses = OrderedDict({
            "ancestry": [],
            "background": [],
            "class": [],
            "free": [Ability.BLANK, Ability.BLANK, Ability.BLANK, Ability.BLANK],
            "flaws": []
        })
        self.size = None

    def display(self):
        for i in range(25):
            print()
        keys = ["player", "ancestry", "background", "class_", "bonuses", "senses", "feats"]
        for key in keys:
            val = self.__dict__.get(key, False)
            if val:
                if key in ["ancestry", "background", "class_"]:
                    print(f"{key}: {val.name}")
                elif key in ["bonuses", "senses", "feats"]:
                    print(f"{key:}")
                    for k, v in val.items():
                        print(f"   {k}: {v}")
                else:
                    print(f"{key}: {val}")

    def assign_ancestry(self, choice: str):
        # ["name", "bonuses", "languages", "speed", "hp", "size", "flaws", "senses"]
        ancestry = Ancestry[choice]()
        # assign ancestry
        self.ancestry = ancestry
        # add languages to list
        for language in ancestry.languages:
            self.languages.append(language)
        # assign speed
        self.speed += ancestry.speed
        # add hit points from ancestry to hit point total
        self.hit_points += ancestry.hp
        self.size = ancestry.size
        for sense in ancestry.senses:
            self.senses[sense] = sense

        for bonus in ancestry.bonuses:
            self.bonuses["ancestry"].append(bonus)
        for flaw in ancestry.flaws:
            self.bonuses["flaws"].append(flaw)

    def assign_background(self, choice: str):
        # "name", "bonuses", "training", "feat"
        background = Backgrounds[choice]()
        self.background = background
        self.bonuses["background"].append(background.bonuses)
        self.skills[background.training] = "trained"
        self.feats["background"].append(background.feat)

    def assign_class(self, choice: str):
        # "name", "ability", "hit points"
        class_ = Class[choice]()
        self.class_ = class_
        self.level += 1
        self.bonuses["class"].append(class_.ability)
        self.hit_points += class_.hitpoints

    def print_stats(self):
        print("\n\n")
        print(f"STR  {self.stats['Strength']}  \t\t  INT  {self.stats['Intelligence']}")
        print(f"DEX  {self.stats['Dexterity']}  \t\t  WIS  {self.stats['Wisdom']}")
        print(f"CON  {self.stats['Constitution']}  \t\t  CHA  {self.stats['Charisma']}")
        print("\n\n")

    def assign_ability_scores(self):
        names = [n for n in self.stats.keys()]

        # assign base scores
        for score in self.stats.keys():
            self.stats[score] = 10

        self.print_stats()

        selected = []
        print(f"Assign ancestry bonuses")
        for bonus in self.bonuses["ancestry"]:
            ability = str(bonus)
            if ability == "blank":
                choices = [name for name in iter(names) if name not in selected]
                print(f"selected = {selected}")
                print(f"choices = {choices}")
                choice = ""
                while choice not in choices:
                    choice = input(f"/nChoose ability to boost./n")
                selected.append(choice)
                print(f"Bonus added to {choice}")
                self.stats[choice] += 2

            else:
                print(f"Bonus added to {ability}")
                selected.append(ability)
                self.stats[ability] += 2

        self.print_stats()


def choose_ancestry(rand: bool=False):
    options = {
        1: "Dwarf",
        2: "Elf",
        3: "Gnome",
        4: "Goblin",
        5: "Halfling",
        6: "Human",
    }

    if rand:
        choice = randint(1, 6)
    else:
        choice = 2
        menu = Menu("Ancestry", options)
        while choice not in options.keys():
            menu.display()
            choice = int(input("Choose an option: "))
    return options[choice]


def choose_background(rand: bool=False):
    index = 1
    options = {}
    for back in Backgrounds:
        options[index] = back().name.capitalize()
        index += 1

    if rand:
        choice = randint(1, len(options.keys()))
    else:
        choice = 1
        menu = Menu("Backgrounds", options)
        while choice not in options.keys():
            menu.display()
            choice = int(input("Choose an option: "))
    return options[choice]


def choose_class(rand: bool=False):
    return "barbarian"
