# 165 immersive/welcome
fill 0 63 273 11 63 286 minecraft:light_gray_concrete
fill 0 64 273 11 71 273 minecraft:light_gray_concrete
fill 0 64 273 0 71 286 minecraft:light_gray_concrete
setblock 1 64 285 minecraft:air
setblock 1 64 285 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "165"}','{"text": "immersive"}','{"text": "welcome"}','{"text": ""}']}}
setblock 2 64 285 minecraft:air
setblock 2 64 285 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the manual open"}','{"text": "on a multiblock"}','{"text": "page"}','{"text": "Handbuch auf"}']}}
setblock 3 64 285 minecraft:air
setblock 3 64 285 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "einer"}','{"text": "Multiblock-Seite"}','{"text": ""}','{"text": ""}']}}
summon text_display 5.5 71 278.5 {text:'[{"text": "165  ", "color": "gold"}, {"text": "immersive/welcome", "color": "gray"}, {"text": "\\nHol dir das Ingenieurshandbuch", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 9 64 282 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"immersiveengineering:manual",count:1}]}
