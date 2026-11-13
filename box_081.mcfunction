# 081 gaia/dandelifeon
#area 220 109 257 152
fill 220 64 109 245 91 152 minecraft:air
fill 246 64 109 257 91 152 minecraft:air
fill 220 60 109 257 62 152 minecraft:stone
fill 220 63 109 257 63 152 minecraft:light_gray_concrete
fill 224 64 115 257 79 115 minecraft:light_gray_concrete
fill 224 64 115 224 79 146 minecraft:light_gray_concrete
setblock 225 64 145 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "081"}','{"text": "gaia"}','{"text": "dandelifeon"}','{"text": ""}']}}
setblock 226 64 145 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a 25x25 cell"}','{"text": "field"}','{"text": ""}','{"text": ""}']}}
fill 252 64 115 252 79 146 minecraft:light_gray_concrete
fill 226 63 117 250 63 141 minecraft:smooth_stone
setblock 238 63 129 minecraft:grass_block
setblock 238 64 129 botania:dandelifeon
setblock 231 64 122 botania:cellular_block
setblock 232 64 123 botania:cellular_block
setblock 233 64 123 botania:cellular_block
setblock 231 64 124 botania:cellular_block
setblock 232 64 124 botania:cellular_block
setblock 243 64 124 botania:cellular_block
setblock 244 64 124 botania:cellular_block
setblock 245 64 124 botania:cellular_block
setblock 232 64 133 botania:cellular_block
setblock 232 64 134 botania:cellular_block
setblock 232 64 135 botania:cellular_block
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
