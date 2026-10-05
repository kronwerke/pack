# 170 immersive/kiln
fill 105 63 273 116 63 286 minecraft:light_gray_concrete
fill 105 64 273 116 71 273 minecraft:light_gray_concrete
fill 105 64 273 105 71 286 minecraft:light_gray_concrete
setblock 106 64 285 minecraft:air
setblock 106 64 285 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "170"}','{"text": "immersive"}','{"text": "kiln"}','{"text": ""}']}}
setblock 107 64 285 minecraft:air
setblock 107 64 285 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "alloy kiln"}','{"text": "making electrum"}','{"text": "Mit dem Hammer"}','{"text": "formen"}']}}
summon text_display 110.5 71 278.5 {text:'[{"text": "170  ", "color": "gold"}, {"text": "immersive/kiln", "color": "gray"}, {"text": "\\nForm einen Legierungsofen", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
place template immersiveengineering:multiblocks/alloy_smelter 107 64 275 none
setblock 114 64 282 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"immersiveengineering:hammer",count:1},{Slot:1b,id:"immersiveengineering:manual",count:1}]}
