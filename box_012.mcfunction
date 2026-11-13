# 012 create/compacting
#area 61 40 80 65
fill 61 64 40 80 91 65 minecraft:air
fill 61 60 40 80 62 65 minecraft:stone
fill 61 63 40 80 63 65 minecraft:light_gray_concrete
fill 65 64 46 80 79 46 minecraft:light_gray_concrete
fill 65 64 46 65 79 59 minecraft:light_gray_concrete
setblock 66 64 58 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "012"}','{"text": "create"}','{"text": "compacting"}','{"text": ""}']}}
setblock 67 64 58 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "press over"}','{"text": "basin making"}','{"text": "andesite from"}','{"text": "flint, gravel"}']}}
setblock 68 64 58 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "and lava"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 75 64 46 75 79 59 minecraft:light_gray_concrete
setblock 70 64 51 create:basin[facing=down]
setblock 70 66 51 create:mechanical_press[facing=south]
fill 69 64 50 71 67 50 create:andesite_casing
setblock 70 66 50 create:andesite_encased_shaft[axis=z]
setblock 70 66 49 create:creative_motor[facing=south]{ScrollValue:32}
summon item 70.5 65 51.5 {Item:{id:"minecraft:flint",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 70.5 65.3 51.5 {Item:{id:"minecraft:gravel",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
kw testworld use 70 64 51 up minecraft:lava_bucket
