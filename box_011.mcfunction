# 011 create/belt
#area 91 21 110 46
fill 91 64 21 110 91 46 minecraft:air
fill 91 60 21 110 62 46 minecraft:stone
fill 91 63 21 110 63 46 minecraft:light_gray_concrete
fill 95 64 27 110 79 27 minecraft:light_gray_concrete
fill 95 64 27 95 79 40 minecraft:light_gray_concrete
setblock 96 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "011"}','{"text": "create"}','{"text": "belt"}','{"text": ""}']}}
setblock 97 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a belt between"}','{"text": "two shafts"}','{"text": ""}','{"text": ""}']}}
fill 105 64 27 105 79 40 minecraft:light_gray_concrete
setblock 100 64 30 create:shaft[axis=x]
setblock 100 64 34 create:shaft[axis=x]
kw testworld use 100 64 30 up create:belt_connector
kw testworld use 100 64 34 up create:belt_connector
execute unless block 100 64 32 minecraft:air
summon item 100.5 65 31.5 {Item:{id:"minecraft:iron_ingot",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 100.5 65 32.5 {Item:{id:"minecraft:iron_ingot",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 100.5 65 33.5 {Item:{id:"minecraft:iron_ingot",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
