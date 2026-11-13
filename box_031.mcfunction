# 031 create_brass/blaze_cake
#area 233 44 254 69
fill 233 64 44 254 91 69 minecraft:air
fill 233 60 44 254 62 69 minecraft:stone
fill 233 63 44 254 63 69 minecraft:light_gray_concrete
fill 237 64 50 254 79 50 minecraft:light_gray_concrete
fill 237 64 50 237 79 63 minecraft:light_gray_concrete
setblock 238 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "031"}','{"text": "create_brass"}','{"text": "blaze_cake"}','{"text": ""}']}}
setblock 239 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "press over"}','{"text": "basin, then"}','{"text": "spout over"}','{"text": "depot"}']}}
fill 249 64 50 249 79 63 minecraft:light_gray_concrete
setblock 241 64 55 create:basin[facing=down]
setblock 241 66 55 create:mechanical_press[facing=south]
fill 240 64 54 242 67 54 create:andesite_casing
setblock 241 66 54 create:andesite_encased_shaft[axis=z]
setblock 241 66 53 create:creative_motor[facing=south]{ScrollValue:32}
summon item 241.5 65 55.5 {Item:{id:"minecraft:egg",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 241.5 65.2 55.5 {Item:{id:"minecraft:sugar",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 241.5 65.4 55.5 {Item:{id:"create:cinder_flour",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
setblock 245 64 55 create:depot
setblock 245 66 55 create:spout
setblock 245 67 55 create:fluid_tank[bottom=true,shape=window,top=true]
kw testworld use 245 64 55 up create:blaze_cake_base
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
