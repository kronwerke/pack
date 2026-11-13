# 039 create_trains/schedule
#area -4 68 22 98
fill -4 64 68 22 91 98 minecraft:air
fill -4 60 68 22 62 98 minecraft:stone
fill -4 63 68 22 63 98 minecraft:light_gray_concrete
fill 0 64 74 22 79 74 minecraft:light_gray_concrete
fill 0 64 74 0 79 92 minecraft:light_gray_concrete
setblock 1 64 91 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "039"}','{"text": "create_trains"}','{"text": "schedule"}','{"text": ""}']}}
setblock 2 64 91 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the schedule"}','{"text": "screen with"}','{"text": "conditions"}','{"text": ""}']}}
fill 17 64 74 17 79 92 minecraft:light_gray_concrete
kw testworld place shots:create/train_station/schedule 2 63 76 none
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
