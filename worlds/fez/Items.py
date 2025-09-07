from BaseClasses import ItemClassification
from typing import TypedDict, List

from BaseClasses import Item


class FezItem(Item):
    name: str = "Fez"


class ItemDict(TypedDict):
    name: str
    count: int
    classification: ItemClassification


progression_items: List[ItemDict] = [
    {'name': "Golden Cube",
     'count': 32,
     'classification': ItemClassification.progression},
    {'name': "Anti-Cube",
     'count': 32,
     'classification': ItemClassification.progression},
    {'name': "Key",
     'count': 8,
     'classification': ItemClassification.progression},
    {'name': "Owl",
     'count': 4,
     'classification': ItemClassification.progression_deprioritized}
]

skippable_items: List[ItemDict] = [
    {'name': "Red Map",
     'count': 1,
     'classification': ItemClassification.deprioritized},
    {'name': "Purple Map",
     'count': 1,
     'classification': ItemClassification.deprioritized},
    {'name': "Tower Map",
     'count': 1,
     'classification': ItemClassification.deprioritized},
    {'name': "QR Code Map",
     'count': 1,
     'classification': ItemClassification.deprioritized},
    {'name': "Burned Map",
     'count': 1,
     'classification': ItemClassification.deprioritized},
    {'name': "Cemetery Map 1",
     'count': 1,
     'classification': ItemClassification.deprioritized},
    {'name': "Cemetery Map 2",
     'count': 1,
     'classification': ItemClassification.deprioritized},
    {'name': "Cemetery Map 3",
     'count': 1,
     'classification': ItemClassification.deprioritized},
    {'name': "Cemetery Map 4",
     'count': 1,
     'classification': ItemClassification.deprioritized},
    {'name': "The Writing Cube",
     'count': 1,
     'classification': ItemClassification.deprioritized},
    {'name': "The Counting Cube",
     'count': 1,
     'classification': ItemClassification.deprioritized},
    {'name': "The Tome Artifact",
     'count': 1,
     'classification': ItemClassification.deprioritized},
    {'name': "The Skull Artifact",
     'count': 1,
     'classification': ItemClassification.deprioritized},
    {'name': "Heart Cube",
     'count': 3,
     'classification': ItemClassification.deprioritized}
]

trap_items: List[ItemDict] = [
    {'name': "Rotation Trap",
     'count': 1,
     'classification': ItemClassification.trap},
    {'name': "Sleep Trap",
     'count': 1,
     'classification': ItemClassification.trap}
]

filler_items: List[ItemDict] = [
    {'name': "Emotional Support",
     'count': 1,
     'classification': ItemClassification.filler}
]
