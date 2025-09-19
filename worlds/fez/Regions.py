from typing import Dict, Set
from .Locations import all_location_data


region_name_to_location_name: Dict[str, Set[str]] = {}
for data in all_location_data:
    region_name_to_location_name[data.region_name].union(data.name)


class FezRegionData:
    def __init__(self, name: str, exits: Set[str]):
        self.name = name
        self.exits = exits


# TODO: Add region information
all_region_data: Set[FezRegionData] = {
    FezRegionData("Villageville", {"Mayor McMayor's House"}),
}
