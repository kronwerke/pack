# 005 create/water_wheel
#area -4 21 16 46
fill -4 64 21 16 91 46 minecraft:air
fill -4 60 21 16 62 46 minecraft:stone
fill -4 63 21 16 63 46 minecraft:light_gray_concrete
fill 0 64 27 16 79 27 minecraft:light_gray_concrete
fill 0 64 27 0 79 40 minecraft:light_gray_concrete
setblock 1 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "005"}','{"text": "create"}','{"text": "water_wheel"}','{"text": ""}']}}
setblock 2 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "four water"}','{"text": "wheels in a row"}','{"text": "with water over"}','{"text": "the paddles"}']}}
setblock 3 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "from above"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 11 64 27 11 79 40 minecraft:light_gray_concrete
setblock 4 65 32 create:water_wheel[facing=east]
setblock 4 63 31 minecraft:air
setblock 5 65 32 create:water_wheel[facing=east]
setblock 5 63 31 minecraft:air
setblock 6 65 32 create:water_wheel[facing=east]
setblock 6 63 31 minecraft:air
setblock 7 65 32 create:water_wheel[facing=east]
setblock 7 63 31 minecraft:air
setblock 3 64 32 create:andesite_casing
setblock 3 65 32 create:andesite_encased_shaft[axis=x]
setblock 8 64 32 create:andesite_casing
setblock 8 65 32 create:andesite_encased_shaft[axis=x]
fill 3 66 30 8 66 31 minecraft:spruce_planks
fill 4 66 32 7 66 32 minecraft:spruce_trapdoor[facing=south,half=bottom,open=true]
fill 4 66 31 7 66 31 minecraft:water
