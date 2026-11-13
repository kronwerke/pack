# 019 create/mixer
#area 46 44 65 69
fill 46 64 44 65 91 69 minecraft:air
fill 46 60 44 65 62 69 minecraft:stone
fill 46 63 44 65 63 69 minecraft:light_gray_concrete
fill 50 64 50 65 79 50 minecraft:light_gray_concrete
fill 50 64 50 50 79 63 minecraft:light_gray_concrete
setblock 51 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "019"}','{"text": "create"}','{"text": "mixer"}','{"text": ""}']}}
setblock 52 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "mixer, one"}','{"text": "block of air,"}','{"text": "basin"}','{"text": ""}']}}
fill 60 64 50 60 79 63 minecraft:light_gray_concrete
setblock 55 64 55 create:basin[facing=down]
setblock 55 66 55 create:mechanical_mixer
setblock 56 66 55 create:cogwheel[axis=y]
setblock 56 63 55 create:shaft[axis=y]
setblock 56 64 55 create:shaft[axis=y]
setblock 56 65 55 create:shaft[axis=y]
setblock 56 62 55 create:creative_motor[facing=up]{ScrollValue:32}
summon item 55.5 65 55.5 {Item:{id:"minecraft:andesite",count:16},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 55.5 65.3 55.5 {Item:{id:"minecraft:iron_nugget",count:16},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
