# 055 gaia/dandelifeon
#area 190 105 227 148
fill 190 64 105 215 91 148 minecraft:air
fill 216 64 105 227 91 148 minecraft:air
fill 190 60 105 227 62 148 minecraft:stone
fill 190 63 105 227 63 148 minecraft:light_gray_concrete
fill 194 64 111 227 79 111 minecraft:light_gray_concrete
fill 194 64 111 194 79 142 minecraft:light_gray_concrete
setblock 195 64 141 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "055"}','{"text": "gaia"}','{"text": "dandelifeon"}','{"text": ""}']}}
setblock 196 64 141 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a 25x25 cell"}','{"text": "field"}','{"text": ""}','{"text": ""}']}}
fill 222 64 111 222 79 142 minecraft:light_gray_concrete
fill 196 63 113 220 63 137 minecraft:smooth_stone
setblock 208 63 125 minecraft:grass_block
setblock 208 64 125 botania:dandelifeon
setblock 201 64 118 botania:cellular_block
setblock 202 64 119 botania:cellular_block
setblock 203 64 119 botania:cellular_block
setblock 201 64 120 botania:cellular_block
setblock 202 64 120 botania:cellular_block
setblock 213 64 120 botania:cellular_block
setblock 214 64 120 botania:cellular_block
setblock 215 64 120 botania:cellular_block
setblock 202 64 129 botania:cellular_block
setblock 202 64 130 botania:cellular_block
setblock 202 64 131 botania:cellular_block
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
