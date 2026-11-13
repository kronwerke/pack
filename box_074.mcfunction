# 074 botania/farm
#area 71 109 94 134
fill 71 64 109 94 91 134 minecraft:air
fill 71 60 109 94 62 134 minecraft:stone
fill 71 63 109 94 63 134 minecraft:light_gray_concrete
fill 75 64 115 94 79 115 minecraft:light_gray_concrete
fill 75 64 115 75 79 128 minecraft:light_gray_concrete
setblock 76 64 127 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "074"}','{"text": "botania"}','{"text": "farm"}','{"text": ""}']}}
setblock 77 64 127 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the finished"}','{"text": "stage 1 mana"}','{"text": "farm"}','{"text": ""}']}}
fill 89 64 115 89 79 128 minecraft:light_gray_concrete
fill 77 63 118 87 63 122 minecraft:grass_block
setblock 82 64 120 botania:mana_pool{mana:200000}
setblock 82 64 121 botania:manastar
setblock 79 64 120 botania:mana_spreader{rotationX:180f,rotationY:0f,mana:1000}
setblock 85 64 120 botania:mana_spreader{rotationX:0f,rotationY:0f,mana:1000}
setblock 78 64 119 botania:endoflame
setblock 78 64 121 botania:endoflame
setblock 86 64 119 botania:endoflame
setblock 86 64 121 botania:endoflame
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
