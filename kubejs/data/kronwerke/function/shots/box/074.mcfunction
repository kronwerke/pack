# 074 mekanism_advanced/cnc_stamper
fill 283 63 108 294 63 121 minecraft:light_gray_concrete
fill 283 64 108 294 71 108 minecraft:light_gray_concrete
fill 283 64 108 283 71 121 minecraft:light_gray_concrete
setblock 284 64 120 minecraft:air
setblock 284 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "074"}','{"text": "mekanism_advanced"}','{"text": "cnc_stamper"}','{"text": ""}']}}
setblock 285 64 120 minecraft:air
setblock 285 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "stamper GUI"}','{"text": "with the"}','{"text": "silicon press"}','{"text": ""}']}}
summon text_display 288.5 71 113.5 {text:'[{"text": "074  ", "color": "gold"}, {"text": "mekanism_advanced/cnc_stamper", "color": "gray"}, {"text": "\\nBau eine CNC Stamper", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 285 64 111 mekmm:cnc_stamper
setblock 292 64 117 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"ae2:silicon_press",count:1}]}
