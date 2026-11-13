# 036 create_trains/conductor
#area 380 42 403 69
fill 380 64 42 403 91 69 minecraft:air
fill 380 60 42 403 62 69 minecraft:stone
fill 380 63 42 403 63 69 minecraft:light_gray_concrete
fill 384 64 48 403 79 48 minecraft:light_gray_concrete
fill 384 64 48 384 79 63 minecraft:light_gray_concrete
setblock 385 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "036"}','{"text": "create_trains"}','{"text": "conductor"}','{"text": ""}']}}
setblock 386 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a blaze burner"}','{"text": "sitting as"}','{"text": "conductor"}','{"text": ""}']}}
fill 398 64 48 398 79 63 minecraft:light_gray_concrete
kw testworld place shots:create/train_schedule 386 63 50 none
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
