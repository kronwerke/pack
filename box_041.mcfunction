# 041 create_trains/schedule
#area -4 70 22 100
fill -4 64 70 22 91 100 minecraft:air
fill -4 60 70 22 62 100 minecraft:stone
fill -4 63 70 22 63 100 minecraft:light_gray_concrete
fill 0 64 76 22 79 76 minecraft:light_gray_concrete
fill 0 64 76 0 79 94 minecraft:light_gray_concrete
setblock 1 64 93 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "041"}','{"text": "create_trains"}','{"text": "schedule"}','{"text": ""}']}}
setblock 2 64 93 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the schedule"}','{"text": "screen with"}','{"text": "conditions"}','{"text": ""}']}}
fill 17 64 76 17 79 94 minecraft:light_gray_concrete
kw testworld place shots:create/train_station/schedule 2 63 78 none
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
