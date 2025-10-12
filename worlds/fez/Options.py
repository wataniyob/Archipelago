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
    """Disables effects that are make eyes not happy like (quantum room and lightning)

    NOTE: For the lightning levels, the invisible triles remain invisible due to a bug that crashes the game if rendering them.
          Hopefully this will be fixed for a future release.
    """
    display_name = "Disable Visual Pain"

class ShuffleClockAntis(Toggle):
    """Whether to add the anti-cubes from the clock tower to the location pool ('true' means you'll likely need to change system time or wait upto a month)."""
    display_name = "Shuffle Clock Antis"

class KnowledgeLogic(Toggle):
    """Whether to have knowledge sources required for logic (e.g. Counting Cube needed before Bell Tower Anti-Cube)"""
    display_name = "Knowledge Logic"

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
    default = {
        "Rotation Trap": 10,
        "Gravity Trap": 10,
        "Sleep Trap": 1,
    }


@dataclass
class FezOptions(DeathLinkMixin, PerGameCommonOptions):
    goal: Goal
    disable_visual_pain: DisableVisualPain
    shuffle_clock_antis: ShuffleClockAntis
    # TODO: Uncomment once fixed
    # knowledge_logic: KnowledgeLogic
    trap_percentage: TrapPercentage
    trap_weights: TrapWeights
