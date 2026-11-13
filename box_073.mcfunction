# 073 ars_master/tribute
#area 180 118 201 145
fill 180 64 118 201 91 145 minecraft:air
fill 180 60 118 201 62 145 minecraft:stone
fill 180 63 118 201 63 145 minecraft:light_gray_concrete
fill 184 64 124 201 79 124 minecraft:light_gray_concrete
fill 184 64 124 184 79 139 minecraft:light_gray_concrete
setblock 185 64 138 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "073"}','{"text": "ars_master"}','{"text": "tribute"}','{"text": ""}']}}
setblock 186 64 138 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the Chimera mid"}','{"text": "fight"}','{"text": ""}','{"text": ""}']}}
fill 196 64 124 196 79 139 minecraft:light_gray_concrete
summon ars_nouveau:wilden_boss 190.5 64 130.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[0f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
