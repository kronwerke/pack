# 057 antimatter/wind
#area 276 95 295 124
fill 276 64 95 295 95 124 minecraft:air
fill 276 60 95 295 62 124 minecraft:stone
fill 276 63 95 295 63 124 minecraft:light_gray_concrete
fill 280 64 101 295 83 101 minecraft:light_gray_concrete
fill 280 64 101 280 83 118 minecraft:light_gray_concrete
setblock 281 64 117 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "057"}','{"text": "antimatter"}','{"text": "wind"}','{"text": ""}']}}
setblock 282 64 117 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the large wind"}','{"text": "generator"}','{"text": ""}','{"text": ""}']}}
fill 290 64 101 290 83 118 minecraft:light_gray_concrete
kw testworld use 285 63 105 up mekanismgenerators:wind_generator
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
