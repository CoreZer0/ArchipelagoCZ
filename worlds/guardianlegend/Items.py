from typing import Callable, Dict, NamedTuple, Optional

from BaseClasses import Item, ItemClassification, MultiWorld


class TGLItem(Item):
    game = "TGL"


class TGLItemData(NamedTuple):
    category: str
    code: Optional[int] = None
    classification: ItemClassification = ItemClassification.filler
    max_quantity: int = 1
    weight: int = 1

def get_items_by_category(category: str) -> Dict[str, TGLItemData]:
    item_dict: Dict[str, TGLItemData] = {}
    for name, data in item_table.items():
        if data.category == category:
            item_dict.setdefault(name, data)

    return item_dict

# ID code base 8471760000 = 'TGL' in ASCII decimal + 0000
TGL_ITEMID_BASE = 8471760000

# These values are the hard-coded chip count upgrade levels
# NOTE: If we decide to randomize/alter those thresholds this will have to be changed
red_lander_thresholds = [50,100,150,200,400,800,1200,1600,2400,4000,6000]

balanced_rapid_fire = [10,8,6,4,2,1]

item_table: Dict[str, TGLItemData] = {
    "Crescent Key":   TGLItemData("Keys", TGL_ITEMID_BASE+2000, ItemClassification.progression),
    "Hook Key":       TGLItemData("Keys", TGL_ITEMID_BASE+2001, ItemClassification.progression),
    "Wave Key":       TGLItemData("Keys", TGL_ITEMID_BASE+2002, ItemClassification.progression),
    "Square Key":     TGLItemData("Keys", TGL_ITEMID_BASE+2003, ItemClassification.progression),
    "Cross Key":      TGLItemData("Keys", TGL_ITEMID_BASE+2004, ItemClassification.progression),
    "Triangle Key":   TGLItemData("Keys", TGL_ITEMID_BASE+2005, ItemClassification.progression),
    "Rectangle Key":  TGLItemData("Keys", TGL_ITEMID_BASE+2006, ItemClassification.progression),

    # Subweapons - In-game itemID order, with offsets
    "Multibullets":   TGLItemData("Subweapons",  TGL_ITEMID_BASE+1000, ItemClassification.useful,  4),
    "Back Fire":      TGLItemData("Subweapons",  TGL_ITEMID_BASE+1001, ItemClassification.useful,  4),
    "Wave Attack":    TGLItemData("Subweapons",  TGL_ITEMID_BASE+1002, ItemClassification.useful,  4),
    "Bullet Shield":  TGLItemData("Subweapons",  TGL_ITEMID_BASE+1003, ItemClassification.useful,  4),
    "Grenade":        TGLItemData("Subweapons",  TGL_ITEMID_BASE+1004, ItemClassification.useful,  4),
    "Fireball":       TGLItemData("Subweapons",  TGL_ITEMID_BASE+1005, ItemClassification.useful,  4),
    "Area Blaster":   TGLItemData("Subweapons",  TGL_ITEMID_BASE+1006, ItemClassification.useful,  4),
    "Repeller":       TGLItemData("Subweapons",  TGL_ITEMID_BASE+1007, ItemClassification.useful,  4),
    "Hyper Laser":    TGLItemData("Subweapons",  TGL_ITEMID_BASE+1008, ItemClassification.useful,  4),
    "Saber Laser":    TGLItemData("Subweapons",  TGL_ITEMID_BASE+1009, ItemClassification.useful,  4),
    "Cutter Laser":   TGLItemData("Subweapons",  TGL_ITEMID_BASE+1010, ItemClassification.useful,  4),

    # Filler / Non-unique
    "Enemy Eraser":  TGLItemData("Filler",  TGL_ITEMID_BASE+1011, ItemClassification.filler,  9),
    "Energy Pack":   TGLItemData("Filler",  TGL_ITEMID_BASE+1012, ItemClassification.filler,  7),

    # Stats
    "Blue Lander":     TGLItemData("Stats",  TGL_ITEMID_BASE+1013, ItemClassification.progression, 10),
    "Attack Up":       TGLItemData("Stats",  TGL_ITEMID_BASE+1014, ItemClassification.progression, 4),
    "Defense Up":      TGLItemData("Stats",  TGL_ITEMID_BASE+1015, ItemClassification.progression, 9),
    "Rapid Fire Up":   TGLItemData("Stats",  TGL_ITEMID_BASE+1016, ItemClassification.progression, 6),
    "Red Lander":      TGLItemData("Stats",  TGL_ITEMID_BASE+1017, ItemClassification.progression, 10),

    # Drops - Not shuffled, here for reference
    #"Life Heart": TGLItemData("Filler",  TGL_ITEMID_BASE+1020, ItemClassification.filler),
    #"Red Chip":   TGLItemData("Filler",  TGL_ITEMID_BASE+1021, ItemClassification.filler),
    #"Blue Chip":  TGLItemData("Filler",  TGL_ITEMID_BASE+1022, ItemClassification.filler),

}

event_item_table: Dict[str, TGLItemData] = {
    "Corridor 1 Cleared":   TGLItemData("Event", classification=ItemClassification.progression),
    "Corridor 2 Cleared":   TGLItemData("Event", classification=ItemClassification.progression),
    "Corridor 3 Cleared":   TGLItemData("Event", classification=ItemClassification.progression),
    "Corridor 4 Cleared":   TGLItemData("Event", classification=ItemClassification.progression),
    "Corridor 5 Cleared":   TGLItemData("Event", classification=ItemClassification.progression),
    "Corridor 6 Cleared":   TGLItemData("Event", classification=ItemClassification.progression),
    "Corridor 7 Cleared":   TGLItemData("Event", classification=ItemClassification.progression),
    "Corridor 8 Cleared":   TGLItemData("Event", classification=ItemClassification.progression),
    "Corridor 9 Cleared":   TGLItemData("Event", classification=ItemClassification.progression),
    "Corridor 10 Cleared":  TGLItemData("Event", classification=ItemClassification.progression),
    "Corridor 21 Cleared":  TGLItemData("Event", classification=ItemClassification.progression),

}



