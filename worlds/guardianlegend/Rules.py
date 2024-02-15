from BaseClasses import CollectionState, MultiWorld
from worlds.generic.Rules import add_rule

from .Items import red_lander_thresholds

# Currently this compares to a hardcoded list of Max chip values as in the vanilla game,
#  based on the current amount of Red Landers collected.
def get_chip_max(state: CollectionState, player: int) -> int:
    return red_lander_thresholds[state.count("Red Lander", player)]

def has_area_key(state: CollectionState, player: int, keyname: str) -> bool:
    return state.has(keyname, player)

def has_enough_defense(state: CollectionState, player: int, threshold: int) -> bool:
    return state.count("Defense Up", player) >= threshold

# All shops are named as 'A# <chip_cost> Chip Shop' so we can pull the second word out as an int
#  to see how much we need. 
def has_enough_chips(state: CollectionState, player: int, shopname: int) -> bool:
    shop_cost = int(shopname.split(' ')[1])
    return get_chip_max(state, player) >= shop_cost

def has_multibullets(state: CollectionState, player: int) -> bool:
    return state.count("Multibullets", player) >= 1

def has_final_boss_access(state: CollectionState, player: int) -> bool:
    all_cleared = True
    for i in range(1,11):
        all_cleared &= state.has("Corridor " + str(i) + " Cleared", player)
    return all_cleared

def set_rules(multiworld: MultiWorld, player: int):

    # Area 1-10 require a specific key, enforced by the game
    # For balancing, we require a certain number of Defense Up upgrades by certain areas, in-game Max is 6
    
    multiworld.get_entrance("Area 1", player).access_rule = \
        lambda state: has_area_key(state, player, "Crescent Key")
    
    multiworld.get_entrance("Area 2", player).access_rule = \
        lambda state: has_area_key(state, player, "Crescent Key") and has_enough_defense(state, player, 1)
    
    multiworld.get_entrance("Area 3", player).access_rule = \
        lambda state: has_area_key(state, player, "Hook Key") and has_enough_defense(state, player, 2)
    
    multiworld.get_entrance("Area 4", player).access_rule = \
        lambda state: has_area_key(state, player, "Wave Key") and has_enough_defense(state, player, 3)
    
    multiworld.get_entrance("Area 5", player).access_rule = \
        lambda state: has_area_key(state, player, "Square Key") and has_enough_defense(state, player, 3)
    
    multiworld.get_entrance("Area 6", player).access_rule = \
        lambda state: has_area_key(state, player, "Square Key") and has_enough_defense(state, player, 4)
    
    multiworld.get_entrance("Area 7", player).access_rule = \
        lambda state: has_area_key(state, player, "Cross Key") and has_enough_defense(state, player, 4)
    
    multiworld.get_entrance("Area 8", player).access_rule = \
        lambda state: has_area_key(state, player, "Cross Key") and has_enough_defense(state, player, 5)
    
    multiworld.get_entrance("Area 9", player).access_rule = \
        lambda state: has_area_key(state, player, "Triangle Key") and has_enough_defense(state, player, 6)
    
    multiworld.get_entrance("Area 10", player).access_rule = \
        lambda state: has_area_key(state, player, "Rectangle Key") and has_enough_defense(state, player, 6)
    
    '''
    # TEMP remove keys to generate local game
    multiworld.get_entrance("Area 2", player).access_rule = \
        lambda state:  has_enough_defense(state, player, 1)
    
    multiworld.get_entrance("Area 3", player).access_rule = \
        lambda state:  has_enough_defense(state, player, 2)
    
    multiworld.get_entrance("Area 4", player).access_rule = \
        lambda state:  has_enough_defense(state, player, 3)
    
    multiworld.get_entrance("Area 5", player).access_rule = \
        lambda state: has_enough_defense(state, player, 3)
    
    multiworld.get_entrance("Area 6", player).access_rule = \
        lambda state: has_enough_defense(state, player, 4)
    
    multiworld.get_entrance("Area 7", player).access_rule = \
        lambda state: has_enough_defense(state, player, 4)
    
    multiworld.get_entrance("Area 8", player).access_rule = \
        lambda state: has_enough_defense(state, player, 5)
    
    multiworld.get_entrance("Area 9", player).access_rule = \
        lambda state: has_enough_defense(state, player, 6)
    
    multiworld.get_entrance("Area 10", player).access_rule = \
        lambda state: has_enough_defense(state, player, 6)
    '''
    
    # Shops require Area access + enough Red Landers to afford the shop
    for shop_location in [location for location in multiworld.get_locations(player) if "Shop" in location.name]:
        add_rule(multiworld.get_location(shop_location.name, player), 
                 lambda state: has_enough_chips(state, player, shop_location.name))

    # Corridor 6 has a chip spending requirement
    # To get around checking ALL subweapons, we just check for one Multibullet.
    add_rule(multiworld.get_location("Corridor 6 (X16 Y11)", player), lambda state: has_multibullets(state, player))

    # Corridor 21 requires Corridor 1-10 Cleared
    multiworld.get_entrance("Corridor 21", player).access_rule = \
        lambda state: has_final_boss_access(state, player)

    # Victory
    multiworld.completion_condition[player] = lambda state: state.has("Corridor 21 Cleared", player)
