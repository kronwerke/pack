# 034 create_trains/welcome
#area 327 42 348 67
fill 327 64 42 348 91 67 minecraft:air
fill 327 60 42 348 62 67 minecraft:stone
fill 327 63 42 348 63 67 minecraft:light_gray_concrete
fill 331 64 48 348 79 48 minecraft:light_gray_concrete
fill 331 64 48 331 79 61 minecraft:light_gray_concrete
setblock 332 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "034"}','{"text": "create_trains"}','{"text": "welcome"}','{"text": ""}']}}
setblock 333 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the track"}','{"text": "assembly belt"}','{"text": ""}','{"text": ""}']}}
fill 343 64 48 343 79 61 minecraft:light_gray_concrete
setblock 334 64 53 create:shaft[axis=z]
setblock 340 64 53 create:shaft[axis=z]
kw testworld use 334 64 53 up create:belt_connector
kw testworld use 340 64 53 up create:belt_connector
execute unless block 337 64 53 minecraft:air
setblock 336 66 53 create:deployer[facing=down,axis_along_first=true]{HeldItem:{id:"minecraft:iron_nugget",count:1}}
setblock 337 66 53 create:deployer[facing=down,axis_along_first=true]{HeldItem:{id:"minecraft:iron_nugget",count:1}}
setblock 339 66 53 create:mechanical_press[facing=south]
fill 336 67 53 339 67 53 create:andesite_casing
summon item 335.5 65 53.5 {Item:{id:"minecraft:andesite_slab",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 338.5 65 53.5 {Item:{id:"create:incomplete_track",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
