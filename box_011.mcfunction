# 011 create/mixer
#area 46 40 65 65
fill 46 64 40 65 91 65 minecraft:air
fill 46 60 40 65 62 65 minecraft:stone
fill 46 63 40 65 63 65 minecraft:light_gray_concrete
fill 50 64 46 65 79 46 minecraft:light_gray_concrete
fill 50 64 46 50 79 59 minecraft:light_gray_concrete
setblock 51 64 58 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "011"}','{"text": "create"}','{"text": "mixer"}','{"text": ""}']}}
setblock 52 64 58 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "mixer, one"}','{"text": "block of air,"}','{"text": "basin"}','{"text": ""}']}}
fill 60 64 46 60 79 59 minecraft:light_gray_concrete
setblock 55 64 51 create:basin[facing=down]
setblock 55 66 51 create:mechanical_mixer
setblock 56 66 51 create:cogwheel[axis=y]
setblock 56 63 51 create:shaft[axis=y]
setblock 56 64 51 create:shaft[axis=y]
setblock 56 65 51 create:shaft[axis=y]
setblock 56 62 51 create:creative_motor[facing=up]{ScrollValue:32}
summon item 55.5 65 51.5 {Item:{id:"minecraft:andesite",count:16},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 55.5 65.3 51.5 {Item:{id:"minecraft:iron_nugget",count:16},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
