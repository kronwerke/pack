# 014 create/belt
#area 91 40 110 65
fill 91 64 40 110 91 65 minecraft:air
fill 91 60 40 110 62 65 minecraft:stone
fill 91 63 40 110 63 65 minecraft:light_gray_concrete
fill 95 64 46 110 79 46 minecraft:light_gray_concrete
fill 95 64 46 95 79 59 minecraft:light_gray_concrete
setblock 96 64 58 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "014"}','{"text": "create"}','{"text": "belt"}','{"text": ""}']}}
setblock 97 64 58 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a belt between"}','{"text": "two shafts"}','{"text": ""}','{"text": ""}']}}
fill 105 64 46 105 79 59 minecraft:light_gray_concrete
setblock 100 64 49 create:shaft[axis=x]
setblock 100 64 53 create:shaft[axis=x]
kw testworld use 100 64 49 up create:belt_connector
kw testworld use 100 64 53 up create:belt_connector
execute unless block 100 64 51 minecraft:air
summon item 100.5 65 50.5 {Item:{id:"minecraft:iron_ingot",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 100.5 65 51.5 {Item:{id:"minecraft:iron_ingot",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 100.5 65 52.5 {Item:{id:"minecraft:iron_ingot",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
