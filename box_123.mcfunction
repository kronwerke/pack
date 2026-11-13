# 123 occultism_afrit/unbound_afrit
#area 184 184 203 209
fill 184 64 184 203 91 209 minecraft:air
fill 184 60 184 203 62 209 minecraft:stone
fill 184 63 184 203 63 209 minecraft:light_gray_concrete
fill 188 64 190 203 79 190 minecraft:light_gray_concrete
fill 188 64 190 188 79 203 minecraft:light_gray_concrete
setblock 189 64 202 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "123"}','{"text": "occultism_afrit"}','{"text": "unbound_afrit"}','{"text": ""}']}}
setblock 190 64 202 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "fight with an"}','{"text": "unbound Afrit"}','{"text": ""}','{"text": ""}']}}
fill 198 64 190 198 79 203 minecraft:light_gray_concrete
summon occultism:afrit_wild 193.5 64 195.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
