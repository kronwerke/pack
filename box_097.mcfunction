# 097 alfheim/pure_essence
#area 302 145 321 170
fill 302 64 145 321 91 170 minecraft:air
fill 302 60 145 321 62 170 minecraft:stone
fill 302 63 145 321 63 170 minecraft:light_gray_concrete
fill 306 64 151 321 79 151 minecraft:light_gray_concrete
fill 306 64 151 306 79 164 minecraft:light_gray_concrete
setblock 307 64 163 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "097"}','{"text": "alfheim"}','{"text": "pure_essence"}','{"text": ""}']}}
setblock 308 64 163 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the pure daisy"}','{"text": "on end stone"}','{"text": "with the"}','{"text": "essence cloud"}']}}
fill 316 64 151 316 79 164 minecraft:light_gray_concrete
setblock 311 63 156 minecraft:grass_block[snowy=false]
setblock 311 64 156 botania:pure_daisy
setblock 310 64 155 minecraft:end_stone
setblock 310 64 156 minecraft:end_stone
setblock 310 64 157 minecraft:end_stone
setblock 311 64 155 minecraft:cobbled_deepslate
setblock 311 64 157 minecraft:end_stone
setblock 312 64 155 minecraft:end_stone
setblock 312 64 156 minecraft:end_stone
setblock 312 64 157 minecraft:cobbled_deepslate
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
