# 035 create_brass/blaze_burner
fill 269 63 52 280 63 65 minecraft:light_gray_concrete
fill 269 64 52 280 71 52 minecraft:light_gray_concrete
fill 269 64 52 269 71 65 minecraft:light_gray_concrete
setblock 270 64 64 minecraft:air
setblock 270 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "035"}','{"text": "create_brass"}','{"text": "blaze_burner"}','{"text": ""}']}}
setblock 271 64 64 minecraft:air
setblock 271 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "catching a"}','{"text": "blaze with the"}','{"text": "empty burner"}','{"text": "Leeren Brenner"}']}}
setblock 272 64 64 minecraft:air
setblock 272 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "auf die Lohe"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
summon text_display 274.5 71 57.5 {text:'[{"text": "035  ", "color": "gold"}, {"text": "create_brass/blaze_burner", "color": "gray"}, {"text": "\\nFang eine Lohe ein", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 271 64 55 create:blaze_burner
summon minecraft:blaze 272.5 64 59.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
