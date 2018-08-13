class Boost:
    # an ability score boost
    sources = set()

    def __init__(self, name, ability, value, source, level):
        self.name = name
        self.ability = ability
        self.value = value
        self.source = source
        Boost.sources.add(source)
        self.level = level
        self.free = ability == "Free"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name})"

    def __str__(self):
        return f"{self.__class__.__name__}({self.name}){self.ability}.{self.source}"