# 168 immersive/treated_wood
fill 65 63 273 76 63 286 minecraft:light_gray_concrete
fill 65 64 273 76 71 273 minecraft:light_gray_concrete
fill 65 64 273 65 71 286 minecraft:light_gray_concrete
setblock 66 64 285 minecraft:air
setblock 66 64 285 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "168"}','{"text": "immersive"}','{"text": "treated_wood"}','{"text": ""}']}}
setblock 67 64 285 minecraft:air
setblock 67 64 285 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "planks around"}','{"text": "the creosote"}','{"text": "bucket"}','{"text": "Mit dem Hammer"}']}}
setblock 68 64 285 minecraft:air
setblock 68 64 285 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "formen"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
summon text_display 70.5 71 278.5 {text:'[{"text": "168  ", "color": "gold"}, {"text": "immersive/treated_wood", "color": "gray"}, {"text": "\\nTränk Bretter in Kreosot", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
place template immersiveengineering:multiblocks/coke_oven 67 64 275 none
setblock 74 64 282 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"immersiveengineering:hammer",count:1},{Slot:1b,id:"immersiveengineering:manual",count:1}]}
