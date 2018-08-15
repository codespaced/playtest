from functools import total_ordering
from math import floor
import grant

class Abilities:
    abilities = "strength", "intelligence", "dexterity", "wisdom", "constitution", "charisma"

    def __init__(self, **kwargs):
        self.parent = kwargs.get("parent", None)
        self._scores = {ability:Ability_score(name=ability, parent=self.parent) for ability in Abilities.abilities}

    def __repr__(self):
        return f"{self.__class__.__name__}"

    def __len__(self):
        return len(self._scores)

    def __getattr__(self, k):
        if k in Abilities.abilities:
            return self._scores[k]
        else:
            raise AttributeError(k)

    def __getitem__(self, k):
        if k in Abilities.abilities:
            return self._scores[k]
        else:
            raise AttributeError(k)

    def print(self):
        print()
        print(f"{self.strength} ({self.strength.bonus:+d}) \t {self.intelligence} ({self.intelligence.bonus:+d}) ")
        print(f"{self.dexterity} ({self.dexterity.bonus:+d}) \t {self.wisdom} ({self.wisdom.bonus:+d}) ")
        print(f"{self.constitution} ({self.constitution.bonus:+d}) \t {self.charisma} ({self.charisma.bonus:+d}) ")
        print()

@total_ordering
class Ability_score:
    # Holds the calculation for an ability score
    base = 10

    def __init__(self, parent, **kwargs):
        self.name = kwargs.get("name", "EMPTY")
        self.parent = parent

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}: {self.value})"

    def __str__(self):
        return f"{self.name[:3].upper()}: {self.value:2d}"

    def __eq__(self, other):
        return self.value == other

    def __lt__(self, other):
        return self.value < other

    @property
    def value(self):
        return self.get_value(self.parent.level)

    def get_value(self, level):
        boosts = sum([boost.amount for boost in self.parent.boosts if boost.value == self.name and boost.level <= level])
        # up to 18, a boost is +2, then it's only +1
        score = Ability_score.base + (0, 2, 4, 6, 8, 9, 10, 11, 12, -9, -9, -9, -9, -8, -6, -4, -2)[boosts]

#        item_boost = self.parent.item_boosts and self.name in self.parent.item_boosts
#            if item_boosts[level]:
#                score = max(score + 2, 18)
        return score

    def get_bonus(self):
        return floor((self.value - 10) / 2)

    @property
    def bonus(self):
        return self.get_bonus()
