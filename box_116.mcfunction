# 116 industrial/sower, bio, crusher
#area 38 216 77 241
fill 38 64 216 77 91 241 minecraft:air
fill 38 60 216 77 62 241 minecraft:stone
fill 38 63 216 77 63 241 minecraft:light_gray_concrete
fill 42 64 222 77 79 222 minecraft:light_gray_concrete
fill 42 64 222 42 79 235 minecraft:light_gray_concrete
setblock 43 64 234 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "116.1"}','{"text": "industrial"}','{"text": "sower"}','{"text": ""}']}}
setblock 44 64 234 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the machines at"}','{"text": "work"}','{"text": ""}','{"text": ""}']}}
fill 52 64 222 52 79 235 minecraft:light_gray_concrete
setblock 46 64 226 minecraft:oak_log[axis=y]
setblock 48 64 226 minecraft:oak_log[axis=y]
setblock 46 64 228 minecraft:oak_log[axis=y]
setblock 48 64 228 minecraft:oak_log[axis=y]
setblock 47 64 227 industrialforegoing:plant_sower[subfacing=south]
fill 46 65 226 48 65 228 minecraft:farmland[moisture=7]
fill 46 66 226 48 66 228 minecraft:wheat[age=7]
fill 47 64 225 47 65 225 minecraft:stone_bricks
setblock 47 66 225 industrialforegoing:plant_gatherer[subfacing=south]
setblock 53 64 234 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "116.2"}','{"text": "industrial"}','{"text": "bio"}','{"text": ""}']}}
setblock 54 64 234 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Betreib einen"}','{"text": "Biogenerator"}','{"text": ""}','{"text": ""}']}}
fill 62 64 222 62 79 235 minecraft:light_gray_concrete
setblock 57 64 227 industrialforegoing:bioreactor[subfacing=south]
setblock 63 64 234 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "116.3"}','{"text": "industrial"}','{"text": "crusher"}','{"text": ""}']}}
setblock 64 64 234 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell einen"}','{"text": "Monsterschnetzler"}','{"text": "auf"}','{"text": ""}']}}
fill 72 64 222 72 79 235 minecraft:light_gray_concrete
setblock 65 64 226 minecraft:oak_fence
setblock 65 64 229 minecraft:oak_fence
setblock 66 64 226 minecraft:oak_fence
setblock 66 64 229 minecraft:oak_fence
setblock 67 64 226 minecraft:oak_fence
setblock 67 64 229 minecraft:oak_fence
setblock 68 64 226 minecraft:oak_fence
setblock 68 64 229 minecraft:oak_fence
setblock 69 64 226 minecraft:oak_fence
setblock 69 64 229 minecraft:oak_fence
setblock 65 64 227 minecraft:oak_fence
setblock 69 64 227 minecraft:oak_fence
setblock 65 64 228 minecraft:oak_fence
setblock 69 64 228 minecraft:oak_fence
summon minecraft:cow 66.5 64 227.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
summon minecraft:cow 68.5 64 228.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 67 64 225 industrialforegoing:mob_crusher[subfacing=south]
setblock 70 64 227 industrialforegoing:mob_duplicator
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
