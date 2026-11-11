# 009 create/compacting
#area 61 21 80 46
fill 61 64 21 80 91 46 minecraft:air
fill 61 60 21 80 62 46 minecraft:stone
fill 61 63 21 80 63 46 minecraft:light_gray_concrete
fill 65 64 27 80 79 27 minecraft:light_gray_concrete
fill 65 64 27 65 79 40 minecraft:light_gray_concrete
setblock 66 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "009"}','{"text": "create"}','{"text": "compacting"}','{"text": ""}']}}
setblock 67 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "press over"}','{"text": "basin making"}','{"text": "andesite from"}','{"text": "flint, gravel"}']}}
setblock 68 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "and lava"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 75 64 27 75 79 40 minecraft:light_gray_concrete
setblock 70 64 32 create:basin[facing=down]
setblock 70 66 32 create:mechanical_press[facing=south]
fill 69 64 31 71 67 31 create:andesite_casing
setblock 70 66 31 create:andesite_encased_shaft[axis=z]
setblock 70 66 30 create:creative_motor[facing=south]{ScrollValue:32}
summon item 70.5 65 32.5 {Item:{id:"minecraft:flint",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 70.5 65.3 32.5 {Item:{id:"minecraft:gravel",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
kw testworld use 70 64 32 up minecraft:lava_bucket
