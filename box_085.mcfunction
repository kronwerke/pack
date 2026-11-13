# 085 ars_master/ritual_awakening
#area 272 126 291 151
fill 272 64 126 291 91 151 minecraft:air
fill 272 60 126 291 62 151 minecraft:stone
fill 272 63 126 291 63 151 minecraft:light_gray_concrete
fill 276 64 132 291 79 132 minecraft:light_gray_concrete
fill 276 64 132 276 79 145 minecraft:light_gray_concrete
setblock 277 64 144 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "085"}','{"text": "ars_master"}','{"text": "ritual_awakening"}','{"text": ""}']}}
setblock 278 64 144 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a Weald Walker"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 286 64 132 286 79 145 minecraft:light_gray_concrete
summon ars_nouveau:cascading_weald_walker 281.5 64 137.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
