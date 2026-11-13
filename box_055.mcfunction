# 055 immersive/tank, silo, shelf
#area 142 158 181 187
fill 142 64 158 176 94 187 minecraft:air
fill 177 64 158 181 94 187 minecraft:air
fill 142 60 158 181 62 187 minecraft:stone
fill 142 63 158 181 63 187 minecraft:light_gray_concrete
fill 146 64 164 181 82 164 minecraft:light_gray_concrete
fill 146 64 164 146 82 181 minecraft:light_gray_concrete
setblock 147 64 180 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "055.1"}','{"text": "immersive"}','{"text": "tank"}','{"text": ""}']}}
setblock 148 64 180 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the formed"}','{"text": "structures"}','{"text": ""}','{"text": ""}']}}
fill 156 64 164 156 82 181 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/sheetmetal_tank 150 64 167 none
kw testworld use 151 65 169 south immersiveengineering:hammer
execute unless block 151 65 169 immersiveengineering:sheetmetal_iron
setblock 157 64 180 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "055.2"}','{"text": "immersive"}','{"text": "silo"}','{"text": ""}']}}
setblock 158 64 180 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form ein"}','{"text": "Elementsilo"}','{"text": ""}','{"text": ""}']}}
fill 166 64 164 166 82 181 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/silo 160 64 167 none
kw testworld use 161 65 169 south immersiveengineering:hammer
execute unless block 161 65 169 immersiveengineering:sheetmetal_iron
setblock 167 64 180 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "055.3"}','{"text": "immersive"}','{"text": "shelf"}','{"text": ""}']}}
setblock 168 64 180 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form ein"}','{"text": "Kistenregal"}','{"text": ""}','{"text": ""}']}}
fill 176 64 164 176 82 181 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/shelf 169 64 167 none
kw testworld use 170 65 168 south immersiveengineering:hammer
execute unless block 170 65 168 immersiveengineering:steel_catwalk
