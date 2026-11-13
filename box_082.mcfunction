# 082 ars_master/tribute
#area 225 126 246 153
fill 225 64 126 246 91 153 minecraft:air
fill 225 60 126 246 62 153 minecraft:stone
fill 225 63 126 246 63 153 minecraft:light_gray_concrete
fill 229 64 132 246 79 132 minecraft:light_gray_concrete
fill 229 64 132 229 79 147 minecraft:light_gray_concrete
setblock 230 64 146 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "082"}','{"text": "ars_master"}','{"text": "tribute"}','{"text": ""}']}}
setblock 231 64 146 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the Chimera mid"}','{"text": "fight"}','{"text": ""}','{"text": ""}']}}
fill 241 64 132 241 79 147 minecraft:light_gray_concrete
summon ars_nouveau:wilden_boss 235.5 64 138.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[0f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
