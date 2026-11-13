# 097 gaia/dandelifeon
#area 252 145 289 188
fill 252 64 145 277 91 188 minecraft:air
fill 278 64 145 289 91 188 minecraft:air
fill 252 60 145 289 62 188 minecraft:stone
fill 252 63 145 289 63 188 minecraft:light_gray_concrete
fill 256 64 151 289 79 151 minecraft:light_gray_concrete
fill 256 64 151 256 79 182 minecraft:light_gray_concrete
setblock 257 64 181 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "097"}','{"text": "gaia"}','{"text": "dandelifeon"}','{"text": ""}']}}
setblock 258 64 181 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a 25x25 cell"}','{"text": "field"}','{"text": ""}','{"text": ""}']}}
fill 284 64 151 284 79 182 minecraft:light_gray_concrete
fill 258 63 153 282 63 177 minecraft:smooth_stone
setblock 270 63 165 minecraft:grass_block
setblock 270 64 165 botania:dandelifeon
setblock 263 64 158 botania:cellular_block
setblock 264 64 159 botania:cellular_block
setblock 265 64 159 botania:cellular_block
setblock 263 64 160 botania:cellular_block
setblock 264 64 160 botania:cellular_block
setblock 275 64 160 botania:cellular_block
setblock 276 64 160 botania:cellular_block
setblock 277 64 160 botania:cellular_block
setblock 264 64 169 botania:cellular_block
setblock 264 64 170 botania:cellular_block
setblock 264 64 171 botania:cellular_block
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
