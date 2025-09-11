from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import FezWorld
else:
    FezWorld = object


def set_all_rules(fez_world: FezWorld) -> None:
    multiworld = fez_world.multiworld
    # TODO: Fill out
