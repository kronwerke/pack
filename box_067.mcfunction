# 067 botania/pool
#area 26 107 45 132
fill 26 64 107 45 91 132 minecraft:air
fill 26 60 107 45 62 132 minecraft:stone
fill 26 63 107 45 63 132 minecraft:light_gray_concrete
fill 30 64 113 45 79 113 minecraft:light_gray_concrete
fill 30 64 113 30 79 126 minecraft:light_gray_concrete
setblock 31 64 125 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "067"}','{"text": "botania"}','{"text": "pool"}','{"text": ""}']}}
setblock 32 64 125 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a full pool"}','{"text": "with a spreader"}','{"text": "beam, wand in"}','{"text": "hand"}']}}
fill 40 64 113 40 79 126 minecraft:light_gray_concrete
setblock 36 64 118 botania:mana_pool{mana:1000000}
setblock 33 64 118 botania:mana_spreader{rotationX:180f,rotationY:0f,mana:1000}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
