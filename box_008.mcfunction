# 008 create/mixer
#area 46 21 65 46
fill 46 64 21 65 91 46 minecraft:air
fill 46 60 21 65 62 46 minecraft:stone
fill 46 63 21 65 63 46 minecraft:light_gray_concrete
fill 50 64 27 65 79 27 minecraft:light_gray_concrete
fill 50 64 27 50 79 40 minecraft:light_gray_concrete
setblock 51 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "008"}','{"text": "create"}','{"text": "mixer"}','{"text": ""}']}}
setblock 52 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "mixer, one"}','{"text": "block of air,"}','{"text": "basin"}','{"text": ""}']}}
fill 60 64 27 60 79 40 minecraft:light_gray_concrete
setblock 55 64 32 create:basin[facing=down]
setblock 55 66 32 create:mechanical_mixer
setblock 56 66 32 create:cogwheel[axis=y]
setblock 56 63 32 create:shaft[axis=y]
setblock 56 64 32 create:shaft[axis=y]
setblock 56 65 32 create:shaft[axis=y]
setblock 56 62 32 create:creative_motor[facing=up]{ScrollValue:32}
summon item 55.5 65 32.5 {Item:{id:"minecraft:andesite",count:16},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 55.5 65.3 32.5 {Item:{id:"minecraft:iron_nugget",count:16},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
