# 073 malum/altar, obelisk
#area 31 290 62 315
fill 31 64 290 62 91 315 minecraft:air
fill 31 60 290 62 62 315 minecraft:stone
fill 31 63 290 62 63 315 minecraft:light_gray_concrete
fill 35 64 296 62 79 296 minecraft:light_gray_concrete
fill 35 64 296 35 79 309 minecraft:light_gray_concrete
setblock 36 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "073.1"}','{"text": "malum"}','{"text": "altar"}','{"text": ""}']}}
setblock 37 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Spirit Altar"}','{"text": ""}','{"text": ""}']}}
fill 45 64 296 45 79 309 minecraft:light_gray_concrete
setblock 40 64 301 malum:spirit_altar
kw testworld use 40 64 301 south malum:runewood_planks
setblock 38 64 301 malum:runewood_planks
setblock 38 65 301 malum:runewood_item_stand[facing=up,waterlogged=false]
kw testworld use 38 65 301 south malum:hallowed_gold_ingot
setblock 42 64 301 malum:runewood_planks
setblock 42 65 301 malum:runewood_item_stand[facing=up,waterlogged=false]
kw testworld use 42 65 301 south malum:hallowed_gold_ingot
setblock 46 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "073.2"}','{"text": "malum"}','{"text": "obelisk"}','{"text": ""}']}}
setblock 47 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell"}','{"text": "Runewood-Obelisken"}','{"text": "auf"}','{"text": ""}']}}
fill 57 64 296 57 79 309 minecraft:light_gray_concrete
setblock 51 64 301 malum:spirit_altar
kw testworld use 51 64 301 south malum:runewood_planks
setblock 49 64 301 malum:runewood_planks
setblock 49 65 301 malum:runewood_item_stand[facing=up,waterlogged=false]
kw testworld use 49 65 301 south malum:hallowed_gold_ingot
setblock 53 64 301 malum:runewood_planks
setblock 53 65 301 malum:runewood_item_stand[facing=up,waterlogged=false]
kw testworld use 53 65 301 south malum:hallowed_gold_ingot
kw testworld use 48 63 299 up malum:runewood_obelisk
execute unless block 48 64 299 minecraft:air
kw testworld use 54 63 299 up malum:runewood_obelisk
execute unless block 54 64 299 minecraft:air
kw testworld use 48 63 303 up malum:runewood_obelisk
execute unless block 48 64 303 minecraft:air
kw testworld use 54 63 303 up malum:runewood_obelisk
execute unless block 54 64 303 minecraft:air
