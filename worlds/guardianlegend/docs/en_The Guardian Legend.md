# The Guardian Legend (NES)

## Summary

A hybrid top-down exploration-adventure game like The Legend of Zelda, with scrolling shoot-em-up segments.

Developed by Compile, published by Irem/Broderbund in 1988.

## Where is the settings page?

The [player settings page for this game](../player-settings) contains all the options you need to configure and
export a config file.

## What items and locations get shuffled?

All locations with one-time-only items are shuffled. More formally:

- All subweapons and upgrades, including Enemy Erasers
- Red Landers (ammo) and Blue Landers (health)
- Stat upgrades for attack power, defense power, and firing speed
- Keys for accessing later Areas

## What does another world's item look like in The Legend of Zelda?

Items from other games will look like a Red Chip. Note that only static items (item boxes in rooms, and miniboss drops)
are shuffled. Enemies will still drop the regular Red Chip items and these are not part of Archipelago.

Items from TGL will look as usual, except for keys, which due to sprite limitations will also look like Red Chips as if
belonging to a different world.

## Are there any other changes made?

- Corridors no longer grant keys, but only the item in the room after clearing.
- Shops that have 3 items will always show one "good" item and 2 Blue Chips. Because of how shops work in TGL,
  Archipelago will always ensure the unique item is considered checked.
