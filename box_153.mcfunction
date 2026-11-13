# 153 oritech/cores, pipes, plastic, laser, atomic_forge, destroyer, fragment_forge, fragment, addons, addon_quarry, addon_crop, exo, reactor
#area -4 277 138 304
fill -4 64 277 36 91 304 minecraft:air
fill 37 64 277 77 91 304 minecraft:air
fill 78 64 277 118 91 304 minecraft:air
fill 119 64 277 138 91 304 minecraft:air
fill -4 60 277 138 62 304 minecraft:stone
fill -4 63 277 138 63 304 minecraft:light_gray_concrete
fill 0 64 283 138 79 283 minecraft:light_gray_concrete
fill 0 64 283 0 79 298 minecraft:light_gray_concrete
setblock 1 64 297 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "153.1"}','{"text": "oritech"}','{"text": "cores"}','{"text": ""}']}}
setblock 2 64 297 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau"}','{"text": "Maschinenkerne"}','{"text": ""}','{"text": ""}']}}
fill 10 64 283 10 79 298 minecraft:light_gray_concrete
setblock 4 64 288 oritech:machine_core_1
setblock 6 64 288 oritech:machine_core_2
setblock 11 64 297 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "153.2"}','{"text": "oritech"}','{"text": "pipes"}','{"text": ""}']}}
setblock 12 64 297 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Leg Rohre"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 21 64 283 21 79 298 minecraft:light_gray_concrete
setblock 13 64 288 oritech:pulverizer_block
setblock 18 64 288 oritech:pulverizer_block
kw testworld use 14 63 288 up oritech:energy_pipe
kw testworld use 15 63 288 up oritech:energy_pipe
kw testworld use 16 63 288 up oritech:energy_pipe
kw testworld use 17 63 288 up oritech:energy_pipe
kw testworld use 14 63 289 up oritech:item_pipe
kw testworld use 15 63 289 up oritech:item_pipe
kw testworld use 16 63 289 up oritech:item_pipe
kw testworld use 17 63 289 up oritech:item_pipe
setblock 22 64 297 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "153.3"}','{"text": "oritech"}','{"text": "plastic"}','{"text": ""}']}}
setblock 23 64 297 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Mach Plastik"}','{"text": "aus Weizen"}','{"text": ""}','{"text": ""}']}}
fill 31 64 283 31 79 298 minecraft:light_gray_concrete
setblock 24 64 288 minecraft:smooth_stone_slab
summon item_display 24.5 64.95 288.5 {item:{id:"oritech:packed_wheat",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 26 64 288 minecraft:smooth_stone_slab
summon item_display 26.5 64.95 288.5 {item:{id:"oritech:raw_biopolymer",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 28 64 288 minecraft:smooth_stone_slab
summon item_display 28.5 64.95 288.5 {item:{id:"oritech:plastic_sheet",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 32 64 297 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "153.4"}','{"text": "oritech"}','{"text": "laser"}','{"text": ""}']}}
setblock 33 64 297 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den"}','{"text": "Enderischen"}','{"text": "Laser"}','{"text": ""}']}}
fill 41 64 283 41 79 298 minecraft:light_gray_concrete
kw testworld use 36 63 288 up oritech:laser_arm_block
setblock 42 64 297 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "153.5"}','{"text": "oritech"}','{"text": "atomic_forge"}','{"text": ""}']}}
setblock 43 64 297 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Speis eine"}','{"text": "Atomic Forge"}','{"text": ""}','{"text": ""}']}}
fill 51 64 283 51 79 298 minecraft:light_gray_concrete
kw testworld use 46 63 288 up oritech:atomic_forge_block
setblock 52 64 297 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "153.6"}','{"text": "oritech"}','{"text": "destroyer"}','{"text": ""}']}}
setblock 53 64 297 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Spann einen"}','{"text": "Rahmen mit"}','{"text": "Zerstörer"}','{"text": ""}']}}
fill 63 64 283 63 79 298 minecraft:light_gray_concrete
fill 54 63 286 60 63 292 minecraft:farmland[moisture=7]
fill 54 64 286 60 64 292 minecraft:wheat[age=7]
setblock 54 66 286 oritech:machine_frame_block
setblock 54 66 287 oritech:machine_frame_block
setblock 54 66 288 oritech:machine_frame_block
setblock 54 66 289 oritech:machine_frame_block
setblock 54 66 290 oritech:machine_frame_block
setblock 54 66 291 oritech:machine_frame_block
setblock 54 66 292 oritech:machine_frame_block
setblock 55 66 286 oritech:machine_frame_block
setblock 55 66 292 oritech:machine_frame_block
setblock 56 66 286 oritech:machine_frame_block
setblock 56 66 292 oritech:machine_frame_block
setblock 57 66 286 oritech:machine_frame_block
setblock 57 66 292 oritech:machine_frame_block
setblock 58 66 286 oritech:machine_frame_block
setblock 58 66 292 oritech:machine_frame_block
setblock 59 66 286 oritech:machine_frame_block
setblock 59 66 292 oritech:machine_frame_block
setblock 60 66 286 oritech:machine_frame_block
setblock 60 66 287 oritech:machine_frame_block
setblock 60 66 288 oritech:machine_frame_block
setblock 60 66 289 oritech:machine_frame_block
setblock 60 66 290 oritech:machine_frame_block
setblock 60 66 291 oritech:machine_frame_block
setblock 60 66 292 oritech:machine_frame_block
fill 53 64 292 53 65 292 minecraft:stone_bricks
setblock 53 66 292 oritech:destroyer_block[facing=south,machine_assembled=false]
setblock 64 64 297 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "153.7"}','{"text": "oritech"}','{"text": "fragment_forge"}','{"text": ""}']}}
setblock 65 64 297 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau die"}','{"text": "Fragment Forge"}','{"text": ""}','{"text": ""}']}}
fill 73 64 283 73 79 298 minecraft:light_gray_concrete
kw testworld use 68 63 288 up oritech:fragment_forge_block
setblock 74 64 297 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "153.8"}','{"text": "oritech"}','{"text": "fragment"}','{"text": ""}']}}
setblock 75 64 297 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Schließ die"}','{"text": "Erzstraße"}','{"text": ""}','{"text": ""}']}}
fill 83 64 283 83 79 298 minecraft:light_gray_concrete
setblock 77 64 288 minecraft:smooth_stone_slab
summon item_display 77.5 64.95 288.5 {item:{id:"oritech:iron_clump",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 79 64 288 minecraft:smooth_stone_slab
summon item_display 79.5 64.95 288.5 {item:{id:"oritech:iron_gem",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 84 64 297 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "153.9"}','{"text": "oritech"}','{"text": "addons"}','{"text": ""}']}}
setblock 85 64 297 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz ein Speed"}','{"text": "Addon an"}','{"text": ""}','{"text": ""}']}}
fill 93 64 283 93 79 298 minecraft:light_gray_concrete
setblock 88 64 288 minecraft:smooth_stone_slab
summon item_display 88.5 65.4 288.5 {item:{id:"oritech:machine_speed_addon",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 94 64 297 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "153.10"}','{"text": "oritech"}','{"text": "addon_quarry"}','{"text": ""}']}}
setblock 95 64 297 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Mach einen"}','{"text": "Steinbruch mit"}','{"text": "dem Mine-Add-On"}','{"text": ""}']}}
fill 103 64 283 103 79 298 minecraft:light_gray_concrete
setblock 98 64 288 minecraft:smooth_stone_slab
summon item_display 98.5 65.4 288.5 {item:{id:"oritech:quarry_addon",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 104 64 297 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "153.11"}','{"text": "oritech"}','{"text": "addon_crop"}','{"text": ""}']}}
setblock 105 64 297 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Ernte nur"}','{"text": "Reifes mit dem"}','{"text": "Ernte-Filter"}','{"text": ""}']}}
fill 113 64 283 113 79 298 minecraft:light_gray_concrete
setblock 108 64 288 minecraft:smooth_stone_slab
summon item_display 108.5 65.4 288.5 {item:{id:"oritech:crop_filter_addon",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 114 64 297 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "153.12"}','{"text": "oritech"}','{"text": "exo"}','{"text": ""}']}}
setblock 115 64 297 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Zieh die"}','{"text": "Exo-Rüstung an"}','{"text": ""}','{"text": ""}']}}
fill 123 64 283 123 79 298 minecraft:light_gray_concrete
summon armor_stand 118.5 64 288.5 {ArmorItems:[{id:"oritech:exo_boots",count:1},{id:"oritech:exo_leggings",count:1},{id:"oritech:exo_chestplate",count:1},{id:"oritech:exo_helmet",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 124 64 297 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "153.13"}','{"text": "oritech"}','{"text": "reactor"}','{"text": ""}']}}
setblock 125 64 297 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Kernreaktor"}','{"text": ""}','{"text": ""}']}}
fill 133 64 283 133 79 298 minecraft:light_gray_concrete
fill 127 64 287 129 67 289 oritech:reactor_wall
setblock 128 65 288 oritech:reactor_rod[lit=false]
setblock 128 66 288 minecraft:air
setblock 128 67 288 oritech:reactor_fuel_port
setblock 128 65 289 oritech:reactor_controller[facing=south]
setblock 130 65 288 oritech:reactor_energy_port[facing=west]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
