# 080 botania/mana_void
#area 56 139 75 164
fill 56 64 139 75 91 164 minecraft:air
fill 56 60 139 75 62 164 minecraft:stone
fill 56 63 139 75 63 164 minecraft:light_gray_concrete
fill 60 64 145 75 79 145 minecraft:light_gray_concrete
fill 60 64 145 60 79 158 minecraft:light_gray_concrete
setblock 61 64 157 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "080"}','{"text": "botania"}','{"text": "mana_void"}','{"text": ""}']}}
setblock 62 64 157 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a mana void"}','{"text": "under a pool"}','{"text": ""}','{"text": ""}']}}
fill 70 64 145 70 79 158 minecraft:light_gray_concrete
setblock 65 64 150 botania:mana_void
setblock 65 65 150 botania:mana_pool{mana:1000000}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
