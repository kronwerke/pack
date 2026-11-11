# 028 immersive/kiln
#area 26 113 45 138
fill 26 64 113 45 91 138 minecraft:air
fill 26 60 113 45 62 138 minecraft:stone
fill 26 63 113 45 63 138 minecraft:light_gray_concrete
fill 30 64 119 45 79 119 minecraft:light_gray_concrete
fill 30 64 119 30 79 132 minecraft:light_gray_concrete
setblock 31 64 131 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "028"}','{"text": "immersive"}','{"text": "kiln"}','{"text": ""}']}}
setblock 32 64 131 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "alloy kiln"}','{"text": "making electrum"}','{"text": ""}','{"text": ""}']}}
summon text_display 35.5 71 124.5 {text:'[{"text": "028  ", "color": "gold"}, {"text": "immersive/kiln", "color": "gray"}, {"text": "\\nForm einen Legierungsofen", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 40 64 119 40 79 132 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/alloy_smelter 34 64 122 none
kw testworld use 35 65 123 south immersiveengineering:hammer
execute unless block 35 65 123 immersiveengineering:alloybrick
