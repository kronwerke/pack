# 069 mekanism_advanced/teleporter
fill 208 63 108 219 63 121 minecraft:light_gray_concrete
fill 208 64 108 219 71 108 minecraft:light_gray_concrete
fill 208 64 108 208 71 121 minecraft:light_gray_concrete
setblock 209 64 120 minecraft:air
setblock 209 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "069"}','{"text": "mekanism_advanced"}','{"text": "teleporter"}','{"text": ""}']}}
setblock 210 64 120 minecraft:air
setblock 210 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "built"}','{"text": "teleporter"}','{"text": "frame with"}','{"text": "portal"}']}}
summon text_display 213.5 71 113.5 {text:'[{"text": "069  ", "color": "gold"}, {"text": "mekanism_advanced/teleporter", "color": "gray"}, {"text": "\\nStell zwei Teleporter auf", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 212 64 113 214 68 113 mekanism:teleporter_frame
fill 213 65 113 213 67 113 minecraft:air
setblock 213 64 114 mekanism:teleporter
setblock 212 64 114 mekanism:creative_energy_cube
