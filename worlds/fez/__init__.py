from .Options import FezOptions
from .Items import progression_items, skippable_items, filler_items
from .Locations import all_locations
from worlds.AutoWorld import WebWorld, World
from BaseClasses import Tutorial


base_id = 0xFE5  # TODO: Figure out if this value can't clash with other worlds


class FezWeb(WebWorld):
    guide_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Fez Archipelago Multiworld",
        "English",
        "setup_en.md",
        "setup/en",
        ["NoliH"]
    )

    tutorials = [guide_en]

    bug_report_page = "https://github.com/nhyldmar/fez-ap/issues"


class FezWorld(World):
    """
    Gomez is a 2D creature living in a 2D world. Or is he?
    When the existence of a mysterious 3rd dimension is revealed to him,
    Gomez is sent out on a journey that will take him to the very end of time and space.
    Use your ability to navigate 3D structures from 4 distinct classic 2D perspectives.
    """
    game = "Fez"
    web = FezWeb()
    options: FezOptions
    options_dataclass = FezOptions
    topology_present = True  # show path to required location checks in spoiler

    all_items = progression_items + skippable_items + filler_items
    item_name_to_id = {item["name"]: i + base_id for i, item in enumerate(all_items)}

    all_locations = all_locations
    location_name_to_id = {location: i + base_id for i, location in enumerate(all_locations)}

    def get_filler_item_name(self) -> str:
        return self.random.choice(filler_items)["name"]
