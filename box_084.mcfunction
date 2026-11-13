# 084 botania/farm
#area 71 143 94 168
fill 71 64 143 94 91 168 minecraft:air
fill 71 60 143 94 62 168 minecraft:stone
fill 71 63 143 94 63 168 minecraft:light_gray_concrete
fill 75 64 149 94 79 149 minecraft:light_gray_concrete
fill 75 64 149 75 79 162 minecraft:light_gray_concrete
setblock 76 64 161 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "084"}','{"text": "botania"}','{"text": "farm"}','{"text": ""}']}}
setblock 77 64 161 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the finished"}','{"text": "stage 1 mana"}','{"text": "farm"}','{"text": ""}']}}
fill 89 64 149 89 79 162 minecraft:light_gray_concrete
fill 77 63 152 87 63 156 minecraft:grass_block
setblock 82 64 154 botania:mana_pool{mana:200000}
setblock 82 64 155 botania:manastar
setblock 79 64 154 botania:mana_spreader{rotationX:180f,rotationY:0f,mana:1000}
setblock 85 64 154 botania:mana_spreader{rotationX:0f,rotationY:0f,mana:1000}
setblock 78 64 153 botania:endoflame
setblock 78 64 155 botania:endoflame
setblock 86 64 153 botania:endoflame
setblock 86 64 155 botania:endoflame
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
