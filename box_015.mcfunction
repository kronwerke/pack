# 015 create/compacting
#area 61 42 80 67
fill 61 64 42 80 91 67 minecraft:air
fill 61 60 42 80 62 67 minecraft:stone
fill 61 63 42 80 63 67 minecraft:light_gray_concrete
fill 65 64 48 80 79 48 minecraft:light_gray_concrete
fill 65 64 48 65 79 61 minecraft:light_gray_concrete
setblock 66 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "015"}','{"text": "create"}','{"text": "compacting"}','{"text": ""}']}}
setblock 67 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "press over"}','{"text": "basin making"}','{"text": "andesite from"}','{"text": "flint, gravel"}']}}
setblock 68 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "and lava"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 75 64 48 75 79 61 minecraft:light_gray_concrete
setblock 70 64 53 create:basin[facing=down]
setblock 70 66 53 create:mechanical_press[facing=south]
fill 69 64 52 71 67 52 create:andesite_casing
setblock 70 66 52 create:andesite_encased_shaft[axis=z]
setblock 70 66 51 create:creative_motor[facing=south]{ScrollValue:32}
summon item 70.5 65 53.5 {Item:{id:"minecraft:flint",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 70.5 65.3 53.5 {Item:{id:"minecraft:gravel",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
kw testworld use 70 64 53 up minecraft:lava_bucket
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
