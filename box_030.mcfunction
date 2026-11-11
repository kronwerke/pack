# 030 immersive_heavy/crusher, press, squeezer, fermenter, mixer, bottling, arc, refinery, diesel, sawmill, assembler, auto_workbench, excavator, lightning_rod, radio_tower
#area 76 113 235 154
fill 76 64 113 93 106 154 minecraft:air
fill 94 64 113 111 106 154 minecraft:air
fill 112 64 113 129 106 154 minecraft:air
fill 130 64 113 147 106 154 minecraft:air
fill 148 64 113 165 106 154 minecraft:air
fill 166 64 113 183 106 154 minecraft:air
fill 184 64 113 201 106 154 minecraft:air
fill 202 64 113 219 106 154 minecraft:air
fill 220 64 113 235 106 154 minecraft:air
fill 76 60 113 235 62 154 minecraft:stone
fill 76 63 113 235 63 154 minecraft:light_gray_concrete
fill 80 64 119 235 94 119 minecraft:light_gray_concrete
fill 80 64 119 80 94 148 minecraft:light_gray_concrete
setblock 81 64 147 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "030.1"}','{"text": "immersive_heavy"}','{"text": "crusher"}','{"text": ""}']}}
setblock 82 64 147 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "each formed"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
summon text_display 85.5 71 124.5 {text:'[{"text": "030.1  ", "color": "gold"}, {"text": "immersive_heavy/crusher", "color": "gray"}, {"text": "\\nForm einen Zerkleinerer", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 90 64 119 90 94 148 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/crusher 83 64 122 none
kw testworld use 85 65 124 south immersiveengineering:hammer
execute unless block 85 65 124 immersiveengineering:steel_fence
setblock 91 64 147 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "030.2"}','{"text": "immersive_heavy"}','{"text": "press"}','{"text": ""}']}}
setblock 92 64 147 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form eine"}','{"text": "Metallpresse"}','{"text": ""}','{"text": ""}']}}
summon text_display 95.5 71 124.5 {text:'[{"text": "030.2  ", "color": "gold"}, {"text": "immersive_heavy/press", "color": "gray"}, {"text": "\\nForm eine Metallpresse", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 100 64 119 100 94 148 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/metal_press 94 64 122 none
kw testworld use 95 65 122 south immersiveengineering:hammer
execute unless block 95 65 122 minecraft:piston
setblock 101 64 147 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "030.3"}','{"text": "immersive_heavy"}','{"text": "squeezer"}','{"text": ""}']}}
setblock 102 64 147 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form eine"}','{"text": "Industriepresse"}','{"text": ""}','{"text": ""}']}}
summon text_display 105.5 71 124.5 {text:'[{"text": "030.3  ", "color": "gold"}, {"text": "immersive_heavy/squeezer", "color": "gray"}, {"text": "\\nForm eine Industriepresse", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 110 64 119 110 94 148 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/squeezer 104 64 122 none
kw testworld use 105 65 123 south immersiveengineering:hammer
execute unless block 105 65 123 immersiveengineering:wooden_barrel
setblock 111 64 147 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "030.4"}','{"text": "immersive_heavy"}','{"text": "fermenter"}','{"text": ""}']}}
setblock 112 64 147 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Industriefermenter"}','{"text": ""}','{"text": ""}']}}
summon text_display 115.5 71 124.5 {text:'[{"text": "030.4  ", "color": "gold"}, {"text": "immersive_heavy/fermenter", "color": "gray"}, {"text": "\\nForm einen Industriefermenter", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 120 64 119 120 94 148 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/fermenter 114 64 122 none
kw testworld use 115 65 123 south immersiveengineering:hammer
execute unless block 115 65 123 minecraft:cauldron
setblock 121 64 147 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "030.5"}','{"text": "immersive_heavy"}','{"text": "mixer"}','{"text": ""}']}}
setblock 122 64 147 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Mischer"}','{"text": ""}','{"text": ""}']}}
summon text_display 125.5 71 124.5 {text:'[{"text": "030.5  ", "color": "gold"}, {"text": "immersive_heavy/mixer", "color": "gray"}, {"text": "\\nForm einen Mischer", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 130 64 119 130 94 148 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/mixer 124 64 122 none
kw testworld use 125 65 123 south immersiveengineering:hammer
execute unless block 125 65 123 immersiveengineering:sheetmetal_iron
setblock 131 64 147 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "030.6"}','{"text": "immersive_heavy"}','{"text": "bottling"}','{"text": ""}']}}
setblock 132 64 147 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form eine"}','{"text": "Abfüllanlage"}','{"text": ""}','{"text": ""}']}}
summon text_display 135.5 71 124.5 {text:'[{"text": "030.6  ", "color": "gold"}, {"text": "immersive_heavy/bottling", "color": "gray"}, {"text": "\\nForm eine Abfüllanlage", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 140 64 119 140 94 148 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/bottling_machine 134 64 122 none
kw testworld use 135 65 123 south immersiveengineering:hammer
execute unless block 135 65 123 immersiveengineering:conveyor_basic
setblock 141 64 147 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "030.7"}','{"text": "immersive_heavy"}','{"text": "arc"}','{"text": ""}']}}
setblock 142 64 147 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Lichtbogenofen"}','{"text": ""}','{"text": ""}']}}
summon text_display 145.5 71 125.5 {text:'[{"text": "030.7  ", "color": "gold"}, {"text": "immersive_heavy/arc", "color": "gray"}, {"text": "\\nForm einen Lichtbogenofen", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 150 64 119 150 94 148 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/arcfurnace 143 64 122 none
kw testworld use 145 64 126 south immersiveengineering:hammer
execute unless block 145 64 126 minecraft:cauldron
setblock 151 64 147 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "030.8"}','{"text": "immersive_heavy"}','{"text": "refinery"}','{"text": ""}']}}
setblock 152 64 147 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form eine"}','{"text": "Raffinerie"}','{"text": ""}','{"text": ""}']}}
summon text_display 155.5 71 124.5 {text:'[{"text": "030.8  ", "color": "gold"}, {"text": "immersive_heavy/refinery", "color": "gray"}, {"text": "\\nForm eine Raffinerie", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 160 64 119 160 94 148 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/refinery 153 64 122 none
kw testworld use 155 65 124 south immersiveengineering:hammer
execute unless block 155 65 124 immersiveengineering:heavy_engineering
setblock 161 64 147 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "030.9"}','{"text": "immersive_heavy"}','{"text": "diesel"}','{"text": ""}']}}
setblock 162 64 147 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Dieselgenerator"}','{"text": ""}','{"text": ""}']}}
summon text_display 165.5 71 124.5 {text:'[{"text": "030.9  ", "color": "gold"}, {"text": "immersive_heavy/diesel", "color": "gray"}, {"text": "\\nForm einen Dieselgenerator", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 170 64 119 170 94 148 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/diesel_generator 164 64 122 none
kw testworld use 165 65 126 south immersiveengineering:hammer
execute unless block 165 65 126 immersiveengineering:generator
setblock 171 64 147 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "030.10"}','{"text": "immersive_heavy"}','{"text": "sawmill"}','{"text": ""}']}}
setblock 172 64 147 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form ein"}','{"text": "Sägewerk"}','{"text": ""}','{"text": ""}']}}
summon text_display 175.5 71 124.5 {text:'[{"text": "030.10  ", "color": "gold"}, {"text": "immersive_heavy/sawmill", "color": "gray"}, {"text": "\\nForm ein Sägewerk", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 180 64 119 180 94 148 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/sawmill 173 64 122 none
kw testworld use 175 64 124 south immersiveengineering:hammer
execute unless block 175 64 124 immersiveengineering:sheetmetal_iron
setblock 181 64 147 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "030.11"}','{"text": "immersive_heavy"}','{"text": "assembler"}','{"text": ""}']}}
setblock 182 64 147 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Monteur"}','{"text": ""}','{"text": ""}']}}
summon text_display 185.5 71 124.5 {text:'[{"text": "030.11  ", "color": "gold"}, {"text": "immersive_heavy/assembler", "color": "gray"}, {"text": "\\nForm einen Monteur", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 190 64 119 190 94 148 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/assembler 184 64 122 none
kw testworld use 185 65 124 south immersiveengineering:hammer
execute unless block 185 65 124 immersiveengineering:conveyor_basic
setblock 191 64 147 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "030.12"}','{"text": "immersive_heavy"}','{"text": "auto_workbench"}','{"text": ""}']}}
setblock 192 64 147 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Automatisierten"}','{"text": "Arbeitstisch"}','{"text": ""}']}}
summon text_display 195.5 71 124.5 {text:'[{"text": "030.12  ", "color": "gold"}, {"text": "immersive_heavy/auto_workbench", "color": "gray"}, {"text": "\\nForm einen Automatisierten Arbeitstisch", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 200 64 119 200 94 148 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/auto_workbench 194 64 122 none
kw testworld use 195 65 124 south immersiveengineering:hammer
execute unless block 195 65 124 immersiveengineering:slab_treated_wood_horizontal
setblock 201 64 147 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "030.13"}','{"text": "immersive_heavy"}','{"text": "excavator"}','{"text": ""}']}}
setblock 202 64 147 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Bagger"}','{"text": ""}','{"text": ""}']}}
summon text_display 205.5 71 125.0 {text:'[{"text": "030.13  ", "color": "gold"}, {"text": "immersive_heavy/excavator", "color": "gray"}, {"text": "\\nForm einen Bagger", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 210 64 119 210 94 148 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/excavator 204 64 122 none
kw testworld use 205 65 127 south immersiveengineering:hammer
execute unless block 205 65 127 immersiveengineering:heavy_engineering
setblock 211 64 147 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "030.14"}','{"text": "immersive_heavy"}','{"text": "lightning_rod"}','{"text": ""}']}}
setblock 212 64 147 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Blitzableiter"}','{"text": ""}','{"text": ""}']}}
summon text_display 215.5 71 124.5 {text:'[{"text": "030.14  ", "color": "gold"}, {"text": "immersive_heavy/lightning_rod", "color": "gray"}, {"text": "\\nForm einen Blitzableiter", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 220 64 119 220 94 148 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/lightning_rod 214 64 122 none
kw testworld use 215 65 124 south immersiveengineering:hammer
execute unless block 215 65 124 immersiveengineering:light_engineering
setblock 221 64 147 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "030.15"}','{"text": "immersive_heavy"}','{"text": "radio_tower"}','{"text": ""}']}}
setblock 222 64 147 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Funkturm"}','{"text": ""}','{"text": ""}']}}
summon text_display 225.5 71 132.5 {text:'[{"text": "030.15  ", "color": "gold"}, {"text": "immersive_heavy/radio_tower", "color": "gray"}, {"text": "\\nForm einen Funkturm", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 230 64 119 230 94 148 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/radio_tower 223 64 122 none
kw testworld use 225 65 127 south immersiveengineering:hammer
execute unless block 225 65 127 immersiveengineering:rs_engineering
