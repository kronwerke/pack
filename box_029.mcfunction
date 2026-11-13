# 029 create_brass/blaze_cake
#area 233 42 254 67
fill 233 64 42 254 91 67 minecraft:air
fill 233 60 42 254 62 67 minecraft:stone
fill 233 63 42 254 63 67 minecraft:light_gray_concrete
fill 237 64 48 254 79 48 minecraft:light_gray_concrete
fill 237 64 48 237 79 61 minecraft:light_gray_concrete
setblock 238 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "029"}','{"text": "create_brass"}','{"text": "blaze_cake"}','{"text": ""}']}}
setblock 239 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "press over"}','{"text": "basin, then"}','{"text": "spout over"}','{"text": "depot"}']}}
fill 249 64 48 249 79 61 minecraft:light_gray_concrete
setblock 241 64 53 create:basin[facing=down]
setblock 241 66 53 create:mechanical_press[facing=south]
fill 240 64 52 242 67 52 create:andesite_casing
setblock 241 66 52 create:andesite_encased_shaft[axis=z]
setblock 241 66 51 create:creative_motor[facing=south]{ScrollValue:32}
summon item 241.5 65 53.5 {Item:{id:"minecraft:egg",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 241.5 65.2 53.5 {Item:{id:"minecraft:sugar",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 241.5 65.4 53.5 {Item:{id:"create:cinder_flour",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
setblock 245 64 53 create:depot
setblock 245 66 53 create:spout
setblock 245 67 53 create:fluid_tank[bottom=true,shape=window,top=true]
kw testworld use 245 64 53 up create:blaze_cake_base
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
