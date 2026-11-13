# 016 create/water_wheel
#area -4 44 16 69
fill -4 64 44 16 91 69 minecraft:air
fill -4 60 44 16 62 69 minecraft:stone
fill -4 63 44 16 63 69 minecraft:light_gray_concrete
fill 0 64 50 16 79 50 minecraft:light_gray_concrete
fill 0 64 50 0 79 63 minecraft:light_gray_concrete
setblock 1 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "016"}','{"text": "create"}','{"text": "water_wheel"}','{"text": ""}']}}
setblock 2 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "four water"}','{"text": "wheels in a row"}','{"text": "with water over"}','{"text": "the paddles"}']}}
setblock 3 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "from above"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 11 64 50 11 79 63 minecraft:light_gray_concrete
setblock 4 63 52 minecraft:water
setblock 4 63 53 minecraft:air
setblock 4 63 54 minecraft:air
setblock 4 63 55 minecraft:air
setblock 4 63 56 minecraft:air
setblock 4 63 57 minecraft:air
setblock 4 63 58 minecraft:air
setblock 4 64 55 create:water_wheel[facing=east]
setblock 5 63 52 minecraft:water
setblock 5 63 53 minecraft:air
setblock 5 63 54 minecraft:air
setblock 5 63 55 minecraft:air
setblock 5 63 56 minecraft:air
setblock 5 63 57 minecraft:air
setblock 5 63 58 minecraft:air
setblock 5 64 55 create:water_wheel[facing=east]
setblock 6 63 52 minecraft:water
setblock 6 63 53 minecraft:air
setblock 6 63 54 minecraft:air
setblock 6 63 55 minecraft:air
setblock 6 63 56 minecraft:air
setblock 6 63 57 minecraft:air
setblock 6 63 58 minecraft:air
setblock 6 64 55 create:water_wheel[facing=east]
setblock 7 63 52 minecraft:water
setblock 7 63 53 minecraft:air
setblock 7 63 54 minecraft:air
setblock 7 63 55 minecraft:air
setblock 7 63 56 minecraft:air
setblock 7 63 57 minecraft:air
setblock 7 63 58 minecraft:air
setblock 7 64 55 create:water_wheel[facing=east]
setblock 3 64 55 create:andesite_encased_shaft[axis=x]
setblock 8 64 55 create:andesite_encased_shaft[axis=x]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
