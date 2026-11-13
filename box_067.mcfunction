# 067 malum/altar, obelisk
#area -4 290 27 315
fill -4 64 290 27 91 315 minecraft:air
fill -4 60 290 27 62 315 minecraft:stone
fill -4 63 290 27 63 315 minecraft:light_gray_concrete
fill 0 64 296 27 79 296 minecraft:light_gray_concrete
fill 0 64 296 0 79 309 minecraft:light_gray_concrete
setblock 1 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "067.1"}','{"text": "malum"}','{"text": "altar"}','{"text": ""}']}}
setblock 2 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Spirit Altar"}','{"text": ""}','{"text": ""}']}}
fill 10 64 296 10 79 309 minecraft:light_gray_concrete
setblock 5 64 301 malum:spirit_altar
kw testworld use 5 64 301 south malum:runewood_planks
setblock 3 64 301 malum:runewood_planks
setblock 3 65 301 malum:runewood_item_stand[facing=up,waterlogged=false]
kw testworld use 3 65 301 south malum:hallowed_gold_ingot
setblock 7 64 301 malum:runewood_planks
setblock 7 65 301 malum:runewood_item_stand[facing=up,waterlogged=false]
kw testworld use 7 65 301 south malum:hallowed_gold_ingot
setblock 11 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "067.2"}','{"text": "malum"}','{"text": "obelisk"}','{"text": ""}']}}
setblock 12 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell"}','{"text": "Runewood-Obelisken"}','{"text": "auf"}','{"text": ""}']}}
fill 22 64 296 22 79 309 minecraft:light_gray_concrete
setblock 16 64 301 malum:spirit_altar
kw testworld use 16 64 301 south malum:runewood_planks
setblock 14 64 301 malum:runewood_planks
setblock 14 65 301 malum:runewood_item_stand[facing=up,waterlogged=false]
kw testworld use 14 65 301 south malum:hallowed_gold_ingot
setblock 18 64 301 malum:runewood_planks
setblock 18 65 301 malum:runewood_item_stand[facing=up,waterlogged=false]
kw testworld use 18 65 301 south malum:hallowed_gold_ingot
kw testworld use 13 63 299 up malum:runewood_obelisk
execute unless block 13 64 299 minecraft:air
kw testworld use 19 63 299 up malum:runewood_obelisk
execute unless block 19 64 299 minecraft:air
kw testworld use 13 63 303 up malum:runewood_obelisk
execute unless block 13 64 303 minecraft:air
kw testworld use 19 63 303 up malum:runewood_obelisk
execute unless block 19 64 303 minecraft:air
