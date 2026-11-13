# 131 industrial/laser
#area 73 250 92 275
fill 73 64 250 92 91 275 minecraft:air
fill 73 60 250 92 62 275 minecraft:stone
fill 73 63 250 92 63 275 minecraft:light_gray_concrete
fill 77 64 256 92 79 256 minecraft:light_gray_concrete
fill 77 64 256 77 79 269 minecraft:light_gray_concrete
setblock 78 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "131"}','{"text": "industrial"}','{"text": "laser"}','{"text": ""}']}}
setblock 79 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "ore laser with"}','{"text": "drills, the"}','{"text": "lens slot,"}','{"text": "fluid laser"}']}}
setblock 80 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "over a wither"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 87 64 256 87 79 269 minecraft:light_gray_concrete
setblock 82 64 261 industrialforegoing:ore_laser_base
setblock 80 64 261 industrialforegoing:laser_drill[facing=east]
setblock 84 64 261 industrialforegoing:laser_drill[facing=west]
setblock 82 64 259 industrialforegoing:laser_drill[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
