# 079 occultism_afrit/mineshaft
#area 122 144 141 169
fill 122 64 144 141 91 169 minecraft:air
fill 122 60 144 141 62 169 minecraft:stone
fill 122 63 144 141 63 169 minecraft:light_gray_concrete
fill 126 64 150 141 79 150 minecraft:light_gray_concrete
fill 126 64 150 126 79 163 minecraft:light_gray_concrete
setblock 127 64 162 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "079"}','{"text": "occultism_afrit"}','{"text": "mineshaft"}','{"text": ""}']}}
setblock 128 64 162 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "dimensional"}','{"text": "mineshaft with"}','{"text": "a lamp inside"}','{"text": "and a hopper"}']}}
setblock 129 64 162 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "below"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 136 64 150 136 79 163 minecraft:light_gray_concrete
setblock 131 64 155 minecraft:hopper[facing=east]
setblock 131 65 155 occultism:dimensional_mineshaft[rotation=0]
setblock 132 64 155 minecraft:chest[facing=south]{Items:[]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
