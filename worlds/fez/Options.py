from collections import Counter
from dataclasses import dataclass

from Options import Choice, DeathLinkMixin, OptionCounter, PerGameCommonOptions, Range, Toggle
from .Items import trap_items


class Goal(Choice):
    """Defines the goal to accomplish in order to complete the randomizer.

    - 32 Cubes: Complete 32 cube ending

    - 64 Cubes: Complete 64 cube ending
    """
    display_name = "Goal"
    option_32_cubes = 0
    option_64_cubes = 1
    default = 0

class DisableVisualPain(Toggle):
    """Disables effects that are make eyes not happy like (quantum room and lightning)"""
    display_name = "Disable Visual Pain"

class ShuffleClockAntis(Toggle):
    """Whether to shuffle the anti-cubes from the clock tower (avoids having to change system time)."""
    display_name = "Shuffle Clock Antis"

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
    default = {name: 1 for name in valid_keys}


@dataclass
class FezOptions(DeathLinkMixin, PerGameCommonOptions):
    goal: Goal
    disable_visual_pain: DisableVisualPain
    shuffle_clock_antis: ShuffleClockAntis
    trap_percentage: TrapPercentage
    trap_weights: TrapWeights
