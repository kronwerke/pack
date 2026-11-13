# 092 botania/manastar
#area 41 147 60 172
fill 41 64 147 60 91 172 minecraft:air
fill 41 60 147 60 62 172 minecraft:stone
fill 41 63 147 60 63 172 minecraft:light_gray_concrete
fill 45 64 153 60 79 153 minecraft:light_gray_concrete
fill 45 64 153 45 79 166 minecraft:light_gray_concrete
setblock 46 64 165 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "092"}','{"text": "botania"}','{"text": "manastar"}','{"text": ""}']}}
setblock 47 64 165 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a blue Manastar"}','{"text": "next to a pool"}','{"text": ""}','{"text": ""}']}}
fill 55 64 153 55 79 166 minecraft:light_gray_concrete
fill 48 63 156 52 63 160 minecraft:grass_block
setblock 50 64 158 botania:mana_pool{mana:400000}
setblock 51 64 158 botania:manastar
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
