# 037 botania_runes/runic_altar
#area 90 86 109 111
fill 90 64 86 109 91 111 minecraft:air
fill 90 60 86 109 62 111 minecraft:stone
fill 90 63 86 109 63 111 minecraft:light_gray_concrete
fill 94 64 92 109 79 92 minecraft:light_gray_concrete
fill 94 64 92 94 79 105 minecraft:light_gray_concrete
setblock 95 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "037"}','{"text": "botania_runes"}','{"text": "runic_altar"}','{"text": ""}']}}
setblock 96 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "altar with"}','{"text": "ingredients, a"}','{"text": "spreader aimed"}','{"text": "at it, wand HUD"}']}}
fill 104 64 92 104 79 105 minecraft:light_gray_concrete
setblock 96 64 97 botania:mana_pool{mana:1000000}
setblock 97 64 97 botania:mana_spreader{rotationX:180f,rotationY:0f,mana:1000}
setblock 101 64 97 botania:runic_altar
kw testworld use 101 64 97 up botania:manasteel_ingot
kw testworld use 101 64 97 up botania:mana_powder
kw testworld use 101 64 97 up minecraft:bone_meal
kw testworld use 101 64 97 up minecraft:sugar_cane
