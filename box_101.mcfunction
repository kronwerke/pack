# 101 occultism/djinni_familiars
#area 110 176 131 201
fill 110 64 176 131 91 201 minecraft:air
fill 110 60 176 131 62 201 minecraft:stone
fill 110 63 176 131 63 201 minecraft:light_gray_concrete
fill 114 64 182 131 79 182 minecraft:light_gray_concrete
fill 114 64 182 114 79 195 minecraft:light_gray_concrete
setblock 115 64 194 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "101"}','{"text": "occultism"}','{"text": "djinni_familiars"}','{"text": ""}']}}
setblock 116 64 194 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a player with"}','{"text": "two or three"}','{"text": "familiars"}','{"text": ""}']}}
fill 126 64 182 126 79 195 minecraft:light_gray_concrete
summon occultism:dragon_familiar 117.5 64 187.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
summon occultism:greedy_familiar 120.5 64 187.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
summon occultism:deer_familiar 123.5 64 187.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
