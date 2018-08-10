from collections import namedtuple
from enum import Enum


class Ability(Enum):
    STRENGTH = "Strength"
    DEXTERITY = "Dexterity"
    CONSTITUTION = "Constitution"
    INTELLIGENCE = "Intelligence"
    WISDOM = "Wisdom"
    CHARISMA = "Charisma"
    BLANK = "blank"

    def __repr__(self):
        return f"<{self.__class__.__name__}.{self.value}>"

    def __str__(self):
        return self.value


SKILL = namedtuple("skill", ["name", "ability", "training", "armor"])


class Skills(Enum):
    ACROBATICS = SKILL("acrobatics", Ability.DEXTERITY, "untrained", True)
    ATHLETICS = SKILL("athletics", Ability.STRENGTH, "untrained", True)
    STEALTH = SKILL("stealth", Ability.DEXTERITY, "untrained", True)
    SURVIVAL = SKILL("survival", Ability.WISDOM, "untrained", False)


BACKGROUND = namedtuple("background", ["name", "bonuses", "training", "feat"])


class Backgrounds(Enum):
    BLACKSMITH = BACKGROUND("blacksmith", (Ability.STRENGTH, Ability.INTELLIGENCE),
                            "Lore (Smithing)", "Specialty Crafting (blacksmithing)")
    FARMER = BACKGROUND("farmer", None, None, None)
    NOMAD = BACKGROUND("nomad", None, "Lore (Choice)", None)
    PATHFINDER_HOPEFUL = BACKGROUND("pathfinder hopeful", (Ability.STRENGTH, Ability.INTELLIGENCE),
                                    "Additional Lore", "Lore (Pathfinder Society")
    STREET_URCHIN = BACKGROUND("street urchin", (Ability.DEXTERITY, Ability.INTELLIGENCE),
                               "Lore (Underworld)", "Pickpocket")

    def __repr__(self):
        return f"<{self.__class__.__name__}.{self.value.name}>"

    def __str__(self):
        return self.value.name

    def __call__(self, *args, **kwargs):
        return self.value


ANCESTRY = namedtuple("ancestry", ["name", "bonuses", "languages", "speed", "hp", "size", "flaws", "senses"])


class Ancestry(Enum):
    DWARF = ANCESTRY(
        "dwarf",
        [Ability.CONSTITUTION, Ability.WISDOM, Ability.BLANK],
        ["Common", "Dwarf"],
        20,
        10,
        "Medium",
        [Ability.CHARISMA],
        ["darkvision"]
    )
    ELF = ANCESTRY(
        "elf",
        [Ability.DEXTERITY, Ability.INTELLIGENCE, Ability.BLANK],
        ["Common", "Elf", ],
        30,
        6,
        "Medium",
        [Ability.CONSTITUTION],
        ["low-light vision"]
    )
    GNOME = ANCESTRY(
        "gnome",
        [Ability.CONSTITUTION, Ability.CHARISMA, Ability.BLANK],
        ["Common", "Gnomish", "Sylvan"],
        20,
        8,
        "Small",
        [Ability.STRENGTH],
        ["darkvision"]
    )
    GOBLIN = ANCESTRY(
        "goblin",
        [Ability.DEXTERITY, Ability.CHARISMA, Ability.BLANK],
        ["Common", "Goblin"],
        25,
        6,
        "Small",
        [Ability.WISDOM],
        ["darkvision"]
    )
    HALFLING = ANCESTRY(
        "halfling",
        [Ability.DEXTERITY, Ability.CHARISMA, Ability.BLANK],
        ["Common", "Halfling"],
        25,
        8,
        "Small",
        [Ability.STRENGTH],
        ["low-light vision"]
    )
    HUMAN = ANCESTRY(
        "human",
        [Ability.BLANK, Ability.BLANK],
        ["Common"],
        25,
        8,
        "Medium",
        [],
        []
    )

    def __repr__(self):
        return f"<{self.__class__.__name__}.{self.value.name}>"

    def __str__(self):
        return self.value.name

    def __call__(self, *args, **kwargs):
        return self.value


CLASS = namedtuple("class_", ["name", "ability", "hitpoints"])


class Class(Enum):
    BARBARIAN = CLASS("barbarian", Ability.BLANK, 12)

    def __repr__(self):
        return f"<{self.__class__.__name__}.{self.value.name}>"

    def __str__(self):
        return self.value.name

    def __call__(self, *args, **kwargs):
        return self.value
