# 050 occultism_afrit/mineshaft
#area 122 123 141 148
fill 122 64 123 141 91 148 minecraft:air
fill 122 60 123 141 62 148 minecraft:stone
fill 122 63 123 141 63 148 minecraft:light_gray_concrete
fill 126 64 129 141 79 129 minecraft:light_gray_concrete
fill 126 64 129 126 79 142 minecraft:light_gray_concrete
setblock 127 64 141 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "050"}','{"text": "occultism_afrit"}','{"text": "mineshaft"}','{"text": ""}']}}
setblock 128 64 141 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "dimensional"}','{"text": "mineshaft with"}','{"text": "a lamp inside"}','{"text": "and a hopper"}']}}
setblock 129 64 141 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "below"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 136 64 129 136 79 142 minecraft:light_gray_concrete
setblock 131 64 134 minecraft:hopper[facing=east]
setblock 131 65 134 occultism:dimensional_mineshaft[rotation=0]
setblock 132 64 134 minecraft:chest[facing=south]{Items:[]}
