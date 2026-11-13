# 030 mekanism/dynamic_tank
#area -4 65 15 90
fill -4 64 65 15 91 90 minecraft:air
fill -4 60 65 15 62 90 minecraft:stone
fill -4 63 65 15 63 90 minecraft:light_gray_concrete
fill 0 64 71 15 79 71 minecraft:light_gray_concrete
fill 0 64 71 0 79 84 minecraft:light_gray_concrete
setblock 1 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "030"}','{"text": "mekanism"}','{"text": "dynamic_tank"}','{"text": ""}']}}
setblock 2 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a 3x3x3 dynamic"}','{"text": "tank with valve"}','{"text": "and structural"}','{"text": "glass"}']}}
fill 10 64 71 10 79 84 minecraft:light_gray_concrete
setblock 3 64 75 mekanism:dynamic_tank
setblock 3 64 76 mekanism:dynamic_tank
setblock 3 64 77 mekanism:dynamic_tank
setblock 3 65 75 mekanism:dynamic_tank
setblock 3 65 76 mekanism:structural_glass
setblock 3 65 77 mekanism:dynamic_tank
setblock 3 66 75 mekanism:dynamic_tank
setblock 3 66 76 mekanism:dynamic_tank
setblock 3 66 77 mekanism:dynamic_tank
setblock 4 64 75 mekanism:dynamic_tank
setblock 4 64 76 mekanism:dynamic_tank
setblock 4 64 77 mekanism:dynamic_tank
setblock 4 65 75 mekanism:structural_glass
setblock 4 65 77 mekanism:structural_glass
setblock 4 66 75 mekanism:dynamic_tank
setblock 4 66 76 mekanism:structural_glass
setblock 4 66 77 mekanism:dynamic_tank
setblock 5 64 75 mekanism:dynamic_tank
setblock 5 64 76 mekanism:dynamic_tank
setblock 5 64 77 mekanism:dynamic_tank
setblock 5 65 75 mekanism:structural_glass
setblock 5 65 77 mekanism:dynamic_valve
setblock 5 66 75 mekanism:dynamic_tank
setblock 5 66 76 mekanism:structural_glass
setblock 5 66 77 mekanism:dynamic_tank
setblock 6 64 75 mekanism:dynamic_tank
setblock 6 64 76 mekanism:dynamic_tank
setblock 6 64 77 mekanism:dynamic_tank
setblock 6 65 75 mekanism:dynamic_tank
setblock 6 65 76 mekanism:structural_glass
setblock 6 65 77 mekanism:dynamic_tank
setblock 6 66 75 mekanism:dynamic_tank
setblock 6 66 76 mekanism:dynamic_tank
setblock 6 66 77 mekanism:dynamic_tank
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
