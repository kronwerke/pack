# 114 industrial/sower, bio, crusher
#area 38 214 77 239
fill 38 64 214 77 91 239 minecraft:air
fill 38 60 214 77 62 239 minecraft:stone
fill 38 63 214 77 63 239 minecraft:light_gray_concrete
fill 42 64 220 77 79 220 minecraft:light_gray_concrete
fill 42 64 220 42 79 233 minecraft:light_gray_concrete
setblock 43 64 232 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "114.1"}','{"text": "industrial"}','{"text": "sower"}','{"text": ""}']}}
setblock 44 64 232 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the machines at"}','{"text": "work"}','{"text": ""}','{"text": ""}']}}
fill 52 64 220 52 79 233 minecraft:light_gray_concrete
setblock 46 64 224 minecraft:oak_log[axis=y]
setblock 48 64 224 minecraft:oak_log[axis=y]
setblock 46 64 226 minecraft:oak_log[axis=y]
setblock 48 64 226 minecraft:oak_log[axis=y]
setblock 47 64 225 industrialforegoing:plant_sower[subfacing=south]
fill 46 65 224 48 65 226 minecraft:farmland[moisture=7]
fill 46 66 224 48 66 226 minecraft:wheat[age=7]
fill 47 64 223 47 65 223 minecraft:stone_bricks
setblock 47 66 223 industrialforegoing:plant_gatherer[subfacing=south]
setblock 53 64 232 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "114.2"}','{"text": "industrial"}','{"text": "bio"}','{"text": ""}']}}
setblock 54 64 232 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Betreib einen"}','{"text": "Biogenerator"}','{"text": ""}','{"text": ""}']}}
fill 62 64 220 62 79 233 minecraft:light_gray_concrete
setblock 57 64 225 industrialforegoing:bioreactor[subfacing=south]
setblock 63 64 232 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "114.3"}','{"text": "industrial"}','{"text": "crusher"}','{"text": ""}']}}
setblock 64 64 232 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell einen"}','{"text": "Monsterschnetzler"}','{"text": "auf"}','{"text": ""}']}}
fill 72 64 220 72 79 233 minecraft:light_gray_concrete
setblock 65 64 224 minecraft:oak_fence
setblock 65 64 227 minecraft:oak_fence
setblock 66 64 224 minecraft:oak_fence
setblock 66 64 227 minecraft:oak_fence
setblock 67 64 224 minecraft:oak_fence
setblock 67 64 227 minecraft:oak_fence
setblock 68 64 224 minecraft:oak_fence
setblock 68 64 227 minecraft:oak_fence
setblock 69 64 224 minecraft:oak_fence
setblock 69 64 227 minecraft:oak_fence
setblock 65 64 225 minecraft:oak_fence
setblock 69 64 225 minecraft:oak_fence
setblock 65 64 226 minecraft:oak_fence
setblock 69 64 226 minecraft:oak_fence
summon minecraft:cow 66.5 64 225.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
summon minecraft:cow 68.5 64 226.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 67 64 223 industrialforegoing:mob_crusher[subfacing=south]
setblock 70 64 225 industrialforegoing:mob_duplicator
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
