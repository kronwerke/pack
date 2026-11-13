# 029 botania/pool
#area 11 86 30 111
fill 11 64 86 30 91 111 minecraft:air
fill 11 60 86 30 62 111 minecraft:stone
fill 11 63 86 30 63 111 minecraft:light_gray_concrete
fill 15 64 92 30 79 92 minecraft:light_gray_concrete
fill 15 64 92 15 79 105 minecraft:light_gray_concrete
setblock 16 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "029"}','{"text": "botania"}','{"text": "pool"}','{"text": ""}']}}
setblock 17 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a full pool"}','{"text": "with a spreader"}','{"text": "beam, wand in"}','{"text": "hand"}']}}
fill 25 64 92 25 79 105 minecraft:light_gray_concrete
setblock 21 64 97 botania:mana_pool{mana:1000000}
setblock 18 64 97 botania:mana_spreader{rotationX:180f,rotationY:0f,mana:1000}
