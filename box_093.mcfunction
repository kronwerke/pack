# 093 botania/mana_void
#area 56 147 75 172
fill 56 64 147 75 91 172 minecraft:air
fill 56 60 147 75 62 172 minecraft:stone
fill 56 63 147 75 63 172 minecraft:light_gray_concrete
fill 60 64 153 75 79 153 minecraft:light_gray_concrete
fill 60 64 153 60 79 166 minecraft:light_gray_concrete
setblock 61 64 165 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "093"}','{"text": "botania"}','{"text": "mana_void"}','{"text": ""}']}}
setblock 62 64 165 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a mana void"}','{"text": "under a pool"}','{"text": ""}','{"text": ""}']}}
fill 70 64 153 70 79 166 minecraft:light_gray_concrete
setblock 65 64 158 botania:mana_void
setblock 65 65 158 botania:mana_pool{mana:1000000}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
