# 011 create/belt
#area 91 21 110 46
fill 91 64 21 110 91 46 minecraft:air
fill 91 60 21 110 62 46 minecraft:stone
fill 91 63 21 110 63 46 minecraft:light_gray_concrete
fill 95 64 27 110 79 27 minecraft:light_gray_concrete
fill 95 64 27 95 79 40 minecraft:light_gray_concrete
setblock 96 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "011"}','{"text": "create"}','{"text": "belt"}','{"text": ""}']}}
setblock 97 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a belt between"}','{"text": "two shafts"}','{"text": ""}','{"text": ""}']}}
fill 105 64 27 105 79 40 minecraft:light_gray_concrete
setblock 98 64 32 create:shaft[axis=z]
setblock 102 64 32 create:shaft[axis=z]
kw testworld use 98 64 32 up create:belt_connector
kw testworld use 102 64 32 up create:belt_connector
execute unless block 100 64 32 minecraft:air
