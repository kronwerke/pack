# 113 industrial/laser
#area 73 214 92 239
fill 73 64 214 92 91 239 minecraft:air
fill 73 60 214 92 62 239 minecraft:stone
fill 73 63 214 92 63 239 minecraft:light_gray_concrete
fill 77 64 220 92 79 220 minecraft:light_gray_concrete
fill 77 64 220 77 79 233 minecraft:light_gray_concrete
setblock 78 64 232 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "113"}','{"text": "industrial"}','{"text": "laser"}','{"text": ""}']}}
setblock 79 64 232 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "ore laser with"}','{"text": "drills, the"}','{"text": "lens slot,"}','{"text": "fluid laser"}']}}
setblock 80 64 232 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "over a wither"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 87 64 220 87 79 233 minecraft:light_gray_concrete
setblock 82 64 225 industrialforegoing:ore_laser_base
setblock 80 64 225 industrialforegoing:laser_drill[facing=east]
setblock 84 64 225 industrialforegoing:laser_drill[facing=west]
setblock 82 64 223 industrialforegoing:laser_drill[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
