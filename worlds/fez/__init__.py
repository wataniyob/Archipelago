from typing import Any, Dict
from .Options import FezOptions
from .Items import FezItem, main_items, item_name_groups, trap_items, filler_items
from .Locations import location_names, location_name_groups
from .Rules import set_all_rules
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
    options: FezOptions
    topology_present = True  # show path to required location checks in spoiler

    # First item and location ID
    base_id = 0xFE500

    all_item_data = main_items + trap_items + filler_items
    item_name_to_id = {item.name: id for id, item in enumerate(all_item_data, base_id)}
    item_name_groups = item_name_groups

    # TODO: Figure out why no items get listed in generation
    location_name_to_id = {name: id for id, name in enumerate(location_names, base_id)}
    location_name_groups = location_name_groups

    def get_filler_item_name(self) -> str:
        return self.random.choice(filler_items).name

    def create_item(self, name: str) -> Item:
        item_id = self.item_name_to_id[name]
        item_data = self.all_item_data[item_id - self.base_id]
        return FezItem(name, item_data.classification, item_id, self.player)

    def create_items(self) -> None:
        for item in main_items:
            for _ in range(item.count):
                new_item = self.create_item(item.name)
                self.multiworld.itempool.append(new_item)

        fill_size = len(self.location_name_to_id) - sum(item.count for item in main_items)
        for _ in range(fill_size):
            name = self.random.choice(["Rotation Trap", "Sleep Trap", "Emotional Support"])
            self.multiworld.itempool.append(self.create_item(name))

    def set_rules(self) -> None:
        set_all_rules(self)

        # Uncomment to visualise world layout
        # from Utils import visualize_regions
        # visualize_regions(self.multiworld.get_region("Menu", self.player), "fez_chart.puml")

    def fill_slot_data(self) -> Dict[str, Any]:
        return self.options.as_dict(
            "death_link",
            "goal",
            "disable_visual_pain"
        )

