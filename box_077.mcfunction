# 077 ars_master/ritual_awakening
#area 227 124 246 149
fill 227 64 124 246 91 149 minecraft:air
fill 227 60 124 246 62 149 minecraft:stone
fill 227 63 124 246 63 149 minecraft:light_gray_concrete
fill 231 64 130 246 79 130 minecraft:light_gray_concrete
fill 231 64 130 231 79 143 minecraft:light_gray_concrete
setblock 232 64 142 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "077"}','{"text": "ars_master"}','{"text": "ritual_awakening"}','{"text": ""}']}}
setblock 233 64 142 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a Weald Walker"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 241 64 130 241 79 143 minecraft:light_gray_concrete
summon ars_nouveau:cascading_weald_walker 236.5 64 135.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
