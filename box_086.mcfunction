# 086 alfheim/pure_essence
#area 287 109 306 134
fill 287 64 109 306 91 134 minecraft:air
fill 287 60 109 306 62 134 minecraft:stone
fill 287 63 109 306 63 134 minecraft:light_gray_concrete
fill 291 64 115 306 79 115 minecraft:light_gray_concrete
fill 291 64 115 291 79 128 minecraft:light_gray_concrete
setblock 292 64 127 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "086"}','{"text": "alfheim"}','{"text": "pure_essence"}','{"text": ""}']}}
setblock 293 64 127 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the pure daisy"}','{"text": "on end stone"}','{"text": "with the"}','{"text": "essence cloud"}']}}
fill 301 64 115 301 79 128 minecraft:light_gray_concrete
setblock 296 63 120 minecraft:grass_block[snowy=false]
setblock 296 64 120 botania:pure_daisy
setblock 295 64 119 minecraft:end_stone
setblock 295 64 120 minecraft:end_stone
setblock 295 64 121 minecraft:end_stone
setblock 296 64 119 minecraft:cobbled_deepslate
setblock 296 64 121 minecraft:end_stone
setblock 297 64 119 minecraft:end_stone
setblock 297 64 120 minecraft:end_stone
setblock 297 64 121 minecraft:cobbled_deepslate
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
