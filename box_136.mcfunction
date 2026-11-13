# 136 industrial/laser
#area 307 240 326 265
fill 307 64 240 326 91 265 minecraft:air
fill 307 60 240 326 62 265 minecraft:stone
fill 307 63 240 326 63 265 minecraft:light_gray_concrete
fill 311 64 246 326 79 246 minecraft:light_gray_concrete
fill 311 64 246 311 79 259 minecraft:light_gray_concrete
setblock 312 64 258 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "136"}','{"text": "industrial"}','{"text": "laser"}','{"text": ""}']}}
setblock 313 64 258 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "ore laser with"}','{"text": "drills, the"}','{"text": "lens slot,"}','{"text": "fluid laser"}']}}
setblock 314 64 258 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "over a wither"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 321 64 246 321 79 259 minecraft:light_gray_concrete
setblock 316 64 251 industrialforegoing:ore_laser_base
setblock 314 64 251 industrialforegoing:laser_drill[facing=east]
setblock 318 64 251 industrialforegoing:laser_drill[facing=west]
setblock 316 64 249 industrialforegoing:laser_drill[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
