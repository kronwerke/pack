# 072 botania/manastar
#area 41 109 60 134
fill 41 64 109 60 91 134 minecraft:air
fill 41 60 109 60 62 134 minecraft:stone
fill 41 63 109 60 63 134 minecraft:light_gray_concrete
fill 45 64 115 60 79 115 minecraft:light_gray_concrete
fill 45 64 115 45 79 128 minecraft:light_gray_concrete
setblock 46 64 127 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "072"}','{"text": "botania"}','{"text": "manastar"}','{"text": ""}']}}
setblock 47 64 127 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a blue Manastar"}','{"text": "next to a pool"}','{"text": ""}','{"text": ""}']}}
fill 55 64 115 55 79 128 minecraft:light_gray_concrete
fill 48 63 118 52 63 122 minecraft:grass_block
setblock 50 64 120 botania:mana_pool{mana:400000}
setblock 51 64 120 botania:manastar
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
