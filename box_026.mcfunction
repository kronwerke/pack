# 026 create_brass/incomplete
#area 199 42 220 67
fill 199 64 42 220 91 67 minecraft:air
fill 199 60 42 220 62 67 minecraft:stone
fill 199 63 42 220 63 67 minecraft:light_gray_concrete
fill 203 64 48 220 79 48 minecraft:light_gray_concrete
fill 203 64 48 203 79 61 minecraft:light_gray_concrete
setblock 204 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "026"}','{"text": "create_brass"}','{"text": "incomplete"}','{"text": ""}']}}
setblock 205 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "belt with three"}','{"text": "deployers"}','{"text": "(cogwheel,"}','{"text": "tube, nugget)"}']}}
setblock 206 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "and a press"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 215 64 48 215 79 61 minecraft:light_gray_concrete
setblock 206 64 53 create:shaft[axis=z]
setblock 212 64 53 create:shaft[axis=z]
kw testworld use 206 64 53 up create:belt_connector
kw testworld use 212 64 53 up create:belt_connector
execute unless block 209 64 53 minecraft:air
setblock 207 66 53 create:deployer[facing=down,axis_along_first=true]{HeldItem:{id:"create:cogwheel",count:1}}
setblock 208 66 53 create:deployer[facing=down,axis_along_first=true]{HeldItem:{id:"create:large_cogwheel",count:1}}
setblock 209 66 53 create:deployer[facing=down,axis_along_first=true]{HeldItem:{id:"minecraft:iron_nugget",count:1}}
setblock 211 66 53 create:mechanical_press[facing=south]
fill 207 67 53 211 67 53 create:andesite_casing
summon item 210.5 65 53.5 {Item:{id:"create:incomplete_precision_mechanism",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
