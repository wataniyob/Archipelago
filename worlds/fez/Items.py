from BaseClasses import Item, ItemClassification
from typing import List

class FezItem(Item):
    game: str = "Fez"


class FezItemData():
    def __init__(self, name: str, count: int, classification: ItemClassification):
        self.name = name
        self.count = count
        self.classification = classification


progression_items: List[FezItemData] = [
    FezItemData("Golden Cube",          32, ItemClassification.progression),
    FezItemData("Anti-Cube",            32, ItemClassification.progression),
    FezItemData("Key",                  8,  ItemClassification.progression),
    FezItemData("Owl",                  4,  ItemClassification.progression_deprioritized)
]

skippable_items: List[FezItemData] = [
    FezItemData("Red Map",              1,  ItemClassification.deprioritized),
    FezItemData("Purple Map",           1,  ItemClassification.deprioritized),
    FezItemData("Tower Map",            1,  ItemClassification.deprioritized),
    FezItemData("QR Code Map",          1,  ItemClassification.deprioritized),
    FezItemData("Burned Map",           1,  ItemClassification.deprioritized),
    FezItemData("Cemetery Map 1",       1,  ItemClassification.deprioritized),
    FezItemData("Cemetery Map 2",       1,  ItemClassification.deprioritized),
    FezItemData("Cemetery Map 3",       1,  ItemClassification.deprioritized),
    FezItemData("Cemetery Map 4",       1,  ItemClassification.deprioritized),
    FezItemData("The Writing Cube",     1,  ItemClassification.deprioritized),
    FezItemData("The Counting Cube",    1,  ItemClassification.deprioritized),
    FezItemData("The Tome Artifact",    1,  ItemClassification.deprioritized),
    FezItemData("The Skull Artifact",   1,  ItemClassification.deprioritized),
    FezItemData("Heart Cube",           3,  ItemClassification.deprioritized),
    FezItemData("Sunglasses",           1,  ItemClassification.deprioritized)
]

trap_items: List[FezItemData] = [
    FezItemData("Rotation Trap",        1,  ItemClassification.trap),
    FezItemData("Sleep Trap",           1,  ItemClassification.trap)
]

filler_items: List[FezItemData] = [
    FezItemData("Emotional Support",    1,  ItemClassification.filler)
]

main_items = progression_items + skippable_items
all_item_data = main_items + trap_items + filler_items

item_name_groups = {
    "Progression":  {item.name for item in progression_items},
    "Skippable":    {item.name for item in skippable_items},
    "Trap":         {item.name for item in trap_items},
    "Filer":        {item.name for item in filler_items},
}
