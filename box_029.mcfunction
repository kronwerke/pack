# 029 immersive/tank, silo, shelf
#area 41 113 80 142
fill 41 64 113 75 94 142 minecraft:air
fill 76 64 113 80 94 142 minecraft:air
fill 41 60 113 80 62 142 minecraft:stone
fill 41 63 113 80 63 142 minecraft:light_gray_concrete
fill 45 64 119 80 82 119 minecraft:light_gray_concrete
fill 45 64 119 45 82 136 minecraft:light_gray_concrete
setblock 46 64 135 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "029.1"}','{"text": "immersive"}','{"text": "tank"}','{"text": ""}']}}
setblock 47 64 135 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the formed"}','{"text": "structures"}','{"text": ""}','{"text": ""}']}}
summon text_display 50.5 71 125.5 {text:'[{"text": "029.1  ", "color": "gold"}, {"text": "immersive/tank", "color": "gray"}, {"text": "\\nForm einen Flüssigkeitstank", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 55 64 119 55 82 136 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/sheetmetal_tank 49 64 122 none
kw testworld use 50 65 124 south immersiveengineering:hammer
execute unless block 50 65 124 immersiveengineering:sheetmetal_iron
setblock 56 64 135 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "029.2"}','{"text": "immersive"}','{"text": "silo"}','{"text": ""}']}}
setblock 57 64 135 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form ein"}','{"text": "Elementsilo"}','{"text": ""}','{"text": ""}']}}
summon text_display 60.5 71 126.5 {text:'[{"text": "029.2  ", "color": "gold"}, {"text": "immersive/silo", "color": "gray"}, {"text": "\\nForm ein Elementsilo", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 65 64 119 65 82 136 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/silo 59 64 122 none
kw testworld use 60 65 124 south immersiveengineering:hammer
execute unless block 60 65 124 immersiveengineering:sheetmetal_iron
setblock 66 64 135 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "029.3"}','{"text": "immersive"}','{"text": "shelf"}','{"text": ""}']}}
setblock 67 64 135 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form ein"}','{"text": "Kistenregal"}','{"text": ""}','{"text": ""}']}}
summon text_display 70.5 71 125.0 {text:'[{"text": "029.3  ", "color": "gold"}, {"text": "immersive/shelf", "color": "gray"}, {"text": "\\nForm ein Kistenregal", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 75 64 119 75 82 136 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/shelf 68 64 122 none
kw testworld use 69 65 123 south immersiveengineering:hammer
execute unless block 69 65 123 immersiveengineering:steel_catwalk
