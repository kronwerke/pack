# 019 create/belt
#area 91 42 110 67
fill 91 64 42 110 91 67 minecraft:air
fill 91 60 42 110 62 67 minecraft:stone
fill 91 63 42 110 63 67 minecraft:light_gray_concrete
fill 95 64 48 110 79 48 minecraft:light_gray_concrete
fill 95 64 48 95 79 61 minecraft:light_gray_concrete
setblock 96 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "019"}','{"text": "create"}','{"text": "belt"}','{"text": ""}']}}
setblock 97 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a belt between"}','{"text": "two shafts"}','{"text": ""}','{"text": ""}']}}
fill 105 64 48 105 79 61 minecraft:light_gray_concrete
setblock 100 64 51 create:shaft[axis=x]
setblock 100 64 55 create:shaft[axis=x]
kw testworld use 100 64 51 up create:belt_connector
kw testworld use 100 64 55 up create:belt_connector
execute unless block 100 64 53 minecraft:air
summon item 100.5 65 52.5 {Item:{id:"minecraft:iron_ingot",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 100.5 65 53.5 {Item:{id:"minecraft:iron_ingot",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 100.5 65 54.5 {Item:{id:"minecraft:iron_ingot",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
