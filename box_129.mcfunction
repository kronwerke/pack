# 129 oritech/cores, pipes, laser, atomic_forge, destroyer, fragment_forge, exo, reactor
#area -4 265 88 292
fill -4 64 265 36 91 292 minecraft:air
fill 37 64 265 77 91 292 minecraft:air
fill 78 64 265 88 91 292 minecraft:air
fill -4 60 265 88 62 292 minecraft:stone
fill -4 63 265 88 63 292 minecraft:light_gray_concrete
fill 0 64 271 88 79 271 minecraft:light_gray_concrete
fill 0 64 271 0 79 286 minecraft:light_gray_concrete
setblock 1 64 285 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "129.1"}','{"text": "oritech"}','{"text": "cores"}','{"text": ""}']}}
setblock 2 64 285 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau"}','{"text": "Maschinenkerne"}','{"text": ""}','{"text": ""}']}}
fill 10 64 271 10 79 286 minecraft:light_gray_concrete
setblock 4 64 276 oritech:machine_core_1
setblock 6 64 276 oritech:machine_core_2
setblock 11 64 285 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "129.2"}','{"text": "oritech"}','{"text": "pipes"}','{"text": ""}']}}
setblock 12 64 285 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Leg Rohre"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 21 64 271 21 79 286 minecraft:light_gray_concrete
setblock 13 64 276 oritech:pulverizer_block
setblock 18 64 276 oritech:pulverizer_block
kw testworld use 14 63 276 up oritech:energy_pipe
kw testworld use 15 63 276 up oritech:energy_pipe
kw testworld use 16 63 276 up oritech:energy_pipe
kw testworld use 17 63 276 up oritech:energy_pipe
kw testworld use 14 63 277 up oritech:item_pipe
kw testworld use 15 63 277 up oritech:item_pipe
kw testworld use 16 63 277 up oritech:item_pipe
kw testworld use 17 63 277 up oritech:item_pipe
setblock 22 64 285 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "129.3"}','{"text": "oritech"}','{"text": "laser"}','{"text": ""}']}}
setblock 23 64 285 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den"}','{"text": "Enderischen"}','{"text": "Laser"}','{"text": ""}']}}
fill 31 64 271 31 79 286 minecraft:light_gray_concrete
kw testworld use 26 63 276 up oritech:laser_arm_block
setblock 32 64 285 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "129.4"}','{"text": "oritech"}','{"text": "atomic_forge"}','{"text": ""}']}}
setblock 33 64 285 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Speis eine"}','{"text": "Atomic Forge"}','{"text": ""}','{"text": ""}']}}
fill 41 64 271 41 79 286 minecraft:light_gray_concrete
kw testworld use 36 63 276 up oritech:atomic_forge_block
setblock 42 64 285 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "129.5"}','{"text": "oritech"}','{"text": "destroyer"}','{"text": ""}']}}
setblock 43 64 285 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Spann einen"}','{"text": "Rahmen mit"}','{"text": "Zerstörer"}','{"text": ""}']}}
fill 53 64 271 53 79 286 minecraft:light_gray_concrete
fill 44 63 274 50 63 280 minecraft:farmland[moisture=7]
fill 44 64 274 50 64 280 minecraft:wheat[age=7]
setblock 44 66 274 oritech:machine_frame_block
setblock 44 66 275 oritech:machine_frame_block
setblock 44 66 276 oritech:machine_frame_block
setblock 44 66 277 oritech:machine_frame_block
setblock 44 66 278 oritech:machine_frame_block
setblock 44 66 279 oritech:machine_frame_block
setblock 44 66 280 oritech:machine_frame_block
setblock 45 66 274 oritech:machine_frame_block
setblock 45 66 280 oritech:machine_frame_block
setblock 46 66 274 oritech:machine_frame_block
setblock 46 66 280 oritech:machine_frame_block
setblock 47 66 274 oritech:machine_frame_block
setblock 47 66 280 oritech:machine_frame_block
setblock 48 66 274 oritech:machine_frame_block
setblock 48 66 280 oritech:machine_frame_block
setblock 49 66 274 oritech:machine_frame_block
setblock 49 66 280 oritech:machine_frame_block
setblock 50 66 274 oritech:machine_frame_block
setblock 50 66 275 oritech:machine_frame_block
setblock 50 66 276 oritech:machine_frame_block
setblock 50 66 277 oritech:machine_frame_block
setblock 50 66 278 oritech:machine_frame_block
setblock 50 66 279 oritech:machine_frame_block
setblock 50 66 280 oritech:machine_frame_block
fill 43 64 280 43 65 280 minecraft:stone_bricks
setblock 43 66 280 oritech:destroyer_block[facing=south,machine_assembled=false]
setblock 54 64 285 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "129.6"}','{"text": "oritech"}','{"text": "fragment_forge"}','{"text": ""}']}}
setblock 55 64 285 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau die"}','{"text": "Fragment Forge"}','{"text": ""}','{"text": ""}']}}
fill 63 64 271 63 79 286 minecraft:light_gray_concrete
kw testworld use 58 63 276 up oritech:fragment_forge_block
setblock 64 64 285 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "129.7"}','{"text": "oritech"}','{"text": "exo"}','{"text": ""}']}}
setblock 65 64 285 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Zieh die"}','{"text": "Exo-Rüstung an"}','{"text": ""}','{"text": ""}']}}
fill 73 64 271 73 79 286 minecraft:light_gray_concrete
summon armor_stand 68.5 64 276.5 {ArmorItems:[{id:"oritech:exo_boots",count:1},{id:"oritech:exo_leggings",count:1},{id:"oritech:exo_chestplate",count:1},{id:"oritech:exo_helmet",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 74 64 285 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "129.8"}','{"text": "oritech"}','{"text": "reactor"}','{"text": ""}']}}
setblock 75 64 285 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Kernreaktor"}','{"text": ""}','{"text": ""}']}}
fill 83 64 271 83 79 286 minecraft:light_gray_concrete
fill 77 64 275 79 67 277 oritech:reactor_wall
setblock 78 65 276 oritech:reactor_rod[lit=false]
setblock 78 66 276 minecraft:air
setblock 78 67 276 oritech:reactor_fuel_port
setblock 78 65 277 oritech:reactor_controller[facing=south]
setblock 80 65 276 oritech:reactor_energy_port[facing=west]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
