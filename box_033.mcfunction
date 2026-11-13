# 033 botania_runes/runic_altar
#area 71 86 90 111
fill 71 64 86 90 91 111 minecraft:air
fill 71 60 86 90 62 111 minecraft:stone
fill 71 63 86 90 63 111 minecraft:light_gray_concrete
fill 75 64 92 90 79 92 minecraft:light_gray_concrete
fill 75 64 92 75 79 105 minecraft:light_gray_concrete
setblock 76 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "033"}','{"text": "botania_runes"}','{"text": "runic_altar"}','{"text": ""}']}}
setblock 77 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "altar with"}','{"text": "ingredients, a"}','{"text": "spreader aimed"}','{"text": "at it, wand HUD"}']}}
fill 85 64 92 85 79 105 minecraft:light_gray_concrete
setblock 77 64 97 botania:mana_pool{mana:1000000}
setblock 78 64 97 botania:mana_spreader{rotationX:180f,rotationY:0f,mana:1000}
setblock 82 64 97 botania:runic_altar
kw testworld use 82 64 97 up botania:manasteel_ingot
kw testworld use 82 64 97 up botania:mana_powder
kw testworld use 82 64 97 up minecraft:bone_meal
kw testworld use 82 64 97 up minecraft:sugar_cane
