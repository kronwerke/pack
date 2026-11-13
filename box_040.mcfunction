# 040 antimatter/wind
#area 243 65 262 94
fill 243 64 65 262 95 94 minecraft:air
fill 243 60 65 262 62 94 minecraft:stone
fill 243 63 65 262 63 94 minecraft:light_gray_concrete
fill 247 64 71 262 83 71 minecraft:light_gray_concrete
fill 247 64 71 247 83 88 minecraft:light_gray_concrete
setblock 248 64 87 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "040"}','{"text": "antimatter"}','{"text": "wind"}','{"text": ""}']}}
setblock 249 64 87 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the large wind"}','{"text": "generator"}','{"text": ""}','{"text": ""}']}}
fill 257 64 71 257 83 88 minecraft:light_gray_concrete
kw testworld use 252 63 75 up mekanismgenerators:wind_generator
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
