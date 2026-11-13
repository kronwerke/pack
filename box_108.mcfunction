# 108 occultism_afrit/unbound_afrit
#area 169 182 188 207
fill 169 64 182 188 91 207 minecraft:air
fill 169 60 182 188 62 207 minecraft:stone
fill 169 63 182 188 63 207 minecraft:light_gray_concrete
fill 173 64 188 188 79 188 minecraft:light_gray_concrete
fill 173 64 188 173 79 201 minecraft:light_gray_concrete
setblock 174 64 200 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "108"}','{"text": "occultism_afrit"}','{"text": "unbound_afrit"}','{"text": ""}']}}
setblock 175 64 200 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "fight with an"}','{"text": "unbound Afrit"}','{"text": ""}','{"text": ""}']}}
fill 183 64 188 183 79 201 minecraft:light_gray_concrete
summon occultism:afrit_wild 178.5 64 193.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
