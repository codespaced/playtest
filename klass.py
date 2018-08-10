class Klass:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name", "EMPTY")
        self.bonuses = kwargs.get("bonuses" , [])
        self.hitpoints = kwargs.get("hitpoints", 0)
        self.training = kwargs.get("training", [])

    def __repr__(self):
        return f"{self.__class__}({self.name})"

    def __str__(self):
        return f"{self.name}"