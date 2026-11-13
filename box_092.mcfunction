# 092 occultism/djinni_familiars
#area 110 146 131 171
fill 110 64 146 131 91 171 minecraft:air
fill 110 60 146 131 62 171 minecraft:stone
fill 110 63 146 131 63 171 minecraft:light_gray_concrete
fill 114 64 152 131 79 152 minecraft:light_gray_concrete
fill 114 64 152 114 79 165 minecraft:light_gray_concrete
setblock 115 64 164 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "092"}','{"text": "occultism"}','{"text": "djinni_familiars"}','{"text": ""}']}}
setblock 116 64 164 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a player with"}','{"text": "two or three"}','{"text": "familiars"}','{"text": ""}']}}
fill 126 64 152 126 79 165 minecraft:light_gray_concrete
summon occultism:dragon_familiar 117.5 64 157.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
summon occultism:greedy_familiar 120.5 64 157.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
summon occultism:deer_familiar 123.5 64 157.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
