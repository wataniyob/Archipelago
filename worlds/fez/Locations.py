from typing import List, Set
from BaseClasses import Location


class FezLocation(Location):
    game: str = "Fez"

class FezLocationData:
    def __init__(self, name: str, region: str):
        self.name = name
        self.region = count


cube_bit_locations = {
    # TODO: Add all 64 cube bit locations
}

golden_cube_locations = {
    # TODO: Add all 24 golden cube locations
}

anti_cube_locations = {
    # TODO: Add all 32 anti-cube locations
}

heart_cube_locations = {
    # TODO: Add all 3 heart cube locations
}

key_locations = {
    # TODO: Add all 8 key locations
}

owl_locations = {
    # TODO: Add all 4 owl locations
}

artifact_locations = {
    FezLocationData("The Writing Cube",     "TODO"),
    FezLocationData("The Counting Cube",    "TODO"),
    FezLocationData("The Tome Artifact",    "TODO"),
    FezLocationData("The Skull Artifact",   "TODO"),
}

map_locations = {
    FezLocationData("Red Map"               "TODO"),
    FezLocationData("Purple Map"            "TODO"),
    FezLocationData("Tower Map"             "TODO"),
    FezLocationData("QR Code Map"           "TODO"),
    FezLocationData("Burned Map"            "TODO"),
    FezLocationData("Cemetery Map 1"        "TODO"),
    FezLocationData("Cemetery Map 2"        "TODO"),
    FezLocationData("Cemetery Map 3"        "TODO"),
    FezLocationData("Cemetery Map 4"        "TODO"),
}

all_locations = cube_bit_locations \
                + golden_cube_locations \
                + anti_cube_locations \
                + heart_cube_locations \
                + key_locations \
                + owl_locations \
                + artifact_locations \
                + map_locations

location_name_groups = {
    "Cube Bit":     cube_bit_locations,
    "Golden Cube":  golden_cube_locations,
    "Anti-Cube":    anti_cube_locations,
    "Heart Cube":   heart_cube_locations,
    "Key":          key_locations,
    "Owl":          owl_locations,
    "Artifact":     artifact_locations,
    "Map":          map_locations,
}
