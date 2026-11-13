# 038 create_trains/conductor
#area 395 42 418 69
fill 395 64 42 418 91 69 minecraft:air
fill 395 60 42 418 62 69 minecraft:stone
fill 395 63 42 418 63 69 minecraft:light_gray_concrete
fill 399 64 48 418 79 48 minecraft:light_gray_concrete
fill 399 64 48 399 79 63 minecraft:light_gray_concrete
setblock 400 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "038"}','{"text": "create_trains"}','{"text": "conductor"}','{"text": ""}']}}
setblock 401 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a blaze burner"}','{"text": "sitting as"}','{"text": "conductor"}','{"text": ""}']}}
fill 413 64 48 413 79 63 minecraft:light_gray_concrete
kw testworld place shots:create/train_schedule 401 63 50 none
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
