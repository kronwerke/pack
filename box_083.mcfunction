# 083 botania/pool
#area 26 145 45 170
fill 26 64 145 45 91 170 minecraft:air
fill 26 60 145 45 62 170 minecraft:stone
fill 26 63 145 45 63 170 minecraft:light_gray_concrete
fill 30 64 151 45 79 151 minecraft:light_gray_concrete
fill 30 64 151 30 79 164 minecraft:light_gray_concrete
setblock 31 64 163 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "083"}','{"text": "botania"}','{"text": "pool"}','{"text": ""}']}}
setblock 32 64 163 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a full pool"}','{"text": "with a spreader"}','{"text": "beam, wand in"}','{"text": "hand"}']}}
fill 40 64 151 40 79 164 minecraft:light_gray_concrete
setblock 36 64 156 botania:mana_pool{mana:1000000}
setblock 33 64 156 botania:mana_spreader{rotationX:180f,rotationY:0f,mana:1000}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
