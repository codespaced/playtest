class Klass:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name", "EMPTY")
        self.bonuses = kwargs.get("bonuses" , [])
        self.hit_points = kwargs.get("hit_points", 0)
        self.training = kwargs.get("training", [])

        self.key_ability_score = kwargs.get("key_ability_score", [])
        self.secondary_ability_scores = kwargs.get("secondary_ability_scores", [])
        self.proficiencies = kwargs.get("proficiencies", {})
        self.signature_skills = kwargs.get("signature skills", [])
        self.class_feats = kwargs.get("class_feats", [])
        self.advancement = kwargs.get("advancement", {})
        self.spell_progression = kwargs.get("spell_progression", [])

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name})"

    def __str__(self):
        return f"{self.name}"