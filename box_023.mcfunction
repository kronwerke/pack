# 023 immersive/kiln
#area 26 111 45 136
fill 26 64 111 45 91 136 minecraft:air
fill 26 60 111 45 62 136 minecraft:stone
fill 26 63 111 45 63 136 minecraft:light_gray_concrete
fill 30 64 117 45 79 117 minecraft:light_gray_concrete
fill 30 64 117 30 79 130 minecraft:light_gray_concrete
setblock 31 64 129 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "023"}','{"text": "immersive"}','{"text": "kiln"}','{"text": ""}']}}
setblock 32 64 129 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "alloy kiln"}','{"text": "making electrum"}','{"text": ""}','{"text": ""}']}}
summon text_display 35.5 71 122.5 {text:'[{"text": "023  ", "color": "gold"}, {"text": "immersive/kiln", "color": "gray"}, {"text": "\\nForm einen Legierungsofen", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 40 64 117 40 79 126 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/alloy_smelter 34 64 122 none
kw testworld use 35 65 123 south immersiveengineering:hammer
execute unless block 35 65 123 immersiveengineering:alloybrick
