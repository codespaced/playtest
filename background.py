class Background:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name", "EMPTY")
        self.text = kwargs.get("text", "")
        self.boosts = kwargs.get("boosts", [])
        self.feat = kwargs.get("feat", None)
        self.training = kwargs.get("training", [])

    def __repr__(self):
        return f"{self.__class__}({self.name})"

    def __str__(self):
        return f"{self.name}"