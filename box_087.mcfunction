# 087 botania_runes/runic_altar
#area 122 143 141 168
fill 122 64 143 141 91 168 minecraft:air
fill 122 60 143 141 62 168 minecraft:stone
fill 122 63 143 141 63 168 minecraft:light_gray_concrete
fill 126 64 149 141 79 149 minecraft:light_gray_concrete
fill 126 64 149 126 79 162 minecraft:light_gray_concrete
setblock 127 64 161 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "087"}','{"text": "botania_runes"}','{"text": "runic_altar"}','{"text": ""}']}}
setblock 128 64 161 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "altar with"}','{"text": "ingredients, a"}','{"text": "spreader aimed"}','{"text": "at it, wand HUD"}']}}
fill 136 64 149 136 79 162 minecraft:light_gray_concrete
setblock 128 64 154 botania:mana_pool{mana:1000000}
setblock 129 64 154 botania:mana_spreader{rotationX:180f,rotationY:0f,mana:1000}
setblock 133 64 154 botania:runic_altar
kw testworld use 133 64 154 up botania:manasteel_ingot
kw testworld use 133 64 154 up botania:mana_powder
kw testworld use 133 64 154 up minecraft:bone_meal
kw testworld use 133 64 154 up minecraft:sugar_cane
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
