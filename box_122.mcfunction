# 122 oritech/cores, pipes, laser, atomic_forge, destroyer, fragment_forge, exo, reactor
#area -4 235 88 262
fill -4 64 235 36 91 262 minecraft:air
fill 37 64 235 77 91 262 minecraft:air
fill 78 64 235 88 91 262 minecraft:air
fill -4 60 235 88 62 262 minecraft:stone
fill -4 63 235 88 63 262 minecraft:light_gray_concrete
fill 0 64 241 88 79 241 minecraft:light_gray_concrete
fill 0 64 241 0 79 256 minecraft:light_gray_concrete
setblock 1 64 255 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "122.1"}','{"text": "oritech"}','{"text": "cores"}','{"text": ""}']}}
setblock 2 64 255 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau"}','{"text": "Maschinenkerne"}','{"text": ""}','{"text": ""}']}}
fill 10 64 241 10 79 256 minecraft:light_gray_concrete
setblock 4 64 246 oritech:machine_core_1
setblock 6 64 246 oritech:machine_core_2
setblock 11 64 255 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "122.2"}','{"text": "oritech"}','{"text": "pipes"}','{"text": ""}']}}
setblock 12 64 255 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Leg Rohre"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 21 64 241 21 79 256 minecraft:light_gray_concrete
setblock 13 64 246 oritech:pulverizer_block
setblock 18 64 246 oritech:pulverizer_block
kw testworld use 14 63 246 up oritech:energy_pipe
kw testworld use 15 63 246 up oritech:energy_pipe
kw testworld use 16 63 246 up oritech:energy_pipe
kw testworld use 17 63 246 up oritech:energy_pipe
kw testworld use 14 63 247 up oritech:item_pipe
kw testworld use 15 63 247 up oritech:item_pipe
kw testworld use 16 63 247 up oritech:item_pipe
kw testworld use 17 63 247 up oritech:item_pipe
setblock 22 64 255 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "122.3"}','{"text": "oritech"}','{"text": "laser"}','{"text": ""}']}}
setblock 23 64 255 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den"}','{"text": "Enderischen"}','{"text": "Laser"}','{"text": ""}']}}
fill 31 64 241 31 79 256 minecraft:light_gray_concrete
kw testworld use 26 63 246 up oritech:laser_arm_block
setblock 32 64 255 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "122.4"}','{"text": "oritech"}','{"text": "atomic_forge"}','{"text": ""}']}}
setblock 33 64 255 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Speis eine"}','{"text": "Atomic Forge"}','{"text": ""}','{"text": ""}']}}
fill 41 64 241 41 79 256 minecraft:light_gray_concrete
kw testworld use 36 63 246 up oritech:atomic_forge_block
setblock 42 64 255 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "122.5"}','{"text": "oritech"}','{"text": "destroyer"}','{"text": ""}']}}
setblock 43 64 255 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Spann einen"}','{"text": "Rahmen mit"}','{"text": "Zerstörer"}','{"text": ""}']}}
fill 53 64 241 53 79 256 minecraft:light_gray_concrete
fill 44 63 244 50 63 250 minecraft:farmland[moisture=7]
fill 44 64 244 50 64 250 minecraft:wheat[age=7]
setblock 44 66 244 oritech:machine_frame_block
setblock 44 66 245 oritech:machine_frame_block
setblock 44 66 246 oritech:machine_frame_block
setblock 44 66 247 oritech:machine_frame_block
setblock 44 66 248 oritech:machine_frame_block
setblock 44 66 249 oritech:machine_frame_block
setblock 44 66 250 oritech:machine_frame_block
setblock 45 66 244 oritech:machine_frame_block
setblock 45 66 250 oritech:machine_frame_block
setblock 46 66 244 oritech:machine_frame_block
setblock 46 66 250 oritech:machine_frame_block
setblock 47 66 244 oritech:machine_frame_block
setblock 47 66 250 oritech:machine_frame_block
setblock 48 66 244 oritech:machine_frame_block
setblock 48 66 250 oritech:machine_frame_block
setblock 49 66 244 oritech:machine_frame_block
setblock 49 66 250 oritech:machine_frame_block
setblock 50 66 244 oritech:machine_frame_block
setblock 50 66 245 oritech:machine_frame_block
setblock 50 66 246 oritech:machine_frame_block
setblock 50 66 247 oritech:machine_frame_block
setblock 50 66 248 oritech:machine_frame_block
setblock 50 66 249 oritech:machine_frame_block
setblock 50 66 250 oritech:machine_frame_block
fill 43 64 250 43 65 250 minecraft:stone_bricks
setblock 43 66 250 oritech:destroyer_block[facing=south,machine_assembled=false]
setblock 54 64 255 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "122.6"}','{"text": "oritech"}','{"text": "fragment_forge"}','{"text": ""}']}}
setblock 55 64 255 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau die"}','{"text": "Fragment Forge"}','{"text": ""}','{"text": ""}']}}
fill 63 64 241 63 79 256 minecraft:light_gray_concrete
kw testworld use 58 63 246 up oritech:fragment_forge_block
setblock 64 64 255 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "122.7"}','{"text": "oritech"}','{"text": "exo"}','{"text": ""}']}}
setblock 65 64 255 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Zieh die"}','{"text": "Exo-Rüstung an"}','{"text": ""}','{"text": ""}']}}
fill 73 64 241 73 79 256 minecraft:light_gray_concrete
summon armor_stand 68.5 64 246.5 {ArmorItems:[{id:"oritech:exo_boots",count:1},{id:"oritech:exo_leggings",count:1},{id:"oritech:exo_chestplate",count:1},{id:"oritech:exo_helmet",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 74 64 255 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "122.8"}','{"text": "oritech"}','{"text": "reactor"}','{"text": ""}']}}
setblock 75 64 255 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Kernreaktor"}','{"text": ""}','{"text": ""}']}}
fill 83 64 241 83 79 256 minecraft:light_gray_concrete
fill 77 64 245 79 67 247 oritech:reactor_wall
setblock 78 65 246 oritech:reactor_rod[lit=false]
setblock 78 66 246 minecraft:air
setblock 78 67 246 oritech:reactor_fuel_port
setblock 78 65 247 oritech:reactor_controller[facing=south]
setblock 80 65 246 oritech:reactor_energy_port[facing=west]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
