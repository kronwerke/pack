# 029 botania_runes/runic_altar
#area 71 84 90 109
fill 71 64 84 90 91 109 minecraft:air
fill 71 60 84 90 62 109 minecraft:stone
fill 71 63 84 90 63 109 minecraft:light_gray_concrete
fill 75 64 90 90 79 90 minecraft:light_gray_concrete
fill 75 64 90 75 79 103 minecraft:light_gray_concrete
setblock 76 64 102 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "029"}','{"text": "botania_runes"}','{"text": "runic_altar"}','{"text": ""}']}}
setblock 77 64 102 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "altar with"}','{"text": "ingredients, a"}','{"text": "spreader aimed"}','{"text": "at it, wand HUD"}']}}
fill 85 64 90 85 79 103 minecraft:light_gray_concrete
setblock 77 64 95 botania:mana_pool{mana:1000000}
setblock 78 64 95 botania:mana_spreader{rotationX:180f,rotationY:0f,mana:1000}
setblock 82 64 95 botania:runic_altar
kw testworld use 82 64 95 up botania:manasteel_ingot
kw testworld use 82 64 95 up botania:mana_powder
kw testworld use 82 64 95 up minecraft:bone_meal
kw testworld use 82 64 95 up minecraft:sugar_cane
