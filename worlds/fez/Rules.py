from typing import TYPE_CHECKING

from ..generic.Rules import CollectionRule, set_rule

if TYPE_CHECKING:
    from . import FezWorld
else:
    FezWorld = object


def set_all_rules(world: FezWorld) -> None:
    get_location = lambda name: world.multiworld.get_location(name, world.player)
    get_entrance = lambda start, end: world.multiworld.get_entrance(f"{start} -> {end}", world.player)

    def set_link_door_rule(region1: str, region2: str):
        rule: CollectionRule = lambda state: state.can_reach_region(region1, world.player) and state.can_reach_region(region2, world.player)
        set_rule(get_entrance(region1, region2), rule)
        set_rule(get_entrance(region2, region1), rule)

    # Key doors (requires a specific key to open, unique behaviour to AP)
    set_rule(get_entrance("Villageville 3D", "Boileroom"),  lambda state: state.has("Boileroom Unlocked", world.player))
    # TODO: Add the other 7

    # Link doors (requires having been to both ends before being able to use)
    set_link_door_rule("Memory Core", "Pivot Watertower")
    # TODO: Add the others

    # Cube count doors (requires having a specific number of either golden or anti cubes)
    set_rule(get_entrance("Villageville 3D",    "Big Tower"),       lambda state: state.has_from_list(["Golden Cube", "Anti-Cube"], world.player, 1))
    set_rule(get_entrance("Big Tower",          "Memory Core"),     lambda state: state.has_from_list(["Golden Cube", "Anti-Cube"], world.player, 2))
    set_rule(get_entrance("Memory Core",        "Wall Village"),    lambda state: state.has_from_list(["Golden Cube", "Anti-Cube"], world.player, 4))
    set_rule(get_entrance("Memory Core",        "Industrial City"), lambda state: state.has_from_list(["Golden Cube", "Anti-Cube"], world.player, 8))
    set_rule(get_entrance("Memory Core",        "Zu City"),         lambda state: state.has_from_list(["Golden Cube", "Anti-Cube"], world.player, 16))
    set_rule(get_entrance("Memory Core",        "Stargate"),        lambda state: state.has_from_list(["Golden Cube", "Anti-Cube"], world.player, 32))
    set_rule(get_entrance("Water Pyramid",      "Temple of Love"),  lambda state: state.has_from_list(["Golden Cube", "Anti-Cube"], world.player, 64))

    # Misc rules
    set_rule(get_location("Big Owl Anti-Cube"), lambda state: state.has("Owl", world.player, 4))
