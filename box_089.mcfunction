# 089 oritech/cores, laser, atomic_forge, destroyer, fragment_forge, exo
#area -4 231 67 258
fill -4 64 231 36 91 258 minecraft:air
fill 37 64 231 67 91 258 minecraft:air
fill -4 60 231 67 62 258 minecraft:stone
fill -4 63 231 67 63 258 minecraft:light_gray_concrete
fill 0 64 237 67 79 237 minecraft:light_gray_concrete
fill 0 64 237 0 79 252 minecraft:light_gray_concrete
setblock 1 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "089.1"}','{"text": "oritech"}','{"text": "cores"}','{"text": ""}']}}
setblock 2 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau"}','{"text": "Maschinenkerne"}','{"text": ""}','{"text": ""}']}}
fill 10 64 237 10 79 252 minecraft:light_gray_concrete
setblock 4 64 242 oritech:machine_core_1
setblock 6 64 242 oritech:machine_core_2
setblock 11 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "089.2"}','{"text": "oritech"}','{"text": "laser"}','{"text": ""}']}}
setblock 12 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den"}','{"text": "Enderischen"}','{"text": "Laser"}','{"text": ""}']}}
fill 20 64 237 20 79 252 minecraft:light_gray_concrete
kw testworld use 15 63 242 up oritech:laser_arm_block
setblock 21 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "089.3"}','{"text": "oritech"}','{"text": "atomic_forge"}','{"text": ""}']}}
setblock 22 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Speis eine"}','{"text": "Atomic Forge"}','{"text": ""}','{"text": ""}']}}
fill 30 64 237 30 79 252 minecraft:light_gray_concrete
kw testworld use 25 63 242 up oritech:atomic_forge_block
setblock 31 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "089.4"}','{"text": "oritech"}','{"text": "destroyer"}','{"text": ""}']}}
setblock 32 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Spann einen"}','{"text": "Rahmen mit"}','{"text": "Zerstörer"}','{"text": ""}']}}
fill 42 64 237 42 79 252 minecraft:light_gray_concrete
fill 33 63 240 39 63 246 minecraft:farmland[moisture=7]
fill 33 64 240 39 64 246 minecraft:wheat[age=7]
setblock 33 66 240 oritech:machine_frame_block
setblock 33 66 241 oritech:machine_frame_block
setblock 33 66 242 oritech:machine_frame_block
setblock 33 66 243 oritech:machine_frame_block
setblock 33 66 244 oritech:machine_frame_block
setblock 33 66 245 oritech:machine_frame_block
setblock 33 66 246 oritech:machine_frame_block
setblock 34 66 240 oritech:machine_frame_block
setblock 34 66 246 oritech:machine_frame_block
setblock 35 66 240 oritech:machine_frame_block
setblock 35 66 246 oritech:machine_frame_block
setblock 36 66 240 oritech:machine_frame_block
setblock 36 66 246 oritech:machine_frame_block
setblock 37 66 240 oritech:machine_frame_block
setblock 37 66 246 oritech:machine_frame_block
setblock 38 66 240 oritech:machine_frame_block
setblock 38 66 246 oritech:machine_frame_block
setblock 39 66 240 oritech:machine_frame_block
setblock 39 66 241 oritech:machine_frame_block
setblock 39 66 242 oritech:machine_frame_block
setblock 39 66 243 oritech:machine_frame_block
setblock 39 66 244 oritech:machine_frame_block
setblock 39 66 245 oritech:machine_frame_block
setblock 39 66 246 oritech:machine_frame_block
fill 32 64 246 32 65 246 minecraft:stone_bricks
setblock 32 66 246 oritech:destroyer_block[facing=south,machine_assembled=false]
setblock 43 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "089.5"}','{"text": "oritech"}','{"text": "fragment_forge"}','{"text": ""}']}}
setblock 44 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau die"}','{"text": "Fragment Forge"}','{"text": ""}','{"text": ""}']}}
fill 52 64 237 52 79 252 minecraft:light_gray_concrete
kw testworld use 47 63 242 up oritech:fragment_forge_block
setblock 53 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "089.6"}','{"text": "oritech"}','{"text": "exo"}','{"text": ""}']}}
setblock 54 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Zieh die"}','{"text": "Exo-Rüstung an"}','{"text": ""}','{"text": ""}']}}
fill 62 64 237 62 79 252 minecraft:light_gray_concrete
summon armor_stand 57.5 64 242.5 {ArmorItems:[{id:"oritech:exo_boots",count:1},{id:"oritech:exo_leggings",count:1},{id:"oritech:exo_chestplate",count:1},{id:"oritech:exo_helmet",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
