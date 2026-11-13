# 009 create/water_wheel
#area -4 40 16 65
fill -4 64 40 16 91 65 minecraft:air
fill -4 60 40 16 62 65 minecraft:stone
fill -4 63 40 16 63 65 minecraft:light_gray_concrete
fill 0 64 46 16 79 46 minecraft:light_gray_concrete
fill 0 64 46 0 79 59 minecraft:light_gray_concrete
setblock 1 64 58 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "009"}','{"text": "create"}','{"text": "water_wheel"}','{"text": ""}']}}
setblock 2 64 58 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "four water"}','{"text": "wheels in a row"}','{"text": "with water over"}','{"text": "the paddles"}']}}
setblock 3 64 58 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "from above"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 11 64 46 11 79 59 minecraft:light_gray_concrete
setblock 4 63 48 minecraft:water
setblock 4 63 49 minecraft:air
setblock 4 63 50 minecraft:air
setblock 4 63 51 minecraft:air
setblock 4 63 52 minecraft:air
setblock 4 63 53 minecraft:air
setblock 4 63 54 minecraft:air
setblock 4 64 51 create:water_wheel[facing=east]
setblock 5 63 48 minecraft:water
setblock 5 63 49 minecraft:air
setblock 5 63 50 minecraft:air
setblock 5 63 51 minecraft:air
setblock 5 63 52 minecraft:air
setblock 5 63 53 minecraft:air
setblock 5 63 54 minecraft:air
setblock 5 64 51 create:water_wheel[facing=east]
setblock 6 63 48 minecraft:water
setblock 6 63 49 minecraft:air
setblock 6 63 50 minecraft:air
setblock 6 63 51 minecraft:air
setblock 6 63 52 minecraft:air
setblock 6 63 53 minecraft:air
setblock 6 63 54 minecraft:air
setblock 6 64 51 create:water_wheel[facing=east]
setblock 7 63 48 minecraft:water
setblock 7 63 49 minecraft:air
setblock 7 63 50 minecraft:air
setblock 7 63 51 minecraft:air
setblock 7 63 52 minecraft:air
setblock 7 63 53 minecraft:air
setblock 7 63 54 minecraft:air
setblock 7 64 51 create:water_wheel[facing=east]
setblock 3 64 51 create:andesite_encased_shaft[axis=x]
setblock 8 64 51 create:andesite_encased_shaft[axis=x]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
