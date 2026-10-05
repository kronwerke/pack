# 171 immersive/bench
fill 120 63 273 131 63 286 minecraft:light_gray_concrete
fill 120 64 273 131 71 273 minecraft:light_gray_concrete
fill 120 64 273 120 71 286 minecraft:light_gray_concrete
setblock 121 64 285 minecraft:air
setblock 121 64 285 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "171"}','{"text": "immersive"}','{"text": "bench"}','{"text": ""}']}}
setblock 122 64 285 minecraft:air
setblock 122 64 285 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "engineer\'s"}','{"text": "workbench with"}','{"text": "the components"}','{"text": "blueprint"}']}}
summon text_display 125.5 71 278.5 {text:'[{"text": "171  ", "color": "gold"}, {"text": "immersive/bench", "color": "gray"}, {"text": "\\nBau einen Ingenieursarbeitstisch", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 122 64 276 immersiveengineering:workbench
setblock 129 64 282 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"immersiveengineering:blueprint",count:1}]}
