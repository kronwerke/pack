# 015 create/stress
#area 31 42 50 66
fill 31 64 42 50 91 66 minecraft:air
fill 31 60 42 50 62 66 minecraft:stone
fill 31 63 42 50 63 66 minecraft:light_gray_concrete
fill 35 64 48 50 79 48 minecraft:light_gray_concrete
fill 35 64 48 35 79 60 minecraft:light_gray_concrete
setblock 36 64 59 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "015"}','{"text": "create"}','{"text": "stress"}','{"text": ""}']}}
setblock 37 64 59 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "goggles overlay"}','{"text": "on an"}','{"text": "overstressed"}','{"text": "network"}']}}
fill 45 64 48 45 79 60 minecraft:light_gray_concrete
kw testworld place shots:create/gauges 37 63 50 none
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
