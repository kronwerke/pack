# 023 create_brass/blaze_cake
#area 185 42 206 67
fill 185 64 42 206 91 67 minecraft:air
fill 185 60 42 206 62 67 minecraft:stone
fill 185 63 42 206 63 67 minecraft:light_gray_concrete
fill 189 64 48 206 79 48 minecraft:light_gray_concrete
fill 189 64 48 189 79 61 minecraft:light_gray_concrete
setblock 190 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "023"}','{"text": "create_brass"}','{"text": "blaze_cake"}','{"text": ""}']}}
setblock 191 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "press over"}','{"text": "basin, then"}','{"text": "spout over"}','{"text": "depot"}']}}
fill 201 64 48 201 79 61 minecraft:light_gray_concrete
setblock 193 64 53 create:basin[facing=down]
setblock 193 66 53 create:mechanical_press[facing=south]
fill 192 64 52 194 67 52 create:andesite_casing
setblock 193 66 52 create:andesite_encased_shaft[axis=z]
setblock 193 66 51 create:creative_motor[facing=south]{ScrollValue:32}
summon item 193.5 65 53.5 {Item:{id:"minecraft:egg",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 193.5 65.2 53.5 {Item:{id:"minecraft:sugar",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 193.5 65.4 53.5 {Item:{id:"create:cinder_flour",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
setblock 197 64 53 create:depot
setblock 197 66 53 create:spout
setblock 197 67 53 create:fluid_tank[bottom=true,shape=window,top=true]
kw testworld use 197 64 53 up create:blaze_cake_base
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
