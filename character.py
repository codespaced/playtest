from typing import Dict, Tuple, List
from collections import Counter
from klass import Klass
from ancestry import Ancestry
from background import Background
from ancestry_feat import Ancestry_feat
from ability_score import Abilities
import grant

ABILITIES = "strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"
MAX_LEVEL = 20

class Character:

    def __init__(self, **kwargs):
        self.name = kwargs.get("name", "EMPTY")
        self.grants = []
        self.klass = kwargs.get("klass", Klass())
        self.background = kwargs.get("background", Background())
        self.voluntary_flaws = kwargs.get("voluntary_flaws", [])
        #self.boosts = kwargs.get("boosts", [])
        self.items = kwargs.get("items", [])
        self.ability_scores = Abilities(parent=self)
        self.__ancestry = None
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


    @property
    def ancestry(self):
        return self.__ancestry

    @ancestry.setter
    def ancestry(self, ancestry):
        self.__ancestry = Ancestry(ancestry)
        self.__ancestry(self)

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
    def speed(self):
        return self.ancestry.speed

    def get_hit_points(self, level):
        grants = self.grants_by_target("hit_points")
        con = self.ability_scores.constitution.bonus
        total = con * level
        for lvl in range(level):
            total += sum([grant.value for grant in grants if lvl in grant.levels])
        return total

    def grants_by_target(self, target):
        return [grant for grant in self.grants if grant.target == target]

    @property
    def hit_points_by_level(self):
        # return a list of hps. we can choose what level we want on the other end
        return [self.get_hit_points(level) for level in range(MAX_LEVEL)]

    @property
    def hit_points(self):
        return self.get_hit_points(self.level)

    def get_class_dc(self, level):
        # todo: key ability bonus
        key = 0
        return 10 + level + key

    @property
    def class_dc_by_level(self):
        return [self.get_class_dc(level) for level in range(MAX_LEVEL)]

    @property
    def class_dc(self):
        return self.get_class_dc(self.level)

    @property
    def item_boosts(self):
        for item in self.items:
            if item.potent:
                return item.boosts
        return []

    @property
    def boosts(self):
        return self.grants_by_target("ability")

    @property
    def special(self):
        return self.grants_by_target("special")

#    def set_boosts(self):
#        # reset boosts
#        self.boosts = []
#        self.add_boosts(self.ancestry.boosts, source="ancestry", value=1, level=1)
#        self.add_boosts(self.ancestry.flaws, source="flaw", value=-1, level=1)
#        self.add_boosts(self.background.boosts, "background", value=1, level=1)
#        self.add_boosts(self.voluntary_flaws, source="voluntary", value=-1, level=1)
#        self.add_boosts(self.klass.key_ability_score, source="class", value=1, level=1)
#        self.add_boosts(["Free"] * 4, source="level", value=1, level=1)
#        self.add_boosts(["Free"] * 4, source="level", value=1, level=5)
#        self.add_boosts(["Free"] * 4, source="level", value=1, level=10)
#        self.add_boosts(["Free"] * 4, source="level", value=1, level=15)
#        self.add_boosts(["Free"] * 4, source="level", value=1, level=20)

#    def add_boosts(self, boosts, source, value, level):
#        for boost in boosts:
#            self.boosts.append(Boost(name=f"{source}.{boost}", source=source, value=value, ability=boost, level=level))

#    def get_boosts(self, source, level):
#        return [boost for boost in self.boosts if boost.source == source and boost.level <= level]

#    def get_used(self, source, level):
#        return [boost for boost in self.boosts if boost.source == source and boost.level == level]
#
#    def get_available(self, source, level):
#        used = self.get_used(source, level)
#        used_abilities = [u.ability for u in used]
#        return [ability for ability in ABILITIES if ability not in used_abilities]
#
#    def get_free(self, source, level):
#        return [boost for boost in self.boosts if boost.free]

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name})"

    def __str__(self):
        return f"{self.name}"

    def display(self):
        for key in [self.ancestry, self.background, self.klass, self.bonuses, self.senses, self.feats]:
            print(f"{key}")

    def print_ability_scores(self):
        print("\n\n")
        print(f"{self.ability_scores.strength}\t\t{self.ability_scores.intelligence}")
        print(f"{self.ability_scores.dexterity}\t\t{self.ability_scores.wisdom}")
        print(f"{self.ability_scores.constitution}\t\t{self.ability_scores.charisma}")
        print("\n\n")

