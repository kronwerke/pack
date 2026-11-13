# 051 botania_runes/runic_altar
#area 122 105 141 130
fill 122 64 105 141 91 130 minecraft:air
fill 122 60 105 141 62 130 minecraft:stone
fill 122 63 105 141 63 130 minecraft:light_gray_concrete
fill 126 64 111 141 79 111 minecraft:light_gray_concrete
fill 126 64 111 126 79 124 minecraft:light_gray_concrete
setblock 127 64 123 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "051"}','{"text": "botania_runes"}','{"text": "runic_altar"}','{"text": ""}']}}
setblock 128 64 123 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "altar with"}','{"text": "ingredients, a"}','{"text": "spreader aimed"}','{"text": "at it, wand HUD"}']}}
fill 136 64 111 136 79 124 minecraft:light_gray_concrete
setblock 128 64 116 botania:mana_pool{mana:1000000}
setblock 129 64 116 botania:mana_spreader{rotationX:180f,rotationY:0f,mana:1000}
setblock 133 64 116 botania:runic_altar
kw testworld use 133 64 116 up botania:manasteel_ingot
kw testworld use 133 64 116 up botania:mana_powder
kw testworld use 133 64 116 up minecraft:bone_meal
kw testworld use 133 64 116 up minecraft:sugar_cane
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
