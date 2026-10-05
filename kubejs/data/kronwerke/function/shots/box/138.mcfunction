# 138 alfheim/corporea_index
fill 15 63 223 26 63 236 minecraft:light_gray_concrete
fill 15 64 223 26 71 223 minecraft:light_gray_concrete
fill 15 64 223 15 71 236 minecraft:light_gray_concrete
setblock 16 64 235 minecraft:air
setblock 16 64 235 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "138"}','{"text": "alfheim"}','{"text": "corporea_index"}','{"text": ""}']}}
setblock 17 64 235 minecraft:air
setblock 17 64 235 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the index with"}','{"text": "a chat request"}','{"text": ""}','{"text": ""}']}}
summon text_display 20.5 71 228.5 {text:'[{"text": "138  ", "color": "gold"}, {"text": "alfheim/corporea_index", "color": "gray"}, {"text": "\\nBau einen Corporea-Index", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 17 64 226 botania:corporea_index
setblock 24 64 232 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"botania:corporea_spark",count:2}]}
