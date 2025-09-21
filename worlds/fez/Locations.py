from typing import Set
from BaseClasses import Location


class FezLocation(Location):
    game: str = "Fez"

class FezLocationData:
    def __init__(self, name: str, region_name: str):
        self.name = name
        self.region_name = region_name


cube_bit_locations: Set[FezLocationData] = {
    FezLocationData("Abandoned A Cube Bit", "Abandoned A"),
    FezLocationData("Abandoned B Cube Bit", "Abandoned B"),
    FezLocationData("Ancient Walls Cube Bit 1", "Ancient Walls"),
    FezLocationData("Ancient Walls Cube Bit 2", "Ancient Walls"),
    FezLocationData("Ancient Walls Cube Bit 3", "Ancient Walls"),
    FezLocationData("Arch Cube Bit 1", "Arch"),
    FezLocationData("Arch Cube Bit 2", "Arch"),
    FezLocationData("Arch Cube Bit 3", "Arch"),
    # TODO
    FezLocationData("Villageville Cube Bit 1", "Villageville 3D"),
    FezLocationData("Villageville Cube Bit 2", "Villageville 3D"),
    FezLocationData("Villageville Cube Bit 3", "Villageville 3D"),
    FezLocationData("Villageville Cube Bit 4", "Villageville 3D"),
    # TODO: Add all 64 cube bit locations
}

golden_cube_locations: Set[FezLocationData] = {
    FezLocationData("Clock Cube", "Clock")
    # TODO: Add all 24 golden cube locations (some already included in chest_locations)
}

anti_cube_locations: Set[FezLocationData] = {
    FezLocationData("Big Owl Anti-Cube", "Big Owl")
    # TODO: Add all 32 anti-cube locations
}

heart_cube_locations: Set[FezLocationData] = {
    FezLocationData("Black Monolith Heart Cube", "Ritual"),
    FezLocationData("Telescope Heart Cube", "Telescope"),
    FezLocationData("Security Question Heart Cube", "Zu Zuish")
}

chest_locations: Set[FezLocationData] = {
    FezLocationData("Arch Chest 1", "Arch"),
    FezLocationData("Arch Chest 2", "Arch"),
    FezLocationData("Five Towers Cave Chest", "Five Towers Cave"),
    FezLocationData("Fox Chest", "Fox"),
    FezLocationData("Globe Interior Chest", "Globe Interior"),
    FezLocationData("Industrial Superspin Chest", "Industrial Superspin"),
    FezLocationData("Lighthouse House A Chest", "Lighthouse House A"),
    FezLocationData("Mausoleum Chest", "Mausoleum"),
    FezLocationData("Mine Bomb Pillar Chest", "Mine Bomb Pillar"),
    FezLocationData("Orrery B Chest", "Orrery B"),
    FezLocationData("Parlor Chest", "Parlor"),
    FezLocationData("Pivot Watertower Chest", "Pivot Watertower"),
    FezLocationData("Sewer Pivot Chest", "Sewer Pivot"),
    FezLocationData("Sewer Treasure 1 Chest", "Sewer Treasure 1"),
    FezLocationData("Sewer Treasure 2 Chest", "Sewer Treasure 2"),
    FezLocationData("Tree Crumble Chest", "Tree Crumble"),
    FezLocationData("Tree of Death Chest", "Tree of Death"),
    FezLocationData("Tree Sky Chest", "Tree Sky"),
    FezLocationData("Villageville Chest", "Villageville 3D"),
    FezLocationData("Wall Hole Chest", "Wall Hole"),
    FezLocationData("Water Wheel B Chest", "Water Wheel B"),
    FezLocationData("Windmill Cave Chest", "Windmill Cave"),
    FezLocationData("Zu City Ruins Chest", "Zu City Ruins"),
    FezLocationData("Zu House Empty B Chest", "Zu House Empty B")
}

owl_locations: Set[FezLocationData] = {
    FezLocationData("Waterfall Owl", "Waterfall"),
    FezLocationData("Visitor Owl", "Visitor"),
    FezLocationData("Pivot 1 Owl", "Pivot 1"),
    FezLocationData("Tree Owl", "Tree")
}

all_location_data = cube_bit_locations \
                .union(golden_cube_locations) \
                .union(anti_cube_locations) \
                .union(heart_cube_locations) \
                .union(chest_locations) \
                .union(owl_locations)

location_name_groups = {
    "Cube Bit":     {data.name for data in cube_bit_locations},
    "Golden Cube":  {data.name for data in golden_cube_locations},
    "Anti-Cube":    {data.name for data in anti_cube_locations},
    "Heart Cube":   {data.name for data in heart_cube_locations},
    "Chest":        {data.name for data in chest_locations},
    "Owl":          {data.name for data in owl_locations}
}
