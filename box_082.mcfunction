# 082 botania/manastar
#area 41 143 60 168
fill 41 64 143 60 91 168 minecraft:air
fill 41 60 143 60 62 168 minecraft:stone
fill 41 63 143 60 63 168 minecraft:light_gray_concrete
fill 45 64 149 60 79 149 minecraft:light_gray_concrete
fill 45 64 149 45 79 162 minecraft:light_gray_concrete
setblock 46 64 161 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "082"}','{"text": "botania"}','{"text": "manastar"}','{"text": ""}']}}
setblock 47 64 161 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a blue Manastar"}','{"text": "next to a pool"}','{"text": ""}','{"text": ""}']}}
fill 55 64 149 55 79 162 minecraft:light_gray_concrete
fill 48 63 152 52 63 156 minecraft:grass_block
setblock 50 64 154 botania:mana_pool{mana:400000}
setblock 51 64 154 botania:manastar
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
