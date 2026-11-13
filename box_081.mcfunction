# 081 botania/farm
#area 71 139 94 164
fill 71 64 139 94 91 164 minecraft:air
fill 71 60 139 94 62 164 minecraft:stone
fill 71 63 139 94 63 164 minecraft:light_gray_concrete
fill 75 64 145 94 79 145 minecraft:light_gray_concrete
fill 75 64 145 75 79 158 minecraft:light_gray_concrete
setblock 76 64 157 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "081"}','{"text": "botania"}','{"text": "farm"}','{"text": ""}']}}
setblock 77 64 157 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the finished"}','{"text": "stage 1 mana"}','{"text": "farm"}','{"text": ""}']}}
fill 89 64 145 89 79 158 minecraft:light_gray_concrete
fill 77 63 148 87 63 152 minecraft:grass_block
setblock 82 64 150 botania:mana_pool{mana:200000}
setblock 82 64 151 botania:manastar
setblock 79 64 150 botania:mana_spreader{rotationX:180f,rotationY:0f,mana:1000}
setblock 85 64 150 botania:mana_spreader{rotationX:0f,rotationY:0f,mana:1000}
setblock 78 64 149 botania:endoflame
setblock 78 64 151 botania:endoflame
setblock 86 64 149 botania:endoflame
setblock 86 64 151 botania:endoflame
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
