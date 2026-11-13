# 052 botania_runes/runic_altar
#area 139 105 158 130
fill 139 64 105 158 91 130 minecraft:air
fill 139 60 105 158 62 130 minecraft:stone
fill 139 63 105 158 63 130 minecraft:light_gray_concrete
fill 143 64 111 158 79 111 minecraft:light_gray_concrete
fill 143 64 111 143 79 124 minecraft:light_gray_concrete
setblock 144 64 123 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "052"}','{"text": "botania_runes"}','{"text": "runic_altar"}','{"text": ""}']}}
setblock 145 64 123 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "altar with"}','{"text": "ingredients, a"}','{"text": "spreader aimed"}','{"text": "at it, wand HUD"}']}}
fill 153 64 111 153 79 124 minecraft:light_gray_concrete
setblock 145 64 116 botania:mana_pool{mana:1000000}
setblock 146 64 116 botania:mana_spreader{rotationX:180f,rotationY:0f,mana:1000}
setblock 150 64 116 botania:runic_altar
kw testworld use 150 64 116 up botania:manasteel_ingot
kw testworld use 150 64 116 up botania:mana_powder
kw testworld use 150 64 116 up minecraft:bone_meal
kw testworld use 150 64 116 up minecraft:sugar_cane
