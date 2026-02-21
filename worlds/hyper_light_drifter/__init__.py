from typing import Any, Dict
from .Options import HldOptions, hld_option_groups, hld_option_presets
from .Items import HldItem, all_item_data, item_name_groups, filler_items, main_items
from .Locations import HldLocation, all_location_data, location_name_groups
from .Regions import all_region_data, region_name_to_location_name
from .Rules import set_rules
from worlds.AutoWorld import WebWorld, World
from BaseClasses import Item, Region, Tutorial


class HldWeb(WebWorld):
    guide_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Hyper Light Drifter Archipelago Multiworld",
        "English",
        "setup_en.md",
        "setup/en",
        ["NoliH"]
    )

    tutorials = [guide_en]

    bug_report_page = "https://github.com/nhyldmar/hld-ap/issues"

    options_presets = hld_option_presets
    option_groups = hld_option_groups


class HldWorld(World):
    """
    Explore a beautiful, vast and ruined world riddled with dangers and lost technologies.
    """
    game = "Hld"
    web = HldWeb()
    options_dataclass = HldOptions
    options: HldOptions # pyright: ignore[reportIncompatibleVariableOverride]
    topology_present = True  # show path to required location checks in spoiler

    origin_region_name = "Town"

    # First item and location ID
    base_id = 0xDA500

    item_name_to_id = {item.name: id for id, item in enumerate(all_item_data, base_id)}
    item_names = set(item_name_to_id)
    item_name_groups = item_name_groups

    location_name_to_id = {data.name: id for id, data in enumerate(all_location_data, base_id)}
    location_names = set(location_name_to_id)
    location_name_groups = location_name_groups

# start of ordered Main.py calls

    def create_regions(self) -> None:
        # Add all regions
        for data in all_region_data:
            region = Region(data.name, self.player, self.multiworld)
            self.multiworld.regions.append(region)

        # Configure all regions
        for data in all_region_data:
            region = self.multiworld.get_region(data.name, self.player)
            location_names = region_name_to_location_name[data.name]
            locations_in_region = {name: self.location_name_to_id.get(name)
                                   for name in location_names
                                   if name in location_names}
            region.add_locations(locations_in_region, HldLocation)
            region.add_exits(data.exits)

    def create_items(self) -> None:
        for item in main_items:
            # Add count of item to pool
            for _ in range(item.count):
                new_item = self.create_item(item.name)
                self.multiworld.itempool.append(new_item)

        # Add filler
        fill_size = len(self.location_name_to_id) - sum(item.count for item in main_items)
        self.add_filler_items(fill_size)

    def set_rules(self) -> None:
        set_rules(self)

    def fill_slot_data(self) -> Dict[str, Any]:
        return self.options.as_dict(
            "death_link",
            "goal",
        )

# end of ordered Main.py calls

    def create_item(self, name: str) -> Item:
        item_id = self.item_name_to_id[name]
        item_data = all_item_data[item_id - self.base_id]
        return HldItem(name, item_data.classification, item_id, self.player)

    def get_filler_item_name(self) -> str:
        return self.random.choice(filler_items).name

    def get_trap_item_name(self) -> str:
        return self.random.choices(list(self.options.trap_weights.keys()), list(self.options.trap_weights.values()))[0]

    def add_filler_items(self, fill_size: int) -> None:
        # Add traps
        trap_count = fill_size * self.options.trap_percentage // 100
        for _ in range(trap_count):
            filler_item = self.create_item(self.get_trap_item_name())
            self.multiworld.itempool.append(filler_item)

        # Add filler
        for _ in range(fill_size - trap_count):
            filler_item = self.create_item(self.get_filler_item_name())
            self.multiworld.itempool.append(filler_item)
