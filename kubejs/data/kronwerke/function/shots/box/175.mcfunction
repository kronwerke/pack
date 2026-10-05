# 175 immersive/tank, silo, shelf
fill 254 63 273 285 63 286 minecraft:light_gray_concrete
fill 254 64 273 285 71 273 minecraft:light_gray_concrete
fill 254 64 273 254 71 286 minecraft:light_gray_concrete
setblock 255 64 285 minecraft:air
setblock 255 64 285 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "175.1"}','{"text": "immersive"}','{"text": "tank"}','{"text": ""}']}}
setblock 256 64 285 minecraft:air
setblock 256 64 285 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the formed"}','{"text": "structures"}','{"text": "Mit dem Hammer"}','{"text": "formen"}']}}
summon text_display 259.5 71 278.5 {text:'[{"text": "175.1  ", "color": "gold"}, {"text": "immersive/tank", "color": "gray"}, {"text": "\\nForm einen Flüssigkeitstank", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
place template immersiveengineering:multiblocks/sheetmetal_tank 256 64 275 none
setblock 263 64 282 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"immersiveengineering:hammer",count:1},{Slot:1b,id:"immersiveengineering:manual",count:1}]}
setblock 265 64 285 minecraft:air
setblock 265 64 285 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "175.2"}','{"text": "immersive"}','{"text": "silo"}','{"text": ""}']}}
setblock 266 64 285 minecraft:air
setblock 266 64 285 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Mit dem Hammer"}','{"text": "formen"}','{"text": ""}','{"text": ""}']}}
summon text_display 269.5 71 278.5 {text:'[{"text": "175.2  ", "color": "gold"}, {"text": "immersive/silo", "color": "gray"}, {"text": "\\nForm ein Elementsilo", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
place template immersiveengineering:multiblocks/silo 266 64 275 none
setblock 273 64 282 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"immersiveengineering:hammer",count:1},{Slot:1b,id:"immersiveengineering:manual",count:1}]}
setblock 275 64 285 minecraft:air
setblock 275 64 285 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "175.3"}','{"text": "immersive"}','{"text": "shelf"}','{"text": ""}']}}
setblock 276 64 285 minecraft:air
setblock 276 64 285 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Mit dem Hammer"}','{"text": "formen"}','{"text": ""}','{"text": ""}']}}
summon text_display 279.5 71 278.5 {text:'[{"text": "175.3  ", "color": "gold"}, {"text": "immersive/shelf", "color": "gray"}, {"text": "\\nForm ein Kistenregal", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
place template immersiveengineering:multiblocks/shelf 276 64 275 none
setblock 283 64 282 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"immersiveengineering:hammer",count:1},{Slot:1b,id:"immersiveengineering:manual",count:1}]}
