# 014 create/depot
#area 31 42 50 67
fill 31 64 42 50 91 67 minecraft:air
fill 31 60 42 50 62 67 minecraft:stone
fill 31 63 42 50 63 67 minecraft:light_gray_concrete
fill 35 64 48 50 79 48 minecraft:light_gray_concrete
fill 35 64 48 35 79 61 minecraft:light_gray_concrete
setblock 36 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "014"}','{"text": "create"}','{"text": "depot"}','{"text": ""}']}}
setblock 37 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "press above a"}','{"text": "depot with one"}','{"text": "block of air"}','{"text": "between"}']}}
fill 45 64 48 45 79 61 minecraft:light_gray_concrete
setblock 40 64 53 create:depot
setblock 40 66 53 create:mechanical_press[facing=south]
fill 39 64 52 41 67 52 create:andesite_casing
setblock 40 66 52 create:andesite_encased_shaft[axis=z]
setblock 40 66 51 create:creative_motor[facing=south]{ScrollValue:32}
kw testworld use 40 64 53 up minecraft:iron_ingot
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
