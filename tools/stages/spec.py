"""Which stage every item belongs to. build.py turns this into the Chapters stage files.

Chapters unlocks an item as soon as the player has ANY stage that lists it, and "@mod"
lists every item of a mod. So "@mekanism" in stage 2 plus "mekanism:elite_bin" in stage 3
would open the elite bin in stage 2. To keep exceptions working, the stage files only
hold plain item ids, and they are generated from the rules below against the item
registry in items.txt (dumped from the test server).

RULES is read top to bottom and the last rule that matches an item wins:
  "@mod"          every item of the mod
  "re:<regex>"    every item whose full id matches (re.search)
  "mod:item"      one item
Stage 1 means open from the start. Anything no rule matches is stage 1.
"""

DIMENSIONS = {
    2: ["minecraft:the_nether", "aether:the_aether"],
    3: ["undergarden:undergarden", "deeperdarker:otherside"],
    4: ["minecraft:the_end", "eternal_starlight:starlight", "mahoutsukai:reality_marble"],
}

RULES = [
    # ---------------------------------------------------------------- Create family
    (2, [
        "create:blaze_burner", "create:empty_blaze_burner", "create:blaze_cake", "create:blaze_cake_base",
        "re:^create:brass_", "re:^create:.*precision_mechanism$",
        "create:mechanical_crafter", "create:deployer", "create:sequenced_gearshift",
        "create:rotation_speed_controller", "create:crushing_wheel", "create:smart_chute", "create:smart_fluid_pipe",
        "create:mechanical_arm", "create:display_link", "create:display_board",
        "create:track", "create:track_station", "create:track_signal", "create:track_observer",
        "create:train_door", "create:train_trapdoor", "create:schematicannon", "create:contraption_controls",
        "create:steam_engine", "create:electron_tube", "create:sturdy_sheet", "create:incomplete_track",
        "create:linked_controller", "create:cart_assembler", "create:controller_rail", "create:clockwork_bearing",
        "create:elevator_pulley", "create:mechanical_roller", "create:potato_cannon", "create:extendo_grip", "create:wand_of_symmetry",
        "create:peculiar_bell", "create:haunted_bell", "create:content_observer", "create:stockpile_switch",
        "create:nixie_tube", "create:pulse_extender", "create:pulse_repeater", "create:pulse_timer",
        "@create_enchantment_industry", "@create_connected", "@create_jetpack", "@create_dragons_plus",
        "@railways", "@createaddition", "@powergrid", "@create_mechanical_spawner", "@createdieselgenerators",
    ]),
    (3, [
        "@createoreexcavation",
        "createdieselgenerators:huge_diesel_engine", "createdieselgenerators:distillation_controller",
        "createdieselgenerators:pumpjack_bearing", "createdieselgenerators:pumpjack_crank",
        "createdieselgenerators:pumpjack_head", "createdieselgenerators:pumpjack_hole",
        "createaddition:modular_accumulator",
    ]),
    (4, ["createoreexcavation:netherite_drill", "createoreexcavation:diamond_drill"]),

    # ---------------------------------------------------------------- Mekanism
    (2, ["@mekanism", "@mekanismgenerators", "@mekanismtools", "@mekanismadditions"]),
    (3, [
        "re:^mekanism:advanced_", "re:^mekanismtools:refined_obsidian_",
        "mekanism:digital_miner", "mekanism:teleporter", "mekanism:portable_teleporter", "mekanism:teleportation_core",
        "mekanism:purification_chamber",
        # the teleporter, the digital miner and the robit all need atomic alloy, so it opens here
        "mekanism:alloy_atomic", "mekanism:robit",
        "mekanism:antiprotonic_nucleosynthesizer", "mekanism:isotopic_centrifuge", "mekanism:nutritional_liquifier",
        "mekanism:modification_station", "re:^mekanism:module_",
        "mekanism:hdpe_sheet", "mekanism:hdpe_rod", "mekanism:hdpe_stick", "mekanism:hdpe_elytra",
        "mekanism:alloy_reinforced", "mekanism:dust_refined_obsidian", "mekanism:ingot_refined_obsidian",
        "mekanism:block_refined_obsidian", "mekanism:nugget_refined_obsidian",
        "mekanismgenerators:advanced_solar_generator",
        "re:^mekanismgenerators:(turbine_|electromagnetic_coil|rotational_complex|saturating_condenser)",
        "@mekmm",
    ]),
    (4, [
        "re:^mekanism:(elite|ultimate)_", "re:^mekanism:qio_", "mekanism:portable_qio_dashboard",
        "mekanism:laser", "mekanism:laser_amplifier", "mekanism:laser_tractor_beam",
        # the 4x and 5x ore lines and the entangloporter need elite or ultimate circuits anyway
        "mekanism:quantum_entangloporter", "mekanism:chemical_injection_chamber",
        "mekanism:chemical_dissolution_chamber", "mekanism:chemical_washer", "mekanism:chemical_crystallizer",
        "mekanism:meka_tool", "re:^mekanism:mekasuit_", "mekanism:elite_control_circuit",
        "re:^mekanism:module_", "re:^mekanismgenerators:fusion_", "mekanismgenerators:laser_focus_matrix", "mekanismgenerators:hohlraum",
        "mekanismgenerators:reactor_glass",
        "re:^mekmm:(elite|ultimate)_", "re:^mekmm:large_",
        # the fusion reactor frame needs polonium pellets, and NuclearCraft makes polonium in stage 4
        "mekanism:pellet_polonium",
    ]),
    (5, [
        "mekanism:pellet_antimatter", "mekanism:antiprotonic_nucleosynthesizer", "mekanism:sps_casing", "mekanism:sps_port",
        "mekanism:pellet_plutonium", "mekanism:supercharged_coil",
        "re:^mekanismgenerators:(fission_|control_rod_assembly)",
        "mekmm:replicator", "mekmm:fluid_replicator", "mekmm:chemical_replicator", "mekmm:uu_matter",
        "re:^mekmm:.*replicating_factory$", "mekmm:large_antiprotonic_nucleosynthesizer",
    ]),
    # mekmm's silver ore generates in the overworld; its raw materials stay usable
    (1, ["re:^mekmm:(silver_ore|deepslate_silver_ore|raw_silver|block_raw_silver)$"]),

    # ---------------------------------------------------------------- Immersive Engineering
    (2, ["@immersiveengineering"]),
    (3, [
        "immersiveengineering:light_engineering", "immersiveengineering:heavy_engineering",
        "immersiveengineering:rs_engineering", "immersiveengineering:generator",
        "immersiveengineering:radiator", "immersiveengineering:component_electronic_adv",
        "immersiveengineering:railgun", "immersiveengineering:chemthrower", "immersiveengineering:tesla_coil",
    ]),

    # ---------------------------------------------------------------- Storage networks
    (3, ["@ae2", "@extendedae", "@appmek", "@ae2wtlib", "@appflux", "@refinedstorage", "@cabletiers"]),
    (4, [
        "re:^ae2:.*(64k|256k)", "re:^ae2:(quantum_|spatial_)",
        "@megacells", "@advanced_ae",
        "re:^extendedae:(ex_|assembler_matrix_|oversize_interface|wireless_|infinity_)",
        "re:^appflux:.*(64k|256k|1m|4m)", "re:^refinedstorage:.*(64k|256k)",
    ]),
    (5, [
        "re:^megacells:.*(16m|64m|256m)", "re:^megacells:bulk_", "megacells:compression_card",
        "re:^advanced_ae:quantum_(core|unit|storage|accelerator|multi_threader|structure|crafter|helmet|chestplate|leggings|boots)",
        "advanced_ae:data_entangler", "re:^appflux:.*(16m|64m|256m)",
    ]),

    # ---------------------------------------------------------------- Other tech
    (3, [
        "@enderio", "@industrialforegoing", "@powah", "@oritech",
        "@integrateddynamics", "@integratedcrafting", "@integratedterminals", "@integratedtunnels",
        "@xnet", "@rftoolsbase", "@compactmachines", "@mininggadgets", "@laserio", "@tempad",
    ]),
    (4, [
        "@rftoolsbuilder", "@quarryplus", "re:^mininggadgets:upgrade_.*_3$",
        "re:^powah:.*_nitro$", "powah:crystal_nitro", "powah:nitro_crystal_block",
    ]),
    (2, ["@modularrouters", "@pipez", "@productivebees", "@productivemetalworks", "@buildinggadgets2"]),
    (3, ["pipez:advanced_upgrade", "pipez:universal_pipe", "buildinggadgets2:gadget_copy_paste", "buildinggadgets2:gadget_cut_paste"]),
    (4, ["pipez:ultimate_upgrade"]),
    (5, ["pipez:infinity_upgrade"]),
    # the foundry's fire bricks and clay are plain building blocks
    (1, ["re:^productivemetalworks:(.*_fire_bricks|fire_brick|fire_clay)$"]),

    # Just Dire Things: ferricore and blazegold with the Nether, then one metal per stage
    (2, ["@justdirethings"]),
    (3, ["re:^justdirethings:.*celestigem", "re:^justdirethings:.*_(t3|tier3)$", "re:^justdirethings:.*t3_fluid"]),
    (4, [
        "re:^justdirethings:.*eclipsealloy", "re:^justdirethings:.*_(t4|tier4)$", "re:^justdirethings:.*t4_fluid",
        "re:^justdirethings:time_", "justdirethings:paradoxmachine", "justdirethings:portalgun_v2",
        "justdirethings:polymorphic_wand_v2",
    ]),

    # Iron Furnaces, one or two tiers per stage
    (2, ["re:^ironfurnaces:(silver|gold|obsidian)_furnace$", "re:^ironfurnaces:upgrade_(silver|gold|obsidian)",
         "re:^ironfurnaces:augment_", "ironfurnaces:item_heater", "ironfurnaces:heater"]),
    (3, ["re:^ironfurnaces:(diamond|emerald)_furnace$", "re:^ironfurnaces:upgrade_(diamond|emerald)$",
         "ironfurnaces:augment_factory", "ironfurnaces:augment_generator"]),
    (4, ["re:^ironfurnaces:(crystal|netherite)_furnace$", "re:^ironfurnaces:upgrade_(crystal|netherite)$"]),
    (5, ["re:^ironfurnaces:(million|allthemodium|vibranium|unobtainium)_furnace$",
         "re:^ironfurnaces:upgrade_(allthemodium|vibranium|unobtainium)$", "re:^ironfurnaces:rainbow_"]),

    # ---------------------------------------------------------------- Storage and backpacks
    # Chests and barrels: copper and iron from the start, one tier per stage after that.
    # Backpacks are a tier behind, they carry a whole base around.
    (2, [
        "re:^sophisticatedbackpacks:(copper|iron)_", "re:^sophisticatedstorage:(gold)_", "re:^sophisticatedstorage:limited_gold_",
        "re:^sophisticatedstorage:.*_to_gold_tier_upgrade$",
        "re:^sophisticated(backpacks|storage):stack_upgrade_tier_2$", "re:^sophisticatedbackpacks:advanced_",
        "functionalstorage:compacting_drawer", "functionalstorage:simple_compacting_drawer", "functionalstorage:framed_simple_compacting_drawer",
        "functionalstorage:compacting_framed_drawer", "functionalstorage:copper_upgrade", "functionalstorage:gold_upgrade",
    ]),
    (3, [
        "re:^sophisticatedbackpacks:(gold|diamond)_", "re:^sophisticatedstorage:(diamond)_", "re:^sophisticatedstorage:limited_diamond_",
        "re:^sophisticatedstorage:.*_to_diamond_tier_upgrade$",
        "re:^sophisticated(backpacks|storage):stack_upgrade_tier_3$",
        "sophisticatedbackpacks:inception_upgrade", "sophisticatedbackpacks:everlasting_upgrade",
        "functionalstorage:diamond_upgrade", "functionalstorage:ender_drawer", "functionalstorage:armory_cabinet",
    ]),
    (4, [
        "re:^sophisticated(backpacks|storage):netherite_", "re:^sophisticatedstorage:.*_to_netherite_tier_upgrade$",
        "re:^sophisticated(backpacks|storage):stack_upgrade_tier_4$", "re:^sophisticatedstorage:limited_netherite_",
        "functionalstorage:netherite_upgrade", "functionalstorage:max_storage_upgrade",
    ]),
    (5, ["re:^sophisticated(backpacks|storage):stack_upgrade_(tier_5|omega)"]),
    # conversion upgrades belong to the tier they convert to
    (2, ["re:^sophisticated(backpacks|storage):stack_upgrade_.*_to_tier_2_conversion$"]),
    (3, ["re:^sophisticated(backpacks|storage):stack_upgrade_.*_to_tier_3_conversion$"]),
    (4, ["re:^sophisticated(backpacks|storage):stack_upgrade_.*_to_tier_4_conversion$"]),
    (5, ["re:^sophisticated(backpacks|storage):stack_upgrade_.*_to_tier_5_conversion$"]),

    # ---------------------------------------------------------------- Farming
    (2, ["re:^mysticalagriculture:.*prudentium", "re:^mysticalagradditions:prudentium", "re:^mysticalagriculture:soulium",
         "mysticalagriculture:soul_extractor", "mysticalagriculture:soulium_spawner", "mysticalagriculture:harvester",
         "mysticalagriculture:enchanter"]),
    (3, ["re:^mysticalagriculture:.*tertium", "re:^mysticalagradditions:tertium"]),
    (4, ["re:^mysticalagriculture:.*imperium", "re:^mysticalagradditions:imperium",
         "mysticalagriculture:awakening_altar", "mysticalagriculture:awakening_pedestal", "mysticalagriculture:essence_vessel"]),
    (5, ["re:^mysticalagriculture:.*supremium", "re:^mysticalagradditions:(supremium|insanium|awakened)",
         "re:^mysticalagradditions:.*_crux$", "mysticalagradditions:creative_essence"]),

    # ---------------------------------------------------------------- Magic
    (2, [
        "ars_nouveau:apprentice_spell_book", "ars_nouveau:relay", "ars_nouveau:relay_splitter", "ars_nouveau:relay_deposit",
        "ars_nouveau:relay_collector", "ars_nouveau:relay_warp", "ars_nouveau:spell_turret",
        "ars_nouveau:basic_spell_turret", "ars_nouveau:ritual_brazier", "ars_nouveau:portal", "ars_nouveau:warp_scroll",
        "ars_nouveau:stable_warp_scroll", "@ars_technica", "re:^ars_elemental:(?!lesser_).*_focus$",
        "ars_additions:warp_index", "ars_additions:stabilized_warp_index", "ars_additions:warp_nexus", "ars_additions:nexus_warp_scroll",
    ]),
    (3, [
        "ars_nouveau:archmage_spell_book", "ars_nouveau:rotating_spell_turret", "ars_nouveau:timer_spell_turret",
        "ars_nouveau:ritual_wilden_summon", "ars_nouveau:ritual_awakening", "ars_nouveau:ritual_flight", "ars_nouveau:ritual_disintegration",
        "ars_nouveau:ritual_warping", "ars_nouveau:ritual_conjure_island_plains", "ars_nouveau:ritual_conjure_island_desert",
        "re:^ars_nouveau:(battlemage|arcanist)_",
    ]),
    (1, ["ars_technica:glyph_pack"]),
    (4, ["ars_nouveau:void_prism", "re:^ars_nouveau:sorcerer_"]),

    (2, [
        "botania:runic_altar", "botania:terrestrial_agglomeration_plate", "botania:terrasteel_ingot", "botania:terrasteel_nugget",
        "botania:terrasteel_block", "botania:natura_pylon", "botania:mana_pylon",
        "botania:mana_enchanter", "botania:botanical_brewery", "botania:manasteel_ingot", "botania:manasteel_nugget",
        "botania:manasteel_block", "botania:mana_pearl", "botania:mana_tablet", "botania:alchemy_catalyst",
        "re:^botania:rune_", "re:^botania:manasteel_", "re:^botania:terrasteel_", "botania:terra_blade", "botania:terra_shatterer",
        "botania:terra_truncator",
    ]),
    (3, [
        "re:^botania:elementium", "re:^botania:.*dreamwood", "botania:pixie_dust", "botania:dragonstone",
        "botania:elven_gateway_core", "re:^botania:dragonstone",
        "botania:elven_mana_spreader", "botania:spectrolus", "botania:dandelifeon", "botania:kekimurus", "botania:rafflowsia",
        "botania:entropinnyum", "botania:orechid", "botania:orechid_ignem", "re:^botania:.*corporea", "botania:conjuration_catalyst",
        "botania:ring_of_thor", "botania:ring_of_loki", "botania:ring_of_odin",
    ]),
    (4, [
        "botania:flugel_tiara", "botania:gaia_pylon", "botania:gaia_spirit", "botania:gaia_head", "botania:gaia_mana_spreader",
        "botania:dice_of_fate", "botania:starcaller", "botania:key_of_the_kings_law", "botania:eye_of_the_flugel",
    ]),
    (5, ["botania:gaia_ingot"]),

    (2, [
        "occultism:book_of_binding_foliot", "occultism:book_of_binding_djinni", "occultism:book_of_binding_empty",
        "occultism:book_of_binding_bound_foliot", "occultism:book_of_binding_bound_djinni",
        "occultism:pentacle_summon", "occultism:pentacle_possess", "occultism:pentacle_craft", "occultism:pentacle_misc",
        "occultism:sacrificial_bowl", "occultism:golden_sacrificial_bowl", "occultism:copper_sacrificial_bowl",
        "occultism:silver_sacrificial_bowl", "re:^occultism:chalk_", "occultism:ritual_satchel_t1",
        "@hexerei", "@evilcraft", "@forbidden_arcanus", "@reliquary",
    ]),
    (3, [
        "occultism:book_of_binding_afrit", "occultism:book_of_binding_marid", "occultism:book_of_binding_bound_afrit",
        "occultism:book_of_binding_bound_marid", "occultism:afrit_essence", "occultism:marid_essence",
        "re:^occultism:iesnium", "occultism:storage_controller", "occultism:storage_controller_base", "occultism:storage_remote",
        "occultism:dimensional_matrix", "occultism:dimensional_mineshaft", "occultism:miner_djinni_ores",
        "occultism:miner_afrit_deeps", "occultism:miner_marid_master", "occultism:ritual_satchel_t2", "occultism:infused_pickaxe",
                "@theurgy", "@eidolon_repraised", "@malum", "@undergarden",
        "forbidden_arcanus:hephaestus_forge_tier_3", "reliquary:alkahestry_tome", "reliquary:rending_gale",
        "reliquary:emperor_chalice", "reliquary:infernal_chalice", "reliquary:midas_touchstone",
    ]),
    (4, ["@eternal_starlight", "@mahoutsukai", "forbidden_arcanus:hephaestus_forge_tier_4", "forbidden_arcanus:hephaestus_forge_tier_5",
         "re:^forbidden_arcanus:draco_arcanus_"]),

    # Nature's Aura: the altar and infused iron from day one, the sky and the depths later
    (2, ["naturesaura:offering_table", "naturesaura:conversion_catalyst", "naturesaura:crushing_catalyst",
         "re:^naturesaura:tainted_gold", "naturesaura:auto_crafter", "naturesaura:animal_generator"]),
    (3, ["re:^naturesaura:sky_", "naturesaura:generator_limit_remover", "naturesaura:chunk_loader", "naturesaura:animal_spawner",
         "naturesaura:rf_converter", "naturesaura:ender_crate", "naturesaura:ender_access", "naturesaura:mover_cart"]),
    (4, ["re:^naturesaura:depth_"]),

    # Iron's Spells: the ink decides which rarity a scroll can have
    (2, ["irons_spellbooks:uncommon_ink", "irons_spellbooks:rare_ink", "irons_spellbooks:gold_spell_book",
         "irons_spellbooks:arcane_anvil", "re:^irons_spellbooks:.*_upgrade_orb$"]),
    (3, ["irons_spellbooks:epic_ink", "irons_spellbooks:diamond_spell_book", "irons_spellbooks:netherite_spell_book"]),
    (4, ["irons_spellbooks:legendary_ink", "irons_spellbooks:legendary_spell_book", "irons_spellbooks:dragonskin_spell_book",
         "irons_spellbooks:dragonskin"]),

    # ---------------------------------------------------------------- Silent Gear
    (2, ["silentgear:crimson_iron_ingot", "silentgear:crimson_steel_ingot", "silentgear:blaze_gold_ingot"]),
    (3, ["silentgear:azure_silver_ingot", "silentgear:azure_electrum_ingot", "silentgear:tyrian_steel_ingot"]),

    # ---------------------------------------------------------------- Endgame
    (4, ["@draconicevolution", "@nuclearcraft", "@nuclear_radiation"]),
    (5, [
        "re:^draconicevolution:(awakened|chaotic|chaos|draconic)_", "re:^draconicevolution:item_(draconic|chaotic)_",
        "re:^draconicevolution:(large|medium|small)_chaos_frag$", "re:^draconicevolution:reactor_",
    ]),

    # ---------------------------------------------------------------- Added in 0.8.0
    # The Aether opens with the Nether; its dungeon gear is a stage later.
    (2, ["@aether"]),
    (3, ["re:^aether:(gravitite|enchanted_gravitite|valkyrie|phoenix|neptune|obsidian_)", "aether:sun_altar"]),
    # Deeper and Darker: the Otherside in stage 3, the warden's gear in stage 4.
    (3, ["@deeperdarker"]),
    (4, ["re:^deeperdarker:(warden_(helmet|chestplate|leggings|boots|upgrade_smithing_template)|soul_elytra|sonorous_staff)$"]),
    # Hostile Neural Networks: learn in stage 2, simulate in stage 3, fabricate in stage 4.
    (2, ["@hostilenetworks"]),
    (3, ["hostilenetworks:sim_chamber", "hostilenetworks:prediction_matrix", "hostilenetworks:overworld_prediction", "hostilenetworks:nether_prediction"]),
    (4, ["hostilenetworks:loot_fabricator", "hostilenetworks:end_prediction", "hostilenetworks:data_center", "hostilenetworks:data_center_io_port"]),
    # Flux Networks: wireless power is a stage 3 thing, the big storages later.
    (3, ["@fluxnetworks"]),
    (4, ["fluxnetworks:herculean_flux_storage"]),
    (5, ["fluxnetworks:gargantuan_flux_storage"]),
    # PneumaticCraft: compressed iron and the first machines in stage 2, advanced tubes,
    # assembly and drones in stage 3, the pneumatic armor and weapons in stage 4.
    (2, ["@pneumaticcraft"]),
    (3, [
        "re:^pneumaticcraft:advanced_", "re:^pneumaticcraft:.*drone$", "pneumaticcraft:programmer", "pneumaticcraft:programming_puzzle",
        "re:^pneumaticcraft:assembly_", "pneumaticcraft:electrostatic_compressor", "pneumaticcraft:flux_compressor", "pneumaticcraft:pneumatic_dynamo",
        "pneumaticcraft:aerial_interface", "pneumaticcraft:thermal_compressor", "pneumaticcraft:solar_compressor", "pneumaticcraft:solar_cell", "pneumaticcraft:solar_wafer",
        "pneumaticcraft:programmable_controller", "re:^pneumaticcraft:network_", "pneumaticcraft:security_station", "pneumaticcraft:universal_sensor",
        "pneumaticcraft:pressurized_spawner", "pneumaticcraft:spawner_extractor", "pneumaticcraft:spawner_agitator", "pneumaticcraft:vacuum_trap",
        "re:^pneumaticcraft:drill_bit_(diamond|netherite)$", "pneumaticcraft:unassembled_netherite_drill_bit",
    ]),
    (4, ["re:^pneumaticcraft:pneumatic_(helmet|chestplate|leggings|boots)$", "pneumaticcraft:minigun", "pneumaticcraft:micromissiles", "pneumaticcraft:nuke_virus", "pneumaticcraft:stop_worm"]),
    # Pylons, Item Collectors and Ranged Pumps: the harvester and the basic collector from
    # day one, the rest with the first machines.
    (2, ["pylons:infusion_pylon", "pylons:interdiction_pylon", "pylons:expulsion_pylon", "pylons:protection_pylon", "itemcollectors:advanced_collector", "rangedpumps:pump"]),

    # Items whose recipes need a later stage than their mod: the tooltip should say so.
    (2, ["pylons:harvester_pylon", "mysticalagriculture:tinkering_table"]),
    (2, ["occultism:spirit_attuned_gem"]),
    (3, ["mekanism:atomic_disassembler", "mekanism:osmium_compressor", "mekanism:teleporter_frame",
         "re:^mekanism:thermal_evaporation_", "mekanism:boiler_valve", "mekanism:painting_machine", "mekanism:flamethrower"]),
    (4, ["mekanism:combiner", "mekanism:solar_neutron_activator", "re:^mekanism:(basic|advanced|elite|ultimate)_induction_",
         "mekanism:induction_casing", "mekanism:induction_port", "mekanism:dust_lithium", "mekanism:dimensional_stabilizer",
         "mekanism:pigment_mixer", "mekanism:modification_station", "mekmm:presser", "mekmm:planting_station", "mekmm:ambient_gas_collector"]),
    (4, ["@create_jetpack", "mekanism:hdpe_elytra", "re:^cabletiers:.*mega_"]),
    # The large wind generator makes more than the nitro reactor and the fusion reactor together.
    (5, ["mekmm:large_wind_generator"]),
    # Azure ore only generates in end stone.
    (4, ["re:^silentgear:(azure_silver|azure_electrum|tyrian_steel)"]),
    # ---------------------------------------------------------------- Milestones (kubejs/startup_scripts/milestones.js)
    (2, ["kronwerke:brass_heart", "kronwerke:rune_core"]),
    (3, ["kronwerke:steel_core", "kronwerke:elven_star"]),
]

