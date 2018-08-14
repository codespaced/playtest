class Grant:
    # a class that represents anything that can be granted to a character
    def __init__(self, source, level, target, value): 
        # source: what thing grants this thing
        self.source = source
        # level: the first level this applies to
        self.level = level
        # target: what thing this is targetting (hp, ability, skill)
        self.target = target
        # value: the value of this thing: ie ability: "strength", language: "Elven"
        self.value = value

    def __call__(self, parent):
        parent[target] += self

    def __repr__(self):
        return f"{self.__class__.__name__}"

    def __str__(self):
        return f"{self.__class__.__name__}({self.source}.{self.target}.{self.value})"

class Boost(Grant):
    # an ability score boost
    def __init__(self, source, level, target, value, amount):
        super().__init__(source, level, target, value)
        # amount: what is the value of the boost
        self.amount = amount
        # choice is whether the player has to make a decision
        self.choice = value == "Free"
   
class Sense(Grant):
    # a sense
    def __init__(self, source, level, target, value, title):
        super().__init__(source, level, target, value)
        self.title = title

class Hit_points(Grant):
    # a hit point increase
    def __init__(self, source, level, target, value, amount):
        super().__init__(source, level, target, value)
        self.amount = amount
        
