class AncestryFeat:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name", "")
        self.level = kwargs.get("level", 0)
        self.traits = kwargs.get("traits", [])
        self.text = kwargs.get("text", "")
        self.special = kwargs.get("special", "")
        self.trigger = kwargs.get("trigger", "")
        self.actions = kwargs.get("actions", [])
        self.prerequisites = kwargs.get("prerequisites", "")
        self.frequency = kwargs.get("frequency", "")

    def __repr__(self):
        return f"{self.__class__}({self.name})"

    def __str__(self):
        return f"{self.name}"
