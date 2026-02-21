from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import HldWorld
else:
    HldWorld = object


def set_rules(world: HldWorld) -> None:
    """Rules that are always present"""
    # TODO: Add any rules
