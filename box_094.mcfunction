# 094 botania/farm
#area 71 147 94 172
fill 71 64 147 94 91 172 minecraft:air
fill 71 60 147 94 62 172 minecraft:stone
fill 71 63 147 94 63 172 minecraft:light_gray_concrete
fill 75 64 153 94 79 153 minecraft:light_gray_concrete
fill 75 64 153 75 79 166 minecraft:light_gray_concrete
setblock 76 64 165 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "094"}','{"text": "botania"}','{"text": "farm"}','{"text": ""}']}}
setblock 77 64 165 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the finished"}','{"text": "stage 1 mana"}','{"text": "farm"}','{"text": ""}']}}
fill 89 64 153 89 79 166 minecraft:light_gray_concrete
fill 77 63 156 87 63 160 minecraft:grass_block
setblock 82 64 158 botania:mana_pool{mana:200000}
setblock 82 64 159 botania:manastar
setblock 79 64 158 botania:mana_spreader{rotationX:180f,rotationY:0f,mana:1000}
setblock 85 64 158 botania:mana_spreader{rotationX:0f,rotationY:0f,mana:1000}
setblock 78 64 157 botania:endoflame
setblock 78 64 159 botania:endoflame
setblock 86 64 157 botania:endoflame
setblock 86 64 159 botania:endoflame
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
