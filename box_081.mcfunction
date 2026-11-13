# 081 botania/pool
#area 26 139 45 164
fill 26 64 139 45 91 164 minecraft:air
fill 26 60 139 45 62 164 minecraft:stone
fill 26 63 139 45 63 164 minecraft:light_gray_concrete
fill 30 64 145 45 79 145 minecraft:light_gray_concrete
fill 30 64 145 30 79 158 minecraft:light_gray_concrete
setblock 31 64 157 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "081"}','{"text": "botania"}','{"text": "pool"}','{"text": ""}']}}
setblock 32 64 157 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a full pool"}','{"text": "with a spreader"}','{"text": "beam, wand in"}','{"text": "hand"}']}}
fill 40 64 145 40 79 158 minecraft:light_gray_concrete
setblock 36 64 150 botania:mana_pool{mana:1000000}
setblock 33 64 150 botania:mana_spreader{rotationX:180f,rotationY:0f,mana:1000}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
