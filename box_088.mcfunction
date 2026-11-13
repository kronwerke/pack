# 088 food/f_pot
#area -4 290 15 315
fill -4 64 290 15 91 315 minecraft:air
fill -4 60 290 15 62 315 minecraft:stone
fill -4 63 290 15 63 315 minecraft:light_gray_concrete
fill 0 64 296 15 79 296 minecraft:light_gray_concrete
fill 0 64 296 0 79 309 minecraft:light_gray_concrete
setblock 1 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "088"}','{"text": "food"}','{"text": "f_pot"}','{"text": ""}']}}
setblock 2 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell einen"}','{"text": "Kochtopf auf"}','{"text": ""}','{"text": ""}']}}
fill 10 64 296 10 79 309 minecraft:light_gray_concrete
setblock 5 64 301 farmersdelight:stove[facing=south,lit=true]
setblock 5 65 301 farmersdelight:cooking_pot[facing=south,support=none]
setblock 6 64 301 minecraft:oak_planks
setblock 6 65 301 farmersdelight:cutting_board[facing=south]
