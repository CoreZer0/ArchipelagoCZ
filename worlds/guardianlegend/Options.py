from dataclasses import dataclass

from Options import Toggle, DeathLink, PerGameCommonOptions

# TODO: Everything.

'''
class HardMode(Toggle):
    """Does nothing...yet."""
    display_name = "Hard Mode"
'''

@dataclass
class TGLOptions(PerGameCommonOptions):
    #hard_mode: HardMode
    #death_link: DeathLink
    pass