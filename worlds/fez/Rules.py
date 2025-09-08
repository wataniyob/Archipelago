from typing import Dict, Callable
from BaseClasses import CollectionState
from . import FezWorld


class FezRules:
    player: int
    world: FezWorld
    location_rules: Dict[str, Callable[[CollectionState], bool]]
    region_rules: Dict[str, Callable[[CollectionState], bool]]

    def __init__(self, world: FezWorld) -> None:
        self.player = world.player
        self.world = world
        # TODO: Populate location and region rules

    def set_all_rules(self) -> None:
        multiworld = self.world.multiworld
        # TODO: Fill out
