# 022 create/windmill
fill 32 63 52 51 63 65 minecraft:light_gray_concrete
fill 32 64 52 51 71 52 minecraft:light_gray_concrete
fill 32 64 52 32 71 65 minecraft:light_gray_concrete
setblock 33 64 64 minecraft:air
setblock 33 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "022"}','{"text": "create"}','{"text": "windmill"}','{"text": ""}']}}
setblock 34 64 64 minecraft:air
setblock 34 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a finished"}','{"text": "windmill with"}','{"text": "32 sails"}','{"text": "Lager anklicken"}']}}
setblock 35 64 64 minecraft:air
setblock 35 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "zum Starten (32"}','{"text": "Segel im"}','{"text": "Original)"}','{"text": ""}']}}
summon text_display 41.5 71 57.5 {text:'[{"text": "022  ", "color": "gold"}, {"text": "create/windmill", "color": "gray"}, {"text": "\\nLass die Windmühle laufen", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 41 64 59 41 68 59 create:andesite_casing
setblock 41 69 59 create:windmill_bearing[facing=north]
fill 41 70 58 41 75 58 create:white_sail[facing=north]
fill 41 64 58 41 68 58 create:white_sail[facing=north]
fill 42 69 58 47 69 58 create:white_sail[facing=north]
fill 35 69 58 40 69 58 create:white_sail[facing=north]
