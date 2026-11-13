# 076 alfheim/pure_essence
#area 287 107 306 132
fill 287 64 107 306 91 132 minecraft:air
fill 287 60 107 306 62 132 minecraft:stone
fill 287 63 107 306 63 132 minecraft:light_gray_concrete
fill 291 64 113 306 79 113 minecraft:light_gray_concrete
fill 291 64 113 291 79 126 minecraft:light_gray_concrete
setblock 292 64 125 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "076"}','{"text": "alfheim"}','{"text": "pure_essence"}','{"text": ""}']}}
setblock 293 64 125 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the pure daisy"}','{"text": "on end stone"}','{"text": "with the"}','{"text": "essence cloud"}']}}
fill 301 64 113 301 79 126 minecraft:light_gray_concrete
setblock 296 63 118 minecraft:grass_block[snowy=false]
setblock 296 64 118 botania:pure_daisy
setblock 295 64 117 minecraft:end_stone
setblock 295 64 118 minecraft:end_stone
setblock 295 64 119 minecraft:end_stone
setblock 296 64 117 minecraft:cobbled_deepslate
setblock 296 64 119 minecraft:end_stone
setblock 297 64 117 minecraft:end_stone
setblock 297 64 118 minecraft:end_stone
setblock 297 64 119 minecraft:cobbled_deepslate
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
