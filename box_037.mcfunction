# 037 create_trains/conductor
#area 378 42 401 69
fill 378 64 42 401 91 69 minecraft:air
fill 378 60 42 401 62 69 minecraft:stone
fill 378 63 42 401 63 69 minecraft:light_gray_concrete
fill 382 64 48 401 79 48 minecraft:light_gray_concrete
fill 382 64 48 382 79 63 minecraft:light_gray_concrete
setblock 383 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "037"}','{"text": "create_trains"}','{"text": "conductor"}','{"text": ""}']}}
setblock 384 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a blaze burner"}','{"text": "sitting as"}','{"text": "conductor"}','{"text": ""}']}}
fill 396 64 48 396 79 63 minecraft:light_gray_concrete
kw testworld place shots:create/train_schedule 384 63 50 none
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
