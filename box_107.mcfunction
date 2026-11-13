# 107 occultism_afrit/unbound_afrit
#area 169 176 188 201
fill 169 64 176 188 91 201 minecraft:air
fill 169 60 176 188 62 201 minecraft:stone
fill 169 63 176 188 63 201 minecraft:light_gray_concrete
fill 173 64 182 188 79 182 minecraft:light_gray_concrete
fill 173 64 182 173 79 195 minecraft:light_gray_concrete
setblock 174 64 194 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "107"}','{"text": "occultism_afrit"}','{"text": "unbound_afrit"}','{"text": ""}']}}
setblock 175 64 194 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "fight with an"}','{"text": "unbound Afrit"}','{"text": ""}','{"text": ""}']}}
fill 183 64 182 183 79 195 minecraft:light_gray_concrete
summon occultism:afrit_wild 178.5 64 187.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
