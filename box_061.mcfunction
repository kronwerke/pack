# 061 botania/farm
#area 71 107 94 132
fill 71 64 107 94 91 132 minecraft:air
fill 71 60 107 94 62 132 minecraft:stone
fill 71 63 107 94 63 132 minecraft:light_gray_concrete
fill 75 64 113 94 79 113 minecraft:light_gray_concrete
fill 75 64 113 75 79 126 minecraft:light_gray_concrete
setblock 76 64 125 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "061"}','{"text": "botania"}','{"text": "farm"}','{"text": ""}']}}
setblock 77 64 125 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the finished"}','{"text": "stage 1 mana"}','{"text": "farm"}','{"text": ""}']}}
fill 89 64 113 89 79 126 minecraft:light_gray_concrete
fill 77 63 116 87 63 120 minecraft:grass_block
setblock 82 64 118 botania:mana_pool{mana:200000}
setblock 82 64 119 botania:manastar
setblock 79 64 118 botania:mana_spreader{rotationX:180f,rotationY:0f,mana:1000}
setblock 85 64 118 botania:mana_spreader{rotationX:0f,rotationY:0f,mana:1000}
setblock 78 64 117 botania:endoflame
setblock 78 64 119 botania:endoflame
setblock 86 64 117 botania:endoflame
setblock 86 64 119 botania:endoflame
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
