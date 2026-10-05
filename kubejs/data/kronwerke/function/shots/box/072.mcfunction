# 072 mekanism_advanced/boiler
fill 253 63 108 264 63 121 minecraft:light_gray_concrete
fill 253 64 108 264 71 108 minecraft:light_gray_concrete
fill 253 64 108 253 71 121 minecraft:light_gray_concrete
setblock 254 64 120 minecraft:air
setblock 254 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "072"}','{"text": "mekanism_advanced"}','{"text": "boiler"}','{"text": ""}']}}
setblock 255 64 120 minecraft:air
setblock 255 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "boiler cutaway"}','{"text": "with heaters"}','{"text": "and conductors"}','{"text": "Schnitt: Front"}']}}
setblock 256 64 120 minecraft:air
setblock 256 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "aus Glas"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
summon text_display 258.5 71 113.5 {text:'[{"text": "072  ", "color": "gold"}, {"text": "mekanism_advanced/boiler", "color": "gray"}, {"text": "\\nBau einen Thermoelektrischen Dampfkessel", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 256 64 111 260 68 115 mekanism:boiler_casing
fill 257 65 112 259 67 114 minecraft:air
fill 257 65 112 259 65 114 mekanism:superheating_element
fill 257 66 112 259 66 114 mekanism:pressure_disperser
fill 256 65 115 260 67 115 mekanism:structural_glass
setblock 258 64 115 mekanism:boiler_valve
