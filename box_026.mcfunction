# 026 create_brass/incomplete
#area 184 42 205 67
fill 184 64 42 205 91 67 minecraft:air
fill 184 60 42 205 62 67 minecraft:stone
fill 184 63 42 205 63 67 minecraft:light_gray_concrete
fill 188 64 48 205 79 48 minecraft:light_gray_concrete
fill 188 64 48 188 79 61 minecraft:light_gray_concrete
setblock 189 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "026"}','{"text": "create_brass"}','{"text": "incomplete"}','{"text": ""}']}}
setblock 190 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "belt with three"}','{"text": "deployers"}','{"text": "(cogwheel,"}','{"text": "tube, nugget)"}']}}
setblock 191 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "and a press"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 200 64 48 200 79 61 minecraft:light_gray_concrete
setblock 191 64 53 create:shaft[axis=z]
setblock 197 64 53 create:shaft[axis=z]
kw testworld use 191 64 53 up create:belt_connector
kw testworld use 197 64 53 up create:belt_connector
execute unless block 194 64 53 minecraft:air
setblock 192 66 53 create:deployer[facing=down,axis_along_first=true]{HeldItem:{id:"create:cogwheel",count:1}}
setblock 193 66 53 create:deployer[facing=down,axis_along_first=true]{HeldItem:{id:"create:large_cogwheel",count:1}}
setblock 194 66 53 create:deployer[facing=down,axis_along_first=true]{HeldItem:{id:"minecraft:iron_nugget",count:1}}
setblock 196 66 53 create:mechanical_press[facing=south]
fill 192 67 53 196 67 53 create:andesite_casing
summon item 195.5 65 53.5 {Item:{id:"create:incomplete_precision_mechanism",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
