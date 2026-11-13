# 016 create/depot
#area 46 42 65 67
fill 46 64 42 65 91 67 minecraft:air
fill 46 60 42 65 62 67 minecraft:stone
fill 46 63 42 65 63 67 minecraft:light_gray_concrete
fill 50 64 48 65 79 48 minecraft:light_gray_concrete
fill 50 64 48 50 79 61 minecraft:light_gray_concrete
setblock 51 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "016"}','{"text": "create"}','{"text": "depot"}','{"text": ""}']}}
setblock 52 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "press above a"}','{"text": "depot with one"}','{"text": "block of air"}','{"text": "between"}']}}
fill 60 64 48 60 79 61 minecraft:light_gray_concrete
setblock 55 64 53 create:depot
setblock 55 66 53 create:mechanical_press[facing=south]
fill 54 64 52 56 67 52 create:andesite_casing
setblock 55 66 52 create:andesite_encased_shaft[axis=z]
setblock 55 66 51 create:creative_motor[facing=south]{ScrollValue:32}
kw testworld use 55 64 53 up minecraft:iron_ingot
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
