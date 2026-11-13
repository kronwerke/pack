# 050 antimatter/wind
#area 276 65 295 94
fill 276 64 65 295 95 94 minecraft:air
fill 276 60 65 295 62 94 minecraft:stone
fill 276 63 65 295 63 94 minecraft:light_gray_concrete
fill 280 64 71 295 83 71 minecraft:light_gray_concrete
fill 280 64 71 280 83 88 minecraft:light_gray_concrete
setblock 281 64 87 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "050"}','{"text": "antimatter"}','{"text": "wind"}','{"text": ""}']}}
setblock 282 64 87 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the large wind"}','{"text": "generator"}','{"text": ""}','{"text": ""}']}}
fill 290 64 71 290 83 88 minecraft:light_gray_concrete
kw testworld use 285 63 75 up mekanismgenerators:wind_generator
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
