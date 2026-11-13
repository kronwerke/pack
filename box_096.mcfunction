# 096 alfheim/pure_essence
#area 287 139 306 164
fill 287 64 139 306 91 164 minecraft:air
fill 287 60 139 306 62 164 minecraft:stone
fill 287 63 139 306 63 164 minecraft:light_gray_concrete
fill 291 64 145 306 79 145 minecraft:light_gray_concrete
fill 291 64 145 291 79 158 minecraft:light_gray_concrete
setblock 292 64 157 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "096"}','{"text": "alfheim"}','{"text": "pure_essence"}','{"text": ""}']}}
setblock 293 64 157 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the pure daisy"}','{"text": "on end stone"}','{"text": "with the"}','{"text": "essence cloud"}']}}
fill 301 64 145 301 79 158 minecraft:light_gray_concrete
setblock 296 63 150 minecraft:grass_block[snowy=false]
setblock 296 64 150 botania:pure_daisy
setblock 295 64 149 minecraft:end_stone
setblock 295 64 150 minecraft:end_stone
setblock 295 64 151 minecraft:end_stone
setblock 296 64 149 minecraft:cobbled_deepslate
setblock 296 64 151 minecraft:end_stone
setblock 297 64 149 minecraft:end_stone
setblock 297 64 150 minecraft:end_stone
setblock 297 64 151 minecraft:cobbled_deepslate
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
