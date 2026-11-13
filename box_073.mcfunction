# 073 gaia/dandelifeon
#area 220 107 257 150
fill 220 64 107 245 91 150 minecraft:air
fill 246 64 107 257 91 150 minecraft:air
fill 220 60 107 257 62 150 minecraft:stone
fill 220 63 107 257 63 150 minecraft:light_gray_concrete
fill 224 64 113 257 79 113 minecraft:light_gray_concrete
fill 224 64 113 224 79 144 minecraft:light_gray_concrete
setblock 225 64 143 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "073"}','{"text": "gaia"}','{"text": "dandelifeon"}','{"text": ""}']}}
setblock 226 64 143 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a 25x25 cell"}','{"text": "field"}','{"text": ""}','{"text": ""}']}}
fill 252 64 113 252 79 144 minecraft:light_gray_concrete
fill 226 63 115 250 63 139 minecraft:smooth_stone
setblock 238 63 127 minecraft:grass_block
setblock 238 64 127 botania:dandelifeon
setblock 231 64 120 botania:cellular_block
setblock 232 64 121 botania:cellular_block
setblock 233 64 121 botania:cellular_block
setblock 231 64 122 botania:cellular_block
setblock 232 64 122 botania:cellular_block
setblock 243 64 122 botania:cellular_block
setblock 244 64 122 botania:cellular_block
setblock 245 64 122 botania:cellular_block
setblock 232 64 131 botania:cellular_block
setblock 232 64 132 botania:cellular_block
setblock 232 64 133 botania:cellular_block
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
