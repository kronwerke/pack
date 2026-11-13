# 025 create_brass/brass_mixing
#area 169 42 188 67
fill 169 64 42 188 91 67 minecraft:air
fill 169 60 42 188 62 67 minecraft:stone
fill 169 63 42 188 63 67 minecraft:light_gray_concrete
fill 173 64 48 188 79 48 minecraft:light_gray_concrete
fill 173 64 48 173 79 61 minecraft:light_gray_concrete
setblock 174 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "025"}','{"text": "create_brass"}','{"text": "brass_mixing"}','{"text": ""}']}}
setblock 175 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "heated burner,"}','{"text": "basin and mixer"}','{"text": "stack"}','{"text": ""}']}}
fill 183 64 48 183 79 61 minecraft:light_gray_concrete
setblock 178 64 53 create:blaze_burner[blaze=smouldering]
kw testworld use 178 64 53 south create:creative_blaze_cake
setblock 178 65 53 create:basin[facing=down]
setblock 178 67 53 create:mechanical_mixer
setblock 179 67 53 create:cogwheel[axis=y]
setblock 179 63 53 create:shaft[axis=y]
setblock 179 64 53 create:shaft[axis=y]
setblock 179 65 53 create:shaft[axis=y]
setblock 179 66 53 create:shaft[axis=y]
setblock 179 62 53 create:creative_motor[facing=up]{ScrollValue:32}
summon item 178.5 66.2 53.5 {Item:{id:"minecraft:copper_ingot",count:64},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 178.5 66.2 53.5 {Item:{id:"create:zinc_ingot",count:32},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 178.5 66.2 53.5 {Item:{id:"minecraft:blaze_powder",count:32},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
