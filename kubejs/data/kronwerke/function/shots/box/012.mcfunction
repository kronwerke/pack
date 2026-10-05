# 012 farms/crops_harvester
fill 34 63 27 47 63 42 minecraft:light_gray_concrete
fill 34 64 27 47 71 27 minecraft:light_gray_concrete
fill 34 64 27 34 71 42 minecraft:light_gray_concrete
setblock 35 64 41 minecraft:air
setblock 35 64 41 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "012"}','{"text": "farms"}','{"text": "crops_harvester"}','{"text": ""}']}}
setblock 36 64 41 minecraft:air
setblock 36 64 41 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "bearing with"}','{"text": "two harvesters"}','{"text": "and a chest"}','{"text": "sweeping a"}']}}
setblock 37 64 41 minecraft:air
setblock 37 64 41 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "round wheat"}','{"text": "field"}','{"text": ""}','{"text": ""}']}}
fill 36 63 29 44 63 37 minecraft:farmland
fill 36 64 29 44 64 37 minecraft:wheat[age=7]
setblock 40 63 33 minecraft:water
setblock 40 64 33 create:mechanical_bearing[facing=up]
fill 40 65 33 43 65 33 create:andesite_casing
setblock 41 65 34 create:mechanical_harvester[facing=south]
setblock 43 65 34 create:mechanical_harvester[facing=south]
setblock 42 65 32 minecraft:chest
