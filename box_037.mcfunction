# 037 antimatter/wind
#area 243 63 262 92
fill 243 64 63 262 95 92 minecraft:air
fill 243 60 63 262 62 92 minecraft:stone
fill 243 63 63 262 63 92 minecraft:light_gray_concrete
fill 247 64 69 262 83 69 minecraft:light_gray_concrete
fill 247 64 69 247 83 86 minecraft:light_gray_concrete
setblock 248 64 85 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "037"}','{"text": "antimatter"}','{"text": "wind"}','{"text": ""}']}}
setblock 249 64 85 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the large wind"}','{"text": "generator"}','{"text": ""}','{"text": ""}']}}
fill 257 64 69 257 83 86 minecraft:light_gray_concrete
kw testworld use 252 63 73 up mekanismgenerators:wind_generator
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
