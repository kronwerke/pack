# 130 industrial/sower, bio, crusher
#area 38 252 77 277
fill 38 64 252 77 91 277 minecraft:air
fill 38 60 252 77 62 277 minecraft:stone
fill 38 63 252 77 63 277 minecraft:light_gray_concrete
fill 42 64 258 77 79 258 minecraft:light_gray_concrete
fill 42 64 258 42 79 271 minecraft:light_gray_concrete
setblock 43 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "130.1"}','{"text": "industrial"}','{"text": "sower"}','{"text": ""}']}}
setblock 44 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the machines at"}','{"text": "work"}','{"text": ""}','{"text": ""}']}}
fill 52 64 258 52 79 271 minecraft:light_gray_concrete
setblock 46 64 262 minecraft:oak_log[axis=y]
setblock 48 64 262 minecraft:oak_log[axis=y]
setblock 46 64 264 minecraft:oak_log[axis=y]
setblock 48 64 264 minecraft:oak_log[axis=y]
setblock 47 64 263 industrialforegoing:plant_sower[subfacing=south]
fill 46 65 262 48 65 264 minecraft:farmland[moisture=7]
fill 46 66 262 48 66 264 minecraft:wheat[age=7]
fill 47 64 261 47 65 261 minecraft:stone_bricks
setblock 47 66 261 industrialforegoing:plant_gatherer[subfacing=south]
setblock 53 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "130.2"}','{"text": "industrial"}','{"text": "bio"}','{"text": ""}']}}
setblock 54 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Betreib einen"}','{"text": "Biogenerator"}','{"text": ""}','{"text": ""}']}}
fill 62 64 258 62 79 271 minecraft:light_gray_concrete
setblock 57 64 263 industrialforegoing:bioreactor[subfacing=south]
setblock 63 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "130.3"}','{"text": "industrial"}','{"text": "crusher"}','{"text": ""}']}}
setblock 64 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell einen"}','{"text": "Monsterschnetzler"}','{"text": "auf"}','{"text": ""}']}}
fill 72 64 258 72 79 271 minecraft:light_gray_concrete
setblock 65 64 262 minecraft:oak_fence
setblock 65 64 265 minecraft:oak_fence
setblock 66 64 262 minecraft:oak_fence
setblock 66 64 265 minecraft:oak_fence
setblock 67 64 262 minecraft:oak_fence
setblock 67 64 265 minecraft:oak_fence
setblock 68 64 262 minecraft:oak_fence
setblock 68 64 265 minecraft:oak_fence
setblock 69 64 262 minecraft:oak_fence
setblock 69 64 265 minecraft:oak_fence
setblock 65 64 263 minecraft:oak_fence
setblock 69 64 263 minecraft:oak_fence
setblock 65 64 264 minecraft:oak_fence
setblock 69 64 264 minecraft:oak_fence
summon minecraft:cow 66.5 64 263.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
summon minecraft:cow 68.5 64 264.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 67 64 261 industrialforegoing:mob_crusher[subfacing=south]
setblock 70 64 263 industrialforegoing:mob_duplicator
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
