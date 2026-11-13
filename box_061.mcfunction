# 061 ars_master/ritual_awakening
#area 210 88 229 113
fill 210 64 88 229 91 113 minecraft:air
fill 210 60 88 229 62 113 minecraft:stone
fill 210 63 88 229 63 113 minecraft:light_gray_concrete
fill 214 64 94 229 79 94 minecraft:light_gray_concrete
fill 214 64 94 214 79 107 minecraft:light_gray_concrete
setblock 215 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "061"}','{"text": "ars_master"}','{"text": "ritual_awakening"}','{"text": ""}']}}
setblock 216 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a Weald Walker"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 224 64 94 224 79 107 minecraft:light_gray_concrete
summon ars_nouveau:cascading_weald_walker 219.5 64 99.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
