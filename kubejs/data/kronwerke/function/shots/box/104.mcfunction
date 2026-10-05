# 104 ars_master/golem_bookwyrm
fill 322 63 148 333 63 161 minecraft:light_gray_concrete
fill 322 64 148 333 71 148 minecraft:light_gray_concrete
fill 322 64 148 322 71 161 minecraft:light_gray_concrete
setblock 323 64 160 minecraft:air
setblock 323 64 160 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "104"}','{"text": "ars_master"}','{"text": "golem_bookwyrm"}','{"text": ""}']}}
setblock 324 64 160 minecraft:air
setblock 324 64 160 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "amethyst golem"}','{"text": "at a geode,"}','{"text": "storage lectern"}','{"text": "GUI"}']}}
summon text_display 327.5 71 153.5 {text:'[{"text": "104  ", "color": "gold"}, {"text": "ars_master/golem_bookwyrm", "color": "gray"}, {"text": "\\nWeck Amethyst-Golem und Bücherwurm", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 324 64 150 326 66 152 minecraft:amethyst_block
setblock 325 67 151 minecraft:budding_amethyst
summon ars_nouveau:amethyst_golem 327.5 64 153.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 330 64 153 ars_nouveau:storage_lectern
