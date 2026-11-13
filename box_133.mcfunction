# 133 oritech/cores, pipes, laser, atomic_forge, destroyer, fragment_forge, exo, reactor
#area -4 269 88 296
fill -4 64 269 36 91 296 minecraft:air
fill 37 64 269 77 91 296 minecraft:air
fill 78 64 269 88 91 296 minecraft:air
fill -4 60 269 88 62 296 minecraft:stone
fill -4 63 269 88 63 296 minecraft:light_gray_concrete
fill 0 64 275 88 79 275 minecraft:light_gray_concrete
fill 0 64 275 0 79 290 minecraft:light_gray_concrete
setblock 1 64 289 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "133.1"}','{"text": "oritech"}','{"text": "cores"}','{"text": ""}']}}
setblock 2 64 289 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau"}','{"text": "Maschinenkerne"}','{"text": ""}','{"text": ""}']}}
fill 10 64 275 10 79 290 minecraft:light_gray_concrete
setblock 4 64 280 oritech:machine_core_1
setblock 6 64 280 oritech:machine_core_2
setblock 11 64 289 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "133.2"}','{"text": "oritech"}','{"text": "pipes"}','{"text": ""}']}}
setblock 12 64 289 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Leg Rohre"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 21 64 275 21 79 290 minecraft:light_gray_concrete
setblock 13 64 280 oritech:pulverizer_block
setblock 18 64 280 oritech:pulverizer_block
kw testworld use 14 63 280 up oritech:energy_pipe
kw testworld use 15 63 280 up oritech:energy_pipe
kw testworld use 16 63 280 up oritech:energy_pipe
kw testworld use 17 63 280 up oritech:energy_pipe
kw testworld use 14 63 281 up oritech:item_pipe
kw testworld use 15 63 281 up oritech:item_pipe
kw testworld use 16 63 281 up oritech:item_pipe
kw testworld use 17 63 281 up oritech:item_pipe
setblock 22 64 289 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "133.3"}','{"text": "oritech"}','{"text": "laser"}','{"text": ""}']}}
setblock 23 64 289 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den"}','{"text": "Enderischen"}','{"text": "Laser"}','{"text": ""}']}}
fill 31 64 275 31 79 290 minecraft:light_gray_concrete
kw testworld use 26 63 280 up oritech:laser_arm_block
setblock 32 64 289 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "133.4"}','{"text": "oritech"}','{"text": "atomic_forge"}','{"text": ""}']}}
setblock 33 64 289 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Speis eine"}','{"text": "Atomic Forge"}','{"text": ""}','{"text": ""}']}}
fill 41 64 275 41 79 290 minecraft:light_gray_concrete
kw testworld use 36 63 280 up oritech:atomic_forge_block
setblock 42 64 289 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "133.5"}','{"text": "oritech"}','{"text": "destroyer"}','{"text": ""}']}}
setblock 43 64 289 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Spann einen"}','{"text": "Rahmen mit"}','{"text": "Zerstörer"}','{"text": ""}']}}
fill 53 64 275 53 79 290 minecraft:light_gray_concrete
fill 44 63 278 50 63 284 minecraft:farmland[moisture=7]
fill 44 64 278 50 64 284 minecraft:wheat[age=7]
setblock 44 66 278 oritech:machine_frame_block
setblock 44 66 279 oritech:machine_frame_block
setblock 44 66 280 oritech:machine_frame_block
setblock 44 66 281 oritech:machine_frame_block
setblock 44 66 282 oritech:machine_frame_block
setblock 44 66 283 oritech:machine_frame_block
setblock 44 66 284 oritech:machine_frame_block
setblock 45 66 278 oritech:machine_frame_block
setblock 45 66 284 oritech:machine_frame_block
setblock 46 66 278 oritech:machine_frame_block
setblock 46 66 284 oritech:machine_frame_block
setblock 47 66 278 oritech:machine_frame_block
setblock 47 66 284 oritech:machine_frame_block
setblock 48 66 278 oritech:machine_frame_block
setblock 48 66 284 oritech:machine_frame_block
setblock 49 66 278 oritech:machine_frame_block
setblock 49 66 284 oritech:machine_frame_block
setblock 50 66 278 oritech:machine_frame_block
setblock 50 66 279 oritech:machine_frame_block
setblock 50 66 280 oritech:machine_frame_block
setblock 50 66 281 oritech:machine_frame_block
setblock 50 66 282 oritech:machine_frame_block
setblock 50 66 283 oritech:machine_frame_block
setblock 50 66 284 oritech:machine_frame_block
fill 43 64 284 43 65 284 minecraft:stone_bricks
setblock 43 66 284 oritech:destroyer_block[facing=south,machine_assembled=false]
setblock 54 64 289 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "133.6"}','{"text": "oritech"}','{"text": "fragment_forge"}','{"text": ""}']}}
setblock 55 64 289 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau die"}','{"text": "Fragment Forge"}','{"text": ""}','{"text": ""}']}}
fill 63 64 275 63 79 290 minecraft:light_gray_concrete
kw testworld use 58 63 280 up oritech:fragment_forge_block
setblock 64 64 289 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "133.7"}','{"text": "oritech"}','{"text": "exo"}','{"text": ""}']}}
setblock 65 64 289 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Zieh die"}','{"text": "Exo-Rüstung an"}','{"text": ""}','{"text": ""}']}}
fill 73 64 275 73 79 290 minecraft:light_gray_concrete
summon armor_stand 68.5 64 280.5 {ArmorItems:[{id:"oritech:exo_boots",count:1},{id:"oritech:exo_leggings",count:1},{id:"oritech:exo_chestplate",count:1},{id:"oritech:exo_helmet",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 74 64 289 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "133.8"}','{"text": "oritech"}','{"text": "reactor"}','{"text": ""}']}}
setblock 75 64 289 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Kernreaktor"}','{"text": ""}','{"text": ""}']}}
fill 83 64 275 83 79 290 minecraft:light_gray_concrete
fill 77 64 279 79 67 281 oritech:reactor_wall
setblock 78 65 280 oritech:reactor_rod[lit=false]
setblock 78 66 280 minecraft:air
setblock 78 67 280 oritech:reactor_fuel_port
setblock 78 65 281 oritech:reactor_controller[facing=south]
setblock 80 65 280 oritech:reactor_energy_port[facing=west]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
