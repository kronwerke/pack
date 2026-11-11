# 025 immersive/tank, silo, shelf
#area 41 111 80 140
fill 41 64 111 75 94 140 minecraft:air
fill 76 64 111 80 94 140 minecraft:air
fill 41 60 111 80 62 140 minecraft:stone
fill 41 63 111 80 63 140 minecraft:light_gray_concrete
fill 45 64 117 80 82 117 minecraft:light_gray_concrete
fill 45 64 117 45 82 134 minecraft:light_gray_concrete
setblock 46 64 133 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "025.1"}','{"text": "immersive"}','{"text": "tank"}','{"text": ""}']}}
setblock 47 64 133 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the formed"}','{"text": "structures"}','{"text": ""}','{"text": ""}']}}
summon text_display 50.5 71 123.5 {text:'[{"text": "025.1  ", "color": "gold"}, {"text": "immersive/tank", "color": "gray"}, {"text": "\\nForm einen Flüssigkeitstank", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 55 64 117 55 82 128 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/sheetmetal_tank 49 64 120 none
kw testworld use 50 65 122 south immersiveengineering:hammer
execute unless block 50 65 122 immersiveengineering:sheetmetal_iron
setblock 56 64 133 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "025.2"}','{"text": "immersive"}','{"text": "silo"}','{"text": ""}']}}
setblock 57 64 133 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form ein"}','{"text": "Elementsilo"}','{"text": ""}','{"text": ""}']}}
summon text_display 60.5 71 124.5 {text:'[{"text": "025.2  ", "color": "gold"}, {"text": "immersive/silo", "color": "gray"}, {"text": "\\nForm ein Elementsilo", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 65 64 117 65 82 130 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/silo 59 64 120 none
kw testworld use 60 65 122 south immersiveengineering:hammer
execute unless block 60 65 122 immersiveengineering:sheetmetal_iron
setblock 66 64 133 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "025.3"}','{"text": "immersive"}','{"text": "shelf"}','{"text": ""}']}}
setblock 67 64 133 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form ein"}','{"text": "Kistenregal"}','{"text": ""}','{"text": ""}']}}
summon text_display 70.5 71 123.0 {text:'[{"text": "025.3  ", "color": "gold"}, {"text": "immersive/shelf", "color": "gray"}, {"text": "\\nForm ein Kistenregal", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 75 64 117 75 82 127 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/shelf 68 64 120 none
kw testworld use 69 65 121 south immersiveengineering:hammer
execute unless block 69 65 121 immersiveengineering:steel_catwalk
