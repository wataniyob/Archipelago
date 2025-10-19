from typing import TYPE_CHECKING

from ..generic.Rules import CollectionRule, set_rule

if TYPE_CHECKING:
    from . import FezWorld
else:
    FezWorld = object


def set_rules(world: FezWorld) -> None:
    """Rules that are always present"""
    # Helper functions
    get_location = lambda name: world.multiworld.get_location(name, world.player)
    get_entrance = lambda start, end: world.multiworld.get_entrance(f"{start} -> {end}", world.player)

    # Key doors (requires a specific key to open, unique behaviour to AP)
    set_rule(get_entrance("Villageville 3D", "Boileroom"),              lambda state: state.has("Boileroom Door Unlocked", world.player))
    set_rule(get_entrance("_LighthouseLower", "Lighthouse House A"),    lambda state: state.has("Lighthouse Door Unlocked", world.player))
    set_rule(get_entrance("Tree", "Tree Crumble"),                      lambda state: state.has("Tree Door Unlocked", world.player))
    set_rule(get_entrance("Rails", "Well 2"),                           lambda state: state.has("Well Door Unlocked", world.player))
    set_rule(get_entrance("Pivot 1", "Windmill Interior"),              lambda state: state.has("Windmill Door Unlocked", world.player))
    set_rule(get_entrance("Mausoleum", "Crypt"),                        lambda state: state.has("Mausoleum Door Unlocked", world.player))
    set_rule(get_entrance("Sewer Hub", "Sewer QR"),                     lambda state: state.has("Sewer Hub Door Unlocked", world.player))
    set_rule(get_entrance("Sewer Pillars", "Sewer Fork"),               lambda state: state.has("Sewer Pillars Door Unlocked", world.player))
    # Custom locked doors to balance sphere sizes
    set_rule(get_entrance("Nature Hub", "Arch"),                        lambda state: state.has("Arch Door Unlocked", world.player))
    set_rule(get_entrance("Nature Hub", "Bell Tower"),                  lambda state: state.has("Bell Tower Door Unlocked", world.player))
    set_rule(get_entrance("Tree", "Cabin Interior B"),                  lambda state: state.has("Cabin Door Unlocked", world.player))
    set_rule(get_entrance("Tree Sky", "Throne"),                        lambda state: state.has("Throne Door Unlocked", world.player))

    # Link doors (requires having been to both ends before being able to use)
    def set_link_door_rule(region1: str, region2: str):
        rule: CollectionRule = lambda state: state.can_reach_region(region1, world.player) and state.can_reach_region(region2, world.player)
        set_rule(get_entrance(region1, region2), rule)
        set_rule(get_entrance(region2, region1), rule)
    set_link_door_rule("Bell Tower", "Five Towers")
    set_link_door_rule("Industrial Hub", "Well 2")
    set_link_door_rule("Mausoleum", "Tree Roots")
    set_link_door_rule("Memory Core", "Pivot Watertower")
    set_link_door_rule("Nature Hub", "Two Walls")
    set_link_door_rule("Nu Zu Abandoned B", "Sewer to Lava")
    set_link_door_rule("Observatory", "Throne")
    set_link_door_rule("Purple Lodge Ruin", "Visitor")
    set_link_door_rule("Sewer Fork", "Sewer Hub")
    set_link_door_rule("Zu City Ruins", "Zu Library")

    # Cube count doors (requires having a specific number of either golden or anti cubes)
    def cube_count_rule(count: int) -> CollectionRule:
        return lambda state: state.has_from_list(["Golden Cube", "Anti-Cube"], world.player, count)
    set_rule(get_entrance("Villageville 3D",    "Big Tower"),       cube_count_rule(1))
    set_rule(get_entrance("Big Tower",          "Memory Core"),     cube_count_rule(2))
    set_rule(get_entrance("Memory Core",        "Wall Village"),    cube_count_rule(4))
    set_rule(get_entrance("Memory Core",        "Industrial City"), cube_count_rule(8))
    set_rule(get_entrance("Memory Core",        "Zu City"),         cube_count_rule(16))
    set_rule(get_entrance("Zu City",            "Stargate"),        cube_count_rule(32))
    set_rule(get_entrance("Water Pyramid",      "Temple of Love"),  cube_count_rule(64))

    # Water level logic (requires lowering the water level)
    water_level_rule: CollectionRule = lambda state: state.can_reach_region("Water Wheel", world.player)
    set_rule(get_entrance("Nature Hub", "Ritual"), water_level_rule)
    set_rule(get_entrance("Waterfall", "Zu Zuish"), water_level_rule)
    set_rule(get_entrance("_LighthouseLower", "Zu Fork"), water_level_rule)
    set_rule(get_entrance("Water Tower", "Watertower Secret"), water_level_rule)
    set_rule(get_entrance("Bell Tower", "Quantum"), water_level_rule)
    set_rule(get_entrance("Water Wheel", "Water Wheel B"), water_level_rule)

    # Owl logic
    set_rule(get_entrance("Owl", "Big Owl"), lambda state: state.has("Owl", world.player, 4))


def set_knowledge_rules(world: FezWorld) -> None:
    """Rules for knowledge logic"""
    # Helper functions
    get_location = lambda name: world.multiworld.get_location(name, world.player)
    get_entrance = lambda start, end: world.multiworld.get_entrance(f"{start} -> {end}", world.player)

    # Zu numerals logic
    number_rule: CollectionRule = lambda state: state.can_reach_region("Oldschool", world.player)
    set_rule(get_location("Bell Tower Anti-Cube"), number_rule)

    # Zu alphabet logic
    alphabet_rule: CollectionRule = lambda state: state.can_reach_region("Fox", world.player)
    set_rule(get_location("Security Question Heart Cube"), alphabet_rule)

    # Tetromino logic
    tetromino_rule: CollectionRule = lambda state: (state.can_reach_region("Code Machine", world.player) and
                                                    state.can_reach_region("Nu Zu School", world.player) and
                                                    number_rule(state))
    set_rule(get_location("Zu Code Loop Anti-Cube"), tetromino_rule)
    set_rule(get_location("Code Machine Anti-Cube"), tetromino_rule)
    set_rule(get_location("Boileroom Anti-Cube"), tetromino_rule)
    set_rule(get_location("Nu Zu School Anti-Cube"), tetromino_rule)
    set_rule(get_location("Telescope Anti-Cube"), tetromino_rule)
    set_rule(get_entrance("Waterfall", "CMY"), tetromino_rule)
    set_rule(get_entrance("Waterfall", "Water Wheel"), tetromino_rule)
    set_rule(get_entrance("Sewer to Lava", "Lava"), tetromino_rule)

    # First-person logic
    first_person_rule: CollectionRule = lambda state: (state.has("Sunglasses", world.player) and tetromino_rule(state))
    set_rule(get_location("Lighthouse Floor Anti-Cube"), first_person_rule)
    set_rule(get_location("Tree Cabin Floor Anti-Cube"), first_person_rule)
    set_rule(get_location("Tree Sky Floor Anti-Cube"), first_person_rule)
    set_rule(get_location("Zu Bridge Floor Anti-Cube"), first_person_rule)

    # Treasure map logic
    def map_rule(map: str) -> CollectionRule:
        return lambda state: state.has(map, world.player)
    set_rule(get_location("Arch Chest 2"), map_rule("Arch Map"))  # TODO: Confirm it's 2 and not 1
    set_rule(get_location("Tree Sky Chest"), map_rule("Tree Sky Map"))
    set_rule(get_location("Pivot Watertower Chest"), map_rule("Tower Map"))
    # TODO: Add QR code map

    # Crypt map logic
    set_rule(get_entrance("Crypt", "Tree of Death"), lambda state: (map_rule("Crypt Map A")(state) and
                                                                    map_rule("Crypt Map B")(state) and
                                                                    map_rule("Crypt Map C")(state) and
                                                                    map_rule("Crypt Map D")(state) and
                                                                    number_rule(state)))

    # Black monolith logic
    set_rule(get_location("Black Monolith Heart Cube"), lambda state: (map_rule("Ritual Map")(state) and
                                                                       first_person_rule(state) and
                                                                       state.has("ssqee w", world.player)))

    # Throne anti-cube logic
    def throne_cube_rule(state) -> bool:
        if state.can_reach_region("Sewer QR", world.player):
            return True
        else:
            retval = state.has("Sunglasses", world.player)
            retval &= state.can_reach_region("Zu House Empty", world.player)
            retval &= state.can_reach_region("Zu Throne Ruins", world.player)
            return retval
    set_rule(get_location("Throne Anti-Cube"), throne_cube_rule)
