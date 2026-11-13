# 120 occultism/djinni_familiars
#area 125 184 146 209
fill 125 64 184 146 91 209 minecraft:air
fill 125 60 184 146 62 209 minecraft:stone
fill 125 63 184 146 63 209 minecraft:light_gray_concrete
fill 129 64 190 146 79 190 minecraft:light_gray_concrete
fill 129 64 190 129 79 203 minecraft:light_gray_concrete
setblock 130 64 202 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "120"}','{"text": "occultism"}','{"text": "djinni_familiars"}','{"text": ""}']}}
setblock 131 64 202 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a player with"}','{"text": "two or three"}','{"text": "familiars"}','{"text": ""}']}}
fill 141 64 190 141 79 203 minecraft:light_gray_concrete
summon occultism:dragon_familiar 132.5 64 195.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
summon occultism:greedy_familiar 135.5 64 195.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
summon occultism:deer_familiar 138.5 64 195.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
