from dataclasses import dataclass

from Options import Choice, DefaultOnToggle, DeathLinkMixin, PerGameCommonOptions, Toggle


class Goal(Choice):
    """Defines the goal to accomplish in order to complete the randomizer.

    - 32 Cubes: Complete 32 cube ending

    - 64 Cubes: Complete 64 cube ending
    """
    display_name = "Goal"
    option_32_cubes = 0
    option_64_cubes = 1
    default = 0


class ShuffleKeys(DefaultOnToggle):
    """Shuffle keys into the item pool."""
    display_name = "Shuffle keys"


class ShuffleOwls(DefaultOnToggle):
    """Shuffle owls into the item pool (for the owl anti-cube)."""
    display_name = "Shuffle owls"


class ShuffleClockTower(Toggle):
    """Shuffle the clock tower anti-cubes (you are given them at the start if false)"""
    display_name = "Shuffle clock tower"


class DisableVisualPain(Toggle):
    """Disables effects that are make eyes not happy like (quantum room and lightning)"""
    display_name = "Disable visual pain"


# TODO: Implement this at some point
# class EntranceRandomizer(Toggle):
#     """Randomizes which location a door or warp will lead to."""
#     display_name = "Entrance randomizer"


@dataclass
class FezOptions(DeathLinkMixin, PerGameCommonOptions): # pyright: ignore[reportGeneralTypeIssues]
    goal = Goal
    shuffle_keys = ShuffleKeys
    shuffle_owls = ShuffleOwls
    shuffle_clock_tower = ShuffleClockTower
    disable_visual_pain = DisableVisualPain
    # entrance_randomizer = EntranceRandomizer
