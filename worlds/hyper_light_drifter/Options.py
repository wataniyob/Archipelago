from dataclasses import dataclass
from typing import Any, Dict, List

from Options import DeathLinkMixin, OptionCounter, OptionGroup, PerGameCommonOptions, Range
from .Items import trap_items


class TrapPercentage(Range):
    """Replaces filler items with traps, at the specified rate."""
    display_name = "Trap Percentage"
    range_start = 0
    range_end = 100
    default = 50


class TrapWeights(OptionCounter):
    """Specify the weights determining how many of each trap item will be in your itempool.

    If you don't want a specific type of trap, you can set the weight for it to 0.
    """
    display_name = "Trap Weights"
    min = 0
    valid_keys = [trap.name for trap in trap_items]
    default = {trap.name: 1 for trap in trap_items}


@dataclass
class HldOptions(DeathLinkMixin, PerGameCommonOptions):
    trap_percentage: TrapPercentage
    trap_weights: TrapWeights


hld_option_groups: List[OptionGroup] = [
    OptionGroup("Filler Items", [
        TrapPercentage,
        TrapWeights
    ]),
]


hld_option_presets: Dict[str, Dict[str, Any]] = {
    "Sync": {
    },
    "Awful": {
        "trap_percentage": 100,
        "death_link": True,
    },
}
