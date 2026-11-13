# 151 industrial/laser
#area 307 242 326 267
fill 307 64 242 326 91 267 minecraft:air
fill 307 60 242 326 62 267 minecraft:stone
fill 307 63 242 326 63 267 minecraft:light_gray_concrete
fill 311 64 248 326 79 248 minecraft:light_gray_concrete
fill 311 64 248 311 79 261 minecraft:light_gray_concrete
setblock 312 64 260 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "151"}','{"text": "industrial"}','{"text": "laser"}','{"text": ""}']}}
setblock 313 64 260 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "ore laser with"}','{"text": "drills, the"}','{"text": "lens slot,"}','{"text": "fluid laser"}']}}
setblock 314 64 260 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "over a wither"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 321 64 248 321 79 261 minecraft:light_gray_concrete
setblock 316 64 253 industrialforegoing:ore_laser_base
setblock 314 64 253 industrialforegoing:laser_drill[facing=east]
setblock 318 64 253 industrialforegoing:laser_drill[facing=west]
setblock 316 64 251 industrialforegoing:laser_drill[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
