# 148 occultism/djinni_familiars
fill 120 63 242 131 63 255 minecraft:light_gray_concrete
fill 120 64 242 131 71 242 minecraft:light_gray_concrete
fill 120 64 242 120 71 255 minecraft:light_gray_concrete
setblock 121 64 254 minecraft:air
setblock 121 64 254 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "148"}','{"text": "occultism"}','{"text": "djinni_familiars"}','{"text": ""}']}}
setblock 122 64 254 minecraft:air
setblock 122 64 254 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a player with"}','{"text": "two or three"}','{"text": "familiars"}','{"text": ""}']}}
summon text_display 125.5 71 247.5 {text:'[{"text": "148  ", "color": "gold"}, {"text": "occultism/djinni_familiars", "color": "gray"}, {"text": "\\nRuf einen Djinni-Vertrauten", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
summon occultism:greedy_familiar 123.5 64 249.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
summon occultism:beholder_familiar 126.5 64 249.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
