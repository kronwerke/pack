# 071 botania/mana_void
#area 56 109 75 134
fill 56 64 109 75 91 134 minecraft:air
fill 56 60 109 75 62 134 minecraft:stone
fill 56 63 109 75 63 134 minecraft:light_gray_concrete
fill 60 64 115 75 79 115 minecraft:light_gray_concrete
fill 60 64 115 60 79 128 minecraft:light_gray_concrete
setblock 61 64 127 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "071"}','{"text": "botania"}','{"text": "mana_void"}','{"text": ""}']}}
setblock 62 64 127 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a mana void"}','{"text": "under a pool"}','{"text": ""}','{"text": ""}']}}
fill 70 64 115 70 79 128 minecraft:light_gray_concrete
setblock 65 64 120 botania:mana_void
setblock 65 65 120 botania:mana_pool{mana:1000000}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
