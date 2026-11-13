# 035 create_trains/first_train
#area 361 42 384 69
fill 361 64 42 384 91 69 minecraft:air
fill 361 60 42 384 62 69 minecraft:stone
fill 361 63 42 384 63 69 minecraft:light_gray_concrete
fill 365 64 48 384 79 48 minecraft:light_gray_concrete
fill 365 64 48 365 79 63 minecraft:light_gray_concrete
setblock 366 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "035"}','{"text": "create_trains"}','{"text": "first_train"}','{"text": ""}']}}
setblock 367 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a finished"}','{"text": "small train"}','{"text": ""}','{"text": ""}']}}
fill 379 64 48 379 79 63 minecraft:light_gray_concrete
kw testworld place shots:create/train_controls 367 63 50 none
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
