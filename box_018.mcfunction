# 018 create/depot
#area 31 44 50 69
fill 31 64 44 50 91 69 minecraft:air
fill 31 60 44 50 62 69 minecraft:stone
fill 31 63 44 50 63 69 minecraft:light_gray_concrete
fill 35 64 50 50 79 50 minecraft:light_gray_concrete
fill 35 64 50 35 79 63 minecraft:light_gray_concrete
setblock 36 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "018"}','{"text": "create"}','{"text": "depot"}','{"text": ""}']}}
setblock 37 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "press above a"}','{"text": "depot with one"}','{"text": "block of air"}','{"text": "between"}']}}
fill 45 64 50 45 79 63 minecraft:light_gray_concrete
setblock 40 64 55 create:depot
setblock 40 66 55 create:mechanical_press[facing=south]
fill 39 64 54 41 67 54 create:andesite_casing
setblock 40 66 54 create:andesite_encased_shaft[axis=z]
setblock 40 66 53 create:creative_motor[facing=south]{ScrollValue:32}
kw testworld use 40 64 55 up minecraft:iron_ingot
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
