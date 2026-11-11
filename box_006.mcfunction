# 006 mekanism_advanced/teleporter
#area 11 13 30 38
fill 11 64 13 30 91 38 minecraft:air
fill 11 60 13 30 62 38 minecraft:stone
fill 11 63 13 30 63 38 minecraft:light_gray_concrete
fill 15 64 19 30 79 19 minecraft:light_gray_concrete
fill 15 64 19 15 79 32 minecraft:light_gray_concrete
setblock 16 64 31 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "006"}','{"text": "mekanism_advanced"}','{"text": "teleporter"}','{"text": ""}']}}
setblock 17 64 31 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "built"}','{"text": "teleporter"}','{"text": "frame with"}','{"text": "portal"}']}}
summon text_display 20.5 71 24.5 {text:'[{"text": "006  ", "color": "gold"}, {"text": "mekanism_advanced/teleporter", "color": "gray"}, {"text": "\\nStell zwei Teleporter auf", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 25 64 19 25 79 32 minecraft:light_gray_concrete
setblock 20 64 24 mekanism:teleporter
setblock 19 64 24 mekanism:teleporter_frame
setblock 21 64 24 mekanism:teleporter_frame
setblock 19 65 24 mekanism:teleporter_frame
setblock 21 65 24 mekanism:teleporter_frame
setblock 19 66 24 mekanism:teleporter_frame
setblock 21 66 24 mekanism:teleporter_frame
setblock 19 67 24 mekanism:teleporter_frame
setblock 21 67 24 mekanism:teleporter_frame
setblock 20 67 24 mekanism:teleporter_frame
