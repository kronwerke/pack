# 044 mekanism/dynamic_tank
#area 11 95 30 120
fill 11 64 95 30 91 120 minecraft:air
fill 11 60 95 30 62 120 minecraft:stone
fill 11 63 95 30 63 120 minecraft:light_gray_concrete
fill 15 64 101 30 79 101 minecraft:light_gray_concrete
fill 15 64 101 15 79 114 minecraft:light_gray_concrete
setblock 16 64 113 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "044"}','{"text": "mekanism"}','{"text": "dynamic_tank"}','{"text": ""}']}}
setblock 17 64 113 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a 3x3x3 dynamic"}','{"text": "tank with valve"}','{"text": "and structural"}','{"text": "glass"}']}}
fill 25 64 101 25 79 114 minecraft:light_gray_concrete
setblock 18 64 105 mekanism:dynamic_tank
setblock 18 64 106 mekanism:dynamic_tank
setblock 18 64 107 mekanism:dynamic_tank
setblock 18 65 105 mekanism:dynamic_tank
setblock 18 65 106 mekanism:structural_glass
setblock 18 65 107 mekanism:dynamic_tank
setblock 18 66 105 mekanism:dynamic_tank
setblock 18 66 106 mekanism:dynamic_tank
setblock 18 66 107 mekanism:dynamic_tank
setblock 19 64 105 mekanism:dynamic_tank
setblock 19 64 106 mekanism:dynamic_tank
setblock 19 64 107 mekanism:dynamic_tank
setblock 19 65 105 mekanism:structural_glass
setblock 19 65 107 mekanism:structural_glass
setblock 19 66 105 mekanism:dynamic_tank
setblock 19 66 106 mekanism:structural_glass
setblock 19 66 107 mekanism:dynamic_tank
setblock 20 64 105 mekanism:dynamic_tank
setblock 20 64 106 mekanism:dynamic_tank
setblock 20 64 107 mekanism:dynamic_tank
setblock 20 65 105 mekanism:structural_glass
setblock 20 65 107 mekanism:dynamic_valve
setblock 20 66 105 mekanism:dynamic_tank
setblock 20 66 106 mekanism:structural_glass
setblock 20 66 107 mekanism:dynamic_tank
setblock 21 64 105 mekanism:dynamic_tank
setblock 21 64 106 mekanism:dynamic_tank
setblock 21 64 107 mekanism:dynamic_tank
setblock 21 65 105 mekanism:dynamic_tank
setblock 21 65 106 mekanism:structural_glass
setblock 21 65 107 mekanism:dynamic_tank
setblock 21 66 105 mekanism:dynamic_tank
setblock 21 66 106 mekanism:dynamic_tank
setblock 21 66 107 mekanism:dynamic_tank
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
