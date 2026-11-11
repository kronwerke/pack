# 007 create/depot
#area 31 21 50 46
fill 31 64 21 50 91 46 minecraft:air
fill 31 60 21 50 62 46 minecraft:stone
fill 31 63 21 50 63 46 minecraft:light_gray_concrete
fill 35 64 27 50 79 27 minecraft:light_gray_concrete
fill 35 64 27 35 79 40 minecraft:light_gray_concrete
setblock 36 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "007"}','{"text": "create"}','{"text": "depot"}','{"text": ""}']}}
setblock 37 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "press above a"}','{"text": "depot with one"}','{"text": "block of air"}','{"text": "between"}']}}
fill 45 64 27 45 79 40 minecraft:light_gray_concrete
setblock 40 64 32 create:depot
setblock 40 66 32 create:mechanical_press[facing=south]
fill 39 64 31 41 67 31 create:andesite_casing
setblock 40 66 31 create:andesite_encased_shaft[axis=z]
setblock 40 66 30 create:creative_motor[facing=south]{ScrollValue:32}
kw testworld use 40 64 32 up minecraft:iron_ingot
