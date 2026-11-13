# 094 gaia/dandelifeon
#area 235 143 272 186
fill 235 64 143 260 91 186 minecraft:air
fill 261 64 143 272 91 186 minecraft:air
fill 235 60 143 272 62 186 minecraft:stone
fill 235 63 143 272 63 186 minecraft:light_gray_concrete
fill 239 64 149 272 79 149 minecraft:light_gray_concrete
fill 239 64 149 239 79 180 minecraft:light_gray_concrete
setblock 240 64 179 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "094"}','{"text": "gaia"}','{"text": "dandelifeon"}','{"text": ""}']}}
setblock 241 64 179 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a 25x25 cell"}','{"text": "field"}','{"text": ""}','{"text": ""}']}}
fill 267 64 149 267 79 180 minecraft:light_gray_concrete
fill 241 63 151 265 63 175 minecraft:smooth_stone
setblock 253 63 163 minecraft:grass_block
setblock 253 64 163 botania:dandelifeon
setblock 246 64 156 botania:cellular_block
setblock 247 64 157 botania:cellular_block
setblock 248 64 157 botania:cellular_block
setblock 246 64 158 botania:cellular_block
setblock 247 64 158 botania:cellular_block
setblock 258 64 158 botania:cellular_block
setblock 259 64 158 botania:cellular_block
setblock 260 64 158 botania:cellular_block
setblock 247 64 167 botania:cellular_block
setblock 247 64 168 botania:cellular_block
setblock 247 64 169 botania:cellular_block
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
