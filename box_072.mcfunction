# 072 immersive/tank, silo, shelf
#area 156 158 195 187
fill 156 64 158 190 94 187 minecraft:air
fill 191 64 158 195 94 187 minecraft:air
fill 156 60 158 195 62 187 minecraft:stone
fill 156 63 158 195 63 187 minecraft:light_gray_concrete
fill 160 64 164 195 82 164 minecraft:light_gray_concrete
fill 160 64 164 160 82 181 minecraft:light_gray_concrete
setblock 161 64 180 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "072.1"}','{"text": "immersive"}','{"text": "tank"}','{"text": ""}']}}
setblock 162 64 180 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the formed"}','{"text": "structures"}','{"text": ""}','{"text": ""}']}}
fill 170 64 164 170 82 181 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/sheetmetal_tank 164 64 167 none
kw testworld use 165 65 169 south immersiveengineering:hammer
execute unless block 165 65 169 immersiveengineering:sheetmetal_iron
setblock 171 64 180 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "072.2"}','{"text": "immersive"}','{"text": "silo"}','{"text": ""}']}}
setblock 172 64 180 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form ein"}','{"text": "Elementsilo"}','{"text": ""}','{"text": ""}']}}
fill 180 64 164 180 82 181 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/silo 174 64 167 none
kw testworld use 175 65 169 south immersiveengineering:hammer
execute unless block 175 65 169 immersiveengineering:sheetmetal_iron
setblock 181 64 180 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "072.3"}','{"text": "immersive"}','{"text": "shelf"}','{"text": ""}']}}
setblock 182 64 180 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form ein"}','{"text": "Kistenregal"}','{"text": ""}','{"text": ""}']}}
fill 190 64 164 190 82 181 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/shelf 183 64 167 none
kw testworld use 184 65 168 south immersiveengineering:hammer
execute unless block 184 65 168 immersiveengineering:steel_catwalk
