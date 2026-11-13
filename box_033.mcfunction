# 033 mekanism/dynamic_tank
#area 11 65 30 90
fill 11 64 65 30 91 90 minecraft:air
fill 11 60 65 30 62 90 minecraft:stone
fill 11 63 65 30 63 90 minecraft:light_gray_concrete
fill 15 64 71 30 79 71 minecraft:light_gray_concrete
fill 15 64 71 15 79 84 minecraft:light_gray_concrete
setblock 16 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "033"}','{"text": "mekanism"}','{"text": "dynamic_tank"}','{"text": ""}']}}
setblock 17 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a 3x3x3 dynamic"}','{"text": "tank with valve"}','{"text": "and structural"}','{"text": "glass"}']}}
fill 25 64 71 25 79 84 minecraft:light_gray_concrete
setblock 18 64 75 mekanism:dynamic_tank
setblock 18 64 76 mekanism:dynamic_tank
setblock 18 64 77 mekanism:dynamic_tank
setblock 18 65 75 mekanism:dynamic_tank
setblock 18 65 76 mekanism:structural_glass
setblock 18 65 77 mekanism:dynamic_tank
setblock 18 66 75 mekanism:dynamic_tank
setblock 18 66 76 mekanism:dynamic_tank
setblock 18 66 77 mekanism:dynamic_tank
setblock 19 64 75 mekanism:dynamic_tank
setblock 19 64 76 mekanism:dynamic_tank
setblock 19 64 77 mekanism:dynamic_tank
setblock 19 65 75 mekanism:structural_glass
setblock 19 65 77 mekanism:structural_glass
setblock 19 66 75 mekanism:dynamic_tank
setblock 19 66 76 mekanism:structural_glass
setblock 19 66 77 mekanism:dynamic_tank
setblock 20 64 75 mekanism:dynamic_tank
setblock 20 64 76 mekanism:dynamic_tank
setblock 20 64 77 mekanism:dynamic_tank
setblock 20 65 75 mekanism:structural_glass
setblock 20 65 77 mekanism:dynamic_valve
setblock 20 66 75 mekanism:dynamic_tank
setblock 20 66 76 mekanism:structural_glass
setblock 20 66 77 mekanism:dynamic_tank
setblock 21 64 75 mekanism:dynamic_tank
setblock 21 64 76 mekanism:dynamic_tank
setblock 21 64 77 mekanism:dynamic_tank
setblock 21 65 75 mekanism:dynamic_tank
setblock 21 65 76 mekanism:structural_glass
setblock 21 65 77 mekanism:dynamic_tank
setblock 21 66 75 mekanism:dynamic_tank
setblock 21 66 76 mekanism:dynamic_tank
setblock 21 66 77 mekanism:dynamic_tank
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
