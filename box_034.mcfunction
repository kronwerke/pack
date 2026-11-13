# 034 mekanism_advanced/teleporter
#area 110 65 129 90
fill 110 64 65 129 91 90 minecraft:air
fill 110 60 65 129 62 90 minecraft:stone
fill 110 63 65 129 63 90 minecraft:light_gray_concrete
fill 114 64 71 129 79 71 minecraft:light_gray_concrete
fill 114 64 71 114 79 84 minecraft:light_gray_concrete
setblock 115 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "034"}','{"text": "mekanism_advanced"}','{"text": "teleporter"}','{"text": ""}']}}
setblock 116 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "built"}','{"text": "teleporter"}','{"text": "frame with"}','{"text": "portal"}']}}
fill 124 64 71 124 79 84 minecraft:light_gray_concrete
setblock 119 64 76 mekanism:teleporter
setblock 118 64 76 mekanism:teleporter_frame
setblock 120 64 76 mekanism:teleporter_frame
setblock 118 65 76 mekanism:teleporter_frame
setblock 120 65 76 mekanism:teleporter_frame
setblock 118 66 76 mekanism:teleporter_frame
setblock 120 66 76 mekanism:teleporter_frame
setblock 118 67 76 mekanism:teleporter_frame
setblock 120 67 76 mekanism:teleporter_frame
setblock 119 67 76 mekanism:teleporter_frame
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
