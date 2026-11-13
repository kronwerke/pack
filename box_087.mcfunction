# 087 botania_runes/runic_altar
#area 122 139 141 164
fill 122 64 139 141 91 164 minecraft:air
fill 122 60 139 141 62 164 minecraft:stone
fill 122 63 139 141 63 164 minecraft:light_gray_concrete
fill 126 64 145 141 79 145 minecraft:light_gray_concrete
fill 126 64 145 126 79 158 minecraft:light_gray_concrete
setblock 127 64 157 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "087"}','{"text": "botania_runes"}','{"text": "runic_altar"}','{"text": ""}']}}
setblock 128 64 157 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "altar with"}','{"text": "ingredients, a"}','{"text": "spreader aimed"}','{"text": "at it, wand HUD"}']}}
fill 136 64 145 136 79 158 minecraft:light_gray_concrete
setblock 128 64 150 botania:mana_pool{mana:1000000}
setblock 129 64 150 botania:mana_spreader{rotationX:180f,rotationY:0f,mana:1000}
setblock 133 64 150 botania:runic_altar
kw testworld use 133 64 150 up botania:manasteel_ingot
kw testworld use 133 64 150 up botania:mana_powder
kw testworld use 133 64 150 up minecraft:bone_meal
kw testworld use 133 64 150 up minecraft:sugar_cane
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
