# 073 ars_master/tribute
#area 180 122 201 149
fill 180 64 122 201 91 149 minecraft:air
fill 180 60 122 201 62 149 minecraft:stone
fill 180 63 122 201 63 149 minecraft:light_gray_concrete
fill 184 64 128 201 79 128 minecraft:light_gray_concrete
fill 184 64 128 184 79 143 minecraft:light_gray_concrete
setblock 185 64 142 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "073"}','{"text": "ars_master"}','{"text": "tribute"}','{"text": ""}']}}
setblock 186 64 142 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the Chimera mid"}','{"text": "fight"}','{"text": ""}','{"text": ""}']}}
fill 196 64 128 196 79 143 minecraft:light_gray_concrete
summon ars_nouveau:wilden_boss 190.5 64 134.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[0f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
