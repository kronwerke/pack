# 075 ars_master/ritual_awakening
#area 212 124 231 149
fill 212 64 124 231 91 149 minecraft:air
fill 212 60 124 231 62 149 minecraft:stone
fill 212 63 124 231 63 149 minecraft:light_gray_concrete
fill 216 64 130 231 79 130 minecraft:light_gray_concrete
fill 216 64 130 216 79 143 minecraft:light_gray_concrete
setblock 217 64 142 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "075"}','{"text": "ars_master"}','{"text": "ritual_awakening"}','{"text": ""}']}}
setblock 218 64 142 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a Weald Walker"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 226 64 130 226 79 143 minecraft:light_gray_concrete
summon ars_nouveau:cascading_weald_walker 221.5 64 135.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
