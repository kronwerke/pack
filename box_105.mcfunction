# 105 occultism/djinni_familiars
#area 110 180 131 205
fill 110 64 180 131 91 205 minecraft:air
fill 110 60 180 131 62 205 minecraft:stone
fill 110 63 180 131 63 205 minecraft:light_gray_concrete
fill 114 64 186 131 79 186 minecraft:light_gray_concrete
fill 114 64 186 114 79 199 minecraft:light_gray_concrete
setblock 115 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "105"}','{"text": "occultism"}','{"text": "djinni_familiars"}','{"text": ""}']}}
setblock 116 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a player with"}','{"text": "two or three"}','{"text": "familiars"}','{"text": ""}']}}
fill 126 64 186 126 79 199 minecraft:light_gray_concrete
summon occultism:dragon_familiar 117.5 64 191.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
summon occultism:greedy_familiar 120.5 64 191.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
summon occultism:deer_familiar 123.5 64 191.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
