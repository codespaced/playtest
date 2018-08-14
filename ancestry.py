from grant import Grant, Boost, Sense, Hit_points

class Ancestry:
    def __init__(self, ancestry=None, **kwargs):
        if ancestry is None:
            self.name = kwargs.get("name", "EMPTY")
            self.backgrounds = kwargs.get("backgrounds", [])
            self.bonus_languages = kwargs.get("bonus_languages", [])
            self.boosts = kwargs.get("boosts", [])
            self.flaws = kwargs.get("flaws", [])
            self.hit_points = kwargs.get("hit_points", 0)
            self.languages = kwargs.get("languages", [])
            self.senses = kwargs.get("senses", [])
            self.size = kwargs.get("size", "")
            self.special = kwargs.get("special", {})
            self.speed = kwargs.get("speed", 0)
            self.traits = kwargs.get("traits", [])
        else:
            self.name = ancestry.name
            self.backgrounds = ancestry.backgrounds
            self.bonus_languages = ancestry.bonus_languages
            self.boosts = ancestry.boosts
            self.flaws = ancestry.flaws
            self.hit_points = ancestry.hit_points
            self.languages = ancestry.languages
            self.senses = ancestry.senses
            self.size = ancestry.size
            self.special = ancestry.special
            self.speed = ancestry.speed
            self.traits = ancestry.traits

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name})"

    def __str__(self):
        return f"{self.__class__.__name__}.{self.name}"

    def __call__(self, parent):
        # todo: clear out old ancestry data
        parent.grants.extend(self.get_grants())

    def get_grants(self):
        grants = []
        source = f"{self}"
        level = 1
        # ability boosts
        for value in self.boosts:
            grants.append(Boost(source, level, "ability", value, amount=1))
        # flaws
        for value in self.flaws:
            grants.append(Boost(source, level, "ability", value, amount=-1))
        # languages       
        for value in self.languages:
            grants.append(Grant(source, level, "languages", value))
        # senses
        for sense in self.senses:
            grants.append(Grant(source, level, "senses", value))
        # size        
        grants.append(Grant(source, level, "size", self.size))
        # speed        
        grants.append(Grant(source, level, "speed", self.speed))
        # hit points
        grants.append(Hit_points(source, level, "hit_points", f"{self}", amount=self.hit_points))
        # traits
        for value in self.traits:
            grants.append(Boost(source, level, "traits", value))
        # special
        for value in self.special:
            grants.append(Grant(source, level, "special", value))
        return grants
