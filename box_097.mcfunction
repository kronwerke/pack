# 097 botania_runes/runic_altar
#area 122 147 141 172
fill 122 64 147 141 91 172 minecraft:air
fill 122 60 147 141 62 172 minecraft:stone
fill 122 63 147 141 63 172 minecraft:light_gray_concrete
fill 126 64 153 141 79 153 minecraft:light_gray_concrete
fill 126 64 153 126 79 166 minecraft:light_gray_concrete
setblock 127 64 165 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "097"}','{"text": "botania_runes"}','{"text": "runic_altar"}','{"text": ""}']}}
setblock 128 64 165 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "altar with"}','{"text": "ingredients, a"}','{"text": "spreader aimed"}','{"text": "at it, wand HUD"}']}}
fill 136 64 153 136 79 166 minecraft:light_gray_concrete
setblock 128 64 158 botania:mana_pool{mana:1000000}
setblock 129 64 158 botania:mana_spreader{rotationX:180f,rotationY:0f,mana:1000}
setblock 133 64 158 botania:runic_altar
kw testworld use 133 64 158 up botania:manasteel_ingot
kw testworld use 133 64 158 up botania:mana_powder
kw testworld use 133 64 158 up minecraft:bone_meal
kw testworld use 133 64 158 up minecraft:sugar_cane
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
