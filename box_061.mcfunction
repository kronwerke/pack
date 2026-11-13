# 061 antimatter/wind
#area 295 95 314 124
fill 295 64 95 314 95 124 minecraft:air
fill 295 60 95 314 62 124 minecraft:stone
fill 295 63 95 314 63 124 minecraft:light_gray_concrete
fill 299 64 101 314 83 101 minecraft:light_gray_concrete
fill 299 64 101 299 83 118 minecraft:light_gray_concrete
setblock 300 64 117 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "061"}','{"text": "antimatter"}','{"text": "wind"}','{"text": ""}']}}
setblock 301 64 117 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the large wind"}','{"text": "generator"}','{"text": ""}','{"text": ""}']}}
fill 309 64 101 309 83 118 minecraft:light_gray_concrete
kw testworld use 304 63 105 up mekanismgenerators:wind_generator
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
