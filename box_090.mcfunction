# 090 occultism/djinni_familiars
#area 110 144 131 169
fill 110 64 144 131 91 169 minecraft:air
fill 110 60 144 131 62 169 minecraft:stone
fill 110 63 144 131 63 169 minecraft:light_gray_concrete
fill 114 64 150 131 79 150 minecraft:light_gray_concrete
fill 114 64 150 114 79 163 minecraft:light_gray_concrete
setblock 115 64 162 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "090"}','{"text": "occultism"}','{"text": "djinni_familiars"}','{"text": ""}']}}
setblock 116 64 162 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a player with"}','{"text": "two or three"}','{"text": "familiars"}','{"text": ""}']}}
fill 126 64 150 126 79 163 minecraft:light_gray_concrete
summon occultism:dragon_familiar 117.5 64 155.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
summon occultism:greedy_familiar 120.5 64 155.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
summon occultism:deer_familiar 123.5 64 155.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
