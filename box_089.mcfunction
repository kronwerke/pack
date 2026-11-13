# 089 botania_runes/runic_altar
#area 122 145 141 170
fill 122 64 145 141 91 170 minecraft:air
fill 122 60 145 141 62 170 minecraft:stone
fill 122 63 145 141 63 170 minecraft:light_gray_concrete
fill 126 64 151 141 79 151 minecraft:light_gray_concrete
fill 126 64 151 126 79 164 minecraft:light_gray_concrete
setblock 127 64 163 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "089"}','{"text": "botania_runes"}','{"text": "runic_altar"}','{"text": ""}']}}
setblock 128 64 163 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "altar with"}','{"text": "ingredients, a"}','{"text": "spreader aimed"}','{"text": "at it, wand HUD"}']}}
fill 136 64 151 136 79 164 minecraft:light_gray_concrete
setblock 128 64 156 botania:mana_pool{mana:1000000}
setblock 129 64 156 botania:mana_spreader{rotationX:180f,rotationY:0f,mana:1000}
setblock 133 64 156 botania:runic_altar
kw testworld use 133 64 156 up botania:manasteel_ingot
kw testworld use 133 64 156 up botania:mana_powder
kw testworld use 133 64 156 up minecraft:bone_meal
kw testworld use 133 64 156 up minecraft:sugar_cane
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
