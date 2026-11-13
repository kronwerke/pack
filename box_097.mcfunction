# 097 industrial/sower, bio, crusher
#area 21 214 60 239
fill 21 64 214 60 91 239 minecraft:air
fill 21 60 214 60 62 239 minecraft:stone
fill 21 63 214 60 63 239 minecraft:light_gray_concrete
fill 25 64 220 60 79 220 minecraft:light_gray_concrete
fill 25 64 220 25 79 233 minecraft:light_gray_concrete
setblock 26 64 232 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "097.1"}','{"text": "industrial"}','{"text": "sower"}','{"text": ""}']}}
setblock 27 64 232 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the machines at"}','{"text": "work"}','{"text": ""}','{"text": ""}']}}
fill 35 64 220 35 79 233 minecraft:light_gray_concrete
setblock 29 64 224 minecraft:oak_log[axis=y]
setblock 31 64 224 minecraft:oak_log[axis=y]
setblock 29 64 226 minecraft:oak_log[axis=y]
setblock 31 64 226 minecraft:oak_log[axis=y]
setblock 30 64 225 industrialforegoing:plant_sower[subfacing=south]
fill 29 65 224 31 65 226 minecraft:farmland[moisture=7]
fill 29 66 224 31 66 226 minecraft:wheat[age=7]
fill 30 64 223 30 65 223 minecraft:stone_bricks
setblock 30 66 223 industrialforegoing:plant_gatherer[subfacing=south]
setblock 36 64 232 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "097.2"}','{"text": "industrial"}','{"text": "bio"}','{"text": ""}']}}
setblock 37 64 232 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Betreib einen"}','{"text": "Biogenerator"}','{"text": ""}','{"text": ""}']}}
fill 45 64 220 45 79 233 minecraft:light_gray_concrete
setblock 40 64 225 industrialforegoing:bioreactor[subfacing=south]
setblock 46 64 232 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "097.3"}','{"text": "industrial"}','{"text": "crusher"}','{"text": ""}']}}
setblock 47 64 232 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell einen"}','{"text": "Monsterschnetzler"}','{"text": "auf"}','{"text": ""}']}}
fill 55 64 220 55 79 233 minecraft:light_gray_concrete
setblock 48 64 224 minecraft:oak_fence
setblock 48 64 227 minecraft:oak_fence
setblock 49 64 224 minecraft:oak_fence
setblock 49 64 227 minecraft:oak_fence
setblock 50 64 224 minecraft:oak_fence
setblock 50 64 227 minecraft:oak_fence
setblock 51 64 224 minecraft:oak_fence
setblock 51 64 227 minecraft:oak_fence
setblock 52 64 224 minecraft:oak_fence
setblock 52 64 227 minecraft:oak_fence
setblock 48 64 225 minecraft:oak_fence
setblock 52 64 225 minecraft:oak_fence
setblock 48 64 226 minecraft:oak_fence
setblock 52 64 226 minecraft:oak_fence
summon minecraft:cow 49.5 64 225.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
summon minecraft:cow 51.5 64 226.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 50 64 223 industrialforegoing:mob_crusher[subfacing=south]
setblock 53 64 225 industrialforegoing:mob_duplicator
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
