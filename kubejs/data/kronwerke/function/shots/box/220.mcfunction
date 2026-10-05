# 220 food/f_cutting_board, f_pot, f_rice, f_rich_soil, f_feast, f_market, f_rod
fill 85 63 492 156 63 505 minecraft:light_gray_concrete
fill 85 64 492 156 71 492 minecraft:light_gray_concrete
fill 85 64 492 85 71 505 minecraft:light_gray_concrete
setblock 86 64 504 minecraft:air
setblock 86 64 504 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "220.1"}','{"text": "food"}','{"text": "f_cutting_board"}','{"text": ""}']}}
setblock 87 64 504 minecraft:air
setblock 87 64 504 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau ein"}','{"text": "Schneidebrett"}','{"text": ""}','{"text": ""}']}}
setblock 87 64 496 farmersdelight:cutting_board
setblock 96 64 504 minecraft:air
setblock 96 64 504 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "220.2"}','{"text": "food"}','{"text": "f_pot"}','{"text": ""}']}}
setblock 97 64 504 minecraft:air
setblock 97 64 504 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell einen"}','{"text": "Kochtopf auf"}','{"text": ""}','{"text": ""}']}}
setblock 97 64 496 farmersdelight:cooking_pot
setblock 106 64 504 minecraft:air
setblock 106 64 504 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "220.3"}','{"text": "food"}','{"text": "f_rice"}','{"text": ""}']}}
setblock 107 64 504 minecraft:air
setblock 107 64 504 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Pflanz Reis ins"}','{"text": "Wasser"}','{"text": ""}','{"text": ""}']}}
setblock 107 64 496 farmersdelight:rice
setblock 116 64 504 minecraft:air
setblock 116 64 504 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "220.4"}','{"text": "food"}','{"text": "f_rich_soil"}','{"text": ""}']}}
setblock 117 64 504 minecraft:air
setblock 117 64 504 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Mach"}','{"text": "Reichhaltige"}','{"text": "Erde"}','{"text": ""}']}}
setblock 117 64 496 farmersdelight:rich_soil
setblock 126 64 504 minecraft:air
setblock 126 64 504 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "220.5"}','{"text": "food"}','{"text": "f_feast"}','{"text": ""}']}}
setblock 127 64 504 minecraft:air
setblock 127 64 504 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Tisch ein"}','{"text": "Backhähnchen"}','{"text": "auf"}','{"text": ""}']}}
fill 128 64 496 132 64 498 minecraft:oak_planks
setblock 129 65 497 farmersdelight:roast_chicken_block
setblock 131 65 497 farmersdelight:shepherds_pie_block
setblock 134 64 501 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"minecraft:bowl",count:8}]}
setblock 136 64 504 minecraft:air
setblock 136 64 504 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "220.6"}','{"text": "food"}','{"text": "f_market"}','{"text": ""}']}}
setblock 137 64 504 minecraft:air
setblock 137 64 504 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell einen"}','{"text": "Markt auf"}','{"text": ""}','{"text": ""}']}}
setblock 137 64 496 farmingforblockheads:market
setblock 146 64 504 minecraft:air
setblock 146 64 504 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "220.7"}','{"text": "food"}','{"text": "f_rod"}','{"text": ""}']}}
setblock 147 64 504 minecraft:air
setblock 147 64 504 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau eine"}','{"text": "Eisen-Angelrute"}','{"text": ""}','{"text": ""}']}}
setblock 147 64 496 minecraft:polished_andesite
summon item_frame 147 64 497 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"aquaculture:iron_fishing_rod",count:1}}
