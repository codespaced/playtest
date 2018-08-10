from character import Character
from klass import Klass
from ancestry import Ancestry
from background import Background

import json


def load_json(file_name, klass):
    with open(file_name) as f:
        data = json.load(f)
    things = []
    for item in data:
        things.append(klass(**item))
    return things

ancestries = load_json("data/ancestries.json", Ancestry)
backgrounds = load_json("data/backgrounds.json", Background)
#ancestry_feats = load_json("data/ancestry_feats.json", Ancestry_feat)
classes = load_json("data/classes.json", Klass)


c = Character(name="Bob",
    ancestry=ancestries[0],
    background=backgrounds[0],
    klass=classes[0])
print(c)
print("ancestry:", c.ancestry)
c.languages = "Undercommon, Gnollish"
print("languages:", c.languages)
print("size:", c.size)
print("hp:", c.hitpoints)
print("background:", c.background)
print("class:", c.klass)
print(dir(c.ancestry))