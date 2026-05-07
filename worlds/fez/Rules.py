import functools
from typing import TYPE_CHECKING, Tuple

from .Items import FezItem
from .Locations import FezLocation

from BaseClasses import Entrance, ItemClassification, Location, Region

from rule_builder.rules import CanReachRegion

from ..generic.Rules import CollectionRule, add_rule

if TYPE_CHECKING:
    from . import FezWorld
else:
    FezWorld = object


########################################
# General Rules
########################################

def _get_location(world: FezWorld, name:str) -> Location:
    return world.multiworld.get_location(name, world.player)


def _get_entrance(world: FezWorld, start: str, end: str) -> Entrance:
    return world.multiworld.get_entrance(f"{start} -> {end}", world.player)


def _add_link_door_rule(world: FezWorld, region1: str, region2: str):
    rule: CollectionRule = lambda state: (state.can_reach_region(region1, world.player) and
                                          state.can_reach_region(region2, world.player))
    add_rule(_get_entrance(world, region1, region2), rule)
    add_rule(_get_entrance(world, region2, region1), rule)


def _cube_count_rule(world: FezWorld, count: int) -> CollectionRule:
    return lambda state: (state.count("Golden Cube", world.player) +
                          state.count("Anti-Cube", world.player) +
                          (state.count("Cube Bit", world.player)//8)
                          >= count)


def _number_rule(world: FezWorld) -> CollectionRule:
    return lambda state: state.can_reach_region("Oldschool", world.player)


def _alphabet_rule(world: FezWorld) -> CollectionRule:
    return lambda state: state.can_reach_region("Fox", world.player)


def _tetromino_rule(world: FezWorld, variant: str) -> CollectionRule:
    if variant == 'knowledge':
        return lambda state: (state.can_reach_region("Code Machine", world.player) and
                              state.can_reach_region("Nu Zu School", world.player) and
                              state.can_reach_region("Oldschool", world.player))
    if variant == 'scramble':
        return lambda state: state.can_reach_region("Code Machine", world.player)
    raise ValueError(f"Invalid variant '{variant}'")


def _first_person_rule(world: FezWorld, variant: str) -> CollectionRule:
    if variant == 'knowledge':
        return lambda state: (state.has("Sunglasses", world.player) and
                              _tetromino_rule(world, variant)(state))
    if variant == 'scramble':
        return lambda state: _tetromino_rule(world, variant)(state)
    raise ValueError(f"Invalid variant '{variant}'")


def _map_rule(world: FezWorld, map: str) -> CollectionRule:
    return lambda state: state.has(map, world.player)


def _throne_cube_rule(world: FezWorld, state) -> bool:
    if state.can_reach_region("Sewer QR", world.player):
        return True
    else:
        retval = state.has("Sunglasses", world.player)
        retval &= state.can_reach_region("Zu House Empty", world.player)
        retval &= state.can_reach_region("Zu Throne Ruins", world.player)
        return retval


########################################
# Specific Rules
########################################

def set_rules(world: FezWorld) -> None:
    """Rules that are always present"""
    # Helper functions
    get_entrance = functools.partial(_get_entrance, world)
    add_link_door_rule = functools.partial(_add_link_door_rule, world)
    cube_count_rule = functools.partial(_cube_count_rule, world)

    # Key doors (requires a specific key to open, unique behaviour to AP)
    add_rule(get_entrance("Villageville 3D", "Boileroom"),              lambda state: state.has("Boileroom Door Unlocked", world.player))
    add_rule(get_entrance("_LighthouseLower", "Lighthouse House A"),    lambda state: state.has("Lighthouse Door Unlocked", world.player))
    add_rule(get_entrance("Tree", "Tree Crumble"),                      lambda state: state.has("Tree Door Unlocked", world.player))
    add_rule(get_entrance("Rails", "Well 2"),                           lambda state: state.has("Well Door Unlocked", world.player))
    add_rule(get_entrance("Pivot 1", "Windmill Interior"),              lambda state: state.has("Windmill Door Unlocked", world.player))
    add_rule(get_entrance("Mausoleum", "Crypt"),                        lambda state: state.has("Mausoleum Door Unlocked", world.player))
    add_rule(get_entrance("Sewer Hub", "Sewer QR"),                     lambda state: state.has("Sewer Hub Door Unlocked", world.player))
    add_rule(get_entrance("Sewer Pillars", "Sewer Fork"),               lambda state: state.has("Sewer Pillars Door Unlocked", world.player))
    # Custom locked doors to balance sphere sizes
    add_rule(get_entrance("Nature Hub", "Arch"),                        lambda state: state.has("Arch Door Unlocked", world.player))
    add_rule(get_entrance("Nature Hub", "Bell Tower"),                  lambda state: state.has("Bell Tower Door Unlocked", world.player))
    add_rule(get_entrance("Tree", "Cabin Interior B"),                  lambda state: state.has("Cabin Door Unlocked", world.player))
    add_rule(get_entrance("Tree Sky", "Throne"),                        lambda state: state.has("Throne Door Unlocked", world.player))

    # Link doors (requires having been to both ends before being able to use)
    add_link_door_rule("Bell Tower", "Five Towers")
    add_link_door_rule("Industrial Hub", "Well 2")
    add_link_door_rule("Mausoleum", "Tree Roots")
    add_link_door_rule("Memory Core", "Pivot Watertower")
    add_link_door_rule("Nature Hub", "Two Walls")
    add_link_door_rule("Nu Zu Abandoned B", "Sewer to Lava")
    add_link_door_rule("Observatory", "Throne")
    add_link_door_rule("Purple Lodge Ruin", "Visitor")
    add_link_door_rule("Sewer Fork", "Sewer Hub")
    add_link_door_rule("Zu City Ruins", "Zu Library")

    # Cube count doors (requires having a specific number of either golden or anti cubes)
    add_rule(get_entrance("Villageville 3D",    "Big Tower"),       cube_count_rule(1))
    add_rule(get_entrance("Big Tower",          "Memory Core"),     cube_count_rule(2))
    add_rule(get_entrance("Memory Core",        "Wall Village"),    cube_count_rule(4))
    add_rule(get_entrance("Memory Core",        "Industrial City"), cube_count_rule(8))
    add_rule(get_entrance("Memory Core",        "Zu City"),         cube_count_rule(16))
    add_rule(get_entrance("Zu City",            "Stargate"),        cube_count_rule(32))
    add_rule(get_entrance("Water Pyramid",      "Temple of Love"),  cube_count_rule(64))

    # Water level logic (requires lowering the water level)
    # Use RuleBuilder to fix issues with indirect connections
    world.set_rule(get_entrance("Nature Hub", "Ritual"), CanReachRegion("Water Wheel"))
    world.set_rule(get_entrance("Waterfall", "Zu Zuish"), CanReachRegion("Water Wheel"))
    world.set_rule(get_entrance("_LighthouseLower", "Zu Fork"), CanReachRegion("Water Wheel"))
    world.set_rule(get_entrance("Water Tower", "Watertower Secret"), CanReachRegion("Water Wheel"))
    world.set_rule(get_entrance("Bell Tower", "Quantum"), CanReachRegion("Water Wheel"))

    # Owl logic
    add_rule(get_entrance("Owl", "Big Owl"), lambda state: state.has("Owl", world.player, 4))


def set_knowledge_rules(world: FezWorld) -> None:
    """Rules for knowledge logic"""
    # Helper functions
    get_location = functools.partial(_get_location, world)
    get_entrance = functools.partial(_get_entrance, world)
    map_rule = functools.partial(_map_rule, world)

    # Set rules associated with teromino sequences
    set_tetromino_rules(world, 'knowledge')

    # Zu numerals logic
    add_rule(get_location("Bell Tower Anti-Cube"), _number_rule(world))

    # Zu alphabet logic
    add_rule(get_location("Security Question Heart Cube"), _alphabet_rule(world))

    # Treasure map logic
    add_rule(get_location("Arch Chest 2"), map_rule("Arch Map"))
    add_rule(get_location("Tree Sky Chest"), map_rule("Tree Sky Map"))
    add_rule(get_location("Pivot Watertower Chest"), map_rule("Pivot Map"))

    # Crypt map logic
    add_rule(get_entrance("Crypt", "Tree of Death"),
             lambda state: (map_rule("Crypt Map A")(state) and
                            map_rule("Crypt Map B")(state) and
                            map_rule("Crypt Map C")(state) and
                            map_rule("Crypt Map D")(state) and
                            _number_rule(world)(state)))

    # Throne anti-cube logic
    add_rule(get_location("Throne Anti-Cube"), functools.partial(_throne_cube_rule, world))


def set_tetromino_rules(world: FezWorld, variant: str):
    """Rules for tetromino codes logic"""
    # Helper functions
    get_location = functools.partial(_get_location, world)
    get_entrance = functools.partial(_get_entrance, world)
    tetromino_rule = _tetromino_rule(world, variant)
    first_person_rule = _first_person_rule(world, variant)

    # Tetromino logic
    add_rule(get_location("Zu Code Loop Anti-Cube"), tetromino_rule)
    add_rule(get_location("Code Machine Anti-Cube"), tetromino_rule)
    add_rule(get_location("Boileroom Anti-Cube"), tetromino_rule)
    add_rule(get_location("Nu Zu School Anti-Cube"), tetromino_rule)
    add_rule(get_location("Telescope Anti-Cube"), tetromino_rule)
    add_rule(get_entrance("Waterfall", "CMY"), tetromino_rule)
    add_rule(get_entrance("Waterfall", "Water Wheel"), tetromino_rule)
    add_rule(get_entrance("Sewer to Lava", "Lava"), tetromino_rule)

    # First-person logic
    add_rule(get_location("Lighthouse Floor Anti-Cube"), first_person_rule)
    add_rule(get_location("Tree Cabin Floor Anti-Cube"), first_person_rule)
    add_rule(get_location("Tree Sky Floor Anti-Cube"), first_person_rule)
    add_rule(get_location("Zu Bridge Floor Anti-Cube"), first_person_rule)

    # Watertower secret logic
    add_rule(get_location("Watertower Secret Anti-Cube"),
             lambda state: (_map_rule(world, "QR Code Map")(state) or tetromino_rule(state)))

    # Black monolith logic
    add_rule(get_location("Black Monolith Heart Cube"),
             lambda state: (_map_rule(world, "Ritual Map")(state) and
                            first_person_rule(state) and
                            state.has("The Skull Artifact", world.player)))
