from typing import Dict, Set
from .Locations import all_location_data


class HldRegionData:
    def __init__(self, name: str, exits: Set[str]):
        self.name = name
        self.exits = exits


# TODO: Consider being more specific than just main regions
all_region_data: Set[HldRegionData] = {
    HldRegionData("Central Town", {"Divine Path", "Eastern Watershelf", "Midnight Woods", "Wastes", "The Abyss"}),
    HldRegionData("Divine Path", {"Central Town"}),
    HldRegionData("Eastern Watershelf", {"Central Town"}),
    HldRegionData("Midnight Woods", {"Central Town"}),
    HldRegionData("Wastes", {"Central Town"}),
    HldRegionData("The Abyss", {"Central Town"}),
}

region_name_to_location_name: Dict[str, Set[str]] = {data.name: set() for data in all_region_data}
for data in all_location_data:
    region_name_to_location_name[data.region_name].add(data.name)
