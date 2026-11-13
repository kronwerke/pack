# 031 mekanism_advanced/teleporter
#area 92 65 111 90
fill 92 64 65 111 91 90 minecraft:air
fill 92 60 65 111 62 90 minecraft:stone
fill 92 63 65 111 63 90 minecraft:light_gray_concrete
fill 96 64 71 111 79 71 minecraft:light_gray_concrete
fill 96 64 71 96 79 84 minecraft:light_gray_concrete
setblock 97 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "031"}','{"text": "mekanism_advanced"}','{"text": "teleporter"}','{"text": ""}']}}
setblock 98 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "built"}','{"text": "teleporter"}','{"text": "frame with"}','{"text": "portal"}']}}
fill 106 64 71 106 79 84 minecraft:light_gray_concrete
setblock 101 64 76 mekanism:teleporter
setblock 100 64 76 mekanism:teleporter_frame
setblock 102 64 76 mekanism:teleporter_frame
setblock 100 65 76 mekanism:teleporter_frame
setblock 102 65 76 mekanism:teleporter_frame
setblock 100 66 76 mekanism:teleporter_frame
setblock 102 66 76 mekanism:teleporter_frame
setblock 100 67 76 mekanism:teleporter_frame
setblock 102 67 76 mekanism:teleporter_frame
setblock 101 67 76 mekanism:teleporter_frame
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
