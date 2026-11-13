# 067 botania/manastar
#area 41 107 60 132
fill 41 64 107 60 91 132 minecraft:air
fill 41 60 107 60 62 132 minecraft:stone
fill 41 63 107 60 63 132 minecraft:light_gray_concrete
fill 45 64 113 60 79 113 minecraft:light_gray_concrete
fill 45 64 113 45 79 126 minecraft:light_gray_concrete
setblock 46 64 125 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "067"}','{"text": "botania"}','{"text": "manastar"}','{"text": ""}']}}
setblock 47 64 125 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a blue Manastar"}','{"text": "next to a pool"}','{"text": ""}','{"text": ""}']}}
fill 55 64 113 55 79 126 minecraft:light_gray_concrete
fill 48 63 116 52 63 120 minecraft:grass_block
setblock 50 64 118 botania:mana_pool{mana:400000}
setblock 51 64 118 botania:manastar
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
