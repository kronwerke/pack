# 082 antimatter/sps
fill 407 63 108 420 63 121 minecraft:light_gray_concrete
fill 407 64 108 420 71 108 minecraft:light_gray_concrete
fill 407 64 108 407 71 121 minecraft:light_gray_concrete
setblock 408 64 120 minecraft:air
setblock 408 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "082"}','{"text": "antimatter"}','{"text": "sps"}','{"text": ""}']}}
setblock 409 64 120 minecraft:air
setblock 409 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "formed SPS with"}','{"text": "ports and"}','{"text": "supercharged"}','{"text": "coil"}']}}
setblock 410 64 120 minecraft:air
setblock 410 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Vereinfachte"}','{"text": "Hülle: im Spiel"}','{"text": "nach Buildguide"}','{"text": "vervollständigen"}']}}
summon text_display 413.5 71 113.5 {text:'[{"text": "082  ", "color": "gold"}, {"text": "antimatter/sps", "color": "gray"}, {"text": "\\nForme das SPS", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 409 64 110 415 70 116 mekanism:sps_casing
fill 410 65 111 414 69 115 minecraft:air
setblock 412 67 113 mekanism:supercharged_coil
setblock 412 67 116 mekanism:sps_port
setblock 409 67 113 mekanism:sps_port
