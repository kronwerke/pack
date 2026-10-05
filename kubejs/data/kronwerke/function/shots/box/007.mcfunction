# 007 start_here/m_altar
fill 108 63 6 119 63 19 minecraft:light_gray_concrete
fill 108 64 6 119 71 6 minecraft:light_gray_concrete
fill 108 64 6 108 71 19 minecraft:light_gray_concrete
setblock 109 64 18 minecraft:air
setblock 109 64 18 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "007"}','{"text": "start_here"}','{"text": "m_altar"}','{"text": ""}']}}
setblock 110 64 18 minecraft:air
setblock 110 64 18 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the finished"}','{"text": "Natural Altar"}','{"text": ""}','{"text": ""}']}}
summon text_display 113.5 71 11.5 {text:'[{"text": "007  ", "color": "gold"}, {"text": "start_here/m_altar", "color": "gray"}, {"text": "\\nBau den Natural Altar", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 110 64 9 naturesaura:nature_altar
