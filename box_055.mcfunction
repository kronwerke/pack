# 055 mekanism_advanced/teleporter
#area 159 97 178 122
fill 159 64 97 178 91 122 minecraft:air
fill 159 60 97 178 62 122 minecraft:stone
fill 159 63 97 178 63 122 minecraft:light_gray_concrete
fill 163 64 103 178 79 103 minecraft:light_gray_concrete
fill 163 64 103 163 79 116 minecraft:light_gray_concrete
setblock 164 64 115 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "055"}','{"text": "mekanism_advanced"}','{"text": "teleporter"}','{"text": ""}']}}
setblock 165 64 115 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "built"}','{"text": "teleporter"}','{"text": "frame with"}','{"text": "portal"}']}}
fill 173 64 103 173 79 116 minecraft:light_gray_concrete
setblock 168 64 108 mekanism:teleporter
setblock 167 64 108 mekanism:teleporter_frame
setblock 169 64 108 mekanism:teleporter_frame
setblock 167 65 108 mekanism:teleporter_frame
setblock 169 65 108 mekanism:teleporter_frame
setblock 167 66 108 mekanism:teleporter_frame
setblock 169 66 108 mekanism:teleporter_frame
setblock 167 67 108 mekanism:teleporter_frame
setblock 169 67 108 mekanism:teleporter_frame
setblock 168 67 108 mekanism:teleporter_frame
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
