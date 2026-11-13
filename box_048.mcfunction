# 048 mekanism_advanced/teleporter
#area 125 95 144 120
fill 125 64 95 144 91 120 minecraft:air
fill 125 60 95 144 62 120 minecraft:stone
fill 125 63 95 144 63 120 minecraft:light_gray_concrete
fill 129 64 101 144 79 101 minecraft:light_gray_concrete
fill 129 64 101 129 79 114 minecraft:light_gray_concrete
setblock 130 64 113 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "048"}','{"text": "mekanism_advanced"}','{"text": "teleporter"}','{"text": ""}']}}
setblock 131 64 113 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "built"}','{"text": "teleporter"}','{"text": "frame with"}','{"text": "portal"}']}}
fill 139 64 101 139 79 114 minecraft:light_gray_concrete
setblock 134 64 106 mekanism:teleporter
setblock 133 64 106 mekanism:teleporter_frame
setblock 135 64 106 mekanism:teleporter_frame
setblock 133 65 106 mekanism:teleporter_frame
setblock 135 65 106 mekanism:teleporter_frame
setblock 133 66 106 mekanism:teleporter_frame
setblock 135 66 106 mekanism:teleporter_frame
setblock 133 67 106 mekanism:teleporter_frame
setblock 135 67 106 mekanism:teleporter_frame
setblock 134 67 106 mekanism:teleporter_frame
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
