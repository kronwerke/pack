# 084 botania/farm
#area 71 145 94 170
fill 71 64 145 94 91 170 minecraft:air
fill 71 60 145 94 62 170 minecraft:stone
fill 71 63 145 94 63 170 minecraft:light_gray_concrete
fill 75 64 151 94 79 151 minecraft:light_gray_concrete
fill 75 64 151 75 79 164 minecraft:light_gray_concrete
setblock 76 64 163 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "084"}','{"text": "botania"}','{"text": "farm"}','{"text": ""}']}}
setblock 77 64 163 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the finished"}','{"text": "stage 1 mana"}','{"text": "farm"}','{"text": ""}']}}
fill 89 64 151 89 79 164 minecraft:light_gray_concrete
fill 77 63 154 87 63 158 minecraft:grass_block
setblock 82 64 156 botania:mana_pool{mana:200000}
setblock 82 64 157 botania:manastar
setblock 79 64 156 botania:mana_spreader{rotationX:180f,rotationY:0f,mana:1000}
setblock 85 64 156 botania:mana_spreader{rotationX:0f,rotationY:0f,mana:1000}
setblock 78 64 155 botania:endoflame
setblock 78 64 157 botania:endoflame
setblock 86 64 155 botania:endoflame
setblock 86 64 157 botania:endoflame
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
