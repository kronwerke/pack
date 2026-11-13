# 124 occultism_afrit/mineshaft
#area 199 184 218 209
fill 199 64 184 218 91 209 minecraft:air
fill 199 60 184 218 62 209 minecraft:stone
fill 199 63 184 218 63 209 minecraft:light_gray_concrete
fill 203 64 190 218 79 190 minecraft:light_gray_concrete
fill 203 64 190 203 79 203 minecraft:light_gray_concrete
setblock 204 64 202 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "124"}','{"text": "occultism_afrit"}','{"text": "mineshaft"}','{"text": ""}']}}
setblock 205 64 202 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "dimensional"}','{"text": "mineshaft with"}','{"text": "a lamp inside"}','{"text": "and a hopper"}']}}
setblock 206 64 202 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "below"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 213 64 190 213 79 203 minecraft:light_gray_concrete
setblock 208 64 195 minecraft:hopper[facing=east]
setblock 208 65 195 occultism:dimensional_mineshaft[rotation=0]
setblock 209 64 195 minecraft:chest[facing=south]{Items:[]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
