# 038 create_trains/schedule
#area 397 42 423 72
fill 397 64 42 423 91 72 minecraft:air
fill 397 60 42 423 62 72 minecraft:stone
fill 397 63 42 423 63 72 minecraft:light_gray_concrete
fill 401 64 48 423 79 48 minecraft:light_gray_concrete
fill 401 64 48 401 79 66 minecraft:light_gray_concrete
setblock 402 64 65 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "038"}','{"text": "create_trains"}','{"text": "schedule"}','{"text": ""}']}}
setblock 403 64 65 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the schedule"}','{"text": "screen with"}','{"text": "conditions"}','{"text": ""}']}}
fill 418 64 48 418 79 66 minecraft:light_gray_concrete
kw testworld place shots:create/train_station/schedule 403 63 50 none
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
