# 022 create_brass/incomplete
#area 153 42 174 67
fill 153 64 42 174 91 67 minecraft:air
fill 153 60 42 174 62 67 minecraft:stone
fill 153 63 42 174 63 67 minecraft:light_gray_concrete
fill 157 64 48 174 79 48 minecraft:light_gray_concrete
fill 157 64 48 157 79 61 minecraft:light_gray_concrete
setblock 158 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "022"}','{"text": "create_brass"}','{"text": "incomplete"}','{"text": ""}']}}
setblock 159 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "belt with three"}','{"text": "deployers"}','{"text": "(cogwheel,"}','{"text": "tube, nugget)"}']}}
setblock 160 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "and a press"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 169 64 48 169 79 61 minecraft:light_gray_concrete
setblock 160 64 53 create:shaft[axis=z]
setblock 166 64 53 create:shaft[axis=z]
kw testworld use 160 64 53 up create:belt_connector
kw testworld use 166 64 53 up create:belt_connector
execute unless block 163 64 53 minecraft:air
setblock 161 66 53 create:deployer[facing=down,axis_along_first=true]{HeldItem:{id:"create:cogwheel",count:1}}
setblock 162 66 53 create:deployer[facing=down,axis_along_first=true]{HeldItem:{id:"create:large_cogwheel",count:1}}
setblock 163 66 53 create:deployer[facing=down,axis_along_first=true]{HeldItem:{id:"minecraft:iron_nugget",count:1}}
setblock 165 66 53 create:mechanical_press[facing=south]
fill 161 67 53 165 67 53 create:andesite_casing
summon item 164.5 65 53.5 {Item:{id:"create:incomplete_precision_mechanism",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
