# 075 ars_master/ritual_awakening
#area 212 122 231 147
fill 212 64 122 231 91 147 minecraft:air
fill 212 60 122 231 62 147 minecraft:stone
fill 212 63 122 231 63 147 minecraft:light_gray_concrete
fill 216 64 128 231 79 128 minecraft:light_gray_concrete
fill 216 64 128 216 79 141 minecraft:light_gray_concrete
setblock 217 64 140 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "075"}','{"text": "ars_master"}','{"text": "ritual_awakening"}','{"text": ""}']}}
setblock 218 64 140 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a Weald Walker"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 226 64 128 226 79 141 minecraft:light_gray_concrete
summon ars_nouveau:cascading_weald_walker 221.5 64 133.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
