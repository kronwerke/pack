# 126 ae2/meteorite, presses, inscriber, network, controller, autocraft, cpu, p2p
#area 13 256 106 281
fill 13 64 256 57 91 281 minecraft:air
fill 58 64 256 102 91 281 minecraft:air
fill 103 64 256 106 91 281 minecraft:air
fill 13 60 256 106 62 281 minecraft:stone
fill 13 63 256 106 63 281 minecraft:light_gray_concrete
fill 17 64 262 106 79 262 minecraft:light_gray_concrete
fill 17 64 262 17 79 275 minecraft:light_gray_concrete
setblock 18 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "126.1"}','{"text": "ae2"}','{"text": "meteorite"}','{"text": ""}']}}
setblock 19 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Finde einen"}','{"text": "Meteoriten"}','{"text": ""}','{"text": ""}']}}
fill 27 64 262 27 79 275 minecraft:light_gray_concrete
fill 19 63 264 25 63 270 ae2:sky_stone_block
fill 19 64 264 25 65 264 ae2:sky_stone_block
fill 19 64 265 19 65 267 ae2:sky_stone_block
fill 25 64 265 25 65 267 ae2:sky_stone_block
fill 19 64 268 19 64 269 ae2:sky_stone_block
fill 25 64 268 25 64 269 ae2:sky_stone_block
setblock 22 64 267 ae2:mysterious_cube
setblock 20 64 265 ae2:flawless_budding_quartz
setblock 20 65 265 ae2:quartz_cluster[facing=up,waterlogged=false]
setblock 20 64 266 ae2:quartz_cluster[facing=south,waterlogged=false]
setblock 24 64 265 ae2:flawless_budding_quartz
setblock 24 65 265 ae2:quartz_cluster[facing=up,waterlogged=false]
setblock 23 64 265 ae2:quartz_cluster[facing=west,waterlogged=false]
setblock 28 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "126.2"}','{"text": "ae2"}','{"text": "presses"}','{"text": ""}']}}
setblock 29 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Hol die vier"}','{"text": "Pressen"}','{"text": ""}','{"text": ""}']}}
fill 38 64 262 38 79 275 minecraft:light_gray_concrete
setblock 30 64 267 minecraft:smooth_stone_slab
summon item_display 30.5 64.95 267.5 {item:{id:"ae2:silicon_press",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 32 64 267 minecraft:smooth_stone_slab
summon item_display 32.5 64.95 267.5 {item:{id:"ae2:logic_processor_press",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 34 64 267 minecraft:smooth_stone_slab
summon item_display 34.5 64.95 267.5 {item:{id:"ae2:calculation_processor_press",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 36 64 267 minecraft:smooth_stone_slab
summon item_display 36.5 64.95 267.5 {item:{id:"ae2:engineering_processor_press",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 39 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "126.3"}','{"text": "ae2"}','{"text": "inscriber"}','{"text": ""}']}}
setblock 40 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau eine"}','{"text": "Gravurmaschine"}','{"text": ""}','{"text": ""}']}}
fill 48 64 262 48 79 275 minecraft:light_gray_concrete
setblock 42 63 267 ae2:creative_energy_cell
setblock 42 64 267 ae2:inscriber[facing=south,spin=0]
setblock 44 64 267 ae2:charger[facing=south,spin=0]
kw testworld use 42 64 267 east ae2:fluix_glass_cable
setblock 49 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "126.4"}','{"text": "ae2"}','{"text": "network"}','{"text": ""}']}}
setblock 50 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Schließ dein"}','{"text": "erstes Netz an"}','{"text": ""}','{"text": ""}']}}
fill 59 64 262 59 79 275 minecraft:light_gray_concrete
setblock 51 63 267 ae2:creative_energy_cell
setblock 51 64 267 ae2:energy_acceptor
kw testworld use 51 64 267 east ae2:fluix_glass_cable
kw testworld use 52 64 267 east ae2:fluix_glass_cable
kw testworld use 53 64 267 east ae2:fluix_glass_cable
execute unless block 54 64 267 minecraft:air
setblock 55 64 267 ae2:drive[facing=south,spin=0]
kw testworld use 53 64 267 south ae2:terminal
setblock 60 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "126.5"}','{"text": "ae2"}','{"text": "controller"}','{"text": ""}']}}
setblock 61 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "ME-Controller"}','{"text": ""}','{"text": ""}']}}
fill 70 64 262 70 79 275 minecraft:light_gray_concrete
setblock 63 63 267 ae2:creative_energy_cell
fill 63 64 267 63 66 267 ae2:controller
kw testworld use 63 64 267 east ae2:fluix_smart_cable
kw testworld use 64 64 267 east ae2:fluix_smart_cable
kw testworld use 65 64 267 east ae2:fluix_smart_cable
kw testworld use 66 64 267 east ae2:fluix_smart_cable
execute unless block 66 64 267 minecraft:air
setblock 67 64 267 ae2:drive[facing=south,spin=0]
setblock 66 65 267 ae2:drive[facing=south,spin=0]
kw testworld use 64 64 267 south ae2:terminal
setblock 71 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "126.6"}','{"text": "ae2"}','{"text": "autocraft"}','{"text": ""}']}}
setblock 72 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell einen"}','{"text": "Molekularassembler"}','{"text": "daneben"}','{"text": ""}']}}
fill 80 64 262 80 79 275 minecraft:light_gray_concrete
setblock 75 63 267 ae2:creative_energy_cell
setblock 75 64 267 ae2:pattern_provider[push_direction=all]
setblock 74 64 267 ae2:molecular_assembler
setblock 76 64 267 ae2:molecular_assembler
setblock 75 65 267 ae2:molecular_assembler
setblock 81 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "126.7"}','{"text": "ae2"}','{"text": "cpu"}','{"text": ""}']}}
setblock 82 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau eine"}','{"text": "Fertigungs-CPU"}','{"text": ""}','{"text": ""}']}}
fill 90 64 262 90 79 275 minecraft:light_gray_concrete
setblock 84 63 268 ae2:creative_energy_cell
fill 84 64 267 85 65 267 ae2:crafting_unit[formed=false]
fill 84 64 268 85 64 268 ae2:1k_crafting_storage[formed=false]
setblock 84 65 268 ae2:crafting_monitor[facing=south,formed=false]
setblock 85 65 268 ae2:crafting_accelerator[formed=false]
setblock 91 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "126.8"}','{"text": "ae2"}','{"text": "p2p"}','{"text": ""}']}}
setblock 92 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen ME"}','{"text": "P2P-Tunnel"}','{"text": ""}','{"text": ""}']}}
fill 101 64 262 101 79 275 minecraft:light_gray_concrete
setblock 92 63 267 ae2:creative_energy_cell
setblock 92 64 267 ae2:energy_acceptor
kw testworld use 92 64 267 east ae2:fluix_glass_cable
kw testworld use 93 64 267 east ae2:me_p2p_tunnel
kw testworld use 94 63 267 up ae2:fluix_covered_dense_cable
kw testworld use 95 63 267 up ae2:fluix_covered_dense_cable
kw testworld use 96 63 267 up ae2:fluix_covered_dense_cable
kw testworld use 97 63 267 up ae2:fluix_covered_dense_cable
kw testworld use 98 63 267 up ae2:fluix_glass_cable
kw testworld use 98 64 267 west ae2:me_p2p_tunnel
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
