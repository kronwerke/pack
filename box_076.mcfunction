# 076 botania_runes/runic_altar
#area 122 109 141 134
fill 122 64 109 141 91 134 minecraft:air
fill 122 60 109 141 62 134 minecraft:stone
fill 122 63 109 141 63 134 minecraft:light_gray_concrete
fill 126 64 115 141 79 115 minecraft:light_gray_concrete
fill 126 64 115 126 79 128 minecraft:light_gray_concrete
setblock 127 64 127 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "076"}','{"text": "botania_runes"}','{"text": "runic_altar"}','{"text": ""}']}}
setblock 128 64 127 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "altar with"}','{"text": "ingredients, a"}','{"text": "spreader aimed"}','{"text": "at it, wand HUD"}']}}
fill 136 64 115 136 79 128 minecraft:light_gray_concrete
setblock 128 64 120 botania:mana_pool{mana:1000000}
setblock 129 64 120 botania:mana_spreader{rotationX:180f,rotationY:0f,mana:1000}
setblock 133 64 120 botania:runic_altar
kw testworld use 133 64 120 up botania:manasteel_ingot
kw testworld use 133 64 120 up botania:mana_powder
kw testworld use 133 64 120 up minecraft:bone_meal
kw testworld use 133 64 120 up minecraft:sugar_cane
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
