# 096 occultism_afrit/mineshaft
#area 184 146 203 171
fill 184 64 146 203 91 171 minecraft:air
fill 184 60 146 203 62 171 minecraft:stone
fill 184 63 146 203 63 171 minecraft:light_gray_concrete
fill 188 64 152 203 79 152 minecraft:light_gray_concrete
fill 188 64 152 188 79 165 minecraft:light_gray_concrete
setblock 189 64 164 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "096"}','{"text": "occultism_afrit"}','{"text": "mineshaft"}','{"text": ""}']}}
setblock 190 64 164 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "dimensional"}','{"text": "mineshaft with"}','{"text": "a lamp inside"}','{"text": "and a hopper"}']}}
setblock 191 64 164 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "below"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 198 64 152 198 79 165 minecraft:light_gray_concrete
setblock 193 64 157 minecraft:hopper[facing=east]
setblock 193 65 157 occultism:dimensional_mineshaft[rotation=0]
setblock 194 64 157 minecraft:chest[facing=south]{Items:[]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
