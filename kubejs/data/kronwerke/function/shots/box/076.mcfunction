# 076 mekanism_elite/qio_dashboard
fill 313 63 108 324 63 121 minecraft:light_gray_concrete
fill 313 64 108 324 71 108 minecraft:light_gray_concrete
fill 313 64 108 313 71 121 minecraft:light_gray_concrete
setblock 314 64 120 minecraft:air
setblock 314 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "076"}','{"text": "mekanism_elite"}','{"text": "qio_dashboard"}','{"text": ""}']}}
setblock 315 64 120 minecraft:air
setblock 315 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the dashboard"}','{"text": "GUI"}','{"text": ""}','{"text": ""}']}}
summon text_display 318.5 71 113.5 {text:'[{"text": "076  ", "color": "gold"}, {"text": "mekanism_elite/qio_dashboard", "color": "gray"}, {"text": "\\nStell ein QIO-Dashboard auf", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 315 64 111 mekanism:qio_dashboard
setblock 317 64 111 mekanism:qio_drive_array
setblock 322 64 117 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"mekanism:qio_drive_base",count:1}]}
