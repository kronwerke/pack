# 039 create_trains/first_train
#area 376 44 399 71
fill 376 64 44 399 91 71 minecraft:air
fill 376 60 44 399 62 71 minecraft:stone
fill 376 63 44 399 63 71 minecraft:light_gray_concrete
fill 380 64 50 399 79 50 minecraft:light_gray_concrete
fill 380 64 50 380 79 65 minecraft:light_gray_concrete
setblock 381 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "039"}','{"text": "create_trains"}','{"text": "first_train"}','{"text": ""}']}}
setblock 382 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a finished"}','{"text": "small train"}','{"text": ""}','{"text": ""}']}}
fill 394 64 50 394 79 65 minecraft:light_gray_concrete
kw testworld place shots:create/train_controls 382 63 52 none
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
