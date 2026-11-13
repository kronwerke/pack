# 040 create_trains/junction
#area 18 68 50 101
fill 18 64 68 50 91 101 minecraft:air
fill 18 60 68 50 62 101 minecraft:stone
fill 18 63 68 50 63 101 minecraft:light_gray_concrete
fill 22 64 74 50 79 74 minecraft:light_gray_concrete
fill 22 64 74 22 79 95 minecraft:light_gray_concrete
setblock 23 64 94 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "040"}','{"text": "create_trains"}','{"text": "junction"}','{"text": ""}']}}
setblock 24 64 94 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chain and entry"}','{"text": "signals at a"}','{"text": "junction,"}','{"text": "goggles overlay"}']}}
fill 45 64 74 45 79 95 minecraft:light_gray_concrete
kw testworld place shots:create/train_signal/signaling 24 63 76 none
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
