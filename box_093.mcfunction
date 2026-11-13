# 093 gaia/dandelifeon
#area 220 139 257 182
fill 220 64 139 245 91 182 minecraft:air
fill 246 64 139 257 91 182 minecraft:air
fill 220 60 139 257 62 182 minecraft:stone
fill 220 63 139 257 63 182 minecraft:light_gray_concrete
fill 224 64 145 257 79 145 minecraft:light_gray_concrete
fill 224 64 145 224 79 176 minecraft:light_gray_concrete
setblock 225 64 175 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "093"}','{"text": "gaia"}','{"text": "dandelifeon"}','{"text": ""}']}}
setblock 226 64 175 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a 25x25 cell"}','{"text": "field"}','{"text": ""}','{"text": ""}']}}
fill 252 64 145 252 79 176 minecraft:light_gray_concrete
fill 226 63 147 250 63 171 minecraft:smooth_stone
setblock 238 63 159 minecraft:grass_block
setblock 238 64 159 botania:dandelifeon
setblock 231 64 152 botania:cellular_block
setblock 232 64 153 botania:cellular_block
setblock 233 64 153 botania:cellular_block
setblock 231 64 154 botania:cellular_block
setblock 232 64 154 botania:cellular_block
setblock 243 64 154 botania:cellular_block
setblock 244 64 154 botania:cellular_block
setblock 245 64 154 botania:cellular_block
setblock 232 64 163 botania:cellular_block
setblock 232 64 164 botania:cellular_block
setblock 232 64 165 botania:cellular_block
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
