# 045 botania/pool
#area 26 105 45 130
fill 26 64 105 45 91 130 minecraft:air
fill 26 60 105 45 62 130 minecraft:stone
fill 26 63 105 45 63 130 minecraft:light_gray_concrete
fill 30 64 111 45 79 111 minecraft:light_gray_concrete
fill 30 64 111 30 79 124 minecraft:light_gray_concrete
setblock 31 64 123 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "045"}','{"text": "botania"}','{"text": "pool"}','{"text": ""}']}}
setblock 32 64 123 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a full pool"}','{"text": "with a spreader"}','{"text": "beam, wand in"}','{"text": "hand"}']}}
fill 40 64 111 40 79 124 minecraft:light_gray_concrete
setblock 36 64 116 botania:mana_pool{mana:1000000}
setblock 33 64 116 botania:mana_spreader{rotationX:180f,rotationY:0f,mana:1000}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
