# 032 create/cobble_gen
fill 202 63 48 213 63 61 minecraft:light_gray_concrete
fill 202 64 48 213 71 48 minecraft:light_gray_concrete
fill 202 64 48 202 71 61 minecraft:light_gray_concrete
setblock 203 64 60 minecraft:air
setblock 203 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "032"}','{"text": "create"}','{"text": "cobble_gen"}','{"text": ""}']}}
setblock 204 64 60 minecraft:air
setblock 204 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "drill in front"}','{"text": "of a cobble"}','{"text": "generator"}','{"text": ""}']}}
setblock 206 64 53 minecraft:water
setblock 208 64 53 minecraft:lava
setblock 207 64 53 minecraft:cobblestone
fill 205 64 52 209 64 52 minecraft:glass
fill 205 64 54 206 64 54 minecraft:glass
fill 208 64 54 209 64 54 minecraft:glass
setblock 207 64 54 create:mechanical_drill[facing=north]
setblock 207 64 55 create:shaft[axis=z]
setblock 207 64 56 create:creative_motor[facing=north]{ScrollValue:64}
