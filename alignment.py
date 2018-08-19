from enum import Enum


class alignment(Enum):
    LAWFUL_GOOD = "LG"
    LAWFUL_NEUTRAL = "LN"
    LAWFUL_EVIL = "LE"
    NEUTRAL_GOOD = "NG"
    TRUE_NEUTRAL = "TN"
    NEUTRAL_EVIL = "NE"
    CHAOTIC_GOOD = "CG"
    CHAOTIC_NEUTRAL = "CN"
    CHAOTIC_EVIL = "CE"

    def __repr__(self):
        return f"<{self.__class__.__name__}.{self.value}>"

    def __str__(self):
        return self.value
