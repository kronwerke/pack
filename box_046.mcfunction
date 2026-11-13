# 046 mekanism/dynamic_tank
#area 11 97 30 122
fill 11 64 97 30 91 122 minecraft:air
fill 11 60 97 30 62 122 minecraft:stone
fill 11 63 97 30 63 122 minecraft:light_gray_concrete
fill 15 64 103 30 79 103 minecraft:light_gray_concrete
fill 15 64 103 15 79 116 minecraft:light_gray_concrete
setblock 16 64 115 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "046"}','{"text": "mekanism"}','{"text": "dynamic_tank"}','{"text": ""}']}}
setblock 17 64 115 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a 3x3x3 dynamic"}','{"text": "tank with valve"}','{"text": "and structural"}','{"text": "glass"}']}}
fill 25 64 103 25 79 116 minecraft:light_gray_concrete
setblock 18 64 107 mekanism:dynamic_tank
setblock 18 64 108 mekanism:dynamic_tank
setblock 18 64 109 mekanism:dynamic_tank
setblock 18 65 107 mekanism:dynamic_tank
setblock 18 65 108 mekanism:structural_glass
setblock 18 65 109 mekanism:dynamic_tank
setblock 18 66 107 mekanism:dynamic_tank
setblock 18 66 108 mekanism:dynamic_tank
setblock 18 66 109 mekanism:dynamic_tank
setblock 19 64 107 mekanism:dynamic_tank
setblock 19 64 108 mekanism:dynamic_tank
setblock 19 64 109 mekanism:dynamic_tank
setblock 19 65 107 mekanism:structural_glass
setblock 19 65 109 mekanism:structural_glass
setblock 19 66 107 mekanism:dynamic_tank
setblock 19 66 108 mekanism:structural_glass
setblock 19 66 109 mekanism:dynamic_tank
setblock 20 64 107 mekanism:dynamic_tank
setblock 20 64 108 mekanism:dynamic_tank
setblock 20 64 109 mekanism:dynamic_tank
setblock 20 65 107 mekanism:structural_glass
setblock 20 65 109 mekanism:dynamic_valve
setblock 20 66 107 mekanism:dynamic_tank
setblock 20 66 108 mekanism:structural_glass
setblock 20 66 109 mekanism:dynamic_tank
setblock 21 64 107 mekanism:dynamic_tank
setblock 21 64 108 mekanism:dynamic_tank
setblock 21 64 109 mekanism:dynamic_tank
setblock 21 65 107 mekanism:dynamic_tank
setblock 21 65 108 mekanism:structural_glass
setblock 21 65 109 mekanism:dynamic_tank
setblock 21 66 107 mekanism:dynamic_tank
setblock 21 66 108 mekanism:dynamic_tank
setblock 21 66 109 mekanism:dynamic_tank
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
