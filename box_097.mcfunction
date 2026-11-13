# 097 food/f_pot
#area -4 309 15 334
fill -4 64 309 15 91 334 minecraft:air
fill -4 60 309 15 62 334 minecraft:stone
fill -4 63 309 15 63 334 minecraft:light_gray_concrete
fill 0 64 315 15 79 315 minecraft:light_gray_concrete
fill 0 64 315 0 79 328 minecraft:light_gray_concrete
setblock 1 64 327 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "097"}','{"text": "food"}','{"text": "f_pot"}','{"text": ""}']}}
setblock 2 64 327 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell einen"}','{"text": "Kochtopf auf"}','{"text": ""}','{"text": ""}']}}
fill 10 64 315 10 79 328 minecraft:light_gray_concrete
setblock 5 64 320 farmersdelight:stove[facing=south,lit=true]
setblock 5 65 320 farmersdelight:cooking_pot[facing=south,support=none]
setblock 6 64 320 minecraft:oak_planks
setblock 6 65 320 farmersdelight:cutting_board[facing=south]
