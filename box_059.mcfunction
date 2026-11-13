# 059 ars_master/tribute
#area 180 88 199 113
fill 180 64 88 199 91 113 minecraft:air
fill 180 60 88 199 62 113 minecraft:stone
fill 180 63 88 199 63 113 minecraft:light_gray_concrete
fill 184 64 94 199 79 94 minecraft:light_gray_concrete
fill 184 64 94 184 79 107 minecraft:light_gray_concrete
setblock 185 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "059"}','{"text": "ars_master"}','{"text": "tribute"}','{"text": ""}']}}
setblock 186 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the Chimera mid"}','{"text": "fight"}','{"text": ""}','{"text": ""}']}}
fill 194 64 94 194 79 107 minecraft:light_gray_concrete
summon ars_nouveau:wilden_boss 189.5 64 99.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
