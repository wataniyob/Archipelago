from typing import List
from BaseClasses import Location


class HldLocation(Location):
    game: str = "Hld"

class HldLocationData:
    def __init__(self, name: str, region_name: str):
        self.name = name
        self.region_name = region_name


# TODO: Give these more specific names
gear_bit_locations: List[HldLocationData] = [
    HldLocationData("Gearbit 1", "Central Town"),
    HldLocationData("Gearbit 2", "Central Town"),
    HldLocationData("Gearbit 3", "Central Town"),
    HldLocationData("Gearbit 4", "Central Town"),
    HldLocationData("Gearbit 5", "Central Town"),
    HldLocationData("Gearbit 6", "Central Town"),
    HldLocationData("Gearbit 7", "Central Town"),
    HldLocationData("Gearbit 8", "Central Town"),
    HldLocationData("Gearbit 9", "Central Town"),
    HldLocationData("Gearbit 10", "Central Town"),
    HldLocationData("Gearbit 11", "Central Town"),
    HldLocationData("Gearbit 12", "Central Town"),

    # TODO: Add remaining entries
    # 47 in Divine Path
    # 44 in Eastern Watershelf
    # 46 in Midnight Woods
    # 37 in Wastes
]

module_locations: List[HldLocationData] = [
    # TODO: Add entries
]

key_locations: List[HldLocationData] = [
    # TODO: Add entries
]

weapon_locations: List[HldLocationData] = [
    # TODO: Add entries
]

outfit_locations: List[HldLocationData] = [
    # TODO: Add entries
]

boss_locations: List[HldLocationData] = [
    HldLocationData("The Archer", "Wastes"),
    HldLocationData("The Emperor", "Eastern Watershelf"),
    HldLocationData("The Hanged Man", "Midnight Woods"),
    HldLocationData("The Hierophant", "Divine Path"),
    HldLocationData("The Reaper", "Wastes"),
    HldLocationData("The Sorcer", "Wastes"),
    HldLocationData("The Summoner", "Wastes"),
    # Defeating Judgement is the goal, so not listed
]

misc_locations: List[HldLocationData] = [
    # TODO: Remove if none not included above
]

all_location_data = gear_bit_locations \
                    + module_locations \
                    + key_locations \
                    + weapon_locations \
                    + outfit_locations \
                    + boss_locations \
                    + misc_locations

location_name_groups = {
    "Gear Bit": {data.name for data in gear_bit_locations},
    "Module":   {data.name for data in module_locations},
    "Key":      {data.name for data in key_locations},
    "Weapon":   {data.name for data in weapon_locations},
    "Outfit":   {data.name for data in outfit_locations},
    "Boss":     {data.name for data in boss_locations},
    "Misc":     {data.name for data in misc_locations},
}
