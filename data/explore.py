import glob
import json
from collections import Counter

def load_json(file_name):
    with open(file_name) as f:
        data = json.load(f)
    return data

for file_name in glob.glob("*.json"):
    if file_name in ["data.json", "weapons.json"]:
        continue
    print(file_name)
    data = load_json(file_name)
    c = Counter()
    item_types = {}
    for item in data:
        c.update(item.keys())
        for k,v in item.items():
            if k in item_types and item_types[k] != type(v).__name__:
                print(f"{k} has multiple types: {item_types[k]}, {type(v).__name__}")
            item_types[k] = type(v).__name__
    for item in c:
        t = {"list":"[]", "str":'""', "int":0, "dict":"{}"}[item_types[item]]
        print(f'self.{item} = kwargs.get("{item}", {t})')
    print()

