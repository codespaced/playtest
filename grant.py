from typing import Dict, Tuple, List


class Grant:
    # a class that represents anything that can be granted to a character
    def __init__(self, source: str, level: int, target: str, value: any):
        # source: what thing grants this thing
        self.source = source
        # level: the first level this applies to
        self.level = level
        # target: what thing this is targeting (hp, ability, skill)
        self.target = target
        # value: the value of this thing: ie ability: "strength", language: "Elven"
        self.value = value

    def __call__(self, parent, target):
        parent[target] += self

    def __repr__(self):
        return f"{self.__class__.__name__}({self.source}.{self.target}): {self.level} {self.value}"

    def __str__(self):
        return f"{self.__class__.__name__}({self.source}.{self.target}): {self.level} {self.value}"


class Boost(Grant):
    # an ability score boost
    def __init__(self, source: str, level: int, target: str, value: any, amount: int):
        super().__init__(source, level, target, value)
        # amount: what is the value of the boost
        self.amount = amount
        # choice is whether the player has to make a decision
        self.choice = value == "Free"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.source}.{self.target}): {self.amount:+d} {self.value}"

    def __str__(self):
        return f"{self.__class__.__name__}({self.source}.{self.target}): {self.amount:+d} {self.value}"


class Sense(Grant):
    # a sense
    def __init__(self, source: str, level: int, target: str, value: any, title):
        super().__init__(source, level, target, value)
        self.title = title


class HitPoints(Grant):
    # a hit point increase
    def __init__(self, source: str, level: int, target: str, value: any, levels: List):
        super().__init__(source, level, target, value)
        self.levels = levels

