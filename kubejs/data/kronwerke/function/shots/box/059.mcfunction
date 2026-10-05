# 059 mekanism/dynamic_tank
fill 30 63 108 41 63 121 minecraft:light_gray_concrete
fill 30 64 108 41 71 108 minecraft:light_gray_concrete
fill 30 64 108 30 71 121 minecraft:light_gray_concrete
setblock 31 64 120 minecraft:air
setblock 31 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "059"}','{"text": "mekanism"}','{"text": "dynamic_tank"}','{"text": ""}']}}
setblock 32 64 120 minecraft:air
setblock 32 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a 3x3x3 dynamic"}','{"text": "tank with valve"}','{"text": "and structural"}','{"text": "glass"}']}}
summon text_display 35.5 71 113.5 {text:'[{"text": "059  ", "color": "gold"}, {"text": "mekanism/dynamic_tank", "color": "gray"}, {"text": "\\nBau einen Dynamischen Tank", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 34 64 112 36 66 114 mekanism:dynamic_tank
fill 35 65 112 35 65 114 mekanism:structural_glass
fill 34 65 113 36 65 113 mekanism:structural_glass
setblock 35 65 114 mekanism:dynamic_valve
fill 35 65 113 35 65 113 minecraft:air
