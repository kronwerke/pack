# 017 farms/source_berries
fill 113 63 31 126 63 44 minecraft:light_gray_concrete
fill 113 64 31 126 71 31 minecraft:light_gray_concrete
fill 113 64 31 113 71 44 minecraft:light_gray_concrete
setblock 114 64 43 minecraft:air
setblock 114 64 43 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "017"}','{"text": "farms"}','{"text": "source_berries"}','{"text": ""}']}}
setblock 115 64 43 minecraft:air
setblock 115 64 43 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "sourceberry"}','{"text": "rows with"}','{"text": "agronomic"}','{"text": "sourcelink,"}']}}
setblock 116 64 43 minecraft:air
setblock 116 64 43 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "source jar,"}','{"text": "imbuement"}','{"text": "chamber and"}','{"text": "Starbuncle"}']}}
summon text_display 119.5 71 36.5 {text:'[{"text": "017  ", "color": "gold"}, {"text": "farms/source_berries", "color": "gray"}, {"text": "\\nPflanze Quellbeeren", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 115 64 34 121 64 35 ars_nouveau:sourceberry_bush[age=3]
setblock 118 64 37 ars_nouveau:agronomic_sourcelink
setblock 120 64 37 ars_nouveau:source_jar
setblock 122 64 37 ars_nouveau:imbuement_chamber
summon ars_nouveau:starbuncle 117.5 64 38.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
