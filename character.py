from collections import Counter
from typing import Dict, Tuple, List

from abilities import Abilities
from ancestry import Ancestry
from ancestry_feat import AncestryFeat
from background import Background
from klass import Klass
import grant

ABILITIES = "strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"
MAX_LEVEL = 20


class Character:

    def __init__(self, **kwargs):
        self.name = kwargs.get("name", "EMPTY")
        self.grants = []
        self.background = kwargs.get("background", Background())
        self.voluntary_flaws = kwargs.get("voluntary_flaws", [])
        # self.boosts = kwargs.get("boosts", [])
        self.items = kwargs.get("items", [])
        self.ability_scores = Abilities(parent=self)
        self.__ancestry = None
        self.__klass = None
        self.__bonus_languages = []

        self.alignment = None
        self.level = kwargs.get("level", 1)
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
            "coins": []  # namedtuple("coins", ["cp", "sp", "gp", "pp"])
        }
        self.bulk = []  # namedtuple("bulk", ["bulk", "light", "encumbered", "max"])
        self.resonance = 0
        self.experience = 0

        self.hero_points = 0

    @property
    def ancestry(self):
        return self.__ancestry

    @ancestry.setter
    def ancestry(self, ancestry):
        self.__ancestry = Ancestry(ancestry)
        self.__ancestry(self)

    @property
    def boosts(self):
        return self.grants_by_target("ability")

    @property
    def class_dc(self):
        return self.get_class_dc(self.level)

    @property
    def class_dc_by_level(self):
        return [self.get_class_dc(level) for level in range(MAX_LEVEL)]

    @property
    def hit_points(self):
        return self.get_hit_points(self.level)

    @property
    def key_ability(self):
        return self.ability_scores[self.klass.key_ability]

    def get_class_dc(self, level):
        # todo: key ability bonus
        key = self.key_ability.bonus
        return 10 + level + key

    @property
    def hit_points_by_level(self):
        # return a list of hps. we can choose what level we want on the other end
        return [self.get_hit_points(level) for level in range(MAX_LEVEL)]

    @property
    def item_boosts(self):
        for item in self.items:
            if item.potent:
                return item.boosts
        return []

    @property
    def klass(self):
        return self.__klass

    @klass.setter
    def klass(self, klass):
        self.__klass = Klass(klass)
        self.__klass(self)

    @property
    def languages(self) -> List:
        return self.ancestry.languages + self.__bonus_languages

    @languages.setter
    def languages(self, languages) -> None:
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
    def special(self):
        return self.grants_by_target("special")

    @property
    def speed(self):
        return self.ancestry.speed

    def grants_by_target(self, target):
        return [grant for grant in self.grants if grant.target == target]

    def get_hit_points(self, level):
        grants = self.grants_by_target("hit_points")
        print(grants)
        con = self.ability_scores.constitution.bonus
        total = con * level
        for lvl in range(level):
            total += sum([grant.value for grant in grants if lvl in grant.levels])
        return total

    @property
    def senses(self):
        return self.grants_by_target("senses")

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name})"

    def __str__(self):
        return f"{self.name}"

    def display(self):
        for key in [self.ancestry, self.background, self.klass, self.bonuses, self.senses, self.feats]:
            print(f"{key}")
