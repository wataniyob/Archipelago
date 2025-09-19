from typing import Set
from BaseClasses import Location


class FezLocation(Location):
    game: str = "Fez"

class FezLocationData:
    def __init__(self, name: str, region_name: str):
        self.name = name
        self.region_name = region_name


cube_bit_locations: Set[FezLocationData] = {
    FezLocationData("Cube Bit 1",           "TODO")
    # TODO: Add all 64 cube bit locations
}

golden_cube_locations: Set[FezLocationData] = {
    FezLocationData("Golden Cube 1",        "TODO")
    # TODO: Add all 24 golden cube locations
}

anti_cube_locations: Set[FezLocationData] = {
    FezLocationData("Anti-Cube 1",          "TODO")
    # TODO: Add all 32 anti-cube locations
}

heart_cube_locations: Set[FezLocationData] = {
    FezLocationData("Heart Cube 1",         "TODO")
    # TODO: Add all 3 heart cube locations
}

key_locations: Set[FezLocationData] = {
    FezLocationData("Key 1",                "TODO")
    # TODO: Add all 8 key locations
}

owl_locations: Set[FezLocationData] = {
    FezLocationData("Owl 1",                "TODO")
    # TODO: Add all 4 owl locations
}

artifact_locations: Set[FezLocationData] = {
    FezLocationData("The Writing Cube",     "TODO"),
    FezLocationData("The Counting Cube",    "TODO"),
    FezLocationData("The Tome Artifact",    "TODO"),
    FezLocationData("The Skull Artifact",   "TODO"),
}

map_locations: Set[FezLocationData] = {
    FezLocationData("Red Map",              "TODO"),
    FezLocationData("Purple Map",           "TODO"),
    FezLocationData("Tower Map",            "TODO"),
    FezLocationData("QR Code Map",          "TODO"),
    FezLocationData("Burned Map",           "TODO"),
    FezLocationData("Cemetery Map 1",       "TODO"),
    FezLocationData("Cemetery Map 2",       "TODO"),
    FezLocationData("Cemetery Map 3",       "TODO"),
    FezLocationData("Cemetery Map 4",       "TODO"),
}

all_location_data = cube_bit_locations \
                .union(golden_cube_locations) \
                .union(anti_cube_locations) \
                .union(heart_cube_locations) \
                .union(key_locations) \
                .union(owl_locations) \
                .union(artifact_locations) \
                .union(map_locations)

location_name_groups = {
    "Cube Bit":     {data.name for data in cube_bit_locations},
    "Golden Cube":  {data.name for data in golden_cube_locations},
    "Anti-Cube":    {data.name for data in anti_cube_locations},
    "Heart Cube":   {data.name for data in heart_cube_locations},
    "Key":          {data.name for data in key_locations},
    "Owl":          {data.name for data in owl_locations},
    "Artifact":     {data.name for data in artifact_locations},
    "Map":          {data.name for data in map_locations},
}
