# 097 alfheim/pure_essence
#area 302 143 321 168
fill 302 64 143 321 91 168 minecraft:air
fill 302 60 143 321 62 168 minecraft:stone
fill 302 63 143 321 63 168 minecraft:light_gray_concrete
fill 306 64 149 321 79 149 minecraft:light_gray_concrete
fill 306 64 149 306 79 162 minecraft:light_gray_concrete
setblock 307 64 161 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "097"}','{"text": "alfheim"}','{"text": "pure_essence"}','{"text": ""}']}}
setblock 308 64 161 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the pure daisy"}','{"text": "on end stone"}','{"text": "with the"}','{"text": "essence cloud"}']}}
fill 316 64 149 316 79 162 minecraft:light_gray_concrete
setblock 311 63 154 minecraft:grass_block[snowy=false]
setblock 311 64 154 botania:pure_daisy
setblock 310 64 153 minecraft:end_stone
setblock 310 64 154 minecraft:end_stone
setblock 310 64 155 minecraft:end_stone
setblock 311 64 153 minecraft:cobbled_deepslate
setblock 311 64 155 minecraft:end_stone
setblock 312 64 153 minecraft:end_stone
setblock 312 64 154 minecraft:end_stone
setblock 312 64 155 minecraft:cobbled_deepslate
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
