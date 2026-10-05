# 160 hexerei/sage_plate
fill 300 63 242 311 63 255 minecraft:light_gray_concrete
fill 300 64 242 311 71 242 minecraft:light_gray_concrete
fill 300 64 242 300 71 255 minecraft:light_gray_concrete
setblock 301 64 254 minecraft:air
setblock 301 64 254 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "160"}','{"text": "hexerei"}','{"text": "sage_plate"}','{"text": ""}']}}
setblock 302 64 254 minecraft:air
setblock 302 64 254 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "burning sage"}','{"text": "plate with the"}','{"text": "smoke ring"}','{"text": ""}']}}
summon text_display 305.5 71 247.5 {text:'[{"text": "160  ", "color": "gold"}, {"text": "hexerei/sage_plate", "color": "gray"}, {"text": "\\nStell eine Sage Burning Plate auf", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 302 64 245 hexerei:sage_burning_plate
setblock 309 64 251 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"hexerei:dried_sage_bundle",count:4}]}
