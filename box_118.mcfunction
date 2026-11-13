# 118 industrial/laser
#area 73 216 92 241
fill 73 64 216 92 91 241 minecraft:air
fill 73 60 216 92 62 241 minecraft:stone
fill 73 63 216 92 63 241 minecraft:light_gray_concrete
fill 77 64 222 92 79 222 minecraft:light_gray_concrete
fill 77 64 222 77 79 235 minecraft:light_gray_concrete
setblock 78 64 234 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "118"}','{"text": "industrial"}','{"text": "laser"}','{"text": ""}']}}
setblock 79 64 234 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "ore laser with"}','{"text": "drills, the"}','{"text": "lens slot,"}','{"text": "fluid laser"}']}}
setblock 80 64 234 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "over a wither"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 87 64 222 87 79 235 minecraft:light_gray_concrete
setblock 82 64 227 industrialforegoing:ore_laser_base
setblock 80 64 227 industrialforegoing:laser_drill[facing=east]
setblock 84 64 227 industrialforegoing:laser_drill[facing=west]
setblock 82 64 225 industrialforegoing:laser_drill[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
