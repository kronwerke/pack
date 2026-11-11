# 016 immersive/kiln
#area 26 105 45 130
fill 26 64 105 45 91 130 minecraft:air
fill 26 60 105 45 62 130 minecraft:stone
fill 26 63 105 45 63 130 minecraft:light_gray_concrete
fill 30 64 111 45 79 111 minecraft:light_gray_concrete
fill 30 64 111 30 79 124 minecraft:light_gray_concrete
setblock 31 64 123 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "016"}','{"text": "immersive"}','{"text": "kiln"}','{"text": ""}']}}
setblock 32 64 123 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "alloy kiln"}','{"text": "making electrum"}','{"text": ""}','{"text": ""}']}}
summon text_display 35.5 71 116.5 {text:'[{"text": "016  ", "color": "gold"}, {"text": "immersive/kiln", "color": "gray"}, {"text": "\\nForm einen Legierungsofen", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 40 64 111 40 79 120 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/alloy_smelter 34 64 116 none
kw testworld use 35 65 117 south immersiveengineering:hammer
execute unless block 35 65 117 immersiveengineering:alloybrick
