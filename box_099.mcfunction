# 099 food/f_pot
#area -4 311 15 336
fill -4 64 311 15 91 336 minecraft:air
fill -4 60 311 15 62 336 minecraft:stone
fill -4 63 311 15 63 336 minecraft:light_gray_concrete
fill 0 64 317 15 79 317 minecraft:light_gray_concrete
fill 0 64 317 0 79 330 minecraft:light_gray_concrete
setblock 1 64 329 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "099"}','{"text": "food"}','{"text": "f_pot"}','{"text": ""}']}}
setblock 2 64 329 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell einen"}','{"text": "Kochtopf auf"}','{"text": ""}','{"text": ""}']}}
fill 10 64 317 10 79 330 minecraft:light_gray_concrete
setblock 5 64 322 farmersdelight:stove[facing=south,lit=true]
setblock 5 65 322 farmersdelight:cooking_pot[facing=south,support=none]
setblock 6 64 322 minecraft:oak_planks
setblock 6 65 322 farmersdelight:cutting_board[facing=south]
