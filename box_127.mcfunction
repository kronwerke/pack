# 127 industrial/laser
#area 73 246 92 271
fill 73 64 246 92 91 271 minecraft:air
fill 73 60 246 92 62 271 minecraft:stone
fill 73 63 246 92 63 271 minecraft:light_gray_concrete
fill 77 64 252 92 79 252 minecraft:light_gray_concrete
fill 77 64 252 77 79 265 minecraft:light_gray_concrete
setblock 78 64 264 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "127"}','{"text": "industrial"}','{"text": "laser"}','{"text": ""}']}}
setblock 79 64 264 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "ore laser with"}','{"text": "drills, the"}','{"text": "lens slot,"}','{"text": "fluid laser"}']}}
setblock 80 64 264 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "over a wither"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 87 64 252 87 79 265 minecraft:light_gray_concrete
setblock 82 64 257 industrialforegoing:ore_laser_base
setblock 80 64 257 industrialforegoing:laser_drill[facing=east]
setblock 84 64 257 industrialforegoing:laser_drill[facing=west]
setblock 82 64 255 industrialforegoing:laser_drill[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
