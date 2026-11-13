# 026 create_brass/blaze_cake
#area 217 42 238 67
fill 217 64 42 238 91 67 minecraft:air
fill 217 60 42 238 62 67 minecraft:stone
fill 217 63 42 238 63 67 minecraft:light_gray_concrete
fill 221 64 48 238 79 48 minecraft:light_gray_concrete
fill 221 64 48 221 79 61 minecraft:light_gray_concrete
setblock 222 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "026"}','{"text": "create_brass"}','{"text": "blaze_cake"}','{"text": ""}']}}
setblock 223 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "press over"}','{"text": "basin, then"}','{"text": "spout over"}','{"text": "depot"}']}}
fill 233 64 48 233 79 61 minecraft:light_gray_concrete
setblock 225 64 53 create:basin[facing=down]
setblock 225 66 53 create:mechanical_press[facing=south]
fill 224 64 52 226 67 52 create:andesite_casing
setblock 225 66 52 create:andesite_encased_shaft[axis=z]
setblock 225 66 51 create:creative_motor[facing=south]{ScrollValue:32}
summon item 225.5 65 53.5 {Item:{id:"minecraft:egg",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 225.5 65.2 53.5 {Item:{id:"minecraft:sugar",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 225.5 65.4 53.5 {Item:{id:"create:cinder_flour",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
setblock 229 64 53 create:depot
setblock 229 66 53 create:spout
setblock 229 67 53 create:fluid_tank[bottom=true,shape=window,top=true]
kw testworld use 229 64 53 up create:blaze_cake_base
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
