"""Chapter groups and the shared reward tables. Imported first."""
from ftbq import group, loot_table

group("start", "Start here")
group("tech", "Technology")
group("magic", "Magic")
group("world", "World and Exploration")
group("storage", "Storage and Tools")

# Loot crates. Weights are relative inside one table.
loot_table("common", "Common Crate", loot_size=1, entries=[
    ("minecraft:iron_ingot", 8, 10, 8),
    ("minecraft:copper_ingot", 12, 10, 12),
    ("minecraft:coal", 16, 10, 16),
    ("minecraft:gold_ingot", 4, 6, 4),
    ("minecraft:bread", 8, 8),
    ("minecraft:oak_log", 16, 8, 16),
    ("minecraft:leather", 6, 5),
    ("minecraft:redstone", 8, 6, 8),
    ("minecraft:lapis_lazuli", 6, 5),
    ("minecraft:ender_pearl", 2, 3),
    ("waystones:warp_stone", 1, 2),
    ("create:andesite_alloy", 8, 6, 8),
    ("ars_nouveau:source_gem", 4, 6, 4),
])

loot_table("uncommon", "Uncommon Crate", loot_size=1, entries=[
    ("minecraft:iron_block", 2, 10, 2),
    ("minecraft:gold_ingot", 8, 8, 8),
    ("minecraft:diamond", 2, 6, 2),
    ("minecraft:emerald", 4, 6, 4),
    ("minecraft:experience_bottle", 8, 8, 8),
    ("minecraft:enchanted_golden_apple", 1, 1),
    ("create:brass_ingot", 6, 6, 6),
    ("create:precision_mechanism", 2, 4),
    ("mekanism:ingot_steel", 8, 6, 8),
    ("ars_nouveau:source_gem_block", 2, 5),
    ("sophisticatedbackpacks:backpack", 1, 3),
    ("waystones:waystone", 1, 4),
    ("minecraft:netherite_scrap", 1, 2),
])

loot_table("rare", "Rare Crate", loot_size=1, entries=[
    ("minecraft:diamond_block", 1, 8),
    ("minecraft:netherite_ingot", 1, 5),
    ("minecraft:totem_of_undying", 1, 3),
    ("minecraft:elytra", 1, 1),
    ("create:electron_tube", 8, 6, 8),
    ("mekanism:alloy_reinforced", 4, 6, 4),
    ("ae2:certus_quartz_crystal", 32, 6, 32),
    ("ars_nouveau:wilden_tribute", 1, 4),
    ("sophisticatedbackpacks:iron_backpack", 1, 4),
    ("artifacts:mimic_spawn_egg", 1, 2),
    ("tempad:tempad", 1, 1),
])

loot_table("epic", "Epic Crate", loot_size=1, entries=[
    ("minecraft:netherite_block", 1, 4),
    ("minecraft:nether_star", 1, 4),
    ("minecraft:enchanted_golden_apple", 4, 5, 4),
    ("mekanism:alloy_atomic", 4, 5, 4),
    ("ae2:controller", 1, 3),
    ("ars_nouveau:dowsing_rod", 1, 3),
    ("sophisticatedbackpacks:diamond_backpack", 1, 3),
    ("draconicevolution:draconium_ingot", 16, 4, 16),
    ("apotheosis:gem_dust", 8, 5, 8),
])
