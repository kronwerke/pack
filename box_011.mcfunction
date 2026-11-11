# 011 immersive/tank, silo, shelf
#area 41 48 80 73
fill 41 64 48 80 91 73 minecraft:air
fill 41 60 48 80 62 73 minecraft:stone
fill 41 63 48 80 63 73 minecraft:light_gray_concrete
fill 45 64 54 80 79 54 minecraft:light_gray_concrete
fill 45 64 54 45 79 67 minecraft:light_gray_concrete
setblock 46 64 66 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "011.1"}','{"text": "immersive"}','{"text": "tank"}','{"text": ""}']}}
setblock 47 64 66 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the formed"}','{"text": "structures"}','{"text": ""}','{"text": ""}']}}
summon text_display 50.5 71 59.5 {text:'[{"text": "011.1  ", "color": "gold"}, {"text": "immersive/tank", "color": "gray"}, {"text": "\\nForm einen Flüssigkeitstank", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 55 64 54 55 79 63 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/sheetmetal_tank 49 64 58 none
kw testworld use 50 65 60 south immersiveengineering:hammer
execute unless block 50 65 60 immersiveengineering:sheetmetal_iron
setblock 56 64 66 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "011.2"}','{"text": "immersive"}','{"text": "silo"}','{"text": ""}']}}
setblock 57 64 66 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form ein"}','{"text": "Elementsilo"}','{"text": ""}','{"text": ""}']}}
summon text_display 60.5 71 59.5 {text:'[{"text": "011.2  ", "color": "gold"}, {"text": "immersive/silo", "color": "gray"}, {"text": "\\nForm ein Elementsilo", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 65 64 54 65 79 63 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/silo 59 64 58 none
kw testworld use 60 65 60 south immersiveengineering:hammer
execute unless block 60 65 60 immersiveengineering:sheetmetal_iron
setblock 66 64 66 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "011.3"}','{"text": "immersive"}','{"text": "shelf"}','{"text": ""}']}}
setblock 67 64 66 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form ein"}','{"text": "Kistenregal"}','{"text": ""}','{"text": ""}']}}
summon text_display 70.5 71 59.5 {text:'[{"text": "011.3  ", "color": "gold"}, {"text": "immersive/shelf", "color": "gray"}, {"text": "\\nForm ein Kistenregal", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 75 64 54 75 79 63 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/shelf 68 64 59 none
kw testworld use 69 65 60 south immersiveengineering:hammer
execute unless block 69 65 60 immersiveengineering:steel_catwalk
