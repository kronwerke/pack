# 103 ae2/meteorite, presses, inscriber, network, controller, autocraft, cpu, p2p
#area -4 254 89 279
fill -4 64 254 40 91 279 minecraft:air
fill 41 64 254 85 91 279 minecraft:air
fill 86 64 254 89 91 279 minecraft:air
fill -4 60 254 89 62 279 minecraft:stone
fill -4 63 254 89 63 279 minecraft:light_gray_concrete
fill 0 64 260 89 79 260 minecraft:light_gray_concrete
fill 0 64 260 0 79 273 minecraft:light_gray_concrete
setblock 1 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "103.1"}','{"text": "ae2"}','{"text": "meteorite"}','{"text": ""}']}}
setblock 2 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Finde einen"}','{"text": "Meteoriten"}','{"text": ""}','{"text": ""}']}}
fill 10 64 260 10 79 273 minecraft:light_gray_concrete
fill 2 63 262 8 63 268 ae2:sky_stone_block
fill 2 64 262 8 65 262 ae2:sky_stone_block
fill 2 64 263 2 65 265 ae2:sky_stone_block
fill 8 64 263 8 65 265 ae2:sky_stone_block
fill 2 64 266 2 64 267 ae2:sky_stone_block
fill 8 64 266 8 64 267 ae2:sky_stone_block
setblock 5 64 265 ae2:mysterious_cube
setblock 3 64 263 ae2:flawless_budding_quartz
setblock 3 65 263 ae2:quartz_cluster[facing=up,waterlogged=false]
setblock 3 64 264 ae2:quartz_cluster[facing=south,waterlogged=false]
setblock 7 64 263 ae2:flawless_budding_quartz
setblock 7 65 263 ae2:quartz_cluster[facing=up,waterlogged=false]
setblock 6 64 263 ae2:quartz_cluster[facing=west,waterlogged=false]
setblock 11 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "103.2"}','{"text": "ae2"}','{"text": "presses"}','{"text": ""}']}}
setblock 12 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Hol die vier"}','{"text": "Pressen"}','{"text": ""}','{"text": ""}']}}
fill 21 64 260 21 79 273 minecraft:light_gray_concrete
setblock 13 64 265 minecraft:smooth_stone_slab
summon item_display 13.5 64.95 265.5 {item:{id:"ae2:silicon_press",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 15 64 265 minecraft:smooth_stone_slab
summon item_display 15.5 64.95 265.5 {item:{id:"ae2:logic_processor_press",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 17 64 265 minecraft:smooth_stone_slab
summon item_display 17.5 64.95 265.5 {item:{id:"ae2:calculation_processor_press",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 19 64 265 minecraft:smooth_stone_slab
summon item_display 19.5 64.95 265.5 {item:{id:"ae2:engineering_processor_press",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 22 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "103.3"}','{"text": "ae2"}','{"text": "inscriber"}','{"text": ""}']}}
setblock 23 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau eine"}','{"text": "Gravurmaschine"}','{"text": ""}','{"text": ""}']}}
fill 31 64 260 31 79 273 minecraft:light_gray_concrete
setblock 25 63 265 ae2:creative_energy_cell
setblock 25 64 265 ae2:inscriber[facing=south,spin=0]
setblock 27 64 265 ae2:charger[facing=south,spin=0]
kw testworld use 25 64 265 east ae2:fluix_glass_cable
setblock 32 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "103.4"}','{"text": "ae2"}','{"text": "network"}','{"text": ""}']}}
setblock 33 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Schließ dein"}','{"text": "erstes Netz an"}','{"text": ""}','{"text": ""}']}}
fill 42 64 260 42 79 273 minecraft:light_gray_concrete
setblock 34 63 265 ae2:creative_energy_cell
setblock 34 64 265 ae2:energy_acceptor
kw testworld use 34 64 265 east ae2:fluix_glass_cable
kw testworld use 35 64 265 east ae2:fluix_glass_cable
kw testworld use 36 64 265 east ae2:fluix_glass_cable
execute unless block 37 64 265 minecraft:air
setblock 38 64 265 ae2:drive[facing=south,spin=0]
kw testworld use 36 64 265 south ae2:terminal
setblock 43 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "103.5"}','{"text": "ae2"}','{"text": "controller"}','{"text": ""}']}}
setblock 44 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "ME-Controller"}','{"text": ""}','{"text": ""}']}}
fill 53 64 260 53 79 273 minecraft:light_gray_concrete
setblock 46 63 265 ae2:creative_energy_cell
fill 46 64 265 46 66 265 ae2:controller
kw testworld use 46 64 265 east ae2:fluix_smart_cable
kw testworld use 47 64 265 east ae2:fluix_smart_cable
kw testworld use 48 64 265 east ae2:fluix_smart_cable
kw testworld use 49 64 265 east ae2:fluix_smart_cable
execute unless block 49 64 265 minecraft:air
setblock 50 64 265 ae2:drive[facing=south,spin=0]
setblock 49 65 265 ae2:drive[facing=south,spin=0]
kw testworld use 47 64 265 south ae2:terminal
setblock 54 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "103.6"}','{"text": "ae2"}','{"text": "autocraft"}','{"text": ""}']}}
setblock 55 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell einen"}','{"text": "Molekularassembler"}','{"text": "daneben"}','{"text": ""}']}}
fill 63 64 260 63 79 273 minecraft:light_gray_concrete
setblock 58 63 265 ae2:creative_energy_cell
setblock 58 64 265 ae2:pattern_provider[push_direction=all]
setblock 57 64 265 ae2:molecular_assembler
setblock 59 64 265 ae2:molecular_assembler
setblock 58 65 265 ae2:molecular_assembler
setblock 64 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "103.7"}','{"text": "ae2"}','{"text": "cpu"}','{"text": ""}']}}
setblock 65 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau eine"}','{"text": "Fertigungs-CPU"}','{"text": ""}','{"text": ""}']}}
fill 73 64 260 73 79 273 minecraft:light_gray_concrete
setblock 67 63 266 ae2:creative_energy_cell
fill 67 64 265 68 65 265 ae2:crafting_unit[formed=false]
fill 67 64 266 68 64 266 ae2:1k_crafting_storage[formed=false]
setblock 67 65 266 ae2:crafting_monitor[facing=south,formed=false]
setblock 68 65 266 ae2:crafting_accelerator[formed=false]
setblock 74 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "103.8"}','{"text": "ae2"}','{"text": "p2p"}','{"text": ""}']}}
setblock 75 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen ME"}','{"text": "P2P-Tunnel"}','{"text": ""}','{"text": ""}']}}
fill 84 64 260 84 79 273 minecraft:light_gray_concrete
setblock 75 63 265 ae2:creative_energy_cell
setblock 75 64 265 ae2:energy_acceptor
kw testworld use 75 64 265 east ae2:fluix_glass_cable
kw testworld use 76 64 265 east ae2:me_p2p_tunnel
kw testworld use 77 63 265 up ae2:fluix_covered_dense_cable
kw testworld use 78 63 265 up ae2:fluix_covered_dense_cable
kw testworld use 79 63 265 up ae2:fluix_covered_dense_cable
kw testworld use 80 63 265 up ae2:fluix_covered_dense_cable
kw testworld use 81 63 265 up ae2:fluix_glass_cable
kw testworld use 81 64 265 west ae2:me_p2p_tunnel
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
