# 151 occultism_afrit/unbound_afrit
fill 165 63 242 176 63 255 minecraft:light_gray_concrete
fill 165 64 242 176 71 242 minecraft:light_gray_concrete
fill 165 64 242 165 71 255 minecraft:light_gray_concrete
setblock 166 64 254 minecraft:air
setblock 166 64 254 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "151"}','{"text": "occultism_afrit"}','{"text": "unbound_afrit"}','{"text": ""}']}}
setblock 167 64 254 minecraft:air
setblock 167 64 254 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "fight with an"}','{"text": "unbound Afrit"}','{"text": ""}','{"text": ""}']}}
summon text_display 170.5 71 247.5 {text:'[{"text": "151  ", "color": "gold"}, {"text": "occultism_afrit/unbound_afrit", "color": "gray"}, {"text": "\\nBesieg einen Unbound Afrit", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
summon occultism:afrit_wild 168.5 64 249.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
