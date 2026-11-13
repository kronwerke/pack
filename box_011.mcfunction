# 011 create/depot
#area 31 40 50 65
fill 31 64 40 50 91 65 minecraft:air
fill 31 60 40 50 62 65 minecraft:stone
fill 31 63 40 50 63 65 minecraft:light_gray_concrete
fill 35 64 46 50 79 46 minecraft:light_gray_concrete
fill 35 64 46 35 79 59 minecraft:light_gray_concrete
setblock 36 64 58 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "011"}','{"text": "create"}','{"text": "depot"}','{"text": ""}']}}
setblock 37 64 58 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "press above a"}','{"text": "depot with one"}','{"text": "block of air"}','{"text": "between"}']}}
fill 45 64 46 45 79 59 minecraft:light_gray_concrete
setblock 40 64 51 create:depot
setblock 40 66 51 create:mechanical_press[facing=south]
fill 39 64 50 41 67 50 create:andesite_casing
setblock 40 66 50 create:andesite_encased_shaft[axis=z]
setblock 40 66 49 create:creative_motor[facing=south]{ScrollValue:32}
kw testworld use 40 64 51 up minecraft:iron_ingot
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
