# 101 ars_apprentice/source_motor
fill 277 63 148 288 63 161 minecraft:light_gray_concrete
fill 277 64 148 288 71 148 minecraft:light_gray_concrete
fill 277 64 148 277 71 161 minecraft:light_gray_concrete
setblock 278 64 160 minecraft:air
setblock 278 64 160 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "101"}','{"text": "ars_apprentice"}','{"text": "source_motor"}','{"text": ""}']}}
setblock 279 64 160 minecraft:air
setblock 279 64 160 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "motor with a"}','{"text": "jar driving a"}','{"text": "Create shaft"}','{"text": ""}']}}
summon text_display 282.5 71 153.5 {text:'[{"text": "101  ", "color": "gold"}, {"text": "ars_apprentice/source_motor", "color": "gray"}, {"text": "\\nBau einen Source Motor", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 281 64 153 ars_technica:source_motor
setblock 281 65 153 ars_nouveau:source_jar
fill 282 64 153 284 64 153 create:shaft[axis=x]
setblock 285 64 153 create:millstone
