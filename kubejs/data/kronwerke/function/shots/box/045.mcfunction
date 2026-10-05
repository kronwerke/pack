# 045 create_brass/alternator
fill 45 63 77 58 63 90 minecraft:light_gray_concrete
fill 45 64 77 58 71 77 minecraft:light_gray_concrete
fill 45 64 77 45 71 90 minecraft:light_gray_concrete
setblock 46 64 89 minecraft:air
setblock 46 64 89 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "045"}','{"text": "create_brass"}','{"text": "alternator"}','{"text": ""}']}}
setblock 47 64 89 minecraft:air
setblock 47 64 89 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "steam engine"}','{"text": "driving an"}','{"text": "alternator with"}','{"text": "connectors"}']}}
summon text_display 51.5 71 82.5 {text:'[{"text": "045  ", "color": "gold"}, {"text": "create_brass/alternator", "color": "gray"}, {"text": "\\nMach FE aus Rotation", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 48 64 82 create:steam_engine[face=floor,facing=east]
fill 49 64 82 50 64 82 create:shaft[axis=x]
setblock 51 64 82 createaddition:alternator[facing=west]
setblock 51 65 82 createaddition:connector
