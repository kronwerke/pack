# 042 create_brass/boiler
fill 388 63 52 401 63 67 minecraft:light_gray_concrete
fill 388 64 52 401 71 52 minecraft:light_gray_concrete
fill 388 64 52 388 71 67 minecraft:light_gray_concrete
setblock 389 64 66 minecraft:air
setblock 389 64 66 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "042"}','{"text": "create_brass"}','{"text": "boiler"}','{"text": ""}']}}
setblock 390 64 66 minecraft:air
setblock 390 64 66 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a four engine"}','{"text": "boiler with the"}','{"text": "goggles boiler"}','{"text": "overlay"}']}}
setblock 391 64 66 minecraft:air
setblock 391 64 66 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Brenner unter"}','{"text": "den Tank, vier"}','{"text": "Motoren, Brille"}','{"text": ""}']}}
summon text_display 394.5 71 58.5 {text:'[{"text": "042  ", "color": "gold"}, {"text": "create_brass/boiler", "color": "gray"}, {"text": "\\nBau ein Kesselkraftwerk", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 392 64 56 394 66 58 create:fluid_tank
fill 392 64 55 394 64 55 create:blaze_burner
setblock 393 65 55 create:steam_engine[face=wall,facing=north]
setblock 393 65 54 create:shaft[axis=z]
setblock 393 65 59 create:steam_engine[face=wall,facing=south]
setblock 393 65 60 create:shaft[axis=z]
setblock 399 64 63 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"create:steam_engine",count:1},{Slot:1b,id:"create:steam_engine",count:1},{Slot:2b,id:"create:goggles",count:1},{Slot:3b,id:"create:blaze_cake",count:8}]}
