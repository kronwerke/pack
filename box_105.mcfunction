# 105 gaia/dandelifeon
#area 250 147 287 190
fill 250 64 147 275 91 190 minecraft:air
fill 276 64 147 287 91 190 minecraft:air
fill 250 60 147 287 62 190 minecraft:stone
fill 250 63 147 287 63 190 minecraft:light_gray_concrete
fill 254 64 153 287 79 153 minecraft:light_gray_concrete
fill 254 64 153 254 79 184 minecraft:light_gray_concrete
setblock 255 64 183 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "105"}','{"text": "gaia"}','{"text": "dandelifeon"}','{"text": ""}']}}
setblock 256 64 183 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a 25x25 cell"}','{"text": "field"}','{"text": ""}','{"text": ""}']}}
fill 282 64 153 282 79 184 minecraft:light_gray_concrete
fill 256 63 155 280 63 179 minecraft:smooth_stone
setblock 268 63 167 minecraft:grass_block
setblock 268 64 167 botania:dandelifeon
setblock 261 64 160 botania:cellular_block
setblock 262 64 161 botania:cellular_block
setblock 263 64 161 botania:cellular_block
setblock 261 64 162 botania:cellular_block
setblock 262 64 162 botania:cellular_block
setblock 273 64 162 botania:cellular_block
setblock 274 64 162 botania:cellular_block
setblock 275 64 162 botania:cellular_block
setblock 262 64 171 botania:cellular_block
setblock 262 64 172 botania:cellular_block
setblock 262 64 173 botania:cellular_block
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
