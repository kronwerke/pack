# 052 mekanism_advanced/teleporter
#area 144 95 163 120
fill 144 64 95 163 91 120 minecraft:air
fill 144 60 95 163 62 120 minecraft:stone
fill 144 63 95 163 63 120 minecraft:light_gray_concrete
fill 148 64 101 163 79 101 minecraft:light_gray_concrete
fill 148 64 101 148 79 114 minecraft:light_gray_concrete
setblock 149 64 113 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "052"}','{"text": "mekanism_advanced"}','{"text": "teleporter"}','{"text": ""}']}}
setblock 150 64 113 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "built"}','{"text": "teleporter"}','{"text": "frame with"}','{"text": "portal"}']}}
fill 158 64 101 158 79 114 minecraft:light_gray_concrete
setblock 153 64 106 mekanism:teleporter
setblock 152 64 106 mekanism:teleporter_frame
setblock 154 64 106 mekanism:teleporter_frame
setblock 152 65 106 mekanism:teleporter_frame
setblock 154 65 106 mekanism:teleporter_frame
setblock 152 66 106 mekanism:teleporter_frame
setblock 154 66 106 mekanism:teleporter_frame
setblock 152 67 106 mekanism:teleporter_frame
setblock 154 67 106 mekanism:teleporter_frame
setblock 153 67 106 mekanism:teleporter_frame
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
