# 021 create_brass/blaze_cake
#area 185 40 206 65
fill 185 64 40 206 91 65 minecraft:air
fill 185 60 40 206 62 65 minecraft:stone
fill 185 63 40 206 63 65 minecraft:light_gray_concrete
fill 189 64 46 206 79 46 minecraft:light_gray_concrete
fill 189 64 46 189 79 59 minecraft:light_gray_concrete
setblock 190 64 58 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "021"}','{"text": "create_brass"}','{"text": "blaze_cake"}','{"text": ""}']}}
setblock 191 64 58 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "press over"}','{"text": "basin, then"}','{"text": "spout over"}','{"text": "depot"}']}}
fill 201 64 46 201 79 59 minecraft:light_gray_concrete
setblock 193 64 51 create:basin[facing=down]
setblock 193 66 51 create:mechanical_press[facing=south]
fill 192 64 50 194 67 50 create:andesite_casing
setblock 193 66 50 create:andesite_encased_shaft[axis=z]
setblock 193 66 49 create:creative_motor[facing=south]{ScrollValue:32}
summon item 193.5 65 51.5 {Item:{id:"minecraft:egg",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 193.5 65.2 51.5 {Item:{id:"minecraft:sugar",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 193.5 65.4 51.5 {Item:{id:"create:cinder_flour",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
setblock 197 64 51 create:depot
setblock 197 66 51 create:spout
setblock 197 67 51 create:fluid_tank[bottom=true,shape=window,top=true]
kw testworld use 197 64 51 up create:blaze_cake_base
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
