# 172 immersive/cloche
fill 135 63 273 146 63 286 minecraft:light_gray_concrete
fill 135 64 273 146 71 273 minecraft:light_gray_concrete
fill 135 64 273 135 71 286 minecraft:light_gray_concrete
setblock 136 64 285 minecraft:air
setblock 136 64 285 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "172"}','{"text": "immersive"}','{"text": "cloche"}','{"text": ""}']}}
setblock 137 64 285 minecraft:air
setblock 137 64 285 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a garden cloche"}','{"text": "growing hemp"}','{"text": ""}','{"text": ""}']}}
summon text_display 140.5 71 278.5 {text:'[{"text": "172  ", "color": "gold"}, {"text": "immersive/cloche", "color": "gray"}, {"text": "\\nStell eine Gartenglocke auf", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 137 64 276 immersiveengineering:cloche
setblock 144 64 282 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"immersiveengineering:seed",count:4}]}
