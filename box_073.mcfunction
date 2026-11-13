# 073 ars_master/tribute
#area 180 124 201 151
fill 180 64 124 201 91 151 minecraft:air
fill 180 60 124 201 62 151 minecraft:stone
fill 180 63 124 201 63 151 minecraft:light_gray_concrete
fill 184 64 130 201 79 130 minecraft:light_gray_concrete
fill 184 64 130 184 79 145 minecraft:light_gray_concrete
setblock 185 64 144 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "073"}','{"text": "ars_master"}','{"text": "tribute"}','{"text": ""}']}}
setblock 186 64 144 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the Chimera mid"}','{"text": "fight"}','{"text": ""}','{"text": ""}']}}
fill 196 64 130 196 79 145 minecraft:light_gray_concrete
summon ars_nouveau:wilden_boss 190.5 64 136.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[0f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
