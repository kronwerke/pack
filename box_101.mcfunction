# 101 malum/altar, obelisk, healing_rite, quickening
#area 56 311 107 336
fill 56 64 311 100 91 336 minecraft:air
fill 101 64 311 107 91 336 minecraft:air
fill 56 60 311 107 62 336 minecraft:stone
fill 56 63 311 107 63 336 minecraft:light_gray_concrete
fill 60 64 317 107 79 317 minecraft:light_gray_concrete
fill 60 64 317 60 79 330 minecraft:light_gray_concrete
setblock 61 64 329 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "101.1"}','{"text": "malum"}','{"text": "altar"}','{"text": ""}']}}
setblock 62 64 329 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Spirit Altar"}','{"text": ""}','{"text": ""}']}}
fill 70 64 317 70 79 330 minecraft:light_gray_concrete
setblock 65 64 322 malum:spirit_altar
kw testworld use 65 64 322 south malum:runewood_planks
setblock 63 64 322 malum:runewood_planks
setblock 63 65 322 malum:runewood_item_stand[facing=up,waterlogged=false]
kw testworld use 63 65 322 south malum:hallowed_gold_ingot
setblock 67 64 322 malum:runewood_planks
setblock 67 65 322 malum:runewood_item_stand[facing=up,waterlogged=false]
kw testworld use 67 65 322 south malum:hallowed_gold_ingot
setblock 71 64 329 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "101.2"}','{"text": "malum"}','{"text": "obelisk"}','{"text": ""}']}}
setblock 72 64 329 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell"}','{"text": "Runewood-Obelisken"}','{"text": "auf"}','{"text": ""}']}}
fill 82 64 317 82 79 330 minecraft:light_gray_concrete
setblock 76 64 322 malum:spirit_altar
kw testworld use 76 64 322 south malum:runewood_planks
setblock 74 64 322 malum:runewood_planks
setblock 74 65 322 malum:runewood_item_stand[facing=up,waterlogged=false]
kw testworld use 74 65 322 south malum:hallowed_gold_ingot
setblock 78 64 322 malum:runewood_planks
setblock 78 65 322 malum:runewood_item_stand[facing=up,waterlogged=false]
kw testworld use 78 65 322 south malum:hallowed_gold_ingot
kw testworld use 73 63 320 up malum:runewood_obelisk
execute unless block 73 64 320 minecraft:air
kw testworld use 79 63 320 up malum:runewood_obelisk
execute unless block 79 64 320 minecraft:air
kw testworld use 73 63 324 up malum:runewood_obelisk
execute unless block 73 64 324 minecraft:air
kw testworld use 79 63 324 up malum:runewood_obelisk
execute unless block 79 64 324 minecraft:air
setblock 83 64 329 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "101.3"}','{"text": "malum"}','{"text": "healing_rite"}','{"text": ""}']}}
setblock 84 64 329 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Zünde den Rite"}','{"text": "of Healing"}','{"text": ""}','{"text": ""}']}}
fill 92 64 317 92 79 330 minecraft:light_gray_concrete
setblock 87 64 322 malum:runewood_totem_base
setblock 87 65 322 malum:runewood_log[axis=y]
kw testworld use 87 65 322 south malum:arcane_spirit
execute unless block 87 65 322 malum:runewood_log
setblock 87 66 322 malum:runewood_log[axis=y]
kw testworld use 87 66 322 south malum:sacred_spirit
execute unless block 87 66 322 malum:runewood_log
setblock 87 67 322 malum:runewood_log[axis=y]
kw testworld use 87 67 322 south malum:sacred_spirit
execute unless block 87 67 322 malum:runewood_log
setblock 93 64 329 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "101.4"}','{"text": "malum"}','{"text": "quickening"}','{"text": ""}']}}
setblock 94 64 329 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Zünde den Rite"}','{"text": "of Quickening"}','{"text": ""}','{"text": ""}']}}
fill 102 64 317 102 79 330 minecraft:light_gray_concrete
setblock 97 64 322 malum:soulwood_totem_base
setblock 97 65 322 malum:soulwood_log[axis=y]
kw testworld use 97 65 322 south malum:eldritch_spirit
execute unless block 97 65 322 malum:soulwood_log
setblock 97 66 322 malum:soulwood_log[axis=y]
kw testworld use 97 66 322 south malum:arcane_spirit
execute unless block 97 66 322 malum:soulwood_log
setblock 97 67 322 malum:soulwood_log[axis=y]
kw testworld use 97 67 322 south malum:infernal_spirit
execute unless block 97 67 322 malum:soulwood_log
setblock 97 68 322 malum:soulwood_log[axis=y]
kw testworld use 97 68 322 south malum:infernal_spirit
execute unless block 97 68 322 malum:soulwood_log
