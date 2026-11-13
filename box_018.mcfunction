# 018 create/compacting
#area 76 42 95 67
fill 76 64 42 95 91 67 minecraft:air
fill 76 60 42 95 62 67 minecraft:stone
fill 76 63 42 95 63 67 minecraft:light_gray_concrete
fill 80 64 48 95 79 48 minecraft:light_gray_concrete
fill 80 64 48 80 79 61 minecraft:light_gray_concrete
setblock 81 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "018"}','{"text": "create"}','{"text": "compacting"}','{"text": ""}']}}
setblock 82 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "press over"}','{"text": "basin making"}','{"text": "andesite from"}','{"text": "flint, gravel"}']}}
setblock 83 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "and lava"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 90 64 48 90 79 61 minecraft:light_gray_concrete
setblock 85 64 53 create:basin[facing=down]
setblock 85 66 53 create:mechanical_press[facing=south]
fill 84 64 52 86 67 52 create:andesite_casing
setblock 85 66 52 create:andesite_encased_shaft[axis=z]
setblock 85 66 51 create:creative_motor[facing=south]{ScrollValue:32}
summon item 85.5 65 53.5 {Item:{id:"minecraft:flint",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 85.5 65.3 53.5 {Item:{id:"minecraft:gravel",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
kw testworld use 85 64 53 up minecraft:lava_bucket
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
