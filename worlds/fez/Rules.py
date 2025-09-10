from ..generic.Rules import set_rule
from typing import Dict, Callable
from BaseClasses import CollectionState
from . import FezWorld


class FezRules:
    player: int
    world: FezWorld
    location_rules: Dict[str, Callable[[CollectionState], bool]]
    region_rules: Dict[str, Callable[[CollectionState], bool]]

#syntax: set_rule(multiworld.get_location("[Location]", player),
#                lambda state: state.can_reach("[Region]", "Region", player) or state.can_reach("[Item]", player number))
    
    def __init__(self, world: FezWorld) -> None:
        self.player = world.player
        self.world = world
        # TODO: Populate location and region rules

    def set_all_rules(self) -> None:
        multiworld = self.world.multiworld
        # TODO: Fill out
