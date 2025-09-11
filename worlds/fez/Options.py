from dataclasses import dataclass

from Options import Choice, DeathLinkMixin, PerGameCommonOptions, Toggle


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
    display_name = "Disable visual pain"


# TODO: Implement this at some point
# class EntranceRandomizer(Toggle):
#     """Randomizes which location a door or warp will lead to."""
#     display_name = "Entrance randomizer"


@dataclass
class FezOptions(DeathLinkMixin, PerGameCommonOptions):
    goal: Goal
    disable_visual_pain: DisableVisualPain
    # entrance_randomizer: EntranceRandomizer
