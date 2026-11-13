# 019 create_brass/brass_mixing
#area 121 42 140 67
fill 121 64 42 140 91 67 minecraft:air
fill 121 60 42 140 62 67 minecraft:stone
fill 121 63 42 140 63 67 minecraft:light_gray_concrete
fill 125 64 48 140 79 48 minecraft:light_gray_concrete
fill 125 64 48 125 79 61 minecraft:light_gray_concrete
setblock 126 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "019"}','{"text": "create_brass"}','{"text": "brass_mixing"}','{"text": ""}']}}
setblock 127 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "heated burner,"}','{"text": "basin and mixer"}','{"text": "stack"}','{"text": ""}']}}
fill 135 64 48 135 79 61 minecraft:light_gray_concrete
setblock 130 64 53 create:blaze_burner[blaze=smouldering]
kw testworld use 130 64 53 south create:creative_blaze_cake
setblock 130 65 53 create:basin[facing=down]
setblock 130 67 53 create:mechanical_mixer
setblock 131 67 53 create:cogwheel[axis=y]
setblock 131 63 53 create:shaft[axis=y]
setblock 131 64 53 create:shaft[axis=y]
setblock 131 65 53 create:shaft[axis=y]
setblock 131 66 53 create:shaft[axis=y]
setblock 131 62 53 create:creative_motor[facing=up]{ScrollValue:32}
summon item 130.5 66.2 53.5 {Item:{id:"minecraft:copper_ingot",count:64},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 130.5 66.2 53.5 {Item:{id:"create:zinc_ingot",count:32},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 130.5 66.2 53.5 {Item:{id:"minecraft:blaze_powder",count:32},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
