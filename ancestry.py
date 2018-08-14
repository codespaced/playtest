class Ancestry:
    def __init__(self, ancestry=None, **kwargs):
        if ancestry is not None:
            self = ancestry

    def __init(self, **kwargs):
        self.name = kwargs.get("name", "EMPTY")
        self.backgrounds = kwargs.get("backgrounds", [])
        self.bonus_languages = kwargs.get("bonus_languages", [])
        self.boosts = kwargs.get("boosts", [])
        self.flaws = kwargs.get("flaws", [])
        self.hit_points = kwargs.get("hit_points", 0)
        self.languages = kwargs.get("languages", [])
        self.senses = kwargs.get("senses", [])
        self.size = kwargs.get("size", "")
        self.special = kwargs.get("special", [])
        self.speed = kwargs.get("speed", 0)
        self.traits = kwargs.get("traits", [])

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name})"

    def __str__(self):
        return f"{self.name}"