# 036 create_trains/welcome
#area 327 44 348 69
fill 327 64 44 348 91 69 minecraft:air
fill 327 60 44 348 62 69 minecraft:stone
fill 327 63 44 348 63 69 minecraft:light_gray_concrete
fill 331 64 50 348 79 50 minecraft:light_gray_concrete
fill 331 64 50 331 79 63 minecraft:light_gray_concrete
setblock 332 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "036"}','{"text": "create_trains"}','{"text": "welcome"}','{"text": ""}']}}
setblock 333 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the track"}','{"text": "assembly belt"}','{"text": ""}','{"text": ""}']}}
fill 343 64 50 343 79 63 minecraft:light_gray_concrete
setblock 334 64 55 create:shaft[axis=z]
setblock 340 64 55 create:shaft[axis=z]
kw testworld use 334 64 55 up create:belt_connector
kw testworld use 340 64 55 up create:belt_connector
execute unless block 337 64 55 minecraft:air
setblock 336 66 55 create:deployer[facing=down,axis_along_first=true]{HeldItem:{id:"minecraft:iron_nugget",count:1}}
setblock 337 66 55 create:deployer[facing=down,axis_along_first=true]{HeldItem:{id:"minecraft:iron_nugget",count:1}}
setblock 339 66 55 create:mechanical_press[facing=south]
fill 336 67 55 339 67 55 create:andesite_casing
summon item 335.5 65 55.5 {Item:{id:"minecraft:andesite_slab",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 338.5 65 55.5 {Item:{id:"create:incomplete_track",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
