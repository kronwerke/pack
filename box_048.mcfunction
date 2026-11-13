# 048 botania_runes/runic_altar
#area 139 86 158 111
fill 139 64 86 158 91 111 minecraft:air
fill 139 60 86 158 62 111 minecraft:stone
fill 139 63 86 158 63 111 minecraft:light_gray_concrete
fill 143 64 92 158 79 92 minecraft:light_gray_concrete
fill 143 64 92 143 79 105 minecraft:light_gray_concrete
setblock 144 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "048"}','{"text": "botania_runes"}','{"text": "runic_altar"}','{"text": ""}']}}
setblock 145 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "altar with"}','{"text": "ingredients, a"}','{"text": "spreader aimed"}','{"text": "at it, wand HUD"}']}}
fill 153 64 92 153 79 105 minecraft:light_gray_concrete
setblock 145 64 97 botania:mana_pool{mana:1000000}
setblock 146 64 97 botania:mana_spreader{rotationX:180f,rotationY:0f,mana:1000}
setblock 150 64 97 botania:runic_altar
kw testworld use 150 64 97 up botania:manasteel_ingot
kw testworld use 150 64 97 up botania:mana_powder
kw testworld use 150 64 97 up minecraft:bone_meal
kw testworld use 150 64 97 up minecraft:sugar_cane
