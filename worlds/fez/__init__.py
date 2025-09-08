from typing import Any, Dict
from .Options import FezOptions
from .Items import FezItem, all_fez_item_data, base_id, item_names, item_name_groups, filler_items
from .Locations import location_names, location_name_groups
from .Rules import FezRules
from worlds.AutoWorld import WebWorld, World
from BaseClasses import Item, Tutorial


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

    all_item_data = all_fez_item_data
    item_name_to_id = {item.name: i + base_id for i, item in enumerate(all_item_data)}
    item_names = item_names
    item_name_groups = item_name_groups

    location_name_to_id = {location: i + base_id for i, location in enumerate(location_names)}
    location_names = location_names
    location_name_groups = location_name_groups

    def generate_early(self) -> None:
        # Filter out things from options
        if not self.options.shuffle_keys:
            self.all_item_data = [item for item in self.all_item_data
                              if item.name is not "Key"]
        if not self.options.shuffle_owls:
            self.all_item_data = [item for item in self.all_item_data
                              if item.name is not "Owl"]
        if not self.options.shuffle_clock_tower:
            item_id = self.item_name_to_id["Anti-Cube"]
            self.all_item_data[item_id].count -= 4
        pass

    def get_filler_item_name(self) -> str:
        return self.random.choice(filler_items).name

    def create_item(self, name: str) -> Item:
        item_id = self.item_name_to_id[name]
        item_data = self.all_item_data[item_id]
        return FezItem(name, item_data.classification, item_id, self.player)

    def create_items(self) -> None:
        # TODO: Figure out how to manage traps and filler properly

        self.all_item_data = [item for item in self.all_item_data
                              if item not in filler_items]

        for item in self.all_item_data:
            for _ in range(item.count):
                new_item = self.create_item(item.name)
                self.multiworld.itempool.append(new_item)

    def set_rules(self) -> None:
        FezRules(self).set_all_rules()

    def fill_slot_data(self) -> Dict[str, Any]:
        return self.options.as_dict(
            "death_link",
            "goal",
            "shuffle_keys",
            "shuffle_owls",
            "shuffle_clock_tower",
            "disable_visual_pain"
        )
