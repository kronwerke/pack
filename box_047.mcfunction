# 047 immersive/tank, silo, shelf
#area 66 144 105 173
fill 66 64 144 100 94 173 minecraft:air
fill 101 64 144 105 94 173 minecraft:air
fill 66 60 144 105 62 173 minecraft:stone
fill 66 63 144 105 63 173 minecraft:light_gray_concrete
fill 70 64 150 105 82 150 minecraft:light_gray_concrete
fill 70 64 150 70 82 167 minecraft:light_gray_concrete
setblock 71 64 166 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "047.1"}','{"text": "immersive"}','{"text": "tank"}','{"text": ""}']}}
setblock 72 64 166 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the formed"}','{"text": "structures"}','{"text": ""}','{"text": ""}']}}
fill 80 64 150 80 82 167 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/sheetmetal_tank 74 64 153 none
kw testworld use 75 65 155 south immersiveengineering:hammer
execute unless block 75 65 155 immersiveengineering:sheetmetal_iron
setblock 81 64 166 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "047.2"}','{"text": "immersive"}','{"text": "silo"}','{"text": ""}']}}
setblock 82 64 166 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form ein"}','{"text": "Elementsilo"}','{"text": ""}','{"text": ""}']}}
fill 90 64 150 90 82 167 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/silo 84 64 153 none
kw testworld use 85 65 155 south immersiveengineering:hammer
execute unless block 85 65 155 immersiveengineering:sheetmetal_iron
setblock 91 64 166 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "047.3"}','{"text": "immersive"}','{"text": "shelf"}','{"text": ""}']}}
setblock 92 64 166 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form ein"}','{"text": "Kistenregal"}','{"text": ""}','{"text": ""}']}}
fill 100 64 150 100 82 167 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/shelf 93 64 153 none
kw testworld use 94 65 154 south immersiveengineering:hammer
execute unless block 94 65 154 immersiveengineering:steel_catwalk
