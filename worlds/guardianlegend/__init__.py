from typing import List

from BaseClasses import Region, Tutorial
from worlds.AutoWorld import WebWorld, World
from Utils import visualize_regions
from .Items import TGLItem, TGLItemData, item_table, event_item_table
from .Locations import TGLLocation, location_table, event_location_table
from .Options import TGLOptions
from .Regions import create_regions
from .Rules import set_rules
from .Rom import TGLDeltaPatch, generate_output
from .Client import TGLClient


class TGLWebWorld(WebWorld):
    theme = "grass"
    tutorials = [
        Tutorial(
            tutorial_name="Start Guide",
            description="A guide to playing The Guardian Legend (NES).",
            language="English",
            file_name="guide_en.md",
            link="guide/en",
            authors=["CoreZero"]
        )
    ]


class TGLWorld(World):
    """THE GUARDIAN LEGEND (NES 1988, Irem/Compile)"""

    game = "The Guardian Legend"
    #data_version = 3
    web = TGLWebWorld()
    options_dataclass = TGLOptions
    options: TGLOptions
    topology_present = True # show path to required location checks in spoiler
    
    location_name_to_id = {name: data.code for name, data in location_table.items()}
    item_name_to_id = {name: data.code for name, data in item_table.items()}

    def create_item(self, name: str) -> TGLItem:
        data = item_table[name]
        return TGLItem(name, data.classification, data.code, self.player)
    
    def create_event(self, name: str) -> TGLItem:
        data = event_item_table[name]
        return TGLItem(name, data.classification, data.code, self.player)

    def create_regions(self):
        create_regions(self.multiworld, self.player)
        self._place_events()
        # REMOVE visualizer for PR/dist
        # visualize_regions(self.multiworld.get_region("Menu", self.player), "TGLRegions.puml")

    def _place_events(self):
        # Place "Corridor" items on "Corridor" event locations for Victory condition
        for locname, locdata in event_location_table.items():
            self.multiworld.get_location(locname, self.player).place_locked_item( 
                self.create_event(locname + " Cleared"))

    def set_rules(self):
        set_rules(self.multiworld, self.player, self.options.item_gating.value)

    def get_filler_item_name(self) -> str:
        return "Enemy Eraser"

    # If I've counted right, we shouldn't need any filler at all (for now)
    def create_items(self) -> None:
        item_pool: List[TGLItem] = []
        for name, data in item_table.items():
            quantity = data.max_quantity
            item_pool += [self.create_item(name) for _ in range(0, quantity)]

        self.multiworld.itempool += item_pool

    def generate_output(self, output_directory: str) -> None:
        generate_output(self.multiworld, self.player, output_directory, self.options)
    