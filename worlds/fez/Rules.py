import functools, dataclasses
from typing import TYPE_CHECKING, Tuple

from typing_extensions import override

from .Items import FezItem
from .Locations import FezLocation

from BaseClasses import Entrance, ItemClassification, Location, Region, CollectionState
from NetUtils import JSONMessagePart

from rule_builder.rules import CanReachRegion, Has, HasAll, Rule
from rule_builder.field_resolvers import FieldResolver, resolve_field

if TYPE_CHECKING:
    from . import FezWorld
else:
    FezWorld = object


########################################
# General Rules
########################################

def _get_location(world: FezWorld, name:str) -> Location:
    return world.multiworld.get_location(name, world.player)


def _get_entrance(world: FezWorld, start: str, end: str) -> Entrance:
    return world.multiworld.get_entrance(f"{start} -> {end}", world.player)


def _add_link_door_rule(world: FezWorld, region1: str, region2: str):
    rule = (CanReachRegion(region1) & CanReachRegion(region2))
    world.set_rule(_get_entrance(world, region1, region2), rule)
    world.set_rule(_get_entrance(world, region2, region1), rule)


@dataclasses.dataclass()
class HasMinCubeCount(Rule["FezWorld"], game="Fez"):
    count: int | FieldResolver
    """The minimum cube count the player is required to have"""
    
    @override
    def _instantiate(self, world: "FezWorld") -> Rule.Resolved:
        return self.Resolved(
            resolve_field(self.count, world, int),
            player=world.player,
            caching_enabled=getattr(world, "rule_caching_enabled", False),
        )

    class Resolved(Rule.Resolved):
        count: int

        @override
        def _evaluate(self, state: CollectionState) -> bool:
            return (state.count("Golden Cube", self.player) + 
                    state.count("Anti-Cube", self.player) + 
                    (state.count("Cube Bit", self.player)//8) 
                    >= self.count)

        @override
        def item_dependencies(self) -> [str, set[int]]:
            return {"Golden Cube": set(), "Anti-Cube": set(), "Cube Bit": set()}

        @override
        def explain_json(self, state: CollectionState | None = None) -> list[JSONMessagePart]:
            verb = "Missing " if state and not self(state) else "Has "
            messages: list[JSONMessagePart] = [{"type": "text", "text": verb}]
            if self.count > 1:
                messages.append({"type": "color", "color": "cyan", "text": str(self.count)})
                messages.append({"type": "text", "text": "x "})
            if state:
                color = "green" if self(state) else "salmon"
                messages.append({"type": "color", "color": color, "text": "Cubes"})
            else:
                messages.append({"type": "item_name", "flags": 0b001, "text": "Cubes", "player": self.player})
            return messages

        @override
        def explain_str(self, state: CollectionState | None = None) -> str:
            if state is None:
                return str(self)
            prefix = "Has" if self(state) else "Missing"
            count = f"{self.count}x " if self.count > 1 else ""
            item_name = "Cubes"
            return f"{prefix} {count}{item_name}"

        @override
        def __str__(self) -> str:
            count = f"{self.count}x " if self.count > 1 else ""
            item_name = "Cubes"
            return f"Has {count}{item_name}"


number_rule = CanReachRegion("Oldschool")


alphabet_rule = CanReachRegion("Fox")


def _tetromino_rule(variant: str) -> Rule:
    if variant == 'knowledge':
        return (CanReachRegion("Code Machine") & CanReachRegion("Nu Zu School") & CanReachRegion("Oldschool"))
    if variant == 'scramble':
        return CanReachRegion("Code Machine")
    raise ValueError(f"Invalid variant '{variant}'")


def _first_person_rule(variant: str) -> Rule:
    if variant == 'knowledge':
        return (Has("Sunglasses") & _tetromino_rule(variant))
    if variant == 'scramble':
        return _tetromino_rule(variant)
    raise ValueError(f"Invalid variant '{variant}'")


########################################
# Specific Rules
########################################

def set_rules(world: FezWorld) -> None:
    """Rules that are always present"""
    # Helper functions
    get_entrance = functools.partial(_get_entrance, world)
    add_link_door_rule = functools.partial(_add_link_door_rule, world)

    # Key doors (requires a specific key to open, unique behaviour to AP)
    world.set_rule(get_entrance("Villageville 3D", "Boileroom"),            Has("Boileroom Door Unlocked"))
    world.set_rule(get_entrance("_LighthouseLower", "Lighthouse House A"),  Has("Lighthouse Door Unlocked"))
    world.set_rule(get_entrance("Tree", "Tree Crumble"),                    Has("Tree Door Unlocked"))
    world.set_rule(get_entrance("Rails", "Well 2"),                         Has("Well Door Unlocked"))
    world.set_rule(get_entrance("Pivot 1", "Windmill Interior"),            Has("Windmill Door Unlocked"))
    world.set_rule(get_entrance("Mausoleum", "Crypt"),                      Has("Mausoleum Door Unlocked"))
    world.set_rule(get_entrance("Sewer Hub", "Sewer QR"),                   Has("Sewer Hub Door Unlocked"))
    world.set_rule(get_entrance("Sewer Pillars", "Sewer Fork"),             Has("Sewer Pillars Door Unlocked"))
    # Custom locked doors to balance sphere sizes
    world.set_rule(get_entrance("Nature Hub", "Arch"),                      Has("Arch Door Unlocked"))
    world.set_rule(get_entrance("Nature Hub", "Bell Tower"),                Has("Bell Tower Door Unlocked"))
    world.set_rule(get_entrance("Tree", "Cabin Interior B"),                Has("Cabin Door Unlocked"))
    world.set_rule(get_entrance("Tree Sky", "Throne"),                      Has("Throne Door Unlocked"))

    # Link doors (requires having been to both ends before being able to use)
    add_link_door_rule("Bell Tower", "Five Towers")
    add_link_door_rule("Industrial Hub", "Well 2")
    add_link_door_rule("Mausoleum", "Tree Roots")
    add_link_door_rule("Memory Core", "Pivot Watertower")
    add_link_door_rule("Nature Hub", "Two Walls")
    add_link_door_rule("Nu Zu Abandoned B", "Sewer to Lava")
    add_link_door_rule("Observatory", "Throne")
    add_link_door_rule("Purple Lodge Ruin", "Visitor")
    add_link_door_rule("Sewer Fork", "Sewer Hub")
    add_link_door_rule("Zu City Ruins", "Zu Library")

    # Cube count doors (requires having a specific number of either golden or anti cubes)
    world.set_rule(get_entrance("Villageville 3D",    "Big Tower"),       HasMinCubeCount(1))
    world.set_rule(get_entrance("Big Tower",          "Memory Core"),     HasMinCubeCount(2))
    world.set_rule(get_entrance("Memory Core",        "Wall Village"),    HasMinCubeCount(4))
    world.set_rule(get_entrance("Memory Core",        "Industrial City"), HasMinCubeCount(8))
    world.set_rule(get_entrance("Memory Core",        "Zu City"),         HasMinCubeCount(16))
    world.set_rule(get_entrance("Zu City",            "Stargate"),        HasMinCubeCount(32))
    world.set_rule(get_entrance("Water Pyramid",      "Temple of Love"),  HasMinCubeCount(64))

    # Water level logic (requires lowering the water level)
    # Use RuleBuilder to fix issues with indirect connections
    world.set_rule(get_entrance("Nature Hub", "Ritual"),              CanReachRegion("Water Wheel"))
    world.set_rule(get_entrance("Waterfall", "Zu Zuish"),             CanReachRegion("Water Wheel"))
    world.set_rule(get_entrance("_LighthouseLower", "Zu Fork"),       CanReachRegion("Water Wheel"))
    world.set_rule(get_entrance("Water Tower", "Watertower Secret"),  CanReachRegion("Water Wheel"))
    world.set_rule(get_entrance("Bell Tower", "Quantum"),             CanReachRegion("Water Wheel"))

    # Owl logic
    world.set_rule(get_entrance("Owl", "Big Owl"), HasAll("Owl"))


def set_knowledge_rules(world: FezWorld) -> None:
    """Rules for knowledge logic"""
    # Helper functions
    get_location = functools.partial(_get_location, world)
    get_entrance = functools.partial(_get_entrance, world)

    # Set rules associated with teromino sequences
    set_tetromino_rules(world, 'knowledge')

    # Zu numerals logic
    world.set_rule(get_location("Bell Tower Anti-Cube"), number_rule)

    # Zu alphabet logic
    world.set_rule(get_location("Security Question Heart Cube"), alphabet_rule)

    # Treasure map logic
    world.set_rule(get_location("Arch Chest 2"),           Has("Arch Map"))
    world.set_rule(get_location("Tree Sky Chest"),         Has("Tree Sky Map"))
    world.set_rule(get_location("Pivot Watertower Chest"), Has("Pivot Map"))

    # Crypt map logic
    world.set_rule(get_entrance("Crypt", "Tree of Death"),
                           (Has("Crypt Map A") &
                            Has("Crypt Map B") &
                            Has("Crypt Map C") &
                            Has("Crypt Map D") &
                            number_rule))

    # Throne anti-cube logic
    world.set_rule(get_location("Throne Anti-Cube"), (CanReachRegion("Sewer QR") |
                                                      (Has("Sunglasses") &
                                                       CanReachRegion("Zu House Empty") &
                                                       CanReachRegion("Zu Throne Ruins"))))


def set_tetromino_rules(world: FezWorld, variant: str):
    """Rules for tetromino codes logic"""
    # Helper functions
    get_location = functools.partial(_get_location, world)
    get_entrance = functools.partial(_get_entrance, world)
    tetromino_rule = _tetromino_rule(variant)
    first_person_rule = _first_person_rule(variant)

    # Tetromino logic
    world.set_rule(get_location("Achievement Anti-Cube"), tetromino_rule)
    world.set_rule(get_location("Zu Code Loop Anti-Cube"), tetromino_rule)
    world.set_rule(get_location("Code Machine Anti-Cube"), tetromino_rule)
    world.set_rule(get_location("Boileroom Anti-Cube"), tetromino_rule)
    world.set_rule(get_location("Nu Zu School Anti-Cube"), tetromino_rule)
    world.set_rule(get_location("Telescope Anti-Cube"), tetromino_rule)
    world.set_rule(get_entrance("Waterfall", "CMY"), tetromino_rule)
    world.set_rule(get_entrance("Waterfall", "Water Wheel"), tetromino_rule)
    world.set_rule(get_entrance("Sewer to Lava", "Lava"), tetromino_rule)

    # First-person logic
    world.set_rule(get_location("Lighthouse Floor Anti-Cube"), first_person_rule)
    world.set_rule(get_location("Tree Cabin Floor Anti-Cube"), first_person_rule)
    world.set_rule(get_location("Tree Sky Floor Anti-Cube"), first_person_rule)
    world.set_rule(get_location("Zu Bridge Floor Anti-Cube"), first_person_rule)

    # Watertower secret logic
    world.set_rule(get_location("Watertower Secret Anti-Cube"), (Has("QR Code Map") | tetromino_rule))

    # Black monolith logic
    world.set_rule(get_location("Black Monolith Heart Cube"), (Has("Ritual Map") &
                                                               first_person_rule &
                                                               Has("The Skull Artifact")))
