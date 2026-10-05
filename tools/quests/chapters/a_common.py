"""Chapter groups and the shared reward tables. Imported first.

Crates are made per stage: a stage 1 quest hands out stage 1 crates, so nothing in a
crate is locked when it drops. check_quest_stages.py enforces that."""
from ftbq import group, loot_table

group("start", "Start")
group("tech", "Technik")
group("magic", "Magie")
group("world", "Welt und Erkundung")
group("storage", "Lager und Werkzeug")
group("lists", "Checklisten")

# ---- Stage 1: Steinwerk ---------------------------------------------------
# Weights are relative inside one table. The fourth value is a random bonus on the count.
# loot_size is how many rolls one crate gives: three for common and uncommon, two for rare,
# so a crate is worth opening and not one stack of iron.

loot_table("s1_common", "Steinkiste", stage=1, loot_size=3, entries=[
    ("minecraft:iron_ingot", 8, 10, 8),
    ("minecraft:copper_ingot", 12, 10, 12),
    ("minecraft:coal", 16, 10, 16),
    ("minecraft:gold_ingot", 4, 6, 4),
    ("minecraft:bread", 8, 8),
    ("minecraft:oak_log", 16, 8, 16),
    ("minecraft:leather", 6, 5),
    ("minecraft:redstone", 8, 6, 8),
    ("minecraft:lapis_lazuli", 6, 5),
    ("minecraft:amethyst_shard", 8, 5, 8),
    ("create:andesite_alloy", 8, 6, 8),
    ("ars_nouveau:source_gem", 4, 6, 4),
    ("botania:white_mystical_petal", 4, 4, 4),
    ("waystones:warp_dust", 4, 3, 4),
])

loot_table("s1_uncommon", "Eisenkiste", stage=1, loot_size=3, entries=[
    ("minecraft:iron_block", 2, 10, 2),
    ("minecraft:gold_ingot", 8, 8, 8),
    ("minecraft:diamond", 2, 6, 2),
    ("minecraft:emerald", 4, 6, 4),
    ("minecraft:experience_bottle", 8, 8, 8),
    ("minecraft:golden_apple", 2, 5),
    ("create:iron_sheet", 16, 6, 16),
    ("create:copper_sheet", 16, 5, 16),
    ("ars_nouveau:source_gem_block", 2, 5),
    ("sophisticatedbackpacks:backpack", 1, 3),
    ("waystones:warp_stone", 1, 3),
    ("waystones:return_scroll", 2, 4),
    ("functionalstorage:oak_1", 4, 4),
    ("apotheosis:gem_dust", 4, 3, 4),
])

loot_table("s1_rare", "Goldkiste", stage=1, loot_size=2, entries=[
    ("minecraft:diamond", 8, 8, 8),
    ("minecraft:diamond_block", 1, 4),
    ("minecraft:emerald_block", 2, 5),
    ("minecraft:golden_apple", 2, 2, 1),
    ("minecraft:totem_of_undying", 1, 3),
    ("botania:mana_diamond", 2, 4),
    ("ars_nouveau:amulet_of_mana_regen", 1, 3),
    ("ars_nouveau:ring_of_potential", 1, 3),
    ("waystones:waystone", 1, 4),
    ("sophisticatedstorage:iron_chest", 2, 4),
    ("artifacts:everlasting_beef", 1, 2),
    ("artifacts:mimic_spawn_egg", 1, 1),
])

# ---- Stage 2: Messingwerk -------------------------------------------------

loot_table("s2_common", "Messingkiste", stage=2, loot_size=3, entries=[
    ("create:brass_ingot", 8, 10, 8),
    ("create:zinc_ingot", 12, 10, 12),
    ("mekanism:ingot_osmium", 8, 8, 8),
    ("minecraft:iron_ingot", 16, 8, 16),
    ("minecraft:copper_ingot", 24, 8, 24),
    ("minecraft:coal", 32, 8, 32),
    ("minecraft:blaze_rod", 2, 5, 2),
    ("minecraft:quartz", 16, 6, 16),
    ("minecraft:glowstone_dust", 8, 5, 8),
    ("create:electron_tube", 2, 5, 2),
    ("botania:manasteel_ingot", 4, 6, 4),
    ("ars_nouveau:source_gem", 8, 6, 8),
    ("minecraft:cooked_beef", 8, 6, 8),
])

loot_table("s2_uncommon", "Stahlkiste", stage=2, loot_size=3, entries=[
    ("mekanism:ingot_steel", 8, 10, 8),
    ("mekanism:basic_control_circuit", 4, 8, 4),
    ("create:brass_casing", 8, 8, 8),
    ("create:precision_mechanism", 1, 6, 1),
    ("botania:mana_pearl", 2, 6, 2),
    ("botania:mana_diamond", 2, 5, 2),
    ("minecraft:ender_pearl", 4, 6, 4),
    ("minecraft:diamond", 3, 6, 3),
    ("minecraft:magma_cream", 4, 4, 4),
    ("minecraft:nether_wart", 8, 4, 8),
    ("ars_nouveau:source_gem_block", 2, 5, 2),
    ("minecraft:experience_bottle", 16, 6, 16),
])

loot_table("s2_rare", "Terrastahlkiste", stage=2, loot_size=2, entries=[
    ("botania:terrasteel_ingot", 1, 6),
    ("create:precision_mechanism", 4, 8, 4),
    ("mekanism:basic_energy_cube", 1, 5),
    ("minecraft:netherite_scrap", 2, 5, 2),
    ("minecraft:ancient_debris", 2, 4, 2),
    ("minecraft:diamond_block", 1, 5),
    ("minecraft:golden_apple", 2, 2, 1),
    ("minecraft:totem_of_undying", 1, 3),
    ("botania:mana_tablet", 1, 4),
    ("create:blaze_cake", 4, 5, 4),
    ("waystones:waystone", 1, 4),
])

# ---- Stage 3: Stahlwerk ---------------------------------------------------

loot_table("s3_common", "Werkskiste", stage=3, loot_size=3, entries=[
    ("mekanism:ingot_steel", 16, 10, 16),
    ("mekanism:alloy_infused", 8, 8, 8),
    ("ae2:certus_quartz_crystal", 16, 8, 16),
    ("ae2:charged_certus_quartz_crystal", 4, 6, 4),
    ("ae2:fluix_crystal", 8, 6, 8),
    ("create:brass_ingot", 16, 6, 16),
    ("botania:manasteel_ingot", 8, 6, 8),
    ("enderio:conductive_alloy_ingot", 8, 6, 8),
    ("industrialforegoing:plastic", 8, 5, 8),
    ("minecraft:ender_pearl", 4, 5, 4),
    ("minecraft:experience_bottle", 16, 5, 16),
    ("undergarden:cloggrum_ingot", 4, 4, 4),
])

loot_table("s3_uncommon", "Elementiumkiste", stage=3, loot_size=3, entries=[
    ("mekanism:alloy_reinforced", 4, 8, 4),
    ("mekanism:advanced_control_circuit", 2, 8, 2),
    ("mekanism:ingot_refined_obsidian", 4, 6, 4),
    ("ae2:logic_processor", 4, 6, 4),
    ("ae2:calculation_processor", 4, 6, 4),
    ("ae2:engineering_processor", 4, 6, 4),
    ("botania:elementium_ingot", 4, 6, 4),
    ("botania:pixie_dust", 2, 5, 2),
    ("enderio:energetic_alloy_ingot", 4, 5, 4),
    ("powah:steel_energized", 8, 5, 8),
    ("malum:soul_stained_steel_ingot", 4, 4, 4),
    ("theurgy:alchemical_sulfur_iron", 4, 4, 4),
])

loot_table("s3_rare", "Elfenkiste", stage=3, loot_size=2, entries=[
    ("ae2:cell_component_16k", 1, 6),
    ("ae2:cell_component_4k", 2, 8),
    ("mekanism:teleportation_core", 1, 4),
    ("botania:dragonstone", 2, 5, 2),
    ("occultism:afrit_essence", 2, 4, 2),
    ("enderio:vibrant_alloy_ingot", 4, 5, 4),
    ("powah:crystal_blazing", 4, 4, 4),
    ("malum:hallowed_gold_ingot", 4, 4, 4),
    ("undergarden:froststeel_ingot", 4, 4, 4),
    ("sophisticatedbackpacks:gold_backpack", 1, 3),
    ("minecraft:diamond_block", 2, 5),
    ("minecraft:totem_of_undying", 1, 2),
])

# ---- Stage 4: Sternwerk ---------------------------------------------------

loot_table("s4_common", "Sternkiste", stage=4, loot_size=3, entries=[
    ("draconicevolution:draconium_ingot", 4, 10, 4),
    ("mekanism:alloy_atomic", 4, 8, 4),
    ("mekanism:ingot_refined_obsidian", 8, 8, 8),
    ("ae2:fluix_crystal", 16, 6, 16),
    ("botania:elementium_ingot", 8, 6, 8),
    ("eternal_starlight:blue_starlight_crystal_shard", 4, 6, 4),
    ("eternal_starlight:thermal_springstone_ingot", 4, 5, 4),
    ("minecraft:ender_pearl", 16, 6, 16),
    ("minecraft:shulker_shell", 2, 4, 2),
    ("minecraft:experience_bottle", 32, 5, 32),
])

loot_table("s4_uncommon", "Drachenkiste", stage=4, loot_size=3, entries=[
    ("mekanism:elite_control_circuit", 2, 8, 2),
    ("draconicevolution:draconium_core", 1, 6),
    ("ae2:cell_component_64k", 1, 6),
    ("megacells:cell_component_1m", 1, 3),
    ("nuclearcraft:uranium_ingot", 4, 5, 4),
    ("minecraft:dragon_breath", 4, 5, 4),
    ("minecraft:nether_star", 1, 3),
    ("minecraft:netherite_ingot", 1, 3),
])

loot_table("s4_rare", "Gaiakiste", stage=4, loot_size=2, entries=[
    ("mekanism:ultimate_control_circuit", 1, 5),
    ("draconicevolution:wyvern_core", 1, 5),
    ("botania:gaia_spirit", 1, 4),
    ("ae2:cell_component_256k", 1, 5),
    ("megacells:cell_component_4m", 1, 3),
    ("minecraft:elytra", 1, 2),
    ("minecraft:totem_of_undying", 1, 3),
])

# ---- Stage 5: Chaoswerk ---------------------------------------------------

loot_table("s5_common", "Chaoskiste", stage=5, loot_size=3, entries=[
    ("draconicevolution:draconium_ingot", 8, 10, 8),
    ("mekanism:elite_control_circuit", 4, 8, 4),
    ("mekanism:pellet_polonium", 2, 5, 2),
    ("mekanism:pellet_plutonium", 2, 5, 2),
    ("megacells:cell_component_1m", 1, 6),
    ("minecraft:experience_bottle", 64, 6, 32),
])

loot_table("s5_rare", "Erwachte Kiste", stage=5, loot_size=2, entries=[
    ("draconicevolution:awakened_draconium_ingot", 2, 8, 2),
    ("draconicevolution:awakened_core", 1, 5),
    ("botania:gaia_ingot", 1, 5),
    ("mekanism:pellet_antimatter", 1, 4),
    ("megacells:cell_component_16m", 1, 4),
    ("draconicevolution:chaos_shard", 1, 2),
])
