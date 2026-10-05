# 092 ars_nouveau/drygmy
fill 130 63 148 141 63 161 minecraft:light_gray_concrete
fill 130 64 148 141 71 148 minecraft:light_gray_concrete
fill 130 64 148 130 71 161 minecraft:light_gray_concrete
setblock 131 64 160 minecraft:air
setblock 131 64 160 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "092"}','{"text": "ars_nouveau"}','{"text": "drygmy"}','{"text": ""}']}}
setblock 132 64 160 minecraft:air
setblock 132 64 160 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Drygmy henge"}','{"text": "with chest and"}','{"text": "jar"}','{"text": ""}']}}
summon text_display 135.5 71 153.5 {text:'[{"text": "092  ", "color": "gold"}, {"text": "ars_nouveau/drygmy", "color": "gray"}, {"text": "\\nRuf einen Drygmy", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 134 64 152 minecraft:mossy_cobblestone
setblock 136 64 152 minecraft:mossy_cobblestone
setblock 134 64 154 minecraft:mossy_cobblestone
setblock 136 64 154 minecraft:mossy_cobblestone
setblock 135 64 153 ars_nouveau:drygmy_stone[converted=true]
setblock 137 64 155 minecraft:chest
setblock 133 64 155 ars_nouveau:source_jar
summon minecraft:cow 138.5 64 152.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
