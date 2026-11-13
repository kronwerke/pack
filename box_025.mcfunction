# 025 botania/pool
#area 11 84 30 109
fill 11 64 84 30 91 109 minecraft:air
fill 11 60 84 30 62 109 minecraft:stone
fill 11 63 84 30 63 109 minecraft:light_gray_concrete
fill 15 64 90 30 79 90 minecraft:light_gray_concrete
fill 15 64 90 15 79 103 minecraft:light_gray_concrete
setblock 16 64 102 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "025"}','{"text": "botania"}','{"text": "pool"}','{"text": ""}']}}
setblock 17 64 102 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a full pool"}','{"text": "with a spreader"}','{"text": "beam, wand in"}','{"text": "hand"}']}}
fill 25 64 90 25 79 103 minecraft:light_gray_concrete
setblock 21 64 95 botania:mana_pool{mana:1000000}
setblock 18 64 95 botania:mana_spreader{rotationX:180f,rotationY:0f,mana:1000}
