from grant import Grant, Boost, Sense, Hit_points


class Klass:
    def __init__(self, klass=None, **kwargs):
        if klass is None:
            self.name = kwargs.get("name", "EMPTY")
            self.key_ability_score = kwargs.get("key_ability_score", [])
            self.secondary_ability_scores = kwargs.get("secondary_ability_scores", [])
            self.hit_points = kwargs.get("hit_points", 0)
            self.proficiencies = kwargs.get("proficiencies", {})
            self.signature_skills = kwargs.get("signature_skills", [])
            self.class_feats = kwargs.get("class_feats", [])
            self.advancement = kwargs.get("advancement", {})
            self.spell_progression = kwargs.get("spell_progression", [])
        else:
            self.name = klass.name
            self.key_ability_score = klass.key_ability_score
            self.secondary_ability_scores = klass.secondary_ability_scores
            self.hit_points = klass.hit_points
            self.proficiencies = klass.proficiencies
            self.signature_skills = klass.signature_skills
            self.class_feats = klass.class_feats
            self.advancement = klass.advancement
            self.spell_progression = klass.spell_progression

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name})"

    def __str__(self):
        return f"{self.name}"

    def __call__(self, parent):
        # todo: clear out old klass data
        parent.grants.extend(self.get_grants())

    def get_grants(self):
        grants = []
        source = f"{self}"
        level = 1
        # hit points
        grants.append(Hit_points(source, level, "hit_points", self.hit_points, range(1,21)))
        # proficiencies
        #for key, value in self.proficiencies.items():
        #    grants.append(Grant(source, level, "skills", value))
        # signature skills
        for value in self.signature_skills:
            grants.append(Grant(source, level, "signature_skills", value))
        # class_feats
        for value in self.class_feats:
            grants.append(Grant(source, level, "class_feats", value))
        # advancement
        for value in self.advancement:
            grants.append(Grant(source, level, "advancement", value))
        # spell_progression
        for value in self.spell_progression:
            grants.append(Grant(source, level, "spell_progression", value))
        return grants
