import random
from character import Character
from alignment import alignment
from ability_score import Abilities
import grant
import data

c = Character(name="Bob",
    ancestry=random.choice(data.ancestries),
    background=random.choice(data.backgrounds),
    klass=random.choice(data.classes),
    level=2)
#c.set_boosts()
print(c)
print("ancestry:", c.ancestry)

# assign random boosts for unselected free boosts
#for source in Boost.sources:
#    free_boosts = c.get_free(source, c.level)
#    for boost in free_boosts:
#        available = c.get_available(source, c.level)
#        boost.ability = random.choice(available)

c.print_ability_scores()

print("size:", c.size)
print("background:", c.background)

# assign random alignment
c.alignment = random.choice(list(alignment))
print("alignment:", c.alignment)

#deity
#age
#gender
if c.ancestry.bonus_languages:
    c.languages = random.choice(c.ancestry.bonus_languages)
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

