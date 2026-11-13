# 094 occultism_afrit/mineshaft
#area 184 144 203 169
fill 184 64 144 203 91 169 minecraft:air
fill 184 60 144 203 62 169 minecraft:stone
fill 184 63 144 203 63 169 minecraft:light_gray_concrete
fill 188 64 150 203 79 150 minecraft:light_gray_concrete
fill 188 64 150 188 79 163 minecraft:light_gray_concrete
setblock 189 64 162 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "094"}','{"text": "occultism_afrit"}','{"text": "mineshaft"}','{"text": ""}']}}
setblock 190 64 162 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "dimensional"}','{"text": "mineshaft with"}','{"text": "a lamp inside"}','{"text": "and a hopper"}']}}
setblock 191 64 162 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "below"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 198 64 150 198 79 163 minecraft:light_gray_concrete
setblock 193 64 155 minecraft:hopper[facing=east]
setblock 193 65 155 occultism:dimensional_mineshaft[rotation=0]
setblock 194 64 155 minecraft:chest[facing=south]{Items:[]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
