# 100 malum/altar, obelisk
#area 56 309 87 334
fill 56 64 309 87 91 334 minecraft:air
fill 56 60 309 87 62 334 minecraft:stone
fill 56 63 309 87 63 334 minecraft:light_gray_concrete
fill 60 64 315 87 79 315 minecraft:light_gray_concrete
fill 60 64 315 60 79 328 minecraft:light_gray_concrete
setblock 61 64 327 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "100.1"}','{"text": "malum"}','{"text": "altar"}','{"text": ""}']}}
setblock 62 64 327 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Spirit Altar"}','{"text": ""}','{"text": ""}']}}
fill 70 64 315 70 79 328 minecraft:light_gray_concrete
setblock 65 64 320 malum:spirit_altar
kw testworld use 65 64 320 south malum:runewood_planks
setblock 63 64 320 malum:runewood_planks
setblock 63 65 320 malum:runewood_item_stand[facing=up,waterlogged=false]
kw testworld use 63 65 320 south malum:hallowed_gold_ingot
setblock 67 64 320 malum:runewood_planks
setblock 67 65 320 malum:runewood_item_stand[facing=up,waterlogged=false]
kw testworld use 67 65 320 south malum:hallowed_gold_ingot
setblock 71 64 327 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "100.2"}','{"text": "malum"}','{"text": "obelisk"}','{"text": ""}']}}
setblock 72 64 327 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell"}','{"text": "Runewood-Obelisken"}','{"text": "auf"}','{"text": ""}']}}
fill 82 64 315 82 79 328 minecraft:light_gray_concrete
setblock 76 64 320 malum:spirit_altar
kw testworld use 76 64 320 south malum:runewood_planks
setblock 74 64 320 malum:runewood_planks
setblock 74 65 320 malum:runewood_item_stand[facing=up,waterlogged=false]
kw testworld use 74 65 320 south malum:hallowed_gold_ingot
setblock 78 64 320 malum:runewood_planks
setblock 78 65 320 malum:runewood_item_stand[facing=up,waterlogged=false]
kw testworld use 78 65 320 south malum:hallowed_gold_ingot
kw testworld use 73 63 318 up malum:runewood_obelisk
execute unless block 73 64 318 minecraft:air
kw testworld use 79 63 318 up malum:runewood_obelisk
execute unless block 79 64 318 minecraft:air
kw testworld use 73 63 322 up malum:runewood_obelisk
execute unless block 73 64 322 minecraft:air
kw testworld use 79 63 322 up malum:runewood_obelisk
execute unless block 79 64 322 minecraft:air
