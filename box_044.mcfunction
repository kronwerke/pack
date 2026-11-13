# 044 botania_runes/runic_altar
#area 124 86 143 111
fill 124 64 86 143 91 111 minecraft:air
fill 124 60 86 143 62 111 minecraft:stone
fill 124 63 86 143 63 111 minecraft:light_gray_concrete
fill 128 64 92 143 79 92 minecraft:light_gray_concrete
fill 128 64 92 128 79 105 minecraft:light_gray_concrete
setblock 129 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "044"}','{"text": "botania_runes"}','{"text": "runic_altar"}','{"text": ""}']}}
setblock 130 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "altar with"}','{"text": "ingredients, a"}','{"text": "spreader aimed"}','{"text": "at it, wand HUD"}']}}
fill 138 64 92 138 79 105 minecraft:light_gray_concrete
setblock 130 64 97 botania:mana_pool{mana:1000000}
setblock 131 64 97 botania:mana_spreader{rotationX:180f,rotationY:0f,mana:1000}
setblock 135 64 97 botania:runic_altar
kw testworld use 135 64 97 up botania:manasteel_ingot
kw testworld use 135 64 97 up botania:mana_powder
kw testworld use 135 64 97 up minecraft:bone_meal
kw testworld use 135 64 97 up minecraft:sugar_cane
