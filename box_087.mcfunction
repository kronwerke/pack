# 087 industrial/laser
#area 31 212 50 237
fill 31 64 212 50 91 237 minecraft:air
fill 31 60 212 50 62 237 minecraft:stone
fill 31 63 212 50 63 237 minecraft:light_gray_concrete
fill 35 64 218 50 79 218 minecraft:light_gray_concrete
fill 35 64 218 35 79 231 minecraft:light_gray_concrete
setblock 36 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "087"}','{"text": "industrial"}','{"text": "laser"}','{"text": ""}']}}
setblock 37 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "ore laser with"}','{"text": "drills, the"}','{"text": "lens slot,"}','{"text": "fluid laser"}']}}
setblock 38 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "over a wither"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 45 64 218 45 79 231 minecraft:light_gray_concrete
setblock 40 64 223 industrialforegoing:ore_laser_base
setblock 38 64 223 industrialforegoing:laser_drill[facing=east]
setblock 42 64 223 industrialforegoing:laser_drill[facing=west]
setblock 40 64 221 industrialforegoing:laser_drill[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
