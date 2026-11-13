# 110 alfheim/pure_essence
#area 347 147 366 172
fill 347 64 147 366 91 172 minecraft:air
fill 347 60 147 366 62 172 minecraft:stone
fill 347 63 147 366 63 172 minecraft:light_gray_concrete
fill 351 64 153 366 79 153 minecraft:light_gray_concrete
fill 351 64 153 351 79 166 minecraft:light_gray_concrete
setblock 352 64 165 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "110"}','{"text": "alfheim"}','{"text": "pure_essence"}','{"text": ""}']}}
setblock 353 64 165 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the pure daisy"}','{"text": "on end stone"}','{"text": "with the"}','{"text": "essence cloud"}']}}
fill 361 64 153 361 79 166 minecraft:light_gray_concrete
setblock 356 63 158 minecraft:grass_block[snowy=false]
setblock 356 64 158 botania:pure_daisy
setblock 355 64 157 minecraft:end_stone
setblock 355 64 158 minecraft:end_stone
setblock 355 64 159 minecraft:end_stone
setblock 356 64 157 minecraft:cobbled_deepslate
setblock 356 64 159 minecraft:end_stone
setblock 357 64 157 minecraft:end_stone
setblock 357 64 158 minecraft:end_stone
setblock 357 64 159 minecraft:cobbled_deepslate
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
