# 024 create_brass/incomplete
#area 168 42 189 67
fill 168 64 42 189 91 67 minecraft:air
fill 168 60 42 189 62 67 minecraft:stone
fill 168 63 42 189 63 67 minecraft:light_gray_concrete
fill 172 64 48 189 79 48 minecraft:light_gray_concrete
fill 172 64 48 172 79 61 minecraft:light_gray_concrete
setblock 173 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "024"}','{"text": "create_brass"}','{"text": "incomplete"}','{"text": ""}']}}
setblock 174 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "belt with three"}','{"text": "deployers"}','{"text": "(cogwheel,"}','{"text": "tube, nugget)"}']}}
setblock 175 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "and a press"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 184 64 48 184 79 61 minecraft:light_gray_concrete
setblock 175 64 53 create:shaft[axis=z]
setblock 181 64 53 create:shaft[axis=z]
kw testworld use 175 64 53 up create:belt_connector
kw testworld use 181 64 53 up create:belt_connector
execute unless block 178 64 53 minecraft:air
setblock 176 66 53 create:deployer[facing=down,axis_along_first=true]{HeldItem:{id:"create:cogwheel",count:1}}
setblock 177 66 53 create:deployer[facing=down,axis_along_first=true]{HeldItem:{id:"create:large_cogwheel",count:1}}
setblock 178 66 53 create:deployer[facing=down,axis_along_first=true]{HeldItem:{id:"minecraft:iron_nugget",count:1}}
setblock 180 66 53 create:mechanical_press[facing=south]
fill 176 67 53 180 67 53 create:andesite_casing
summon item 179.5 65 53.5 {Item:{id:"create:incomplete_precision_mechanism",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
