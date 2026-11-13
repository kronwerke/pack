# 092 occultism_afrit/unbound_afrit
#area 169 144 188 169
fill 169 64 144 188 91 169 minecraft:air
fill 169 60 144 188 62 169 minecraft:stone
fill 169 63 144 188 63 169 minecraft:light_gray_concrete
fill 173 64 150 188 79 150 minecraft:light_gray_concrete
fill 173 64 150 173 79 163 minecraft:light_gray_concrete
setblock 174 64 162 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "092"}','{"text": "occultism_afrit"}','{"text": "unbound_afrit"}','{"text": ""}']}}
setblock 175 64 162 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "fight with an"}','{"text": "unbound Afrit"}','{"text": ""}','{"text": ""}']}}
fill 183 64 150 183 79 163 minecraft:light_gray_concrete
summon occultism:afrit_wild 178.5 64 155.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
