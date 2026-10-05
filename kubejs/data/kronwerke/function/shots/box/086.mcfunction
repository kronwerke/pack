# 086 ars_nouveau/chamber_auto
fill 40 63 148 51 63 161 minecraft:light_gray_concrete
fill 40 64 148 51 71 148 minecraft:light_gray_concrete
fill 40 64 148 40 71 161 minecraft:light_gray_concrete
setblock 41 64 160 minecraft:air
setblock 41 64 160 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "086"}','{"text": "ars_nouveau"}','{"text": "chamber_auto"}','{"text": ""}']}}
setblock 42 64 160 minecraft:air
setblock 42 64 160 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "hoppers above"}','{"text": "and below a"}','{"text": "chamber feeding"}','{"text": "a chest"}']}}
summon text_display 45.5 71 153.5 {text:'[{"text": "086  ", "color": "gold"}, {"text": "ars_nouveau/chamber_auto", "color": "gray"}, {"text": "\\nAutomatisiere die Kammer", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 45 66 153 minecraft:hopper[facing=down]
setblock 45 65 153 ars_nouveau:imbuement_chamber
setblock 45 64 153 minecraft:hopper[facing=south]
setblock 45 64 154 minecraft:chest
setblock 43 65 153 ars_nouveau:source_jar
