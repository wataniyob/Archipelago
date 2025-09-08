from typing import Any, Dict
from .Options import FezOptions
from .Items import FezItem, all_items, item_names, item_name_groups, filler_items
from .Locations import location_names, location_name_groups
from .Rules import FezRules
from worlds.AutoWorld import WebWorld, World
from BaseClasses import Item, Tutorial


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
    options_dataclass = FezOptions
    options: FezOptions # pyright: ignore[reportIncompatibleVariableOverride]
    topology_present = True  # show path to required location checks in spoiler

    origin_region_name = "Villageville"

    all_items = all_items
    item_names = item_names
    item_name_groups = item_name_groups

    location_names = location_names
    location_name_groups = location_name_groups

    def generate_early(self) -> None:
        # TODO: Handle shuffle options
        pass

    def get_filler_item_name(self) -> str:
        return self.random.choice(filler_items)["name"]

    def create_item(self, name: str) -> Item:
        item_id = self.item_name_to_id[name]
        item_data = self.all_items[item_id]
        return FezItem(name, item_data["classification"], item_id, self.player)

    def create_items(self) -> None:
        # TODO: Handle shuffle options and other stuff
        pass

    def set_rules(self) -> None:
        FezRules(self).set_all_rules()

    def fill_slot_data(self) -> Dict[str, Any]:
        return self.options.as_dict()
