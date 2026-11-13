# 042 create_trains/junction
#area 18 70 50 103
fill 18 64 70 50 91 103 minecraft:air
fill 18 60 70 50 62 103 minecraft:stone
fill 18 63 70 50 63 103 minecraft:light_gray_concrete
fill 22 64 76 50 79 76 minecraft:light_gray_concrete
fill 22 64 76 22 79 97 minecraft:light_gray_concrete
setblock 23 64 96 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "042"}','{"text": "create_trains"}','{"text": "junction"}','{"text": ""}']}}
setblock 24 64 96 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chain and entry"}','{"text": "signals at a"}','{"text": "junction,"}','{"text": "goggles overlay"}']}}
fill 45 64 76 45 79 97 minecraft:light_gray_concrete
kw testworld place shots:create/train_signal/signaling 24 63 78 none
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
