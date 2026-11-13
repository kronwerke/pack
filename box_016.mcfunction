# 016 create_brass/brass_mixing
#area 121 40 140 65
fill 121 64 40 140 91 65 minecraft:air
fill 121 60 40 140 62 65 minecraft:stone
fill 121 63 40 140 63 65 minecraft:light_gray_concrete
fill 125 64 46 140 79 46 minecraft:light_gray_concrete
fill 125 64 46 125 79 59 minecraft:light_gray_concrete
setblock 126 64 58 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "016"}','{"text": "create_brass"}','{"text": "brass_mixing"}','{"text": ""}']}}
setblock 127 64 58 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "heated burner,"}','{"text": "basin and mixer"}','{"text": "stack"}','{"text": ""}']}}
fill 135 64 46 135 79 59 minecraft:light_gray_concrete
setblock 130 64 51 create:blaze_burner[blaze=smouldering]
kw testworld use 130 64 51 south create:creative_blaze_cake
setblock 130 65 51 create:basin[facing=down]
setblock 130 67 51 create:mechanical_mixer
setblock 131 67 51 create:cogwheel[axis=y]
setblock 131 63 51 create:shaft[axis=y]
setblock 131 64 51 create:shaft[axis=y]
setblock 131 65 51 create:shaft[axis=y]
setblock 131 66 51 create:shaft[axis=y]
setblock 131 62 51 create:creative_motor[facing=up]{ScrollValue:32}
summon item 130.5 66.2 51.5 {Item:{id:"minecraft:copper_ingot",count:64},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 130.5 66.2 51.5 {Item:{id:"create:zinc_ingot",count:32},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 130.5 66.2 51.5 {Item:{id:"minecraft:blaze_powder",count:32},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
