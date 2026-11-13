# 117 oritech/cores, pipes, laser, atomic_forge, destroyer, fragment_forge, exo, reactor
#area -4 233 88 260
fill -4 64 233 36 91 260 minecraft:air
fill 37 64 233 77 91 260 minecraft:air
fill 78 64 233 88 91 260 minecraft:air
fill -4 60 233 88 62 260 minecraft:stone
fill -4 63 233 88 63 260 minecraft:light_gray_concrete
fill 0 64 239 88 79 239 minecraft:light_gray_concrete
fill 0 64 239 0 79 254 minecraft:light_gray_concrete
setblock 1 64 253 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "117.1"}','{"text": "oritech"}','{"text": "cores"}','{"text": ""}']}}
setblock 2 64 253 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau"}','{"text": "Maschinenkerne"}','{"text": ""}','{"text": ""}']}}
fill 10 64 239 10 79 254 minecraft:light_gray_concrete
setblock 4 64 244 oritech:machine_core_1
setblock 6 64 244 oritech:machine_core_2
setblock 11 64 253 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "117.2"}','{"text": "oritech"}','{"text": "pipes"}','{"text": ""}']}}
setblock 12 64 253 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Leg Rohre"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 21 64 239 21 79 254 minecraft:light_gray_concrete
setblock 13 64 244 oritech:pulverizer_block
setblock 18 64 244 oritech:pulverizer_block
kw testworld use 14 63 244 up oritech:energy_pipe
kw testworld use 15 63 244 up oritech:energy_pipe
kw testworld use 16 63 244 up oritech:energy_pipe
kw testworld use 17 63 244 up oritech:energy_pipe
kw testworld use 14 63 245 up oritech:item_pipe
kw testworld use 15 63 245 up oritech:item_pipe
kw testworld use 16 63 245 up oritech:item_pipe
kw testworld use 17 63 245 up oritech:item_pipe
setblock 22 64 253 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "117.3"}','{"text": "oritech"}','{"text": "laser"}','{"text": ""}']}}
setblock 23 64 253 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den"}','{"text": "Enderischen"}','{"text": "Laser"}','{"text": ""}']}}
fill 31 64 239 31 79 254 minecraft:light_gray_concrete
kw testworld use 26 63 244 up oritech:laser_arm_block
setblock 32 64 253 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "117.4"}','{"text": "oritech"}','{"text": "atomic_forge"}','{"text": ""}']}}
setblock 33 64 253 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Speis eine"}','{"text": "Atomic Forge"}','{"text": ""}','{"text": ""}']}}
fill 41 64 239 41 79 254 minecraft:light_gray_concrete
kw testworld use 36 63 244 up oritech:atomic_forge_block
setblock 42 64 253 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "117.5"}','{"text": "oritech"}','{"text": "destroyer"}','{"text": ""}']}}
setblock 43 64 253 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Spann einen"}','{"text": "Rahmen mit"}','{"text": "Zerstörer"}','{"text": ""}']}}
fill 53 64 239 53 79 254 minecraft:light_gray_concrete
fill 44 63 242 50 63 248 minecraft:farmland[moisture=7]
fill 44 64 242 50 64 248 minecraft:wheat[age=7]
setblock 44 66 242 oritech:machine_frame_block
setblock 44 66 243 oritech:machine_frame_block
setblock 44 66 244 oritech:machine_frame_block
setblock 44 66 245 oritech:machine_frame_block
setblock 44 66 246 oritech:machine_frame_block
setblock 44 66 247 oritech:machine_frame_block
setblock 44 66 248 oritech:machine_frame_block
setblock 45 66 242 oritech:machine_frame_block
setblock 45 66 248 oritech:machine_frame_block
setblock 46 66 242 oritech:machine_frame_block
setblock 46 66 248 oritech:machine_frame_block
setblock 47 66 242 oritech:machine_frame_block
setblock 47 66 248 oritech:machine_frame_block
setblock 48 66 242 oritech:machine_frame_block
setblock 48 66 248 oritech:machine_frame_block
setblock 49 66 242 oritech:machine_frame_block
setblock 49 66 248 oritech:machine_frame_block
setblock 50 66 242 oritech:machine_frame_block
setblock 50 66 243 oritech:machine_frame_block
setblock 50 66 244 oritech:machine_frame_block
setblock 50 66 245 oritech:machine_frame_block
setblock 50 66 246 oritech:machine_frame_block
setblock 50 66 247 oritech:machine_frame_block
setblock 50 66 248 oritech:machine_frame_block
fill 43 64 248 43 65 248 minecraft:stone_bricks
setblock 43 66 248 oritech:destroyer_block[facing=south,machine_assembled=false]
setblock 54 64 253 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "117.6"}','{"text": "oritech"}','{"text": "fragment_forge"}','{"text": ""}']}}
setblock 55 64 253 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau die"}','{"text": "Fragment Forge"}','{"text": ""}','{"text": ""}']}}
fill 63 64 239 63 79 254 minecraft:light_gray_concrete
kw testworld use 58 63 244 up oritech:fragment_forge_block
setblock 64 64 253 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "117.7"}','{"text": "oritech"}','{"text": "exo"}','{"text": ""}']}}
setblock 65 64 253 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Zieh die"}','{"text": "Exo-Rüstung an"}','{"text": ""}','{"text": ""}']}}
fill 73 64 239 73 79 254 minecraft:light_gray_concrete
summon armor_stand 68.5 64 244.5 {ArmorItems:[{id:"oritech:exo_boots",count:1},{id:"oritech:exo_leggings",count:1},{id:"oritech:exo_chestplate",count:1},{id:"oritech:exo_helmet",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 74 64 253 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "117.8"}','{"text": "oritech"}','{"text": "reactor"}','{"text": ""}']}}
setblock 75 64 253 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Kernreaktor"}','{"text": ""}','{"text": ""}']}}
fill 83 64 239 83 79 254 minecraft:light_gray_concrete
fill 77 64 243 79 67 245 oritech:reactor_wall
setblock 78 65 244 oritech:reactor_rod[lit=false]
setblock 78 66 244 minecraft:air
setblock 78 67 244 oritech:reactor_fuel_port
setblock 78 65 245 oritech:reactor_controller[facing=south]
setblock 80 65 244 oritech:reactor_energy_port[facing=west]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
