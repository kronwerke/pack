# 066 antimatter/wind
#area 342 97 361 126
fill 342 64 97 361 95 126 minecraft:air
fill 342 60 97 361 62 126 minecraft:stone
fill 342 63 97 361 63 126 minecraft:light_gray_concrete
fill 346 64 103 361 83 103 minecraft:light_gray_concrete
fill 346 64 103 346 83 120 minecraft:light_gray_concrete
setblock 347 64 119 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "066"}','{"text": "antimatter"}','{"text": "wind"}','{"text": ""}']}}
setblock 348 64 119 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the large wind"}','{"text": "generator"}','{"text": ""}','{"text": ""}']}}
fill 356 64 103 356 83 120 minecraft:light_gray_concrete
kw testworld use 351 63 107 up mekanismgenerators:wind_generator
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
