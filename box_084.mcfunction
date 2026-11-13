# 084 ars_master/golem_bookwyrm
#area 257 126 276 151
fill 257 64 126 276 91 151 minecraft:air
fill 257 60 126 276 62 151 minecraft:stone
fill 257 63 126 276 63 151 minecraft:light_gray_concrete
fill 261 64 132 276 79 132 minecraft:light_gray_concrete
fill 261 64 132 261 79 145 minecraft:light_gray_concrete
setblock 262 64 144 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "084"}','{"text": "ars_master"}','{"text": "golem_bookwyrm"}','{"text": ""}']}}
setblock 263 64 144 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "amethyst golem"}','{"text": "at a geode,"}','{"text": "storage lectern"}','{"text": "GUI"}']}}
fill 271 64 132 271 79 145 minecraft:light_gray_concrete
fill 264 64 136 266 66 137 minecraft:calcite
fill 265 64 137 265 65 137 minecraft:budding_amethyst
setblock 264 65 137 minecraft:amethyst_block
setblock 266 64 137 minecraft:amethyst_block
setblock 265 64 138 minecraft:amethyst_cluster[facing=south]
setblock 265 66 137 minecraft:amethyst_block
summon ars_nouveau:amethyst_golem 266.5 64 139.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[0f,0f]}
setblock 268 64 137 ars_nouveau:storage_lectern
setblock 269 64 137 minecraft:chest[facing=south,type=single,waterlogged=false]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
