# 051 mekanism_advanced/teleporter
#area 140 95 159 120
fill 140 64 95 159 91 120 minecraft:air
fill 140 60 95 159 62 120 minecraft:stone
fill 140 63 95 159 63 120 minecraft:light_gray_concrete
fill 144 64 101 159 79 101 minecraft:light_gray_concrete
fill 144 64 101 144 79 114 minecraft:light_gray_concrete
setblock 145 64 113 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "051"}','{"text": "mekanism_advanced"}','{"text": "teleporter"}','{"text": ""}']}}
setblock 146 64 113 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "built"}','{"text": "teleporter"}','{"text": "frame with"}','{"text": "portal"}']}}
fill 154 64 101 154 79 114 minecraft:light_gray_concrete
setblock 149 64 106 mekanism:teleporter
setblock 148 64 106 mekanism:teleporter_frame
setblock 150 64 106 mekanism:teleporter_frame
setblock 148 65 106 mekanism:teleporter_frame
setblock 150 65 106 mekanism:teleporter_frame
setblock 148 66 106 mekanism:teleporter_frame
setblock 150 66 106 mekanism:teleporter_frame
setblock 148 67 106 mekanism:teleporter_frame
setblock 150 67 106 mekanism:teleporter_frame
setblock 149 67 106 mekanism:teleporter_frame
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
