# 036 create_trains/first_train
#area 359 42 382 69
fill 359 64 42 382 91 69 minecraft:air
fill 359 60 42 382 62 69 minecraft:stone
fill 359 63 42 382 63 69 minecraft:light_gray_concrete
fill 363 64 48 382 79 48 minecraft:light_gray_concrete
fill 363 64 48 363 79 63 minecraft:light_gray_concrete
setblock 364 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "036"}','{"text": "create_trains"}','{"text": "first_train"}','{"text": ""}']}}
setblock 365 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a finished"}','{"text": "small train"}','{"text": ""}','{"text": ""}']}}
fill 377 64 48 377 79 63 minecraft:light_gray_concrete
kw testworld place shots:create/train_controls 365 63 50 none
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
