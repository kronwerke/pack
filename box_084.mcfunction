# 084 botania/manastar
#area 41 145 60 170
fill 41 64 145 60 91 170 minecraft:air
fill 41 60 145 60 62 170 minecraft:stone
fill 41 63 145 60 63 170 minecraft:light_gray_concrete
fill 45 64 151 60 79 151 minecraft:light_gray_concrete
fill 45 64 151 45 79 164 minecraft:light_gray_concrete
setblock 46 64 163 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "084"}','{"text": "botania"}','{"text": "manastar"}','{"text": ""}']}}
setblock 47 64 163 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a blue Manastar"}','{"text": "next to a pool"}','{"text": ""}','{"text": ""}']}}
fill 55 64 151 55 79 164 minecraft:light_gray_concrete
fill 48 63 154 52 63 158 minecraft:grass_block
setblock 50 64 156 botania:mana_pool{mana:400000}
setblock 51 64 156 botania:manastar
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
