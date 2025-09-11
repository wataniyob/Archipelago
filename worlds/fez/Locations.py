# TODO: Name each bit, cube and collectible uniquely

from typing import Set
from Archipelago.worlds.fez.Options import FezOptions
from BaseClasses import Location


class FezLocation(Location):
    game: str = "Fez"

class LocData(NamedTuple):
    ap_code: Optional[int]
    region: Optional[str]

def get_location_names() -> Dict[str, int]:
    # This is just a fancy way of getting all the names and data in the location table and making a dictionary thats {name, code}
    # If you have dynamic locations then you want to add them to the dictionary as well
    names = {name: data.ap_code for name, data in location_table.items()}


#codes: always have 20050 at front
#       1XX: Cube Bits
#       2XX: Golden Cubes
#       3XX: Anti-Cubes
#       40X: Heart Cubes
#       41X: Keys
#       42X: Owls


non_distinct_locations = {}

for i in range(1,65):
    reg = ""
    if i in range(1,9):
        reg = "0 Cubes"
    elif i in range(9,17):
        reg = "1 Cube"
    else:
        reg = "Menu"
    non_distinct_locations[f"Cube Bit {i}"] = LocData(20050100+i,reg)

for i in range(1,33):
    reg = "Menu"
    # no golden cubes in villageville
    non_distinct_locations[f"Golden Cube {i}"] = LocData(20050200+i,reg)

for i in range(1,33):
    reg = ""
    if i in [1,2]:
        reg = "0 Cubes"
    else:
        reg = "Menu"
    non_distinct_locations[f"Anti-Cube {i}"] = LocData(20050300+i,reg)

for i in range(1,4):
    reg = "Menu"
    # no heart cubes in villageville
    non_distinct_locations[f"Heart Cube {i}"] = LocData(20050400+i,reg)

for i in range(1,9):
    reg = ""
    if i in [1,2]:
        reg = "0 Cubes"
    else:
        reg = "Menu"
    non_distinct_locations[f"Key {i}"] = LocData(20050410+i,reg)

for i in range(1,5):
    reg = "Menu"
    # no Owls in villageville
    non_distinct_locations[f"Owl {i}"] = LocData(20050420+i,reg)

artifact
    

#I've commented this out since I want to create a location system that will be easier for me to access later

#artifact_locations = [
#    "The Writing Cube",
#    "The Counting Cube",
#    "The Tome Artifact",
#    "The Skull Artifact"
#]

#map_locations = [
#    "Red Map"
#    "Purple Map"
#    "Tower Map"
#    "QR Code Map"
#    "Burned Map"
#    "Cemetery Map 1"
#    "Cemetery Map 2"
#    "Cemetery Map 3"
#    "Cemetery Map 4"
#]

#location_names: Set[str] = set()
#location_names.union(artifact_locations)
#location_names.union(map_locations)
#location_names.union([f"Cube Bit {i}" for i in range(1, 65)])       # 64 Cube Bits
#location_names.union([f"Golden Cube {i}" for i in range(1, 25)])    # 24 Golden Cubes
#location_names.union([f"Anti-Cube {i}" for i in range(1, 32)])      # 32 Anti-Cubes
#location_names.union([f"Heart Cube {i}" for i in range(1, 4)])      # 3 Heart Cubes
#location_names.union([f"Key {i}" for i in range(1, 9)])             # 8 Keys
#location_names.union([f"Owl {i}" for i in range(1, 5)])             # 4 Owls

#location_name_groups = {
#    "Cube Bit":     {location for location in location_names if "Cube Bit" in location},
#    "Golden Cube":  {location for location in location_names if "Golden Cube" in location},
#    "Anti-Cube":    {location for location in location_names if "Anti-Cube" in location},
#    "Heart Cube":   {location for location in location_names if "Heart Cube" in location},
#    "Key":          {location for location in location_names if "Key" in location},
#    "Owl":          {location for location in location_names if "Owl" in location},
#    "Artifact":     set(artifact_locations),
#    "Map":          set(map_locations)
#}
