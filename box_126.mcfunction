# 126 industrial/sower, bio, crusher
#area 38 246 77 271
fill 38 64 246 77 91 271 minecraft:air
fill 38 60 246 77 62 271 minecraft:stone
fill 38 63 246 77 63 271 minecraft:light_gray_concrete
fill 42 64 252 77 79 252 minecraft:light_gray_concrete
fill 42 64 252 42 79 265 minecraft:light_gray_concrete
setblock 43 64 264 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "126.1"}','{"text": "industrial"}','{"text": "sower"}','{"text": ""}']}}
setblock 44 64 264 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the machines at"}','{"text": "work"}','{"text": ""}','{"text": ""}']}}
fill 52 64 252 52 79 265 minecraft:light_gray_concrete
setblock 46 64 256 minecraft:oak_log[axis=y]
setblock 48 64 256 minecraft:oak_log[axis=y]
setblock 46 64 258 minecraft:oak_log[axis=y]
setblock 48 64 258 minecraft:oak_log[axis=y]
setblock 47 64 257 industrialforegoing:plant_sower[subfacing=south]
fill 46 65 256 48 65 258 minecraft:farmland[moisture=7]
fill 46 66 256 48 66 258 minecraft:wheat[age=7]
fill 47 64 255 47 65 255 minecraft:stone_bricks
setblock 47 66 255 industrialforegoing:plant_gatherer[subfacing=south]
setblock 53 64 264 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "126.2"}','{"text": "industrial"}','{"text": "bio"}','{"text": ""}']}}
setblock 54 64 264 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Betreib einen"}','{"text": "Biogenerator"}','{"text": ""}','{"text": ""}']}}
fill 62 64 252 62 79 265 minecraft:light_gray_concrete
setblock 57 64 257 industrialforegoing:bioreactor[subfacing=south]
setblock 63 64 264 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "126.3"}','{"text": "industrial"}','{"text": "crusher"}','{"text": ""}']}}
setblock 64 64 264 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell einen"}','{"text": "Monsterschnetzler"}','{"text": "auf"}','{"text": ""}']}}
fill 72 64 252 72 79 265 minecraft:light_gray_concrete
setblock 65 64 256 minecraft:oak_fence
setblock 65 64 259 minecraft:oak_fence
setblock 66 64 256 minecraft:oak_fence
setblock 66 64 259 minecraft:oak_fence
setblock 67 64 256 minecraft:oak_fence
setblock 67 64 259 minecraft:oak_fence
setblock 68 64 256 minecraft:oak_fence
setblock 68 64 259 minecraft:oak_fence
setblock 69 64 256 minecraft:oak_fence
setblock 69 64 259 minecraft:oak_fence
setblock 65 64 257 minecraft:oak_fence
setblock 69 64 257 minecraft:oak_fence
setblock 65 64 258 minecraft:oak_fence
setblock 69 64 258 minecraft:oak_fence
summon minecraft:cow 66.5 64 257.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
summon minecraft:cow 68.5 64 258.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 67 64 255 industrialforegoing:mob_crusher[subfacing=south]
setblock 70 64 257 industrialforegoing:mob_duplicator
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
