# 070 mekanism_advanced/miner
fill 223 63 108 234 63 121 minecraft:light_gray_concrete
fill 223 64 108 234 71 108 minecraft:light_gray_concrete
fill 223 64 108 223 71 121 minecraft:light_gray_concrete
setblock 224 64 120 minecraft:air
setblock 224 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "070"}','{"text": "mekanism_advanced"}','{"text": "miner"}','{"text": ""}']}}
setblock 225 64 120 minecraft:air
setblock 225 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "digital miner"}','{"text": "GUI with"}','{"text": "filters and"}','{"text": "radius"}']}}
setblock 226 64 120 minecraft:air
setblock 226 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "GUI mit Filtern"}','{"text": "und Radius"}','{"text": ""}','{"text": ""}']}}
summon text_display 228.5 71 113.5 {text:'[{"text": "070  ", "color": "gold"}, {"text": "mekanism_advanced/miner", "color": "gray"}, {"text": "\\nStell einen Digitalen Miner auf", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 225 64 111 mekanism:digital_miner
