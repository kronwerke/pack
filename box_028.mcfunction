# 028 mekanism_advanced/teleporter
#area 92 63 111 88
fill 92 64 63 111 91 88 minecraft:air
fill 92 60 63 111 62 88 minecraft:stone
fill 92 63 63 111 63 88 minecraft:light_gray_concrete
fill 96 64 69 111 79 69 minecraft:light_gray_concrete
fill 96 64 69 96 79 82 minecraft:light_gray_concrete
setblock 97 64 81 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "028"}','{"text": "mekanism_advanced"}','{"text": "teleporter"}','{"text": ""}']}}
setblock 98 64 81 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "built"}','{"text": "teleporter"}','{"text": "frame with"}','{"text": "portal"}']}}
fill 106 64 69 106 79 82 minecraft:light_gray_concrete
setblock 101 64 74 mekanism:teleporter
setblock 100 64 74 mekanism:teleporter_frame
setblock 102 64 74 mekanism:teleporter_frame
setblock 100 65 74 mekanism:teleporter_frame
setblock 102 65 74 mekanism:teleporter_frame
setblock 100 66 74 mekanism:teleporter_frame
setblock 102 66 74 mekanism:teleporter_frame
setblock 100 67 74 mekanism:teleporter_frame
setblock 102 67 74 mekanism:teleporter_frame
setblock 101 67 74 mekanism:teleporter_frame
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
