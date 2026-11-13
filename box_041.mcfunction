# 041 mekanism_advanced/teleporter
#area 125 65 144 90
fill 125 64 65 144 91 90 minecraft:air
fill 125 60 65 144 62 90 minecraft:stone
fill 125 63 65 144 63 90 minecraft:light_gray_concrete
fill 129 64 71 144 79 71 minecraft:light_gray_concrete
fill 129 64 71 129 79 84 minecraft:light_gray_concrete
setblock 130 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "041"}','{"text": "mekanism_advanced"}','{"text": "teleporter"}','{"text": ""}']}}
setblock 131 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "built"}','{"text": "teleporter"}','{"text": "frame with"}','{"text": "portal"}']}}
fill 139 64 71 139 79 84 minecraft:light_gray_concrete
setblock 134 64 76 mekanism:teleporter
setblock 133 64 76 mekanism:teleporter_frame
setblock 135 64 76 mekanism:teleporter_frame
setblock 133 65 76 mekanism:teleporter_frame
setblock 135 65 76 mekanism:teleporter_frame
setblock 133 66 76 mekanism:teleporter_frame
setblock 135 66 76 mekanism:teleporter_frame
setblock 133 67 76 mekanism:teleporter_frame
setblock 135 67 76 mekanism:teleporter_frame
setblock 134 67 76 mekanism:teleporter_frame
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
