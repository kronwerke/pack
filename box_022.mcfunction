# 022 create_brass/brass_mixing
#area 153 42 172 67
fill 153 64 42 172 91 67 minecraft:air
fill 153 60 42 172 62 67 minecraft:stone
fill 153 63 42 172 63 67 minecraft:light_gray_concrete
fill 157 64 48 172 79 48 minecraft:light_gray_concrete
fill 157 64 48 157 79 61 minecraft:light_gray_concrete
setblock 158 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "022"}','{"text": "create_brass"}','{"text": "brass_mixing"}','{"text": ""}']}}
setblock 159 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "heated burner,"}','{"text": "basin and mixer"}','{"text": "stack"}','{"text": ""}']}}
fill 167 64 48 167 79 61 minecraft:light_gray_concrete
setblock 162 64 53 create:blaze_burner[blaze=smouldering]
kw testworld use 162 64 53 south create:creative_blaze_cake
setblock 162 65 53 create:basin[facing=down]
setblock 162 67 53 create:mechanical_mixer
setblock 163 67 53 create:cogwheel[axis=y]
setblock 163 63 53 create:shaft[axis=y]
setblock 163 64 53 create:shaft[axis=y]
setblock 163 65 53 create:shaft[axis=y]
setblock 163 66 53 create:shaft[axis=y]
setblock 163 62 53 create:creative_motor[facing=up]{ScrollValue:32}
summon item 162.5 66.2 53.5 {Item:{id:"minecraft:copper_ingot",count:64},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 162.5 66.2 53.5 {Item:{id:"create:zinc_ingot",count:32},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 162.5 66.2 53.5 {Item:{id:"minecraft:blaze_powder",count:32},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
