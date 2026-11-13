# 092 ae2/meteorite, presses, inscriber, network, controller, autocraft, cpu
#area -4 252 78 277
fill -4 64 252 40 91 277 minecraft:air
fill 41 64 252 78 91 277 minecraft:air
fill -4 60 252 78 62 277 minecraft:stone
fill -4 63 252 78 63 277 minecraft:light_gray_concrete
fill 0 64 258 78 79 258 minecraft:light_gray_concrete
fill 0 64 258 0 79 271 minecraft:light_gray_concrete
setblock 1 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "092.1"}','{"text": "ae2"}','{"text": "meteorite"}','{"text": ""}']}}
setblock 2 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Finde einen"}','{"text": "Meteoriten"}','{"text": ""}','{"text": ""}']}}
fill 10 64 258 10 79 271 minecraft:light_gray_concrete
fill 2 63 260 8 63 266 ae2:sky_stone_block
fill 2 64 260 8 65 260 ae2:sky_stone_block
fill 2 64 261 2 65 263 ae2:sky_stone_block
fill 8 64 261 8 65 263 ae2:sky_stone_block
fill 2 64 264 2 64 265 ae2:sky_stone_block
fill 8 64 264 8 64 265 ae2:sky_stone_block
setblock 5 64 263 ae2:mysterious_cube
setblock 3 64 261 ae2:flawless_budding_quartz
setblock 3 65 261 ae2:quartz_cluster[facing=up,waterlogged=false]
setblock 3 64 262 ae2:quartz_cluster[facing=south,waterlogged=false]
setblock 7 64 261 ae2:flawless_budding_quartz
setblock 7 65 261 ae2:quartz_cluster[facing=up,waterlogged=false]
setblock 6 64 261 ae2:quartz_cluster[facing=west,waterlogged=false]
setblock 11 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "092.2"}','{"text": "ae2"}','{"text": "presses"}','{"text": ""}']}}
setblock 12 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Hol die vier"}','{"text": "Pressen"}','{"text": ""}','{"text": ""}']}}
fill 21 64 258 21 79 271 minecraft:light_gray_concrete
setblock 13 64 263 minecraft:smooth_stone_slab
summon item_display 13.5 64.95 263.5 {item:{id:"ae2:silicon_press",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 15 64 263 minecraft:smooth_stone_slab
summon item_display 15.5 64.95 263.5 {item:{id:"ae2:logic_processor_press",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 17 64 263 minecraft:smooth_stone_slab
summon item_display 17.5 64.95 263.5 {item:{id:"ae2:calculation_processor_press",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 19 64 263 minecraft:smooth_stone_slab
summon item_display 19.5 64.95 263.5 {item:{id:"ae2:engineering_processor_press",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 22 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "092.3"}','{"text": "ae2"}','{"text": "inscriber"}','{"text": ""}']}}
setblock 23 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau eine"}','{"text": "Gravurmaschine"}','{"text": ""}','{"text": ""}']}}
fill 31 64 258 31 79 271 minecraft:light_gray_concrete
setblock 25 63 263 ae2:creative_energy_cell
setblock 25 64 263 ae2:inscriber[facing=south,spin=0]
setblock 27 64 263 ae2:charger[facing=south,spin=0]
kw testworld use 25 64 263 east ae2:fluix_glass_cable
setblock 32 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "092.4"}','{"text": "ae2"}','{"text": "network"}','{"text": ""}']}}
setblock 33 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Schließ dein"}','{"text": "erstes Netz an"}','{"text": ""}','{"text": ""}']}}
fill 42 64 258 42 79 271 minecraft:light_gray_concrete
setblock 34 63 263 ae2:creative_energy_cell
setblock 34 64 263 ae2:energy_acceptor
kw testworld use 34 64 263 east ae2:fluix_glass_cable
kw testworld use 35 64 263 east ae2:fluix_glass_cable
kw testworld use 36 64 263 east ae2:fluix_glass_cable
execute unless block 37 64 263 minecraft:air
setblock 38 64 263 ae2:drive[facing=south,spin=0]
kw testworld use 36 64 263 south ae2:terminal
setblock 43 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "092.5"}','{"text": "ae2"}','{"text": "controller"}','{"text": ""}']}}
setblock 44 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "ME-Controller"}','{"text": ""}','{"text": ""}']}}
fill 53 64 258 53 79 271 minecraft:light_gray_concrete
setblock 46 63 263 ae2:creative_energy_cell
fill 46 64 263 46 66 263 ae2:controller
kw testworld use 46 64 263 east ae2:fluix_smart_cable
kw testworld use 47 64 263 east ae2:fluix_smart_cable
kw testworld use 48 64 263 east ae2:fluix_smart_cable
kw testworld use 49 64 263 east ae2:fluix_smart_cable
execute unless block 49 64 263 minecraft:air
setblock 50 64 263 ae2:drive[facing=south,spin=0]
setblock 49 65 263 ae2:drive[facing=south,spin=0]
kw testworld use 47 64 263 south ae2:terminal
setblock 54 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "092.6"}','{"text": "ae2"}','{"text": "autocraft"}','{"text": ""}']}}
setblock 55 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell einen"}','{"text": "Molekularassembler"}','{"text": "daneben"}','{"text": ""}']}}
fill 63 64 258 63 79 271 minecraft:light_gray_concrete
setblock 58 63 263 ae2:creative_energy_cell
setblock 58 64 263 ae2:pattern_provider[push_direction=all]
setblock 57 64 263 ae2:molecular_assembler
setblock 59 64 263 ae2:molecular_assembler
setblock 58 65 263 ae2:molecular_assembler
setblock 64 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "092.7"}','{"text": "ae2"}','{"text": "cpu"}','{"text": ""}']}}
setblock 65 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau eine"}','{"text": "Fertigungs-CPU"}','{"text": ""}','{"text": ""}']}}
fill 73 64 258 73 79 271 minecraft:light_gray_concrete
setblock 67 63 264 ae2:creative_energy_cell
fill 67 64 263 68 65 263 ae2:crafting_unit[formed=false]
fill 67 64 264 68 64 264 ae2:1k_crafting_storage[formed=false]
setblock 67 65 264 ae2:crafting_monitor[facing=south,formed=false]
setblock 68 65 264 ae2:crafting_accelerator[formed=false]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
