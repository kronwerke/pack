# 013 create_brass/brass_mixing
#area 121 21 140 46
fill 121 64 21 140 91 46 minecraft:air
fill 121 60 21 140 62 46 minecraft:stone
fill 121 63 21 140 63 46 minecraft:light_gray_concrete
fill 125 64 27 140 79 27 minecraft:light_gray_concrete
fill 125 64 27 125 79 40 minecraft:light_gray_concrete
setblock 126 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "013"}','{"text": "create_brass"}','{"text": "brass_mixing"}','{"text": ""}']}}
setblock 127 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "heated burner,"}','{"text": "basin and mixer"}','{"text": "stack"}','{"text": ""}']}}
fill 135 64 27 135 79 40 minecraft:light_gray_concrete
setblock 130 64 32 create:blaze_burner[blaze=smouldering]
kw testworld use 130 64 32 south create:creative_blaze_cake
setblock 130 65 32 create:basin[facing=down]
setblock 130 67 32 create:mechanical_mixer
setblock 131 67 32 create:cogwheel[axis=y]
setblock 131 63 32 create:shaft[axis=y]
setblock 131 64 32 create:shaft[axis=y]
setblock 131 65 32 create:shaft[axis=y]
setblock 131 66 32 create:shaft[axis=y]
setblock 131 62 32 create:creative_motor[facing=up]{ScrollValue:32}
summon item 130.5 66.2 32.5 {Item:{id:"minecraft:copper_ingot",count:64},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 130.5 66.2 32.5 {Item:{id:"create:zinc_ingot",count:32},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 130.5 66.2 32.5 {Item:{id:"minecraft:blaze_powder",count:32},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
