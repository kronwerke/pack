# 010 farms/cobble_drill
fill 0 63 27 13 63 40 minecraft:light_gray_concrete
fill 0 64 27 13 71 27 minecraft:light_gray_concrete
fill 0 64 27 0 71 40 minecraft:light_gray_concrete
setblock 1 64 39 minecraft:air
setblock 1 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "010"}','{"text": "farms"}','{"text": "cobble_drill"}','{"text": ""}']}}
setblock 2 64 39 minecraft:air
setblock 2 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "water and lava"}','{"text": "cobble"}','{"text": "generator with"}','{"text": "a drill and an"}']}}
setblock 3 64 39 minecraft:air
setblock 3 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "andesite"}','{"text": "funnel, belt"}','{"text": "leading away"}','{"text": ""}']}}
setblock 4 64 32 minecraft:water
setblock 6 64 32 minecraft:lava
fill 3 64 31 7 64 31 minecraft:glass
fill 3 64 33 7 64 33 minecraft:glass
setblock 3 64 32 minecraft:glass
setblock 7 64 32 minecraft:glass
setblock 5 64 32 minecraft:cobblestone
setblock 5 64 34 create:mechanical_drill[facing=north]
setblock 5 64 35 create:shaft[axis=z]
setblock 5 64 36 create:creative_motor[facing=north]{ScrollValue:64}
setblock 6 64 34 create:andesite_funnel[facing=north]
setblock 10 64 36 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"create:belt_connector",count:1}]}
