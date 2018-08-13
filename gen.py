import random
from character import Character
from alignment import alignment
from ability_score import Abilities
from boost import Boost
import data

c = Character(name="Bob",
    ancestry=data.ancestries[0],
    background=data.backgrounds[0],
    klass=data.classes[0],
    level=2)
c.set_boosts()
print(c)
print("ancestry:", c.ancestry)

# assign random boosts for unselected free boosts
for source in Boost.sources:
    free_boosts = c.get_free(source, c.level)
    for boost in free_boosts:
        available = c.get_available(source, c.level)
        boost.ability = random.choice(available)

c.print_ability_scores()

print("size:", c.size)
print("background:", c.background)

# assign random alignment
c.alignment = random.choice(list(alignment))
print("alignment:", c.alignment)

#deity
#age
#gender
c.languages = [c.ancestry.bonus_languages[0], c.ancestry.bonus_languages[1], ]
print("languages:", c.languages)
print("speed:", c.speed)
print("level:", c.level)
print("class dc:", c.class_dc)
#hero points
print("hp:", c.hit_points)
c.level = 5
print("level:", c.level)
print("class dc:", c.class_dc)
print("hp:", c.hit_points)

#senses
#perception
#wisdom
#teml
#saves
#fortitude
#reflex
#will
#ac
#ability scores
#str
#dex
#con
#int
#wis
#cha
#weapon proficiencies
#armor proficiencies
#light
#medium
#heavy
#shields
#melee strikes
#ranged strikes
#skills
#actions and activities
#reactions and free actions

