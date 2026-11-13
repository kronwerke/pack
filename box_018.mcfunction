# 018 create_brass/incomplete
#area 136 40 157 65
fill 136 64 40 157 91 65 minecraft:air
fill 136 60 40 157 62 65 minecraft:stone
fill 136 63 40 157 63 65 minecraft:light_gray_concrete
fill 140 64 46 157 79 46 minecraft:light_gray_concrete
fill 140 64 46 140 79 59 minecraft:light_gray_concrete
setblock 141 64 58 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "018"}','{"text": "create_brass"}','{"text": "incomplete"}','{"text": ""}']}}
setblock 142 64 58 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "belt with three"}','{"text": "deployers"}','{"text": "(cogwheel,"}','{"text": "tube, nugget)"}']}}
setblock 143 64 58 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "and a press"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 152 64 46 152 79 59 minecraft:light_gray_concrete
setblock 143 64 51 create:shaft[axis=z]
setblock 149 64 51 create:shaft[axis=z]
kw testworld use 143 64 51 up create:belt_connector
kw testworld use 149 64 51 up create:belt_connector
execute unless block 146 64 51 minecraft:air
setblock 144 66 51 create:deployer[facing=down,axis_along_first=true]{HeldItem:{id:"create:cogwheel",count:1}}
setblock 145 66 51 create:deployer[facing=down,axis_along_first=true]{HeldItem:{id:"create:large_cogwheel",count:1}}
setblock 146 66 51 create:deployer[facing=down,axis_along_first=true]{HeldItem:{id:"minecraft:iron_nugget",count:1}}
setblock 148 66 51 create:mechanical_press[facing=south]
fill 144 67 51 148 67 51 create:andesite_casing
summon item 147.5 65 51.5 {Item:{id:"create:incomplete_precision_mechanism",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
