# 040 create_trains/conductor
#area 395 44 418 71
fill 395 64 44 418 91 71 minecraft:air
fill 395 60 44 418 62 71 minecraft:stone
fill 395 63 44 418 63 71 minecraft:light_gray_concrete
fill 399 64 50 418 79 50 minecraft:light_gray_concrete
fill 399 64 50 399 79 65 minecraft:light_gray_concrete
setblock 400 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "040"}','{"text": "create_trains"}','{"text": "conductor"}','{"text": ""}']}}
setblock 401 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a blaze burner"}','{"text": "sitting as"}','{"text": "conductor"}','{"text": ""}']}}
fill 413 64 50 413 79 65 minecraft:light_gray_concrete
kw testworld place shots:create/train_schedule 401 63 52 none
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
