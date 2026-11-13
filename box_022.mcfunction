# 022 create/belt
#area 91 44 110 69
fill 91 64 44 110 91 69 minecraft:air
fill 91 60 44 110 62 69 minecraft:stone
fill 91 63 44 110 63 69 minecraft:light_gray_concrete
fill 95 64 50 110 79 50 minecraft:light_gray_concrete
fill 95 64 50 95 79 63 minecraft:light_gray_concrete
setblock 96 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "022"}','{"text": "create"}','{"text": "belt"}','{"text": ""}']}}
setblock 97 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a belt between"}','{"text": "two shafts"}','{"text": ""}','{"text": ""}']}}
fill 105 64 50 105 79 63 minecraft:light_gray_concrete
setblock 100 64 53 create:shaft[axis=x]
setblock 100 64 57 create:shaft[axis=x]
kw testworld use 100 64 53 up create:belt_connector
kw testworld use 100 64 57 up create:belt_connector
execute unless block 100 64 55 minecraft:air
summon item 100.5 65 54.5 {Item:{id:"minecraft:iron_ingot",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 100.5 65 55.5 {Item:{id:"minecraft:iron_ingot",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 100.5 65 56.5 {Item:{id:"minecraft:iron_ingot",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
