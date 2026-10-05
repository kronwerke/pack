# 071 mekanism_advanced/evap
fill 238 63 108 249 63 121 minecraft:light_gray_concrete
fill 238 64 108 249 71 108 minecraft:light_gray_concrete
fill 238 64 108 238 71 121 minecraft:light_gray_concrete
setblock 239 64 120 minecraft:air
setblock 239 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "071"}','{"text": "mekanism_advanced"}','{"text": "evap"}','{"text": ""}']}}
setblock 240 64 120 minecraft:air
setblock 240 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "thermal"}','{"text": "evaporation"}','{"text": "tower"}','{"text": ""}']}}
summon text_display 243.5 71 113.5 {text:'[{"text": "071  ", "color": "gold"}, {"text": "mekanism_advanced/evap", "color": "gray"}, {"text": "\\nBau die Wärmeverdampfungsanlage", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 242 64 112 245 73 115 mekanism:thermal_evaporation_block
fill 243 65 113 244 73 114 minecraft:air
fill 243 73 112 244 73 115 mekanism:thermal_evaporation_block
setblock 243 64 115 mekanism:thermal_evaporation_controller
setblock 244 64 115 mekanism:thermal_evaporation_valve
fill 243 66 115 244 72 115 mekanism:structural_glass
