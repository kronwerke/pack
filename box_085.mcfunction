# 085 list_power/steam_engine, mek_heat, ie_thermo, powah_reactor, flux, draconic_core
#area -4 250 69 277
fill -4 64 250 34 93 277 minecraft:air
fill 35 64 250 69 93 277 minecraft:air
fill -4 60 250 69 62 277 minecraft:stone
fill -4 63 250 69 63 277 minecraft:light_gray_concrete
fill 0 64 256 69 81 256 minecraft:light_gray_concrete
fill 0 64 256 0 81 271 minecraft:light_gray_concrete
setblock 1 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "085.1"}','{"text": "list_power"}','{"text": "steam_engine"}','{"text": ""}']}}
setblock 2 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Heiz einen"}','{"text": "Dampfkessel an"}','{"text": ""}','{"text": ""}']}}
fill 11 64 256 11 81 271 minecraft:light_gray_concrete
setblock 4 64 260 create:blaze_burner[blaze=smouldering]
kw testworld use 4 64 260 up create:creative_blaze_cake
setblock 4 64 261 create:blaze_burner[blaze=smouldering]
kw testworld use 4 64 261 up create:creative_blaze_cake
setblock 5 64 260 create:blaze_burner[blaze=smouldering]
kw testworld use 5 64 260 up create:creative_blaze_cake
setblock 5 64 261 create:blaze_burner[blaze=smouldering]
kw testworld use 5 64 261 up create:creative_blaze_cake
fill 4 65 260 5 67 261 create:fluid_tank[bottom=false,shape=window,top=false]
setblock 4 66 263 create:shaft[axis=x]
setblock 4 66 262 create:steam_engine[face=wall,facing=south,waterlogged=false]
setblock 12 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "085.2"}','{"text": "list_power"}','{"text": "mek_heat"}','{"text": ""}']}}
setblock 13 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell einen"}','{"text": "Wärmegenerator"}','{"text": "in Lava"}','{"text": ""}']}}
fill 21 64 256 21 81 271 minecraft:light_gray_concrete
setblock 14 64 259 minecraft:stone_bricks
setblock 14 64 260 minecraft:stone_bricks
setblock 14 64 261 minecraft:stone_bricks
setblock 14 64 262 minecraft:stone_bricks
setblock 14 64 263 minecraft:glass
setblock 15 64 259 minecraft:stone_bricks
setblock 15 64 260 minecraft:lava
setblock 15 64 261 minecraft:lava
setblock 15 64 262 minecraft:lava
setblock 15 64 263 minecraft:glass
setblock 16 64 259 minecraft:stone_bricks
setblock 16 64 260 minecraft:lava
setblock 16 64 261 mekanismgenerators:heat_generator[facing=south]
setblock 16 64 262 minecraft:glass
setblock 16 64 263 minecraft:glass
setblock 17 64 259 minecraft:stone_bricks
setblock 17 64 260 minecraft:lava
setblock 17 64 261 minecraft:lava
setblock 17 64 262 minecraft:lava
setblock 17 64 263 minecraft:glass
setblock 18 64 259 minecraft:stone_bricks
setblock 18 64 260 minecraft:stone_bricks
setblock 18 64 261 minecraft:stone_bricks
setblock 18 64 262 minecraft:stone_bricks
setblock 18 64 263 minecraft:glass
setblock 22 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "085.3"}','{"text": "list_power"}','{"text": "ie_thermo"}','{"text": ""}']}}
setblock 23 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Spann Lava"}','{"text": "gegen Wasser"}','{"text": ""}','{"text": ""}']}}
fill 31 64 256 31 81 271 minecraft:light_gray_concrete
setblock 25 64 261 minecraft:magma_block
setblock 26 64 261 immersiveengineering:thermoelectric_generator
setblock 27 64 261 minecraft:blue_ice
kw testworld use 26 64 261 up immersiveengineering:connector_lv
setblock 32 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "085.4"}','{"text": "list_power"}','{"text": "powah_reactor"}','{"text": ""}']}}
setblock 33 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Zünde den"}','{"text": "Powah-Reaktor"}','{"text": ""}','{"text": ""}']}}
fill 41 64 256 41 81 271 minecraft:light_gray_concrete
setblock 36 64 261 powah:reactor_starter[core=true]
setblock 42 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "085.5"}','{"text": "list_power"}','{"text": "flux"}','{"text": ""}']}}
setblock 43 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau ein"}','{"text": "Flux-Netzwerk"}','{"text": ""}','{"text": ""}']}}
fill 52 64 256 52 81 271 minecraft:light_gray_concrete
setblock 44 64 261 powah:furnator_starter[facing=south]
setblock 44 65 261 fluxnetworks:flux_plug
setblock 49 64 261 mekanism:enrichment_chamber[facing=south]
setblock 49 65 261 fluxnetworks:flux_point
setblock 53 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "085.6"}','{"text": "list_power"}','{"text": "draconic_core"}','{"text": ""}']}}
setblock 54 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den"}','{"text": "Energiekern"}','{"text": ""}','{"text": ""}']}}
fill 64 64 256 64 81 271 minecraft:light_gray_concrete
fill 57 64 261 59 66 263 draconicevolution:draconium_block
setblock 58 65 262 draconicevolution:energy_core
setblock 54 64 262 minecraft:polished_deepslate
setblock 54 65 262 draconicevolution:energy_core_stabilizer
setblock 62 64 262 minecraft:polished_deepslate
setblock 62 65 262 draconicevolution:energy_core_stabilizer
setblock 58 64 258 minecraft:polished_deepslate
setblock 58 65 258 draconicevolution:energy_core_stabilizer
setblock 58 64 266 minecraft:polished_deepslate
setblock 58 65 266 draconicevolution:energy_core_stabilizer
