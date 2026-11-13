# 021 create_brass/brass_mixing
#area 138 42 157 67
fill 138 64 42 157 91 67 minecraft:air
fill 138 60 42 157 62 67 minecraft:stone
fill 138 63 42 157 63 67 minecraft:light_gray_concrete
fill 142 64 48 157 79 48 minecraft:light_gray_concrete
fill 142 64 48 142 79 61 minecraft:light_gray_concrete
setblock 143 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "021"}','{"text": "create_brass"}','{"text": "brass_mixing"}','{"text": ""}']}}
setblock 144 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "heated burner,"}','{"text": "basin and mixer"}','{"text": "stack"}','{"text": ""}']}}
fill 152 64 48 152 79 61 minecraft:light_gray_concrete
setblock 147 64 53 create:blaze_burner[blaze=smouldering]
kw testworld use 147 64 53 south create:creative_blaze_cake
setblock 147 65 53 create:basin[facing=down]
setblock 147 67 53 create:mechanical_mixer
setblock 148 67 53 create:cogwheel[axis=y]
setblock 148 63 53 create:shaft[axis=y]
setblock 148 64 53 create:shaft[axis=y]
setblock 148 65 53 create:shaft[axis=y]
setblock 148 66 53 create:shaft[axis=y]
setblock 148 62 53 create:creative_motor[facing=up]{ScrollValue:32}
summon item 147.5 66.2 53.5 {Item:{id:"minecraft:copper_ingot",count:64},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 147.5 66.2 53.5 {Item:{id:"create:zinc_ingot",count:32},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 147.5 66.2 53.5 {Item:{id:"minecraft:blaze_powder",count:32},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
