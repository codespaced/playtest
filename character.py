from klass import Klass
from ancestry import Ancestry
from background import Background

class Character:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name", "EMPTY")
        self.ancestry = kwargs.get("ancestry", Ancestry())
        self.klass = kwargs.get("klass", Klass())
        self.levels = []
        self.background = kwargs.get("background", Background())
        self.ability_scores = {
            "Strength": 0,
            "Dexterity": 0,
            "Constitution": 0,
            "Intelligence": 0,
            "Wisdom": 0,
            "Charisma": 0
        }
        self.saves = {
            "Fortitude": 0,
            "Reflex": 0,
            "Will": 0
        }
    
        self.__bonus_languages = []

        self.hit_points = 0
        self.alignment = None
        self.age = 0
        self.gender = None
        self.armor_class = 0
        self.touch = 0  # touch armor class
        self.feats = {
            "ancestry": [],
            "background": [],
            "class": [],
            "skill": []
        }
        self.class_features = []
        self.strikes = {
            "melee": [],
            "ranged": []
        }
        self.skills = {
            "Acrobatics": "",
            "Athletics": "",
            "Intimidation": "",
            "Lore [Farming]": "",
            "Lore [Warfare]": "",
            "Perception": ""
        }
        self.gear = {
            "gear": [],
            "ready": [],
            "stowed": [],
            "coins": [] #namedtuple("coins", ["cp", "sp", "gp", "pp"])
        }
        self.bulk = [] #namedtuple("bulk", ["bulk", "light", "encumbered", "max"])
        self.resonance = 0
        self.experience = 0
        self.senses = {"Perception": self.skills["Perception"]}
        self.hero_points = 0
        self.bonuses = {
            "ancestry": [],
            "background": [],
            "class": [],
            "free": [], #[Ability.BLANK, Ability.BLANK, Ability.BLANK, Ability.BLANK],
            "flaws": []
        }

    @property
    def languages(self):
        return self.ancestry.languages + self.__bonus_languages

    @languages.setter
    def languages(self, languages):
        # try to split on ", "
        try:
            languages = languages.split(", ")
        # lists don't have .split
        except AttributeError:
            pass
        for language in languages:
            self.__bonus_languages.append(language)

    @property
    def size(self):
        return self.ancestry.size

    @property
    def speed(self):
        return self.ancestry.speed

    @property
    def hitpoints(self):
        return self.ancestry.hitpoints

    

    def __repr__(self):
        return f"{self.__class__}({self.name})"

    def __str__(self):
        return f"{self.name}"

    def display(self):
        for key in [self.ancestry, self.background, self.klass, self.bonuses, self.senses, self.feats]:
            print(f"{key}")

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

    def print_ability_scores(self):
        print("\n\n")
        print(f"STR  {self.ability_scores['Strength']}  \t\t  INT  {self.ability_scores['Intelligence']}")
        print(f"DEX  {self.ability_scores['Dexterity']}  \t\t  WIS  {self.ability_scores['Wisdom']}")
        print(f"CON  {self.ability_scores['Constitution']}  \t\t  CHA  {self.ability_scores['Charisma']}")
        print("\n\n")

    def assign_ability_scores(self):
        names = [n for n in self.ability_scores.keys()]

        # assign base scores
        for score in self.ability_scores.keys():
            self.ability_scores[score] = 10

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
                self.ability_scores[choice] += 2

            else:
                print(f"Bonus added to {ability}")
                selected.append(ability)
                self.ability_scores[ability] += 2

        self.print_stats()