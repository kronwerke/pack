# 027 create_brass/brass_mixing
#area 169 44 188 69
fill 169 64 44 188 91 69 minecraft:air
fill 169 60 44 188 62 69 minecraft:stone
fill 169 63 44 188 63 69 minecraft:light_gray_concrete
fill 173 64 50 188 79 50 minecraft:light_gray_concrete
fill 173 64 50 173 79 63 minecraft:light_gray_concrete
setblock 174 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "027"}','{"text": "create_brass"}','{"text": "brass_mixing"}','{"text": ""}']}}
setblock 175 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "heated burner,"}','{"text": "basin and mixer"}','{"text": "stack"}','{"text": ""}']}}
fill 183 64 50 183 79 63 minecraft:light_gray_concrete
setblock 178 64 55 create:blaze_burner[blaze=smouldering]
kw testworld use 178 64 55 south create:creative_blaze_cake
setblock 178 65 55 create:basin[facing=down]
setblock 178 67 55 create:mechanical_mixer
setblock 179 67 55 create:cogwheel[axis=y]
setblock 179 63 55 create:shaft[axis=y]
setblock 179 64 55 create:shaft[axis=y]
setblock 179 65 55 create:shaft[axis=y]
setblock 179 66 55 create:shaft[axis=y]
setblock 179 62 55 create:creative_motor[facing=up]{ScrollValue:32}
summon item 178.5 66.2 55.5 {Item:{id:"minecraft:copper_ingot",count:64},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 178.5 66.2 55.5 {Item:{id:"create:zinc_ingot",count:32},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 178.5 66.2 55.5 {Item:{id:"minecraft:blaze_powder",count:32},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
