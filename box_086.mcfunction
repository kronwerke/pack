# 086 industrial/sower, bio, crusher
#area -4 212 35 237
fill -4 64 212 35 91 237 minecraft:air
fill -4 60 212 35 62 237 minecraft:stone
fill -4 63 212 35 63 237 minecraft:light_gray_concrete
fill 0 64 218 35 79 218 minecraft:light_gray_concrete
fill 0 64 218 0 79 231 minecraft:light_gray_concrete
setblock 1 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "086.1"}','{"text": "industrial"}','{"text": "sower"}','{"text": ""}']}}
setblock 2 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the machines at"}','{"text": "work"}','{"text": ""}','{"text": ""}']}}
fill 10 64 218 10 79 231 minecraft:light_gray_concrete
setblock 4 64 222 minecraft:oak_log[axis=y]
setblock 6 64 222 minecraft:oak_log[axis=y]
setblock 4 64 224 minecraft:oak_log[axis=y]
setblock 6 64 224 minecraft:oak_log[axis=y]
setblock 5 64 223 industrialforegoing:plant_sower[subfacing=south]
fill 4 65 222 6 65 224 minecraft:farmland[moisture=7]
fill 4 66 222 6 66 224 minecraft:wheat[age=7]
fill 5 64 221 5 65 221 minecraft:stone_bricks
setblock 5 66 221 industrialforegoing:plant_gatherer[subfacing=south]
setblock 11 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "086.2"}','{"text": "industrial"}','{"text": "bio"}','{"text": ""}']}}
setblock 12 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Betreib einen"}','{"text": "Biogenerator"}','{"text": ""}','{"text": ""}']}}
fill 20 64 218 20 79 231 minecraft:light_gray_concrete
setblock 15 64 223 industrialforegoing:bioreactor[subfacing=south]
setblock 21 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "086.3"}','{"text": "industrial"}','{"text": "crusher"}','{"text": ""}']}}
setblock 22 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell einen"}','{"text": "Monsterschnetzler"}','{"text": "auf"}','{"text": ""}']}}
fill 30 64 218 30 79 231 minecraft:light_gray_concrete
setblock 23 64 222 minecraft:oak_fence
setblock 23 64 225 minecraft:oak_fence
setblock 24 64 222 minecraft:oak_fence
setblock 24 64 225 minecraft:oak_fence
setblock 25 64 222 minecraft:oak_fence
setblock 25 64 225 minecraft:oak_fence
setblock 26 64 222 minecraft:oak_fence
setblock 26 64 225 minecraft:oak_fence
setblock 27 64 222 minecraft:oak_fence
setblock 27 64 225 minecraft:oak_fence
setblock 23 64 223 minecraft:oak_fence
setblock 27 64 223 minecraft:oak_fence
setblock 23 64 224 minecraft:oak_fence
setblock 27 64 224 minecraft:oak_fence
summon minecraft:cow 24.5 64 223.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
summon minecraft:cow 26.5 64 224.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 25 64 221 industrialforegoing:mob_crusher[subfacing=south]
setblock 28 64 223 industrialforegoing:mob_duplicator
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
