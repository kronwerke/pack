# 111 ars_epic/phases
fill 15 63 167 26 63 180 minecraft:light_gray_concrete
fill 15 64 167 26 71 167 minecraft:light_gray_concrete
fill 15 64 167 15 71 180 minecraft:light_gray_concrete
setblock 16 64 179 minecraft:air
setblock 16 64 179 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "111"}','{"text": "ars_epic"}','{"text": "phases"}','{"text": ""}']}}
setblock 17 64 179 minecraft:air
setblock 17 64 179 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the Chimera"}','{"text": "curled up with"}','{"text": "spikes"}','{"text": "Chimäre steht"}']}}
setblock 18 64 179 minecraft:air
setblock 18 64 179 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "still (NoAI)"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
summon text_display 20.5 71 172.5 {text:'[{"text": "111  ", "color": "gold"}, {"text": "ars_epic/phases", "color": "gray"}, {"text": "\\nLern die vier Phasen", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
summon ars_nouveau:wilden_boss 18.5 64 174.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
