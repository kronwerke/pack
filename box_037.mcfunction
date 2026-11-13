# 037 create_trains/junction
#area -4 68 28 101
fill -4 64 68 28 91 101 minecraft:air
fill -4 60 68 28 62 101 minecraft:stone
fill -4 63 68 28 63 101 minecraft:light_gray_concrete
fill 0 64 74 28 79 74 minecraft:light_gray_concrete
fill 0 64 74 0 79 95 minecraft:light_gray_concrete
setblock 1 64 94 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "037"}','{"text": "create_trains"}','{"text": "junction"}','{"text": ""}']}}
setblock 2 64 94 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chain and entry"}','{"text": "signals at a"}','{"text": "junction,"}','{"text": "goggles overlay"}']}}
fill 23 64 74 23 79 95 minecraft:light_gray_concrete
kw testworld place shots:create/train_signal/signaling 2 63 76 none
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
