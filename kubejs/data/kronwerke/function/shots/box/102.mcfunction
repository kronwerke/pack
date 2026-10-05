# 102 ars_master/tribute
fill 292 63 148 303 63 161 minecraft:light_gray_concrete
fill 292 64 148 303 71 148 minecraft:light_gray_concrete
fill 292 64 148 292 71 161 minecraft:light_gray_concrete
setblock 293 64 160 minecraft:air
setblock 293 64 160 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "102"}','{"text": "ars_master"}','{"text": "tribute"}','{"text": ""}']}}
setblock 294 64 160 minecraft:air
setblock 294 64 160 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the Chimera mid"}','{"text": "fight"}','{"text": "Chimäre steht"}','{"text": "still (NoAI)"}']}}
summon text_display 297.5 71 153.5 {text:'[{"text": "102  ", "color": "gold"}, {"text": "ars_master/tribute", "color": "gray"}, {"text": "\\nBesieg die Wilden-Chimäre", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
summon ars_nouveau:wilden_boss 295.5 64 155.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
