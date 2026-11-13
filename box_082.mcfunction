# 082 ae2/meteorite, presses, inscriber, network, controller, autocraft, cpu
#area -4 233 78 258
fill -4 64 233 40 91 258 minecraft:air
fill 41 64 233 78 91 258 minecraft:air
fill -4 60 233 78 62 258 minecraft:stone
fill -4 63 233 78 63 258 minecraft:light_gray_concrete
fill 0 64 239 78 79 239 minecraft:light_gray_concrete
fill 0 64 239 0 79 252 minecraft:light_gray_concrete
setblock 1 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "082.1"}','{"text": "ae2"}','{"text": "meteorite"}','{"text": ""}']}}
setblock 2 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Finde einen"}','{"text": "Meteoriten"}','{"text": ""}','{"text": ""}']}}
fill 10 64 239 10 79 252 minecraft:light_gray_concrete
fill 2 63 241 8 63 247 ae2:sky_stone_block
fill 2 64 241 8 65 241 ae2:sky_stone_block
fill 2 64 242 2 65 244 ae2:sky_stone_block
fill 8 64 242 8 65 244 ae2:sky_stone_block
fill 2 64 245 2 64 246 ae2:sky_stone_block
fill 8 64 245 8 64 246 ae2:sky_stone_block
setblock 5 64 244 ae2:mysterious_cube
setblock 3 64 242 ae2:flawless_budding_quartz
setblock 3 65 242 ae2:quartz_cluster[facing=up,waterlogged=false]
setblock 3 64 243 ae2:quartz_cluster[facing=south,waterlogged=false]
setblock 7 64 242 ae2:flawless_budding_quartz
setblock 7 65 242 ae2:quartz_cluster[facing=up,waterlogged=false]
setblock 6 64 242 ae2:quartz_cluster[facing=west,waterlogged=false]
setblock 11 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "082.2"}','{"text": "ae2"}','{"text": "presses"}','{"text": ""}']}}
setblock 12 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Hol die vier"}','{"text": "Pressen"}','{"text": ""}','{"text": ""}']}}
fill 21 64 239 21 79 252 minecraft:light_gray_concrete
setblock 13 64 244 minecraft:smooth_stone_slab
summon item_display 13.5 64.95 244.5 {item:{id:"ae2:silicon_press",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 15 64 244 minecraft:smooth_stone_slab
summon item_display 15.5 64.95 244.5 {item:{id:"ae2:logic_processor_press",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 17 64 244 minecraft:smooth_stone_slab
summon item_display 17.5 64.95 244.5 {item:{id:"ae2:calculation_processor_press",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 19 64 244 minecraft:smooth_stone_slab
summon item_display 19.5 64.95 244.5 {item:{id:"ae2:engineering_processor_press",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 22 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "082.3"}','{"text": "ae2"}','{"text": "inscriber"}','{"text": ""}']}}
setblock 23 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau eine"}','{"text": "Gravurmaschine"}','{"text": ""}','{"text": ""}']}}
fill 31 64 239 31 79 252 minecraft:light_gray_concrete
setblock 25 63 244 ae2:creative_energy_cell
setblock 25 64 244 ae2:inscriber[facing=south,spin=0]
setblock 27 64 244 ae2:charger[facing=south,spin=0]
kw testworld use 25 64 244 east ae2:fluix_glass_cable
setblock 32 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "082.4"}','{"text": "ae2"}','{"text": "network"}','{"text": ""}']}}
setblock 33 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Schließ dein"}','{"text": "erstes Netz an"}','{"text": ""}','{"text": ""}']}}
fill 42 64 239 42 79 252 minecraft:light_gray_concrete
setblock 34 63 244 ae2:creative_energy_cell
setblock 34 64 244 ae2:energy_acceptor
kw testworld use 34 64 244 east ae2:fluix_glass_cable
kw testworld use 35 64 244 east ae2:fluix_glass_cable
kw testworld use 36 64 244 east ae2:fluix_glass_cable
execute unless block 37 64 244 minecraft:air
setblock 38 64 244 ae2:drive[facing=south,spin=0]
kw testworld use 36 64 244 south ae2:terminal
setblock 43 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "082.5"}','{"text": "ae2"}','{"text": "controller"}','{"text": ""}']}}
setblock 44 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "ME-Controller"}','{"text": ""}','{"text": ""}']}}
fill 53 64 239 53 79 252 minecraft:light_gray_concrete
setblock 46 63 244 ae2:creative_energy_cell
fill 46 64 244 46 66 244 ae2:controller
kw testworld use 46 64 244 east ae2:fluix_smart_cable
kw testworld use 47 64 244 east ae2:fluix_smart_cable
kw testworld use 48 64 244 east ae2:fluix_smart_cable
kw testworld use 49 64 244 east ae2:fluix_smart_cable
execute unless block 49 64 244 minecraft:air
setblock 50 64 244 ae2:drive[facing=south,spin=0]
setblock 49 65 244 ae2:drive[facing=south,spin=0]
kw testworld use 47 64 244 south ae2:terminal
setblock 54 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "082.6"}','{"text": "ae2"}','{"text": "autocraft"}','{"text": ""}']}}
setblock 55 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell einen"}','{"text": "Molekularassembler"}','{"text": "daneben"}','{"text": ""}']}}
fill 63 64 239 63 79 252 minecraft:light_gray_concrete
setblock 58 63 244 ae2:creative_energy_cell
setblock 58 64 244 ae2:pattern_provider[push_direction=all]
setblock 57 64 244 ae2:molecular_assembler
setblock 59 64 244 ae2:molecular_assembler
setblock 58 65 244 ae2:molecular_assembler
setblock 64 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "082.7"}','{"text": "ae2"}','{"text": "cpu"}','{"text": ""}']}}
setblock 65 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau eine"}','{"text": "Fertigungs-CPU"}','{"text": ""}','{"text": ""}']}}
fill 73 64 239 73 79 252 minecraft:light_gray_concrete
setblock 67 63 245 ae2:creative_energy_cell
fill 67 64 244 68 65 244 ae2:crafting_unit[formed=false]
fill 67 64 245 68 64 245 ae2:1k_crafting_storage[formed=false]
setblock 67 65 245 ae2:crafting_monitor[facing=south,formed=false]
setblock 68 65 245 ae2:crafting_accelerator[formed=false]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
