# 094 gaia/dandelifeon
#area 235 145 272 188
fill 235 64 145 260 91 188 minecraft:air
fill 261 64 145 272 91 188 minecraft:air
fill 235 60 145 272 62 188 minecraft:stone
fill 235 63 145 272 63 188 minecraft:light_gray_concrete
fill 239 64 151 272 79 151 minecraft:light_gray_concrete
fill 239 64 151 239 79 182 minecraft:light_gray_concrete
setblock 240 64 181 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "094"}','{"text": "gaia"}','{"text": "dandelifeon"}','{"text": ""}']}}
setblock 241 64 181 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a 25x25 cell"}','{"text": "field"}','{"text": ""}','{"text": ""}']}}
fill 267 64 151 267 79 182 minecraft:light_gray_concrete
fill 241 63 153 265 63 177 minecraft:smooth_stone
setblock 253 63 165 minecraft:grass_block
setblock 253 64 165 botania:dandelifeon
setblock 246 64 158 botania:cellular_block
setblock 247 64 159 botania:cellular_block
setblock 248 64 159 botania:cellular_block
setblock 246 64 160 botania:cellular_block
setblock 247 64 160 botania:cellular_block
setblock 258 64 160 botania:cellular_block
setblock 259 64 160 botania:cellular_block
setblock 260 64 160 botania:cellular_block
setblock 247 64 169 botania:cellular_block
setblock 247 64 170 botania:cellular_block
setblock 247 64 171 botania:cellular_block
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
