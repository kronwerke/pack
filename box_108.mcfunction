# 108 occultism_afrit/unbound_afrit
#area 169 180 188 205
fill 169 64 180 188 91 205 minecraft:air
fill 169 60 180 188 62 205 minecraft:stone
fill 169 63 180 188 63 205 minecraft:light_gray_concrete
fill 173 64 186 188 79 186 minecraft:light_gray_concrete
fill 173 64 186 173 79 199 minecraft:light_gray_concrete
setblock 174 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "108"}','{"text": "occultism_afrit"}','{"text": "unbound_afrit"}','{"text": ""}']}}
setblock 175 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "fight with an"}','{"text": "unbound Afrit"}','{"text": ""}','{"text": ""}']}}
fill 183 64 186 183 79 199 minecraft:light_gray_concrete
summon occultism:afrit_wild 178.5 64 191.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
