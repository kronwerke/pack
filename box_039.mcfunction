# 039 immersive/tank, silo, shelf
#area 41 144 80 173
fill 41 64 144 75 94 173 minecraft:air
fill 76 64 144 80 94 173 minecraft:air
fill 41 60 144 80 62 173 minecraft:stone
fill 41 63 144 80 63 173 minecraft:light_gray_concrete
fill 45 64 150 80 82 150 minecraft:light_gray_concrete
fill 45 64 150 45 82 167 minecraft:light_gray_concrete
setblock 46 64 166 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "039.1"}','{"text": "immersive"}','{"text": "tank"}','{"text": ""}']}}
setblock 47 64 166 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the formed"}','{"text": "structures"}','{"text": ""}','{"text": ""}']}}
fill 55 64 150 55 82 167 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/sheetmetal_tank 49 64 153 none
kw testworld use 50 65 155 south immersiveengineering:hammer
execute unless block 50 65 155 immersiveengineering:sheetmetal_iron
setblock 56 64 166 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "039.2"}','{"text": "immersive"}','{"text": "silo"}','{"text": ""}']}}
setblock 57 64 166 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form ein"}','{"text": "Elementsilo"}','{"text": ""}','{"text": ""}']}}
fill 65 64 150 65 82 167 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/silo 59 64 153 none
kw testworld use 60 65 155 south immersiveengineering:hammer
execute unless block 60 65 155 immersiveengineering:sheetmetal_iron
setblock 66 64 166 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "039.3"}','{"text": "immersive"}','{"text": "shelf"}','{"text": ""}']}}
setblock 67 64 166 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form ein"}','{"text": "Kistenregal"}','{"text": ""}','{"text": ""}']}}
fill 75 64 150 75 82 167 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/shelf 68 64 153 none
kw testworld use 69 65 154 south immersiveengineering:hammer
execute unless block 69 65 154 immersiveengineering:steel_catwalk
