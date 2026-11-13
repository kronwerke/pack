# 017 create/mixer
#area 46 42 65 67
fill 46 64 42 65 91 67 minecraft:air
fill 46 60 42 65 62 67 minecraft:stone
fill 46 63 42 65 63 67 minecraft:light_gray_concrete
fill 50 64 48 65 79 48 minecraft:light_gray_concrete
fill 50 64 48 50 79 61 minecraft:light_gray_concrete
setblock 51 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "017"}','{"text": "create"}','{"text": "mixer"}','{"text": ""}']}}
setblock 52 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "mixer, one"}','{"text": "block of air,"}','{"text": "basin"}','{"text": ""}']}}
fill 60 64 48 60 79 61 minecraft:light_gray_concrete
setblock 55 64 53 create:basin[facing=down]
setblock 55 66 53 create:mechanical_mixer
setblock 56 66 53 create:cogwheel[axis=y]
setblock 56 63 53 create:shaft[axis=y]
setblock 56 64 53 create:shaft[axis=y]
setblock 56 65 53 create:shaft[axis=y]
setblock 56 62 53 create:creative_motor[facing=up]{ScrollValue:32}
summon item 55.5 65 53.5 {Item:{id:"minecraft:andesite",count:16},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 55.5 65.3 53.5 {Item:{id:"minecraft:iron_nugget",count:16},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
