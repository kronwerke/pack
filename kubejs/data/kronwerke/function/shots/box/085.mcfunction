# 085 ars_nouveau/fill_jar
fill 25 63 148 36 63 161 minecraft:light_gray_concrete
fill 25 64 148 36 71 148 minecraft:light_gray_concrete
fill 25 64 148 25 71 161 minecraft:light_gray_concrete
setblock 26 64 160 minecraft:air
setblock 26 64 160 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "085"}','{"text": "ars_nouveau"}','{"text": "fill_jar"}','{"text": ""}']}}
setblock 27 64 160 minecraft:air
setblock 27 64 160 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "volcanic"}','{"text": "sourcelink, jar"}','{"text": "and chamber"}','{"text": "within range,"}']}}
setblock 28 64 160 minecraft:air
setblock 28 64 160 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "logs on the"}','{"text": "ground"}','{"text": ""}','{"text": ""}']}}
summon text_display 30.5 71 153.5 {text:'[{"text": "085  ", "color": "gold"}, {"text": "ars_nouveau/fill_jar", "color": "gray"}, {"text": "\\nFüll dein erstes Glas", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 29 64 153 ars_nouveau:volcanic_sourcelink
setblock 31 64 153 ars_nouveau:source_jar
setblock 33 64 153 ars_nouveau:imbuement_chamber
fill 27 64 155 30 64 155 minecraft:oak_log[axis=x]
