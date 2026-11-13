# 037 create_trains/first_train
#area 376 42 399 69
fill 376 64 42 399 91 69 minecraft:air
fill 376 60 42 399 62 69 minecraft:stone
fill 376 63 42 399 63 69 minecraft:light_gray_concrete
fill 380 64 48 399 79 48 minecraft:light_gray_concrete
fill 380 64 48 380 79 63 minecraft:light_gray_concrete
setblock 381 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "037"}','{"text": "create_trains"}','{"text": "first_train"}','{"text": ""}']}}
setblock 382 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a finished"}','{"text": "small train"}','{"text": ""}','{"text": ""}']}}
fill 394 64 48 394 79 63 minecraft:light_gray_concrete
kw testworld place shots:create/train_controls 382 63 50 none
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
