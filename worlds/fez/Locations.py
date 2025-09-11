# TODO: Name each bit, cube and collectible uniquely

from typing import Set
from BaseClasses import Location


class FezLocation(Location):
    game: str = "Fez"


artifact_locations = [
    "The Writing Cube",
    "The Counting Cube",
    "The Tome Artifact",
    "The Skull Artifact"
]

map_locations = [
    "Red Map"
    "Purple Map"
    "Tower Map"
    "QR Code Map"
    "Burned Map"
    "Cemetery Map 1"
    "Cemetery Map 2"
    "Cemetery Map 3"
    "Cemetery Map 4"
]

location_names: Set[str] = set()
location_names.union(artifact_locations)
location_names.union(map_locations)
location_names.union([f"Cube Bit {i}" for i in range(1, 65)])       # 64 Cube Bits
location_names.union([f"Golden Cube {i}" for i in range(1, 25)])    # 24 Golden Cubes
location_names.union([f"Anti-Cube {i}" for i in range(1, 32)])      # 32 Anti-Cubes
location_names.union([f"Heart Cube {i}" for i in range(1, 4)])      # 3 Heart Cubes
location_names.union([f"Key {i}" for i in range(1, 9)])             # 8 Keys
location_names.union([f"Owl {i}" for i in range(1, 5)])             # 4 Owls

location_name_groups = {
    "Cube Bit":     {location for location in location_names if "Cube Bit" in location},
    "Golden Cube":  {location for location in location_names if "Golden Cube" in location},
    "Anti-Cube":    {location for location in location_names if "Anti-Cube" in location},
    "Heart Cube":   {location for location in location_names if "Heart Cube" in location},
    "Key":          {location for location in location_names if "Key" in location},
    "Owl":          {location for location in location_names if "Owl" in location},
    "Artifact":     set(artifact_locations),
    "Map":          set(map_locations)
}
