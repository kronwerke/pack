# 061 gaia/dandelifeon
#area 220 105 257 148
fill 220 64 105 245 91 148 minecraft:air
fill 246 64 105 257 91 148 minecraft:air
fill 220 60 105 257 62 148 minecraft:stone
fill 220 63 105 257 63 148 minecraft:light_gray_concrete
fill 224 64 111 257 79 111 minecraft:light_gray_concrete
fill 224 64 111 224 79 142 minecraft:light_gray_concrete
setblock 225 64 141 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "061"}','{"text": "gaia"}','{"text": "dandelifeon"}','{"text": ""}']}}
setblock 226 64 141 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a 25x25 cell"}','{"text": "field"}','{"text": ""}','{"text": ""}']}}
fill 252 64 111 252 79 142 minecraft:light_gray_concrete
fill 226 63 113 250 63 137 minecraft:smooth_stone
setblock 238 63 125 minecraft:grass_block
setblock 238 64 125 botania:dandelifeon
setblock 231 64 118 botania:cellular_block
setblock 232 64 119 botania:cellular_block
setblock 233 64 119 botania:cellular_block
setblock 231 64 120 botania:cellular_block
setblock 232 64 120 botania:cellular_block
setblock 243 64 120 botania:cellular_block
setblock 244 64 120 botania:cellular_block
setblock 245 64 120 botania:cellular_block
setblock 232 64 129 botania:cellular_block
setblock 232 64 130 botania:cellular_block
setblock 232 64 131 botania:cellular_block
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
