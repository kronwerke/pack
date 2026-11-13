# 090 malum/altar, obelisk
#area 56 290 87 315
fill 56 64 290 87 91 315 minecraft:air
fill 56 60 290 87 62 315 minecraft:stone
fill 56 63 290 87 63 315 minecraft:light_gray_concrete
fill 60 64 296 87 79 296 minecraft:light_gray_concrete
fill 60 64 296 60 79 309 minecraft:light_gray_concrete
setblock 61 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "090.1"}','{"text": "malum"}','{"text": "altar"}','{"text": ""}']}}
setblock 62 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Spirit Altar"}','{"text": ""}','{"text": ""}']}}
fill 70 64 296 70 79 309 minecraft:light_gray_concrete
setblock 65 64 301 malum:spirit_altar
kw testworld use 65 64 301 south malum:runewood_planks
setblock 63 64 301 malum:runewood_planks
setblock 63 65 301 malum:runewood_item_stand[facing=up,waterlogged=false]
kw testworld use 63 65 301 south malum:hallowed_gold_ingot
setblock 67 64 301 malum:runewood_planks
setblock 67 65 301 malum:runewood_item_stand[facing=up,waterlogged=false]
kw testworld use 67 65 301 south malum:hallowed_gold_ingot
setblock 71 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "090.2"}','{"text": "malum"}','{"text": "obelisk"}','{"text": ""}']}}
setblock 72 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell"}','{"text": "Runewood-Obelisken"}','{"text": "auf"}','{"text": ""}']}}
fill 82 64 296 82 79 309 minecraft:light_gray_concrete
setblock 76 64 301 malum:spirit_altar
kw testworld use 76 64 301 south malum:runewood_planks
setblock 74 64 301 malum:runewood_planks
setblock 74 65 301 malum:runewood_item_stand[facing=up,waterlogged=false]
kw testworld use 74 65 301 south malum:hallowed_gold_ingot
setblock 78 64 301 malum:runewood_planks
setblock 78 65 301 malum:runewood_item_stand[facing=up,waterlogged=false]
kw testworld use 78 65 301 south malum:hallowed_gold_ingot
kw testworld use 73 63 299 up malum:runewood_obelisk
execute unless block 73 64 299 minecraft:air
kw testworld use 79 63 299 up malum:runewood_obelisk
execute unless block 79 64 299 minecraft:air
kw testworld use 73 63 303 up malum:runewood_obelisk
execute unless block 73 64 303 minecraft:air
kw testworld use 79 63 303 up malum:runewood_obelisk
execute unless block 79 64 303 minecraft:air
