# 064 botania_runes/runic_altar
#area 122 107 141 132
fill 122 64 107 141 91 132 minecraft:air
fill 122 60 107 141 62 132 minecraft:stone
fill 122 63 107 141 63 132 minecraft:light_gray_concrete
fill 126 64 113 141 79 113 minecraft:light_gray_concrete
fill 126 64 113 126 79 126 minecraft:light_gray_concrete
setblock 127 64 125 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "064"}','{"text": "botania_runes"}','{"text": "runic_altar"}','{"text": ""}']}}
setblock 128 64 125 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "altar with"}','{"text": "ingredients, a"}','{"text": "spreader aimed"}','{"text": "at it, wand HUD"}']}}
fill 136 64 113 136 79 126 minecraft:light_gray_concrete
setblock 128 64 118 botania:mana_pool{mana:1000000}
setblock 129 64 118 botania:mana_spreader{rotationX:180f,rotationY:0f,mana:1000}
setblock 133 64 118 botania:runic_altar
kw testworld use 133 64 118 up botania:manasteel_ingot
kw testworld use 133 64 118 up botania:mana_powder
kw testworld use 133 64 118 up minecraft:bone_meal
kw testworld use 133 64 118 up minecraft:sugar_cane
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
