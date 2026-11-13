# 131 industrial/laser
#area 73 252 92 277
fill 73 64 252 92 91 277 minecraft:air
fill 73 60 252 92 62 277 minecraft:stone
fill 73 63 252 92 63 277 minecraft:light_gray_concrete
fill 77 64 258 92 79 258 minecraft:light_gray_concrete
fill 77 64 258 77 79 271 minecraft:light_gray_concrete
setblock 78 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "131"}','{"text": "industrial"}','{"text": "laser"}','{"text": ""}']}}
setblock 79 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "ore laser with"}','{"text": "drills, the"}','{"text": "lens slot,"}','{"text": "fluid laser"}']}}
setblock 80 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "over a wither"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 87 64 258 87 79 271 minecraft:light_gray_concrete
setblock 82 64 263 industrialforegoing:ore_laser_base
setblock 80 64 263 industrialforegoing:laser_drill[facing=east]
setblock 84 64 263 industrialforegoing:laser_drill[facing=west]
setblock 82 64 261 industrialforegoing:laser_drill[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
