# 020 create/belt
#area 106 42 125 67
fill 106 64 42 125 91 67 minecraft:air
fill 106 60 42 125 62 67 minecraft:stone
fill 106 63 42 125 63 67 minecraft:light_gray_concrete
fill 110 64 48 125 79 48 minecraft:light_gray_concrete
fill 110 64 48 110 79 61 minecraft:light_gray_concrete
setblock 111 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "020"}','{"text": "create"}','{"text": "belt"}','{"text": ""}']}}
setblock 112 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a belt between"}','{"text": "two shafts"}','{"text": ""}','{"text": ""}']}}
fill 120 64 48 120 79 61 minecraft:light_gray_concrete
setblock 115 64 51 create:shaft[axis=x]
setblock 115 64 55 create:shaft[axis=x]
kw testworld use 115 64 51 up create:belt_connector
kw testworld use 115 64 55 up create:belt_connector
execute unless block 115 64 53 minecraft:air
summon item 115.5 65 52.5 {Item:{id:"minecraft:iron_ingot",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 115.5 65 53.5 {Item:{id:"minecraft:iron_ingot",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 115.5 65 54.5 {Item:{id:"minecraft:iron_ingot",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
