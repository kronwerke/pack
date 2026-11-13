# 048 antimatter/wind
#area 261 65 280 94
fill 261 64 65 280 95 94 minecraft:air
fill 261 60 65 280 62 94 minecraft:stone
fill 261 63 65 280 63 94 minecraft:light_gray_concrete
fill 265 64 71 280 83 71 minecraft:light_gray_concrete
fill 265 64 71 265 83 88 minecraft:light_gray_concrete
setblock 266 64 87 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "048"}','{"text": "antimatter"}','{"text": "wind"}','{"text": ""}']}}
setblock 267 64 87 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the large wind"}','{"text": "generator"}','{"text": ""}','{"text": ""}']}}
fill 275 64 71 275 83 88 minecraft:light_gray_concrete
kw testworld use 270 63 75 up mekanismgenerators:wind_generator
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
