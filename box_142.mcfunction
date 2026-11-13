# 142 ae2/meteorite, presses, inscriber, network, controller, autocraft, cpu, p2p
#area 13 296 106 321
fill 13 64 296 57 91 321 minecraft:air
fill 58 64 296 102 91 321 minecraft:air
fill 103 64 296 106 91 321 minecraft:air
fill 13 60 296 106 62 321 minecraft:stone
fill 13 63 296 106 63 321 minecraft:light_gray_concrete
fill 17 64 302 106 79 302 minecraft:light_gray_concrete
fill 17 64 302 17 79 315 minecraft:light_gray_concrete
setblock 18 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "142.1"}','{"text": "ae2"}','{"text": "meteorite"}','{"text": ""}']}}
setblock 19 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Finde einen"}','{"text": "Meteoriten"}','{"text": ""}','{"text": ""}']}}
fill 27 64 302 27 79 315 minecraft:light_gray_concrete
fill 19 63 304 25 63 310 ae2:sky_stone_block
fill 19 64 304 25 65 304 ae2:sky_stone_block
fill 19 64 305 19 65 307 ae2:sky_stone_block
fill 25 64 305 25 65 307 ae2:sky_stone_block
fill 19 64 308 19 64 309 ae2:sky_stone_block
fill 25 64 308 25 64 309 ae2:sky_stone_block
setblock 22 64 307 ae2:mysterious_cube
setblock 20 64 305 ae2:flawless_budding_quartz
setblock 20 65 305 ae2:quartz_cluster[facing=up,waterlogged=false]
setblock 20 64 306 ae2:quartz_cluster[facing=south,waterlogged=false]
setblock 24 64 305 ae2:flawless_budding_quartz
setblock 24 65 305 ae2:quartz_cluster[facing=up,waterlogged=false]
setblock 23 64 305 ae2:quartz_cluster[facing=west,waterlogged=false]
setblock 28 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "142.2"}','{"text": "ae2"}','{"text": "presses"}','{"text": ""}']}}
setblock 29 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Hol die vier"}','{"text": "Pressen"}','{"text": ""}','{"text": ""}']}}
fill 38 64 302 38 79 315 minecraft:light_gray_concrete
setblock 30 64 307 minecraft:smooth_stone_slab
summon item_display 30.5 64.95 307.5 {item:{id:"ae2:silicon_press",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 32 64 307 minecraft:smooth_stone_slab
summon item_display 32.5 64.95 307.5 {item:{id:"ae2:logic_processor_press",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 34 64 307 minecraft:smooth_stone_slab
summon item_display 34.5 64.95 307.5 {item:{id:"ae2:calculation_processor_press",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 36 64 307 minecraft:smooth_stone_slab
summon item_display 36.5 64.95 307.5 {item:{id:"ae2:engineering_processor_press",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 39 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "142.3"}','{"text": "ae2"}','{"text": "inscriber"}','{"text": ""}']}}
setblock 40 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau eine"}','{"text": "Gravurmaschine"}','{"text": ""}','{"text": ""}']}}
fill 48 64 302 48 79 315 minecraft:light_gray_concrete
setblock 42 63 307 ae2:creative_energy_cell
setblock 42 64 307 ae2:inscriber[facing=south,spin=0]
setblock 44 64 307 ae2:charger[facing=south,spin=0]
kw testworld use 42 64 307 east ae2:fluix_glass_cable
setblock 49 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "142.4"}','{"text": "ae2"}','{"text": "network"}','{"text": ""}']}}
setblock 50 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Schließ dein"}','{"text": "erstes Netz an"}','{"text": ""}','{"text": ""}']}}
fill 59 64 302 59 79 315 minecraft:light_gray_concrete
setblock 51 63 307 ae2:creative_energy_cell
setblock 51 64 307 ae2:energy_acceptor
kw testworld use 51 64 307 east ae2:fluix_glass_cable
kw testworld use 52 64 307 east ae2:fluix_glass_cable
kw testworld use 53 64 307 east ae2:fluix_glass_cable
execute unless block 54 64 307 minecraft:air
setblock 55 64 307 ae2:drive[facing=south,spin=0]
kw testworld use 53 64 307 south ae2:terminal
setblock 60 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "142.5"}','{"text": "ae2"}','{"text": "controller"}','{"text": ""}']}}
setblock 61 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "ME-Controller"}','{"text": ""}','{"text": ""}']}}
fill 70 64 302 70 79 315 minecraft:light_gray_concrete
setblock 63 63 307 ae2:creative_energy_cell
fill 63 64 307 63 66 307 ae2:controller
kw testworld use 63 64 307 east ae2:fluix_smart_cable
kw testworld use 64 64 307 east ae2:fluix_smart_cable
kw testworld use 65 64 307 east ae2:fluix_smart_cable
kw testworld use 66 64 307 east ae2:fluix_smart_cable
execute unless block 66 64 307 minecraft:air
setblock 67 64 307 ae2:drive[facing=south,spin=0]
setblock 66 65 307 ae2:drive[facing=south,spin=0]
kw testworld use 64 64 307 south ae2:terminal
setblock 71 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "142.6"}','{"text": "ae2"}','{"text": "autocraft"}','{"text": ""}']}}
setblock 72 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell einen"}','{"text": "Molekularassembler"}','{"text": "daneben"}','{"text": ""}']}}
fill 80 64 302 80 79 315 minecraft:light_gray_concrete
setblock 75 63 307 ae2:creative_energy_cell
setblock 75 64 307 ae2:pattern_provider[push_direction=all]
setblock 74 64 307 ae2:molecular_assembler
setblock 76 64 307 ae2:molecular_assembler
setblock 75 65 307 ae2:molecular_assembler
setblock 81 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "142.7"}','{"text": "ae2"}','{"text": "cpu"}','{"text": ""}']}}
setblock 82 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau eine"}','{"text": "Fertigungs-CPU"}','{"text": ""}','{"text": ""}']}}
fill 90 64 302 90 79 315 minecraft:light_gray_concrete
setblock 84 63 308 ae2:creative_energy_cell
fill 84 64 307 85 65 307 ae2:crafting_unit[formed=false]
fill 84 64 308 85 64 308 ae2:1k_crafting_storage[formed=false]
setblock 84 65 308 ae2:crafting_monitor[facing=south,formed=false]
setblock 85 65 308 ae2:crafting_accelerator[formed=false]
setblock 91 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "142.8"}','{"text": "ae2"}','{"text": "p2p"}','{"text": ""}']}}
setblock 92 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen ME"}','{"text": "P2P-Tunnel"}','{"text": ""}','{"text": ""}']}}
fill 101 64 302 101 79 315 minecraft:light_gray_concrete
setblock 92 63 307 ae2:creative_energy_cell
setblock 92 64 307 ae2:energy_acceptor
kw testworld use 92 64 307 east ae2:fluix_glass_cable
kw testworld use 93 64 307 east ae2:me_p2p_tunnel
kw testworld use 94 63 307 up ae2:fluix_covered_dense_cable
kw testworld use 95 63 307 up ae2:fluix_covered_dense_cable
kw testworld use 96 63 307 up ae2:fluix_covered_dense_cable
kw testworld use 97 63 307 up ae2:fluix_covered_dense_cable
kw testworld use 98 63 307 up ae2:fluix_glass_cable
kw testworld use 98 64 307 west ae2:me_p2p_tunnel
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
