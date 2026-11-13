# 020 create/compacting
#area 61 44 80 69
fill 61 64 44 80 91 69 minecraft:air
fill 61 60 44 80 62 69 minecraft:stone
fill 61 63 44 80 63 69 minecraft:light_gray_concrete
fill 65 64 50 80 79 50 minecraft:light_gray_concrete
fill 65 64 50 65 79 63 minecraft:light_gray_concrete
setblock 66 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "020"}','{"text": "create"}','{"text": "compacting"}','{"text": ""}']}}
setblock 67 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "press over"}','{"text": "basin making"}','{"text": "andesite from"}','{"text": "flint, gravel"}']}}
setblock 68 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "and lava"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 75 64 50 75 79 63 minecraft:light_gray_concrete
setblock 70 64 55 create:basin[facing=down]
setblock 70 66 55 create:mechanical_press[facing=south]
fill 69 64 54 71 67 54 create:andesite_casing
setblock 70 66 54 create:andesite_encased_shaft[axis=z]
setblock 70 66 53 create:creative_motor[facing=south]{ScrollValue:32}
summon item 70.5 65 55.5 {Item:{id:"minecraft:flint",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 70.5 65.3 55.5 {Item:{id:"minecraft:gravel",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
kw testworld use 70 64 55 up minecraft:lava_bucket
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
