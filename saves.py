class Saves:
    saves = {"fortitude": "constitution",
             "reflex": "dexterity",
             "will": "wisdom"}

    def __init__(self, **kwargs):
        self.parent = kwargs.get("parent", None)
        self._saves = {}
        for name, proficiency in self.parent.klass.proficiencies['saving_throws'].items():
            # print(name, proficiency, Saves.saves[name])
            self._saves[name] = Save(name=name, parent=self.parent, ability=Saves.saves[name], proficiency=proficiency)

    def __repr__(self):
        return f"{self.__class__.__name__}"

    def __len__(self):
        return len(self._saves)

    def __getattr__(self, k):
        if k in Saves.saves:
            return self._saves[k]
        else:
            raise AttributeError(k)

    def print(self):
        print(self.fortitude)
        print(self.reflex)
        print(self.will)


class Save:

    proficiency = {"trained": 0, "expert": 1, "master": 2, "legendary": 3}

    def __init__(self, name, parent, ability, proficiency):
        self.name = name
        self.parent = parent
        self.ability = ability
        self.proficiency = proficiency

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}: {self.value})"

    def __str__(self):
        return f"{self.name}: {self.value}"

    @property
    def value(self):
        return self.get_value(self.parent.level)

    def get_value(self, level):
        return self.parent.abilities[self.ability].bonus + level + self.proficiency_value

    @property
    def proficiency_value(self):
        return Save.proficiency[self.proficiency]
