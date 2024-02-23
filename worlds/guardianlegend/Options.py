from dataclasses import dataclass

from Options import DefaultOnToggle, Toggle, Choice, DeathLink, PerGameCommonOptions

class BalancedRapidFire(DefaultOnToggle):
    """Makes the upgrade power of Rapid Fire more evenly distributed, and gives a slightly faster starting speed.
    
    On: 10/8/6/4/2/1 frames per shot.
    Off: 12/5/4/3/2/1 frames per shot (vanilla behavior)."""
    display_name = "Balanced Rapid Fire"

'''
class ItemDistribution(Choice):
    """Determines how many copies of items and upgrades exist in the item pool. Note vanilla maximums still apply, the extra copies only make it more likely to max out earlier.
    Filler is split between Blue Landers and Enemy Erasers, for excess slots.

    Vanilla: Uses the vanilla item distribution, where possible. Some items have extra copies, some don't.
    Extra: One or two extra copies of all items are added to the pool.
    Exact: Only the exact number of items to max out stats and subweapons is provided.
    Reduced: Hard mode, for experts! Reduced maximum for stats and subweapons."""
    display_name = "Item Distribution"
    option_vanilla = 0
    option_exact = 1
    option_reduced = 2
    option_extra = 3
    default = 3
'''

class ItemGating(Choice):
    """Determines how many stat ups and Landers are checked for before putting later Areas in logic. Higher settings will be easier but more linear.

    Low: 6 stat points, 7 Landers
    Normal: 8 stat points, 10 Landers
    High: 10 stat points, 14 Landers"""
    display_name = "Area Gating Strength"
    option_low = 0
    option_normal = 1
    option_high = 2
    default = 1

'''
class LimitedSubweapons(Toggle):
    """An extra challenge! A random set of subweapons will be excluded from the pool entirely."""
    pass
'''

@dataclass
class TGLOptions(PerGameCommonOptions):
    balanced_rapid_fire: BalancedRapidFire
    item_gating: ItemGating
    #death_link: DeathLink