# 075 immersive/tank, silo, shelf
#area 156 177 195 206
fill 156 64 177 190 94 206 minecraft:air
fill 191 64 177 195 94 206 minecraft:air
fill 156 60 177 195 62 206 minecraft:stone
fill 156 63 177 195 63 206 minecraft:light_gray_concrete
fill 160 64 183 195 82 183 minecraft:light_gray_concrete
fill 160 64 183 160 82 200 minecraft:light_gray_concrete
setblock 161 64 199 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "075.1"}','{"text": "immersive"}','{"text": "tank"}','{"text": ""}']}}
setblock 162 64 199 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the formed"}','{"text": "structures"}','{"text": ""}','{"text": ""}']}}
fill 170 64 183 170 82 200 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/sheetmetal_tank 164 64 186 none
kw testworld use 165 65 188 south immersiveengineering:hammer
execute unless block 165 65 188 immersiveengineering:sheetmetal_iron
setblock 171 64 199 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "075.2"}','{"text": "immersive"}','{"text": "silo"}','{"text": ""}']}}
setblock 172 64 199 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form ein"}','{"text": "Elementsilo"}','{"text": ""}','{"text": ""}']}}
fill 180 64 183 180 82 200 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/silo 174 64 186 none
kw testworld use 175 65 188 south immersiveengineering:hammer
execute unless block 175 65 188 immersiveengineering:sheetmetal_iron
setblock 181 64 199 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "075.3"}','{"text": "immersive"}','{"text": "shelf"}','{"text": ""}']}}
setblock 182 64 199 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form ein"}','{"text": "Kistenregal"}','{"text": ""}','{"text": ""}']}}
fill 190 64 183 190 82 200 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/shelf 183 64 186 none
kw testworld use 184 65 187 south immersiveengineering:hammer
execute unless block 184 65 187 immersiveengineering:steel_catwalk
