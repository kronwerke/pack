# 052 botania/farm
#area 71 105 94 130
fill 71 64 105 94 91 130 minecraft:air
fill 71 60 105 94 62 130 minecraft:stone
fill 71 63 105 94 63 130 minecraft:light_gray_concrete
fill 75 64 111 94 79 111 minecraft:light_gray_concrete
fill 75 64 111 75 79 124 minecraft:light_gray_concrete
setblock 76 64 123 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "052"}','{"text": "botania"}','{"text": "farm"}','{"text": ""}']}}
setblock 77 64 123 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the finished"}','{"text": "stage 1 mana"}','{"text": "farm"}','{"text": ""}']}}
fill 89 64 111 89 79 124 minecraft:light_gray_concrete
fill 77 63 114 87 63 118 minecraft:grass_block
setblock 82 64 116 botania:mana_pool{mana:200000}
setblock 82 64 117 botania:manastar
setblock 79 64 116 botania:mana_spreader{rotationX:180f,rotationY:0f,mana:1000}
setblock 85 64 116 botania:mana_spreader{rotationX:0f,rotationY:0f,mana:1000}
setblock 78 64 115 botania:endoflame
setblock 78 64 117 botania:endoflame
setblock 86 64 115 botania:endoflame
setblock 86 64 117 botania:endoflame
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
