# 081 botania/pool
#area 26 143 45 168
fill 26 64 143 45 91 168 minecraft:air
fill 26 60 143 45 62 168 minecraft:stone
fill 26 63 143 45 63 168 minecraft:light_gray_concrete
fill 30 64 149 45 79 149 minecraft:light_gray_concrete
fill 30 64 149 30 79 162 minecraft:light_gray_concrete
setblock 31 64 161 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "081"}','{"text": "botania"}','{"text": "pool"}','{"text": ""}']}}
setblock 32 64 161 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a full pool"}','{"text": "with a spreader"}','{"text": "beam, wand in"}','{"text": "hand"}']}}
fill 40 64 149 40 79 162 minecraft:light_gray_concrete
setblock 36 64 154 botania:mana_pool{mana:1000000}
setblock 33 64 154 botania:mana_spreader{rotationX:180f,rotationY:0f,mana:1000}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
