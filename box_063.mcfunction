# 063 ars_master/ritual_awakening
#area 212 88 231 113
fill 212 64 88 231 91 113 minecraft:air
fill 212 60 88 231 62 113 minecraft:stone
fill 212 63 88 231 63 113 minecraft:light_gray_concrete
fill 216 64 94 231 79 94 minecraft:light_gray_concrete
fill 216 64 94 216 79 107 minecraft:light_gray_concrete
setblock 217 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "063"}','{"text": "ars_master"}','{"text": "ritual_awakening"}','{"text": ""}']}}
setblock 218 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a Weald Walker"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 226 64 94 226 79 107 minecraft:light_gray_concrete
summon ars_nouveau:cascading_weald_walker 221.5 64 99.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
