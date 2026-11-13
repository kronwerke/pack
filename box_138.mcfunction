# 138 oritech/cores, pipes, plastic, laser, atomic_forge, destroyer, fragment_forge, fragment, addons, addon_quarry, addon_crop, exo, reactor
#area -4 275 138 302
fill -4 64 275 36 91 302 minecraft:air
fill 37 64 275 77 91 302 minecraft:air
fill 78 64 275 118 91 302 minecraft:air
fill 119 64 275 138 91 302 minecraft:air
fill -4 60 275 138 62 302 minecraft:stone
fill -4 63 275 138 63 302 minecraft:light_gray_concrete
fill 0 64 281 138 79 281 minecraft:light_gray_concrete
fill 0 64 281 0 79 296 minecraft:light_gray_concrete
setblock 1 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "138.1"}','{"text": "oritech"}','{"text": "cores"}','{"text": ""}']}}
setblock 2 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau"}','{"text": "Maschinenkerne"}','{"text": ""}','{"text": ""}']}}
fill 10 64 281 10 79 296 minecraft:light_gray_concrete
setblock 4 64 286 oritech:machine_core_1
setblock 6 64 286 oritech:machine_core_2
setblock 11 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "138.2"}','{"text": "oritech"}','{"text": "pipes"}','{"text": ""}']}}
setblock 12 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Leg Rohre"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 21 64 281 21 79 296 minecraft:light_gray_concrete
setblock 13 64 286 oritech:pulverizer_block
setblock 18 64 286 oritech:pulverizer_block
kw testworld use 14 63 286 up oritech:energy_pipe
kw testworld use 15 63 286 up oritech:energy_pipe
kw testworld use 16 63 286 up oritech:energy_pipe
kw testworld use 17 63 286 up oritech:energy_pipe
kw testworld use 14 63 287 up oritech:item_pipe
kw testworld use 15 63 287 up oritech:item_pipe
kw testworld use 16 63 287 up oritech:item_pipe
kw testworld use 17 63 287 up oritech:item_pipe
setblock 22 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "138.3"}','{"text": "oritech"}','{"text": "plastic"}','{"text": ""}']}}
setblock 23 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Mach Plastik"}','{"text": "aus Weizen"}','{"text": ""}','{"text": ""}']}}
fill 31 64 281 31 79 296 minecraft:light_gray_concrete
setblock 24 64 286 minecraft:smooth_stone_slab
summon item_display 24.5 64.95 286.5 {item:{id:"oritech:packed_wheat",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 26 64 286 minecraft:smooth_stone_slab
summon item_display 26.5 64.95 286.5 {item:{id:"oritech:raw_biopolymer",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 28 64 286 minecraft:smooth_stone_slab
summon item_display 28.5 64.95 286.5 {item:{id:"oritech:plastic_sheet",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 32 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "138.4"}','{"text": "oritech"}','{"text": "laser"}','{"text": ""}']}}
setblock 33 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den"}','{"text": "Enderischen"}','{"text": "Laser"}','{"text": ""}']}}
fill 41 64 281 41 79 296 minecraft:light_gray_concrete
kw testworld use 36 63 286 up oritech:laser_arm_block
setblock 42 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "138.5"}','{"text": "oritech"}','{"text": "atomic_forge"}','{"text": ""}']}}
setblock 43 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Speis eine"}','{"text": "Atomic Forge"}','{"text": ""}','{"text": ""}']}}
fill 51 64 281 51 79 296 minecraft:light_gray_concrete
kw testworld use 46 63 286 up oritech:atomic_forge_block
setblock 52 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "138.6"}','{"text": "oritech"}','{"text": "destroyer"}','{"text": ""}']}}
setblock 53 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Spann einen"}','{"text": "Rahmen mit"}','{"text": "Zerstörer"}','{"text": ""}']}}
fill 63 64 281 63 79 296 minecraft:light_gray_concrete
fill 54 63 284 60 63 290 minecraft:farmland[moisture=7]
fill 54 64 284 60 64 290 minecraft:wheat[age=7]
setblock 54 66 284 oritech:machine_frame_block
setblock 54 66 285 oritech:machine_frame_block
setblock 54 66 286 oritech:machine_frame_block
setblock 54 66 287 oritech:machine_frame_block
setblock 54 66 288 oritech:machine_frame_block
setblock 54 66 289 oritech:machine_frame_block
setblock 54 66 290 oritech:machine_frame_block
setblock 55 66 284 oritech:machine_frame_block
setblock 55 66 290 oritech:machine_frame_block
setblock 56 66 284 oritech:machine_frame_block
setblock 56 66 290 oritech:machine_frame_block
setblock 57 66 284 oritech:machine_frame_block
setblock 57 66 290 oritech:machine_frame_block
setblock 58 66 284 oritech:machine_frame_block
setblock 58 66 290 oritech:machine_frame_block
setblock 59 66 284 oritech:machine_frame_block
setblock 59 66 290 oritech:machine_frame_block
setblock 60 66 284 oritech:machine_frame_block
setblock 60 66 285 oritech:machine_frame_block
setblock 60 66 286 oritech:machine_frame_block
setblock 60 66 287 oritech:machine_frame_block
setblock 60 66 288 oritech:machine_frame_block
setblock 60 66 289 oritech:machine_frame_block
setblock 60 66 290 oritech:machine_frame_block
fill 53 64 290 53 65 290 minecraft:stone_bricks
setblock 53 66 290 oritech:destroyer_block[facing=south,machine_assembled=false]
setblock 64 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "138.7"}','{"text": "oritech"}','{"text": "fragment_forge"}','{"text": ""}']}}
setblock 65 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau die"}','{"text": "Fragment Forge"}','{"text": ""}','{"text": ""}']}}
fill 73 64 281 73 79 296 minecraft:light_gray_concrete
kw testworld use 68 63 286 up oritech:fragment_forge_block
setblock 74 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "138.8"}','{"text": "oritech"}','{"text": "fragment"}','{"text": ""}']}}
setblock 75 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Schließ die"}','{"text": "Erzstraße"}','{"text": ""}','{"text": ""}']}}
fill 83 64 281 83 79 296 minecraft:light_gray_concrete
setblock 77 64 286 minecraft:smooth_stone_slab
summon item_display 77.5 64.95 286.5 {item:{id:"oritech:iron_clump",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 79 64 286 minecraft:smooth_stone_slab
summon item_display 79.5 64.95 286.5 {item:{id:"oritech:iron_gem",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 84 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "138.9"}','{"text": "oritech"}','{"text": "addons"}','{"text": ""}']}}
setblock 85 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz ein Speed"}','{"text": "Addon an"}','{"text": ""}','{"text": ""}']}}
fill 93 64 281 93 79 296 minecraft:light_gray_concrete
setblock 88 64 286 minecraft:smooth_stone_slab
summon item_display 88.5 65.4 286.5 {item:{id:"oritech:machine_speed_addon",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 94 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "138.10"}','{"text": "oritech"}','{"text": "addon_quarry"}','{"text": ""}']}}
setblock 95 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Mach einen"}','{"text": "Steinbruch mit"}','{"text": "dem Mine-Add-On"}','{"text": ""}']}}
fill 103 64 281 103 79 296 minecraft:light_gray_concrete
setblock 98 64 286 minecraft:smooth_stone_slab
summon item_display 98.5 65.4 286.5 {item:{id:"oritech:quarry_addon",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 104 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "138.11"}','{"text": "oritech"}','{"text": "addon_crop"}','{"text": ""}']}}
setblock 105 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Ernte nur"}','{"text": "Reifes mit dem"}','{"text": "Ernte-Filter"}','{"text": ""}']}}
fill 113 64 281 113 79 296 minecraft:light_gray_concrete
setblock 108 64 286 minecraft:smooth_stone_slab
summon item_display 108.5 65.4 286.5 {item:{id:"oritech:crop_filter_addon",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 114 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "138.12"}','{"text": "oritech"}','{"text": "exo"}','{"text": ""}']}}
setblock 115 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Zieh die"}','{"text": "Exo-Rüstung an"}','{"text": ""}','{"text": ""}']}}
fill 123 64 281 123 79 296 minecraft:light_gray_concrete
summon armor_stand 118.5 64 286.5 {ArmorItems:[{id:"oritech:exo_boots",count:1},{id:"oritech:exo_leggings",count:1},{id:"oritech:exo_chestplate",count:1},{id:"oritech:exo_helmet",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 124 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "138.13"}','{"text": "oritech"}','{"text": "reactor"}','{"text": ""}']}}
setblock 125 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Kernreaktor"}','{"text": ""}','{"text": ""}']}}
fill 133 64 281 133 79 296 minecraft:light_gray_concrete
fill 127 64 285 129 67 287 oritech:reactor_wall
setblock 128 65 286 oritech:reactor_rod[lit=false]
setblock 128 66 286 minecraft:air
setblock 128 67 286 oritech:reactor_fuel_port
setblock 128 65 287 oritech:reactor_controller[facing=south]
setblock 130 65 286 oritech:reactor_energy_port[facing=west]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
