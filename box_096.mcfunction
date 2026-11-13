# 096 occultism_afrit/unbound_afrit
#area 169 146 188 171
fill 169 64 146 188 91 171 minecraft:air
fill 169 60 146 188 62 171 minecraft:stone
fill 169 63 146 188 63 171 minecraft:light_gray_concrete
fill 173 64 152 188 79 152 minecraft:light_gray_concrete
fill 173 64 152 173 79 165 minecraft:light_gray_concrete
setblock 174 64 164 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "096"}','{"text": "occultism_afrit"}','{"text": "unbound_afrit"}','{"text": ""}']}}
setblock 175 64 164 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "fight with an"}','{"text": "unbound Afrit"}','{"text": ""}','{"text": ""}']}}
fill 183 64 152 183 79 165 minecraft:light_gray_concrete
summon occultism:afrit_wild 178.5 64 157.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
