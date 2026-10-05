# 166 immersive/hammer
fill 15 63 273 26 63 286 minecraft:light_gray_concrete
fill 15 64 273 26 71 273 minecraft:light_gray_concrete
fill 15 64 273 15 71 286 minecraft:light_gray_concrete
setblock 16 64 285 minecraft:air
setblock 16 64 285 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "166"}','{"text": "immersive"}','{"text": "hammer"}','{"text": ""}']}}
setblock 17 64 285 minecraft:air
setblock 17 64 285 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "right-clicking"}','{"text": "a structure"}','{"text": "with the hammer"}','{"text": "Mit dem Hammer"}']}}
setblock 18 64 285 minecraft:air
setblock 18 64 285 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "formen"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
summon text_display 20.5 71 278.5 {text:'[{"text": "166  ", "color": "gold"}, {"text": "immersive/hammer", "color": "gray"}, {"text": "\\nBau einen Ingenieurshammer", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
place template immersiveengineering:multiblocks/coke_oven 17 64 275 none
setblock 24 64 282 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"immersiveengineering:hammer",count:1},{Slot:1b,id:"immersiveengineering:manual",count:1}]}
