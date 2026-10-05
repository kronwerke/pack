# Screenshots for the quest book

Pictures the quests should get, by chapter. Each line is the quest id and what the shot should show. Take them at 16:9, GUI scale 2 or 3, HUD hidden (F1) unless the line says the HUD matters. Save as PNG named `<chapter>_<quest id>.png`; they go into `kubejs/assets/kronwerke/textures/quests/shots/` and get wired into the chapters afterwards.

The test world has every line of this list as a grey box: `/kw testworld` takes an operator there (it builds the world on the first visit), `/kw testworld rebuild` builds it again after a change. Each box holds the scene for its shot, a chest with what still has to happen by hand, and signs facing the path. The boxes are generated from this list and `tools/shots/scenes.py` by `tools/shots/build.py`; a line without a hand made scene shows the quest's task items.

Chapters without a list here (most of the stage 1 gap chapters from the first wave) work without pictures for now.

## Start

- start_here/o_handin: a player sneaking and right-clicking the obelisk, boss bar visible
- start_here/o_feeder: a barrel next to the obelisk fed by a hopper or a belt
- start_here/o_obelisk: the boss bar with the three pillars
- start_here/s_locked: a veiled "???" item with its three tooltip lines, and JEI with veiled stage 2 items
- start_here/m_goldleaf: a tree with golden leaves
- start_here/m_ritual: the gold powder ring with wooden stands and a sapling in the middle
- start_here/m_altar: the finished Natural Altar
- start_here/m_gearbox, m_keystone: the crafting grid in JEI
- start_here/v_claim: the FTB Chunks claim view

## Erste Farmen

- farms/cobble_drill: water and lava cobble generator with a drill and an andesite funnel, belt leading away
- farms/wood_saw: mechanical bearing with a saw arm over a ring of saplings, glued chest and portable storage interface
- farms/crops_harvester: bearing with two harvesters and a chest sweeping a round wheat field
- farms/crops_essence: cross section of inferium farmland with growth accelerators underneath
- farms/animals_thorn: fenced pen with feeding trough, Dreadthorne, hopper floor, mana pool nearby
- farms/mobs_dark: cutaway of the dark room with trapdoor edges and the 22 block shaft with hoppers
- farms/lava_seeds: fire seed field, the lava bucket recipe, item drain into fluid tanks
- farms/source_berries: sourceberry rows with agronomic sourcelink, source jar, imbuement chamber and Starbuncle
- farms/mana_endoflame: Endoflame ring, spreader, open crate with hopper and chest, pressure plate
- farms/s2_xp: grindstone drain stack with experience hatch on a tank

## Create

- create/welcome: the Ponder view opened with W over a cogwheel
- create/water_wheel: four water wheels in a row with water over the paddles from above
- create/windmill: a finished windmill with 32 sails
- create/stress: goggles overlay on an overstressed network
- create/depot: press above a depot with one block of air between
- create/mixer: mixer, one block of air, basin
- create/alloy_mixing: the whole andesite alloy line with belts, funnels, mixer and output chest
- create/compacting: press over basin making andesite from flint, gravel and lava
- create/washing: fan blowing through water over a belt of gravel
- create/belt: a belt between two shafts
- create/frogport: chain conveyor with a frogport carrying a package
- create/stock_ticker: a seated villager next to the stock ticker, order screen open
- create/cobble_gen: drill in front of a cobble generator
- create/tree_farm: radial chassis saw wheel cutting a row of trees
- create/factory: andesite factory feeding a chest beside the obelisk
- create_brass/blaze_burner: catching a blaze with the empty burner
- create_brass/brass_mixing: heated burner, basin and mixer stack
- create_brass/incomplete: belt with three deployers (cogwheel, tube, nugget) and a press
- create_brass/precision: the looped precision mechanism belt
- create_brass/crafter: a 3x3 mechanical crafter grid with its arrows
- create_brass/crushing_wheel: a pair of crushing wheels, goggles showing the stress
- create_brass/blaze_cake: press over basin, then spout over depot
- create_brass/boiler: a four engine boiler with the goggles boiler overlay
- create_brass/arm: a mechanical arm feeding a blaze burner
- create_brass/pg_winding, pg_generator, pg_rheostat, pg_magnet: the Power Grid parts, the full generator with a lamp, the self excited wiring, the electromagnet over a depot
- create_brass/alternator: steam engine driving an alternator with connectors
- create_trains/welcome: the track assembly belt
- create_trains/unprocessed_sheet: spout pouring lava on powdered obsidian
- create_trains/station: station in assembly mode with bogeys
- create_trains/first_train: a finished small train
- create_trains/drive: the driver's view from the controls
- create_trains/conductor: a blaze burner sitting as conductor
- create_trains/schedule: the schedule screen with conditions
- create_trains/junction: chain and entry signals at a junction, goggles overlay
- create_trains/cargo: a portable storage interface pair at a platform
- create_trains/postbox: a postbox next to a station
- create_trains/obelisk_line: spawn station unloading into the obelisk feeder

## Mekanism

- mekanism/infuser: infuser GUI with the carbon bar and the electron tube to circuit recipe
- mekanism/configurator: side configuration tab with auto eject
- mekanism/dynamic_tank: a 3x3x3 dynamic tank with valve and structural glass
- mekanism/ethene: pressurized reaction chamber making ethene
- mekanism/ore_line: the steel line from enrichment chamber to the obelisk chest
- mekanism_ores/line2: chest, transporters, enrichment chamber, smelter, chest, cables
- mekanism_ores/layout: the 3x line with all three transmitter types visible
- mekanism_ores/tripling: purification chamber, crusher, enrichment chamber, smelter with separator and pump
- mekanism_ores/shards: the 4x line with injection chamber, two separators and chemical infuser
- mekanism_ores/quintupling: the full eight machine ladder with gas tubes
- mekanism_ores/full: a machine GUI with 8 speed and 8 energy upgrades
- mekanism_ores/foundry: the Metalworks foundry with raw ore going in and the ingot cast
- mekanism_advanced/teleporter: built teleporter frame with portal
- mekanism_advanced/miner: digital miner GUI with filters and radius
- mekanism_advanced/evap: thermal evaporation tower
- mekanism_advanced/boiler: boiler cutaway with heaters and conductors
- mekanism_advanced/turbine: turbine cutaway with rotors, dispersers, coils
- mekanism_advanced/cnc_stamper: stamper GUI with the silicon press
- mekanism_elite/induction_matrix: matrix with cells and providers behind glass, port GUI
- mekanism_elite/qio_dashboard: the dashboard GUI
- mekanism_elite/polonium: NuclearCraft irradiation chain
- mekanism_elite/fusion: fusion reactor with laser and amplifier
- mekanism_elite/mekasuit: full MekaSuit at the modification station
- antimatter/reactor: fission reactor GUI with fuel assemblies and control rods
- antimatter/waste: row of solar neutron activators under open sky
- antimatter/sps: formed SPS with ports and supercharged coil
- antimatter/wind: the large wind generator

## Ars Nouveau

- ars_nouveau/imbuement, first_gem: the chamber with an amethyst shard, then with a finished gem
- ars_nouveau/fill_jar: volcanic sourcelink, jar and chamber within range, logs on the ground
- ars_nouveau/chamber_auto: hoppers above and below a chamber feeding a chest
- ars_nouveau/first_spell: the spell book GUI with Projectile and Break
- ars_nouveau/scribes_table: the glyph selection screen with ingredients over the table
- ars_nouveau/apparatus: core, apparatus and pedestals in range
- ars_nouveau/earth_essence: chamber with three pedestals next to it
- ars_nouveau/starbuncle_work: dominion wand links between chamber, Starbuncle and chest
- ars_nouveau/drygmy: Drygmy henge with chest and jar
- ars_nouveau/mana: the mana bar
- ars_apprentice/relay: two relays bridging jars about 20 blocks apart
- ars_apprentice/collector: collector at the link farm, depositor at the workshop
- ars_apprentice/brazier: a tablet on the lit brazier
- ars_apprentice/ritual_scrying: scrying particles through stone
- ars_apprentice/wixie: Wixie cauldron with chests
- ars_apprentice/potions: potion jars next to the cauldron and an alchemical sourcelink
- ars_apprentice/turret: turret in front of a cobblestone generator
- ars_apprentice/source_motor: motor with a jar driving a Create shaft
- ars_master/tribute: the Chimera mid fight
- ars_master/wilden_ritual: brazier with spike, horn and wing
- ars_master/golem_bookwyrm: amethyst golem at a geode, storage lectern GUI
- ars_master/ritual_awakening: a Weald Walker
- ars_master/alteration: alteration table with a robe on the stand
- ars_master/charged_certus: chamber with redstone and glowstone pedestals
- ars_epic/breath: bottling dragon breath
- ars_epic/linger: a Linger field over mobs
- ars_epic/elevator: slipstream elevator in use
- ars_epic/phases: the Chimera curled up with spikes
- ars_epic/el_armor: a full elemental robe set

## Botania

- botania/pure_daisy: the daisy with 8 stone or logs, half converted
- botania/endo_auto: chest, hopper and open crate over four Endoflames, pressure plate
- botania/pool: a full pool with a spreader beam, wand in hand
- botania/manastar: a blue Manastar next to a pool
- botania/mana_void: a mana void under a pool
- botania/farm: the finished stage 1 mana farm
- botania/manasteel_prep: the Nature's Aura ritual layout with gold powder and stands
- botania_runes/mana_pearl: a pool on a brass casing with a pearl in it
- botania_runes/ritual: the oak ritual growing
- botania_runes/runic_altar: altar with ingredients, a spreader aimed at it, wand HUD
- botania_runes/thermalily: a hose pulley feeding lava next to the lily
- botania_runes/gourmaryllis: a belt dropping varied food
- botania_runes/plate_base: the 3x3 lapis and livingrock base with plate and sparks
- botania_runes/terrasteel: the plate mid craft
- botania_runes/baubles_rings: the Curios screen with rings worn
- botania_runes/rune_core: the crafting grid
- gaia/arena: beacon with four pylons from above
- gaia/fight: the guardian with the purple traps
- gaia/tiara: flying with the flight bar visible
- gaia/dandelifeon: a 25x25 cell field
- gaia/goal: a chest by the obelisk holding spirits
- alfheim/frame: the finished gateway with two pools and natura pylons
- alfheim/open: the open portal with an item flying out
- alfheim/elementium_line: an automated manasteel block line into the portal
- alfheim/pure_essence: the pure daisy on end stone with the essence cloud
- alfheim/corporea_index: the index with a chat request
- alfheim/elementium_armor: a pixie attacking a mob

## Occultism and Hexerei

- occultism/spirit_fire: spirit fire turning andesite into otherstone
- occultism/aviar: finished Aviar's Circle with golden bowl, candles and sacrificial bowls
- occultism/foliot_crusher: Foliot crusher next to a pile of dust
- occultism/foliot_janitor: transporter, crusher and janitor working with chests
- occultism/hedyrin: Hedyrin's Lure with the yellow glyphs
- occultism/ophyx: Ophyx' Calling from above, with skulls
- occultism/strigeor: Strigeor's Higher Binding from above
- occultism/satchel: the Dictionary pentacle preview in the world
- occultism/djinni_familiars: a player with two or three familiars
- occultism_afrit/iesnium: divination rod highlight on iesnium ore in the Nether
- occultism_afrit/kandar: Kandar's Opened Conjure from above
- occultism_afrit/unbound_afrit: fight with an unbound Afrit
- occultism_afrit/mineshaft: dimensional mineshaft with a lamp inside and a hopper below
- occultism_afrit/storage: storage actuator with four stabilizers
- occultism_afrit/reinforced_deepslate: the Kronwerke crafting grid next to the Osorin pentacle
- occultism_afrit/marid_crusher: Fatma's Incentivized Attraction
- hexerei/herbs: herb garden with all four plants grown
- hexerei/cauldron: two mixing cauldrons, one heated over lava
- hexerei/candles: candle dipper on a tallow cauldron with candles
- hexerei/blood: cauldron menu with the blood sigil
- hexerei/sage_plate: burning sage plate with the smoke ring
- hexerei/potion_brew: dipper dipping a candle into a potion
- hexerei/willow_broom: flying on a broom, plus the broom menu
- hexerei/crow: crow on the shoulder, crow flute menu
- hexerei/witch_house: a finished witch hut

## Immersive Engineering and Industrial Foregoing

- immersive/welcome: the manual open on a multiblock page
- immersive/hammer: right-clicking a structure with the hammer
- immersive/coke_oven, creosote, pump: formed coke oven with GUI, the bucket slot, a pump with pipes
- immersive/treated_wood: planks around the creosote bucket
- immersive/blast_furnace, improved_form: crude blast furnace GUI, improved furnace with hopper and preheaters
- immersive/kiln: alloy kiln making electrum
- immersive/bench: engineer's workbench with the components blueprint
- immersive/cloche: a garden cloche growing hemp
- immersive/dynamo, windmill, watermill: dynamo with windmill, a windmill on a tower, three water wheels on one shaft
- immersive/connectors, capacitor, thermoelectric, transformer: LV wires on posts, the accumulator, the generator between magma and blue ice, a transformer with LV and MV
- immersive/tank, silo, shelf: the formed structures
- immersive/list_mb: all seven stage 2 structures side by side
- immersive_heavy/light, heavy: the Kronwerke recipes in the grid
- immersive_heavy/crusher, press, squeezer, fermenter, mixer, bottling, arc, refinery, diesel, sawmill, assembler, auto_workbench, excavator, lightning_rod, radio_tower, resonanz: each formed
- immersive_heavy/hv, duroplast, survey: an HV line on steel posts, the bottling machine with resin, a core sample on the ground
- immersive_heavy/list_big: an overview of the factory
- industrial/welcome, extractor, latex_unit, plastic, dissolution: pity frame recipe, extractors around a log column, the latex unit GUI, dry rubber in a furnace, the dissolution chamber GUI
- industrial/frame_simple, frame_adv, frame_supreme: the three frame recipes
- industrial/addons, sower, gatherer, bio, slaughter, crusher, duplicator: the machines at work
- industrial/laser, lens, fluid_laser: ore laser with drills, the lens slot, fluid laser over a wither
- industrial/washing, conveyor, transporters: the ore meat machines in a row, conveyors with upgrades, two transporters

## Oritech, Powah, Ender IO

- oritech/cores, pipes, plastic, laser, atomic_forge, destroyer, fragment_forge, fragment, addons, addon_quarry, addon_crop, exo, reactor
- powah/orb, rods, furnator, thermo, reactor, reactor_fuel, ender_cell, transmitter, power_plant
- enderio/grains, capacitor, smelter, cap_bank, conduits, filter, sag_mill, vial, soul_binder, vacuum_chest, enchanter

## AE2, logistics, storage

- ae2/channels: controller with dense cables branching into normal smart cables, channel stripes visible
- ae2/meteorite, presses, inscriber, network, controller, autocraft, cpu, p2p, factory
- ae2_advanced/bridge, spatial, reaction, matrix, mega_4m
- logistics/menril, programmer, counter, xnet_connectors, laser_node, mg_gadget
- storage/welcome, drawers_4, config_tool, copper_tier, controller, vault_big, trash
- refined_storage: the network grid and the autocrafter
- list_transport/belt, packages, create_tank, hose_pulley, ie_wire, mek_transporter, vault, drawers

## Power, flux and new tech

- list_power/steam_engine, mek_heat, ie_thermo, alternator, powah_reactor, flux, mekmm_large, nc_passive, draconic_core
- flux_networks/dust: the bedrock gap with redstone and obsidian, left-clicking the obsidian
- flux_networks/first_link: a generator with a plug and a machine with a point, no cables
- flux_networks/sides, wireless, stats: the point's side tab, the wireless charging tab, the statistics tab
- flux_networks/setup_mek, setup_reactor, whole_base: a factory row with points, a Powah reactor with a plug, a machine hall without cables
- pneumaticcraft/chamber, refinery, vortex, elevator, safety, plastic, etching
- pneumaticcraft_advanced/first_run, electrostatic, thermal, adv_air, first_program, frames, security_station, spawner_extractor, pressurized_spawner
- hostile_networks/deep_learner, learner_gui, sim_chamber, scaling, loot_fab, data_center

## Dimensions

- nether/welcome, fortress, blaze_burner, biomes, structures, ig_kill, nm_kill, bastion, debris
- the_end/arrival, crystals, dragon, egg, respawn, elytra, cg_find, cg_kill, st_aviary, draconium
- exploration/e_compass, e_frame, e_enter, e_veins, e_lootr, e_campsite, e_dnt_tavern, e_arise_sky, e_tnt_village, e_yung_dungeon
- aether/portal, arrive, altar, freezer, incubator, ride, gloves, bronze, slider, silver, queen
- deeper_darker/portal, arrival, deeplands, echoing_forest, blooming_caverns, overcast_columns, temple, transmitter, resonarium, stalker, echo_shard
- undergarden/arrival, catacombs, guardian, forgotten, depths, infuser, b_cold
- eternal_starlight/orb, portal, starfire, desert, forge, golem, garden, monstrosity
- list_dimensions/d_mining, d_aether, d_undergarden, d_otherside, r_plates, r_mekanism, r_enderio, r_chunks
- productive_trees/first_tree, mega, pots, sawmill_run, stripper, wood_set, station, pollinated, loot_saplings, amber, time_traveller

## Late game

- draconic/dust, injectors, stabilizer, tiers, tools
- draconic_chaos/awakened, crystals, guardian, reactor
- nuclearcraft/reactor, irradiation, geiger
- quarries/first_dig, quarry, destroyer, coe_netherite
- mahou_tsukai/blood, cloth, fay_sight, marble_visit, staff
- finale/fight_info, f_crystals, tech

## Magic, gear, food

- silent_gear/stone_anvil, pickaxe, reading_stats, crude_mixer, hammer, repair_kit, alloy_forge, charger
- food/f_cutting_board, f_pot, f_rice, f_rich_soil, f_feast, f_market, f_rod
- theurgy/sal_tank, liquefaction, vessels, wire, array, fermentation
- eidolon/brazier, soul_shard, crucible, altar, prayer, stone_altar
- malum/spirits, altar, obelisk, crucible, healing_rite, quickening
- list_gear/mek_jetpack, drilling, mekasuit, wyvern, sg_end
