from BaseClasses import Item, ItemClassification
from typing import List

class HldItem(Item):
    game: str = "Hyper Light Drifter"


class HldItemData():
    def __init__(self, name: str, count: int, classification: ItemClassification):
        self.name = name
        self.count = count
        self.classification = classification


# TODO: Add anything else I might have forgotten
progression_items: List[HldItemData] = [
    HldItemData("Module",           32, ItemClassification.progression),
]

# TODO: Replace gears with each unique weapon and upgrade
skippable_items: List[HldItemData] = [
    # TODO: Figure out if this should be progression instead
    HldItemData("Key",              4,  ItemClassification.deprioritized),

    # Weapons (sword and pistol guaranteed for start)
    # TODO: Consider making sword and pistol not starting items
    HldItemData("Blade Caster",     1, ItemClassification.deprioritized),
    HldItemData("Blunderbuss",      1, ItemClassification.deprioritized),
    HldItemData("Crystal Shot",     1, ItemClassification.deprioritized),
    HldItemData("Diamond Shotgun",  1, ItemClassification.deprioritized),
    HldItemData("Impact Railgun",   1, ItemClassification.deprioritized),
    HldItemData("Railgun",          1, ItemClassification.deprioritized),
    HldItemData("Special Grenade",  1, ItemClassification.deprioritized),
    HldItemData("Zeliska",          1, ItemClassification.deprioritized),

    # Abilities
    # TODO: Consider making dash not starting items
    HldItemData("Heavy Strike",     1, ItemClassification.deprioritized),
    HldItemData("Bullet Deflect",   1, ItemClassification.deprioritized),
    HldItemData("Phantom Strike",   1, ItemClassification.deprioritized),
    # TODO: Figure out if chain dash should be progression due to quality of life
    HldItemData("Chain Dash",       1, ItemClassification.deprioritized),
    HldItemData("Bullet Absorb",    1, ItemClassification.deprioritized),
    HldItemData("Dash Attack",      1, ItemClassification.deprioritized),
    HldItemData("Grenade Upgrade",  1, ItemClassification.deprioritized),
    # TODO: Think of how to handle gun upgrades
    HldItemData("Health Upgrade",   2, ItemClassification.deprioritized),
]

trap_items: List[HldItemData] = [
    # Boss summon traps
    HldItemData("The Archer",       1,  ItemClassification.trap),
    HldItemData("The Emperor",      1,  ItemClassification.trap),
    HldItemData("The Hanged Man",   1,  ItemClassification.trap),
    HldItemData("The Hierophant",   1,  ItemClassification.trap),
    HldItemData("The Reaper",       1,  ItemClassification.trap),
    HldItemData("The Sorcer",       1,  ItemClassification.trap),
    HldItemData("The Summoner",     1,  ItemClassification.trap),
    HldItemData("Judgement",        1,  ItemClassification.trap),
]

filler_items: List[HldItemData] = [
    HldItemData("Med Kit",          1,  ItemClassification.filler),
    HldItemData("Recharge All",     1,  ItemClassification.filler),  # Recharges weapon and grenade
]

main_items = progression_items + skippable_items
all_item_data = main_items + trap_items + filler_items

item_name_groups = {
    "Progression":  {item.name for item in progression_items},
    "Skippable":    {item.name for item in skippable_items},
    "Trap":         {item.name for item in trap_items},
    "Filer":        {item.name for item in filler_items},
}
