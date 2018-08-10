class Ancestry:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name", "EMPTY")
        self.boosts = kwargs.get("boosts", [])
        self.languages = kwargs.get("languages", [])
        self.speed = kwargs.get("speed", 0)
        self.hitpoints = kwargs.get("hitpoints", 0)
        self.size = kwargs.get("size", "EMPTY")
        self.flaws = kwargs.get("flaws", [])
        self.senses = kwargs.get("senses", [])

    def __repr__(self):
        return f"{self.__class__}({self.name})"

    def __str__(self):
        return f"{self.name}"