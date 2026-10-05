# 152 occultism_afrit/mineshaft
fill 180 63 242 191 63 255 minecraft:light_gray_concrete
fill 180 64 242 191 71 242 minecraft:light_gray_concrete
fill 180 64 242 180 71 255 minecraft:light_gray_concrete
setblock 181 64 254 minecraft:air
setblock 181 64 254 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "152"}','{"text": "occultism_afrit"}','{"text": "mineshaft"}','{"text": ""}']}}
setblock 182 64 254 minecraft:air
setblock 182 64 254 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "dimensional"}','{"text": "mineshaft with"}','{"text": "a lamp inside"}','{"text": "and a hopper"}']}}
setblock 183 64 254 minecraft:air
setblock 183 64 254 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "below"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
summon text_display 185.5 71 247.5 {text:'[{"text": "152  ", "color": "gold"}, {"text": "occultism_afrit/mineshaft", "color": "gray"}, {"text": "\\nBau den Dimensional Mineshaft", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 185 65 247 occultism:dimensional_mineshaft
setblock 185 64 247 minecraft:hopper
setblock 186 64 247 minecraft:chest
