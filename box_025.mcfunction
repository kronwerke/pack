# 025 create_brass/brass_mixing
#area 184 42 203 67
fill 184 64 42 203 91 67 minecraft:air
fill 184 60 42 203 62 67 minecraft:stone
fill 184 63 42 203 63 67 minecraft:light_gray_concrete
fill 188 64 48 203 79 48 minecraft:light_gray_concrete
fill 188 64 48 188 79 61 minecraft:light_gray_concrete
setblock 189 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "025"}','{"text": "create_brass"}','{"text": "brass_mixing"}','{"text": ""}']}}
setblock 190 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "heated burner,"}','{"text": "basin and mixer"}','{"text": "stack"}','{"text": ""}']}}
fill 198 64 48 198 79 61 minecraft:light_gray_concrete
setblock 193 64 53 create:blaze_burner[blaze=smouldering]
kw testworld use 193 64 53 south create:creative_blaze_cake
setblock 193 65 53 create:basin[facing=down]
setblock 193 67 53 create:mechanical_mixer
setblock 194 67 53 create:cogwheel[axis=y]
setblock 194 63 53 create:shaft[axis=y]
setblock 194 64 53 create:shaft[axis=y]
setblock 194 65 53 create:shaft[axis=y]
setblock 194 66 53 create:shaft[axis=y]
setblock 194 62 53 create:creative_motor[facing=up]{ScrollValue:32}
summon item 193.5 66.2 53.5 {Item:{id:"minecraft:copper_ingot",count:64},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 193.5 66.2 53.5 {Item:{id:"create:zinc_ingot",count:32},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 193.5 66.2 53.5 {Item:{id:"minecraft:blaze_powder",count:32},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
