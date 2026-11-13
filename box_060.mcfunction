# 060 antimatter/wind
#area 291 95 310 124
fill 291 64 95 310 95 124 minecraft:air
fill 291 60 95 310 62 124 minecraft:stone
fill 291 63 95 310 63 124 minecraft:light_gray_concrete
fill 295 64 101 310 83 101 minecraft:light_gray_concrete
fill 295 64 101 295 83 118 minecraft:light_gray_concrete
setblock 296 64 117 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "060"}','{"text": "antimatter"}','{"text": "wind"}','{"text": ""}']}}
setblock 297 64 117 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the large wind"}','{"text": "generator"}','{"text": ""}','{"text": ""}']}}
fill 305 64 101 305 83 118 minecraft:light_gray_concrete
kw testworld use 300 63 105 up mekanismgenerators:wind_generator
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
