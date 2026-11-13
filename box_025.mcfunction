# 025 create_brass/blaze_cake
#area 202 42 223 67
fill 202 64 42 223 91 67 minecraft:air
fill 202 60 42 223 62 67 minecraft:stone
fill 202 63 42 223 63 67 minecraft:light_gray_concrete
fill 206 64 48 223 79 48 minecraft:light_gray_concrete
fill 206 64 48 206 79 61 minecraft:light_gray_concrete
setblock 207 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "025"}','{"text": "create_brass"}','{"text": "blaze_cake"}','{"text": ""}']}}
setblock 208 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "press over"}','{"text": "basin, then"}','{"text": "spout over"}','{"text": "depot"}']}}
fill 218 64 48 218 79 61 minecraft:light_gray_concrete
setblock 210 64 53 create:basin[facing=down]
setblock 210 66 53 create:mechanical_press[facing=south]
fill 209 64 52 211 67 52 create:andesite_casing
setblock 210 66 52 create:andesite_encased_shaft[axis=z]
setblock 210 66 51 create:creative_motor[facing=south]{ScrollValue:32}
summon item 210.5 65 53.5 {Item:{id:"minecraft:egg",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 210.5 65.2 53.5 {Item:{id:"minecraft:sugar",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 210.5 65.4 53.5 {Item:{id:"create:cinder_flour",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
setblock 214 64 53 create:depot
setblock 214 66 53 create:spout
setblock 214 67 53 create:fluid_tank[bottom=true,shape=window,top=true]
kw testworld use 214 64 53 up create:blaze_cake_base
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
