# 079 oritech/cores, laser, atomic_forge, destroyer, fragment_forge, exo
#area -4 212 67 239
fill -4 64 212 36 91 239 minecraft:air
fill 37 64 212 67 91 239 minecraft:air
fill -4 60 212 67 62 239 minecraft:stone
fill -4 63 212 67 63 239 minecraft:light_gray_concrete
fill 0 64 218 67 79 218 minecraft:light_gray_concrete
fill 0 64 218 0 79 233 minecraft:light_gray_concrete
setblock 1 64 232 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "079.1"}','{"text": "oritech"}','{"text": "cores"}','{"text": ""}']}}
setblock 2 64 232 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau"}','{"text": "Maschinenkerne"}','{"text": ""}','{"text": ""}']}}
fill 10 64 218 10 79 233 minecraft:light_gray_concrete
setblock 4 64 223 oritech:machine_core_1
setblock 6 64 223 oritech:machine_core_2
setblock 11 64 232 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "079.2"}','{"text": "oritech"}','{"text": "laser"}','{"text": ""}']}}
setblock 12 64 232 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den"}','{"text": "Enderischen"}','{"text": "Laser"}','{"text": ""}']}}
fill 20 64 218 20 79 233 minecraft:light_gray_concrete
kw testworld use 15 63 223 up oritech:laser_arm_block
setblock 21 64 232 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "079.3"}','{"text": "oritech"}','{"text": "atomic_forge"}','{"text": ""}']}}
setblock 22 64 232 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Speis eine"}','{"text": "Atomic Forge"}','{"text": ""}','{"text": ""}']}}
fill 30 64 218 30 79 233 minecraft:light_gray_concrete
kw testworld use 25 63 223 up oritech:atomic_forge_block
setblock 31 64 232 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "079.4"}','{"text": "oritech"}','{"text": "destroyer"}','{"text": ""}']}}
setblock 32 64 232 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Spann einen"}','{"text": "Rahmen mit"}','{"text": "Zerstörer"}','{"text": ""}']}}
fill 42 64 218 42 79 233 minecraft:light_gray_concrete
fill 33 63 221 39 63 227 minecraft:farmland[moisture=7]
fill 33 64 221 39 64 227 minecraft:wheat[age=7]
setblock 33 66 221 oritech:machine_frame_block
setblock 33 66 222 oritech:machine_frame_block
setblock 33 66 223 oritech:machine_frame_block
setblock 33 66 224 oritech:machine_frame_block
setblock 33 66 225 oritech:machine_frame_block
setblock 33 66 226 oritech:machine_frame_block
setblock 33 66 227 oritech:machine_frame_block
setblock 34 66 221 oritech:machine_frame_block
setblock 34 66 227 oritech:machine_frame_block
setblock 35 66 221 oritech:machine_frame_block
setblock 35 66 227 oritech:machine_frame_block
setblock 36 66 221 oritech:machine_frame_block
setblock 36 66 227 oritech:machine_frame_block
setblock 37 66 221 oritech:machine_frame_block
setblock 37 66 227 oritech:machine_frame_block
setblock 38 66 221 oritech:machine_frame_block
setblock 38 66 227 oritech:machine_frame_block
setblock 39 66 221 oritech:machine_frame_block
setblock 39 66 222 oritech:machine_frame_block
setblock 39 66 223 oritech:machine_frame_block
setblock 39 66 224 oritech:machine_frame_block
setblock 39 66 225 oritech:machine_frame_block
setblock 39 66 226 oritech:machine_frame_block
setblock 39 66 227 oritech:machine_frame_block
fill 32 64 227 32 65 227 minecraft:stone_bricks
setblock 32 66 227 oritech:destroyer_block[facing=south,machine_assembled=false]
setblock 43 64 232 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "079.5"}','{"text": "oritech"}','{"text": "fragment_forge"}','{"text": ""}']}}
setblock 44 64 232 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau die"}','{"text": "Fragment Forge"}','{"text": ""}','{"text": ""}']}}
fill 52 64 218 52 79 233 minecraft:light_gray_concrete
kw testworld use 47 63 223 up oritech:fragment_forge_block
setblock 53 64 232 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "079.6"}','{"text": "oritech"}','{"text": "exo"}','{"text": ""}']}}
setblock 54 64 232 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Zieh die"}','{"text": "Exo-Rüstung an"}','{"text": ""}','{"text": ""}']}}
fill 62 64 218 62 79 233 minecraft:light_gray_concrete
summon armor_stand 57.5 64 223.5 {ArmorItems:[{id:"oritech:exo_boots",count:1},{id:"oritech:exo_leggings",count:1},{id:"oritech:exo_chestplate",count:1},{id:"oritech:exo_helmet",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
