# 025 mekanism_advanced/teleporter
#area 77 63 96 88
fill 77 64 63 96 91 88 minecraft:air
fill 77 60 63 96 62 88 minecraft:stone
fill 77 63 63 96 63 88 minecraft:light_gray_concrete
fill 81 64 69 96 79 69 minecraft:light_gray_concrete
fill 81 64 69 81 79 82 minecraft:light_gray_concrete
setblock 82 64 81 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "025"}','{"text": "mekanism_advanced"}','{"text": "teleporter"}','{"text": ""}']}}
setblock 83 64 81 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "built"}','{"text": "teleporter"}','{"text": "frame with"}','{"text": "portal"}']}}
fill 91 64 69 91 79 82 minecraft:light_gray_concrete
setblock 86 64 74 mekanism:teleporter
setblock 85 64 74 mekanism:teleporter_frame
setblock 87 64 74 mekanism:teleporter_frame
setblock 85 65 74 mekanism:teleporter_frame
setblock 87 65 74 mekanism:teleporter_frame
setblock 85 66 74 mekanism:teleporter_frame
setblock 87 66 74 mekanism:teleporter_frame
setblock 85 67 74 mekanism:teleporter_frame
setblock 87 67 74 mekanism:teleporter_frame
setblock 86 67 74 mekanism:teleporter_frame
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
