import json
from klass import Klass
from ancestry import Ancestry
from background import Background
from ancestry_feat import AncestryFeat


def load_json(file_name, klass):
    with open(file_name) as f:
        data = json.load(f)
    things = []
    for item in data:
        things.append(klass(**item))
    return things


ancestries = load_json("data/ancestries.json", Ancestry)
backgrounds = load_json("data/backgrounds.json", Background)
ancestry_feats = load_json("data/ancestry_feats.json", AncestryFeat)
classes = load_json("data/classes.json", Klass)
