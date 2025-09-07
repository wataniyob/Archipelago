from typing import Dict, List

from BaseClasses import Location


class FezLocation(Location):
    game: str = "Fez"


# TODO: Name each bit, cube and collectible uniquely
# TODO: Place non-location specific antis in Menu (like QR code cube)
# TODO: Split by room rather than region ahead of entrance rando

natural_region_locations = [
    "Bit",  # 37
    "Golden Cube",  # 5
    "Anti-Cube",  # 12
    "Heart Cube",  # 2
    "Key",  # 3
    "Treasure Map",  # 4
    "Writing Cube"  # 1
]

industrial_district_locations = [
    "Bit",  # 16
    "Golden Cube",  # 4
    "Treasure Map",  # 1
]

sewers_locations = [
    "Bit",  # 11
    "Golden Cube",  # 2
    "Anti-Cube",  # 4
    "Key",  # 2
]

cemetery_loactions = [
    "Bit",  # 26
    "Golden Cube",  # 2
    "Anti-Cube",  # 2
    "Treasure Map",  # 1
    "Skull Artifact"  # 1
]

scientific_region_locations = [
    "Bit",  # 11
    "Golden Cube",  # 3
    "Anti-Cube",  # 11
    "Heart Cube"  # 1
    "Treasure Map",  # 2
    "Counting Cube",  # 1
    "Tome Artifact"  # 1
]

misc_regions_locations = [
    "Bit",  # 27
    "Anti-Cube",  # 4
    "Key",  # 3
    "Treasure Map",  # 1
]

regions_to_locations: Dict[str, List[str]] = {
    "Menu": [],
    "Natural Region": natural_region_locations,
    "Industrial District": industrial_district_locations,
    "Sewers": sewers_locations,
    "Cemetery": cemetery_loactions,
    "Scientific Region": scientific_region_locations,
    "Misc Regions": misc_regions_locations
}

all_locations = (natural_region_locations
                 + industrial_district_locations
                 + sewers_locations
                 + cemetery_loactions
                 + scientific_region_locations
                 + misc_regions_locations)
