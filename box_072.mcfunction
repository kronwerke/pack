# 072 ars_master/ritual_awakening
#area 212 118 231 143
fill 212 64 118 231 91 143 minecraft:air
fill 212 60 118 231 62 143 minecraft:stone
fill 212 63 118 231 63 143 minecraft:light_gray_concrete
fill 216 64 124 231 79 124 minecraft:light_gray_concrete
fill 216 64 124 216 79 137 minecraft:light_gray_concrete
setblock 217 64 136 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "072"}','{"text": "ars_master"}','{"text": "ritual_awakening"}','{"text": ""}']}}
setblock 218 64 136 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a Weald Walker"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 226 64 124 226 79 137 minecraft:light_gray_concrete
summon ars_nouveau:cascading_weald_walker 221.5 64 129.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
