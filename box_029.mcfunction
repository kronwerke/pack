# 029 create_brass/blaze_cake
#area 248 42 269 67
fill 248 64 42 269 91 67 minecraft:air
fill 248 60 42 269 62 67 minecraft:stone
fill 248 63 42 269 63 67 minecraft:light_gray_concrete
fill 252 64 48 269 79 48 minecraft:light_gray_concrete
fill 252 64 48 252 79 61 minecraft:light_gray_concrete
setblock 253 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "029"}','{"text": "create_brass"}','{"text": "blaze_cake"}','{"text": ""}']}}
setblock 254 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "press over"}','{"text": "basin, then"}','{"text": "spout over"}','{"text": "depot"}']}}
fill 264 64 48 264 79 61 minecraft:light_gray_concrete
setblock 256 64 53 create:basin[facing=down]
setblock 256 66 53 create:mechanical_press[facing=south]
fill 255 64 52 257 67 52 create:andesite_casing
setblock 256 66 52 create:andesite_encased_shaft[axis=z]
setblock 256 66 51 create:creative_motor[facing=south]{ScrollValue:32}
summon item 256.5 65 53.5 {Item:{id:"minecraft:egg",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 256.5 65.2 53.5 {Item:{id:"minecraft:sugar",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 256.5 65.4 53.5 {Item:{id:"create:cinder_flour",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
setblock 260 64 53 create:depot
setblock 260 66 53 create:spout
setblock 260 67 53 create:fluid_tank[bottom=true,shape=window,top=true]
kw testworld use 260 64 53 up create:blaze_cake_base
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
