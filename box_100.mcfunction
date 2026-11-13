# 100 alfheim/pure_essence
#area 319 145 338 170
fill 319 64 145 338 91 170 minecraft:air
fill 319 60 145 338 62 170 minecraft:stone
fill 319 63 145 338 63 170 minecraft:light_gray_concrete
fill 323 64 151 338 79 151 minecraft:light_gray_concrete
fill 323 64 151 323 79 164 minecraft:light_gray_concrete
setblock 324 64 163 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "100"}','{"text": "alfheim"}','{"text": "pure_essence"}','{"text": ""}']}}
setblock 325 64 163 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the pure daisy"}','{"text": "on end stone"}','{"text": "with the"}','{"text": "essence cloud"}']}}
fill 333 64 151 333 79 164 minecraft:light_gray_concrete
setblock 328 63 156 minecraft:grass_block[snowy=false]
setblock 328 64 156 botania:pure_daisy
setblock 327 64 155 minecraft:end_stone
setblock 327 64 156 minecraft:end_stone
setblock 327 64 157 minecraft:end_stone
setblock 328 64 155 minecraft:cobbled_deepslate
setblock 328 64 157 minecraft:end_stone
setblock 329 64 155 minecraft:end_stone
setblock 329 64 156 minecraft:end_stone
setblock 329 64 157 minecraft:cobbled_deepslate
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
