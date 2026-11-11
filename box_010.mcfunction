# 010 immersive/kiln
#area 26 48 45 73
fill 26 64 48 45 91 73 minecraft:air
fill 26 60 48 45 62 73 minecraft:stone
fill 26 63 48 45 63 73 minecraft:light_gray_concrete
fill 30 64 54 45 79 54 minecraft:light_gray_concrete
fill 30 64 54 30 79 67 minecraft:light_gray_concrete
setblock 31 64 66 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "010"}','{"text": "immersive"}','{"text": "kiln"}','{"text": ""}']}}
setblock 32 64 66 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "alloy kiln"}','{"text": "making electrum"}','{"text": ""}','{"text": ""}']}}
summon text_display 35.5 71 59.5 {text:'[{"text": "010  ", "color": "gold"}, {"text": "immersive/kiln", "color": "gray"}, {"text": "\\nForm einen Legierungsofen", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 40 64 54 40 79 63 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/alloy_smelter 34 64 59 none
kw testworld use 35 65 60 south immersiveengineering:hammer
execute unless block 35 65 60 immersiveengineering:alloybrick
