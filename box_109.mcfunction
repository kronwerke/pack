# 109 occultism_afrit/mineshaft
#area 184 180 203 205
fill 184 64 180 203 91 205 minecraft:air
fill 184 60 180 203 62 205 minecraft:stone
fill 184 63 180 203 63 205 minecraft:light_gray_concrete
fill 188 64 186 203 79 186 minecraft:light_gray_concrete
fill 188 64 186 188 79 199 minecraft:light_gray_concrete
setblock 189 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "109"}','{"text": "occultism_afrit"}','{"text": "mineshaft"}','{"text": ""}']}}
setblock 190 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "dimensional"}','{"text": "mineshaft with"}','{"text": "a lamp inside"}','{"text": "and a hopper"}']}}
setblock 191 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "below"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 198 64 186 198 79 199 minecraft:light_gray_concrete
setblock 193 64 191 minecraft:hopper[facing=east]
setblock 193 65 191 occultism:dimensional_mineshaft[rotation=0]
setblock 194 64 191 minecraft:chest[facing=south]{Items:[]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
