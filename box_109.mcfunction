# 109 occultism_afrit/mineshaft
#area 184 182 203 207
fill 184 64 182 203 91 207 minecraft:air
fill 184 60 182 203 62 207 minecraft:stone
fill 184 63 182 203 63 207 minecraft:light_gray_concrete
fill 188 64 188 203 79 188 minecraft:light_gray_concrete
fill 188 64 188 188 79 201 minecraft:light_gray_concrete
setblock 189 64 200 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "109"}','{"text": "occultism_afrit"}','{"text": "mineshaft"}','{"text": ""}']}}
setblock 190 64 200 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "dimensional"}','{"text": "mineshaft with"}','{"text": "a lamp inside"}','{"text": "and a hopper"}']}}
setblock 191 64 200 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "below"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 198 64 188 198 79 201 minecraft:light_gray_concrete
setblock 193 64 193 minecraft:hopper[facing=east]
setblock 193 65 193 occultism:dimensional_mineshaft[rotation=0]
setblock 194 64 193 minecraft:chest[facing=south]{Items:[]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
