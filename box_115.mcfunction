# 115 oritech/cores, laser, atomic_forge, destroyer, fragment_forge, exo, reactor
#area -4 233 77 260
fill -4 64 233 36 91 260 minecraft:air
fill 37 64 233 77 91 260 minecraft:air
fill -4 60 233 77 62 260 minecraft:stone
fill -4 63 233 77 63 260 minecraft:light_gray_concrete
fill 0 64 239 77 79 239 minecraft:light_gray_concrete
fill 0 64 239 0 79 254 minecraft:light_gray_concrete
setblock 1 64 253 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "115.1"}','{"text": "oritech"}','{"text": "cores"}','{"text": ""}']}}
setblock 2 64 253 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau"}','{"text": "Maschinenkerne"}','{"text": ""}','{"text": ""}']}}
fill 10 64 239 10 79 254 minecraft:light_gray_concrete
setblock 4 64 244 oritech:machine_core_1
setblock 6 64 244 oritech:machine_core_2
setblock 11 64 253 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "115.2"}','{"text": "oritech"}','{"text": "laser"}','{"text": ""}']}}
setblock 12 64 253 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den"}','{"text": "Enderischen"}','{"text": "Laser"}','{"text": ""}']}}
fill 20 64 239 20 79 254 minecraft:light_gray_concrete
kw testworld use 15 63 244 up oritech:laser_arm_block
setblock 21 64 253 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "115.3"}','{"text": "oritech"}','{"text": "atomic_forge"}','{"text": ""}']}}
setblock 22 64 253 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Speis eine"}','{"text": "Atomic Forge"}','{"text": ""}','{"text": ""}']}}
fill 30 64 239 30 79 254 minecraft:light_gray_concrete
kw testworld use 25 63 244 up oritech:atomic_forge_block
setblock 31 64 253 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "115.4"}','{"text": "oritech"}','{"text": "destroyer"}','{"text": ""}']}}
setblock 32 64 253 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Spann einen"}','{"text": "Rahmen mit"}','{"text": "Zerstörer"}','{"text": ""}']}}
fill 42 64 239 42 79 254 minecraft:light_gray_concrete
fill 33 63 242 39 63 248 minecraft:farmland[moisture=7]
fill 33 64 242 39 64 248 minecraft:wheat[age=7]
setblock 33 66 242 oritech:machine_frame_block
setblock 33 66 243 oritech:machine_frame_block
setblock 33 66 244 oritech:machine_frame_block
setblock 33 66 245 oritech:machine_frame_block
setblock 33 66 246 oritech:machine_frame_block
setblock 33 66 247 oritech:machine_frame_block
setblock 33 66 248 oritech:machine_frame_block
setblock 34 66 242 oritech:machine_frame_block
setblock 34 66 248 oritech:machine_frame_block
setblock 35 66 242 oritech:machine_frame_block
setblock 35 66 248 oritech:machine_frame_block
setblock 36 66 242 oritech:machine_frame_block
setblock 36 66 248 oritech:machine_frame_block
setblock 37 66 242 oritech:machine_frame_block
setblock 37 66 248 oritech:machine_frame_block
setblock 38 66 242 oritech:machine_frame_block
setblock 38 66 248 oritech:machine_frame_block
setblock 39 66 242 oritech:machine_frame_block
setblock 39 66 243 oritech:machine_frame_block
setblock 39 66 244 oritech:machine_frame_block
setblock 39 66 245 oritech:machine_frame_block
setblock 39 66 246 oritech:machine_frame_block
setblock 39 66 247 oritech:machine_frame_block
setblock 39 66 248 oritech:machine_frame_block
fill 32 64 248 32 65 248 minecraft:stone_bricks
setblock 32 66 248 oritech:destroyer_block[facing=south,machine_assembled=false]
setblock 43 64 253 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "115.5"}','{"text": "oritech"}','{"text": "fragment_forge"}','{"text": ""}']}}
setblock 44 64 253 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau die"}','{"text": "Fragment Forge"}','{"text": ""}','{"text": ""}']}}
fill 52 64 239 52 79 254 minecraft:light_gray_concrete
kw testworld use 47 63 244 up oritech:fragment_forge_block
setblock 53 64 253 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "115.6"}','{"text": "oritech"}','{"text": "exo"}','{"text": ""}']}}
setblock 54 64 253 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Zieh die"}','{"text": "Exo-Rüstung an"}','{"text": ""}','{"text": ""}']}}
fill 62 64 239 62 79 254 minecraft:light_gray_concrete
summon armor_stand 57.5 64 244.5 {ArmorItems:[{id:"oritech:exo_boots",count:1},{id:"oritech:exo_leggings",count:1},{id:"oritech:exo_chestplate",count:1},{id:"oritech:exo_helmet",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 63 64 253 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "115.7"}','{"text": "oritech"}','{"text": "reactor"}','{"text": ""}']}}
setblock 64 64 253 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Kernreaktor"}','{"text": ""}','{"text": ""}']}}
fill 72 64 239 72 79 254 minecraft:light_gray_concrete
fill 66 64 243 68 67 245 oritech:reactor_wall
setblock 67 65 244 oritech:reactor_rod[lit=false]
setblock 67 66 244 minecraft:air
setblock 67 67 244 oritech:reactor_fuel_port
setblock 67 65 245 oritech:reactor_controller[facing=south]
setblock 69 65 244 oritech:reactor_energy_port[facing=west]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
