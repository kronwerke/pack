# 012 create/water_wheel
#area -4 42 16 67
fill -4 64 42 16 91 67 minecraft:air
fill -4 60 42 16 62 67 minecraft:stone
fill -4 63 42 16 63 67 minecraft:light_gray_concrete
fill 0 64 48 16 79 48 minecraft:light_gray_concrete
fill 0 64 48 0 79 61 minecraft:light_gray_concrete
setblock 1 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "012"}','{"text": "create"}','{"text": "water_wheel"}','{"text": ""}']}}
setblock 2 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "four water"}','{"text": "wheels in a row"}','{"text": "with water over"}','{"text": "the paddles"}']}}
setblock 3 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "from above"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 11 64 48 11 79 61 minecraft:light_gray_concrete
setblock 4 63 50 minecraft:water
setblock 4 63 51 minecraft:air
setblock 4 63 52 minecraft:air
setblock 4 63 53 minecraft:air
setblock 4 63 54 minecraft:air
setblock 4 63 55 minecraft:air
setblock 4 63 56 minecraft:air
setblock 4 64 53 create:water_wheel[facing=east]
setblock 5 63 50 minecraft:water
setblock 5 63 51 minecraft:air
setblock 5 63 52 minecraft:air
setblock 5 63 53 minecraft:air
setblock 5 63 54 minecraft:air
setblock 5 63 55 minecraft:air
setblock 5 63 56 minecraft:air
setblock 5 64 53 create:water_wheel[facing=east]
setblock 6 63 50 minecraft:water
setblock 6 63 51 minecraft:air
setblock 6 63 52 minecraft:air
setblock 6 63 53 minecraft:air
setblock 6 63 54 minecraft:air
setblock 6 63 55 minecraft:air
setblock 6 63 56 minecraft:air
setblock 6 64 53 create:water_wheel[facing=east]
setblock 7 63 50 minecraft:water
setblock 7 63 51 minecraft:air
setblock 7 63 52 minecraft:air
setblock 7 63 53 minecraft:air
setblock 7 63 54 minecraft:air
setblock 7 63 55 minecraft:air
setblock 7 63 56 minecraft:air
setblock 7 64 53 create:water_wheel[facing=east]
setblock 3 64 53 create:andesite_encased_shaft[axis=x]
setblock 8 64 53 create:andesite_encased_shaft[axis=x]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
