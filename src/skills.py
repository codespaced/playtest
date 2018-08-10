class Skill:
    def __init__(self, name: str, ability: "Ability", armor: bool=False):
        self.name = name
        self.ability = ability
        self.armor = armor
        self.training = None
        self.signature = False
        self.bonuses = {}
        self.total = 0

    def __repr__(self):
        return f"<{self.__class__.__name__}.{self.name}>"

    def __str__(self):
        return self.name

    def __call__(self, *args, **kwargs):
        message = self.name.capitalize()
        if self.total < 0:
            message += f" -{self.total}"
        else:
            message += f" +{self.total}"

        return message
