# 061 ars_master/tribute
#area 180 88 201 115
fill 180 64 88 201 91 115 minecraft:air
fill 180 60 88 201 62 115 minecraft:stone
fill 180 63 88 201 63 115 minecraft:light_gray_concrete
fill 184 64 94 201 79 94 minecraft:light_gray_concrete
fill 184 64 94 184 79 109 minecraft:light_gray_concrete
setblock 185 64 108 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "061"}','{"text": "ars_master"}','{"text": "tribute"}','{"text": ""}']}}
setblock 186 64 108 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the Chimera mid"}','{"text": "fight"}','{"text": ""}','{"text": ""}']}}
fill 196 64 94 196 79 109 minecraft:light_gray_concrete
summon ars_nouveau:wilden_boss 190.5 64 100.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
