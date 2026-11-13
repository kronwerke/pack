# 063 botania/mana_void
#area 56 107 75 132
fill 56 64 107 75 91 132 minecraft:air
fill 56 60 107 75 62 132 minecraft:stone
fill 56 63 107 75 63 132 minecraft:light_gray_concrete
fill 60 64 113 75 79 113 minecraft:light_gray_concrete
fill 60 64 113 60 79 126 minecraft:light_gray_concrete
setblock 61 64 125 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "063"}','{"text": "botania"}','{"text": "mana_void"}','{"text": ""}']}}
setblock 62 64 125 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a mana void"}','{"text": "under a pool"}','{"text": ""}','{"text": ""}']}}
fill 70 64 113 70 79 126 minecraft:light_gray_concrete
setblock 65 64 118 botania:mana_void
setblock 65 65 118 botania:mana_pool{mana:1000000}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
