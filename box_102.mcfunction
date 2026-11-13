# 102 industrial/laser
#area 56 214 75 239
fill 56 64 214 75 91 239 minecraft:air
fill 56 60 214 75 62 239 minecraft:stone
fill 56 63 214 75 63 239 minecraft:light_gray_concrete
fill 60 64 220 75 79 220 minecraft:light_gray_concrete
fill 60 64 220 60 79 233 minecraft:light_gray_concrete
setblock 61 64 232 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "102"}','{"text": "industrial"}','{"text": "laser"}','{"text": ""}']}}
setblock 62 64 232 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "ore laser with"}','{"text": "drills, the"}','{"text": "lens slot,"}','{"text": "fluid laser"}']}}
setblock 63 64 232 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "over a wither"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 70 64 220 70 79 233 minecraft:light_gray_concrete
setblock 65 64 225 industrialforegoing:ore_laser_base
setblock 63 64 225 industrialforegoing:laser_drill[facing=east]
setblock 67 64 225 industrialforegoing:laser_drill[facing=west]
setblock 65 64 223 industrialforegoing:laser_drill[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
