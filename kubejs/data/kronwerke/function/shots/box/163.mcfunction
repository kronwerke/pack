# 163 hexerei/crow
fill 345 63 242 356 63 255 minecraft:light_gray_concrete
fill 345 64 242 356 71 242 minecraft:light_gray_concrete
fill 345 64 242 345 71 255 minecraft:light_gray_concrete
setblock 346 64 254 minecraft:air
setblock 346 64 254 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "163"}','{"text": "hexerei"}','{"text": "crow"}','{"text": ""}']}}
setblock 347 64 254 minecraft:air
setblock 347 64 254 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "crow on the"}','{"text": "shoulder, crow"}','{"text": "flute menu"}','{"text": ""}']}}
summon text_display 350.5 71 247.5 {text:'[{"text": "163  ", "color": "gold"}, {"text": "hexerei/crow", "color": "gray"}, {"text": "\\nZähm eine Krähe", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 354 64 251 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"hexerei:crow_flute",count:1}]}
summon hexerei:crow 348.5 64 249.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
