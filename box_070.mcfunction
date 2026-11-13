# 070 immersive/tank, silo, shelf
#area 154 158 193 187
fill 154 64 158 188 94 187 minecraft:air
fill 189 64 158 193 94 187 minecraft:air
fill 154 60 158 193 62 187 minecraft:stone
fill 154 63 158 193 63 187 minecraft:light_gray_concrete
fill 158 64 164 193 82 164 minecraft:light_gray_concrete
fill 158 64 164 158 82 181 minecraft:light_gray_concrete
setblock 159 64 180 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "070.1"}','{"text": "immersive"}','{"text": "tank"}','{"text": ""}']}}
setblock 160 64 180 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the formed"}','{"text": "structures"}','{"text": ""}','{"text": ""}']}}
fill 168 64 164 168 82 181 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/sheetmetal_tank 162 64 167 none
kw testworld use 163 65 169 south immersiveengineering:hammer
execute unless block 163 65 169 immersiveengineering:sheetmetal_iron
setblock 169 64 180 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "070.2"}','{"text": "immersive"}','{"text": "silo"}','{"text": ""}']}}
setblock 170 64 180 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form ein"}','{"text": "Elementsilo"}','{"text": ""}','{"text": ""}']}}
fill 178 64 164 178 82 181 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/silo 172 64 167 none
kw testworld use 173 65 169 south immersiveengineering:hammer
execute unless block 173 65 169 immersiveengineering:sheetmetal_iron
setblock 179 64 180 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "070.3"}','{"text": "immersive"}','{"text": "shelf"}','{"text": ""}']}}
setblock 180 64 180 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form ein"}','{"text": "Kistenregal"}','{"text": ""}','{"text": ""}']}}
fill 188 64 164 188 82 181 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/shelf 181 64 167 none
kw testworld use 182 65 168 south immersiveengineering:hammer
execute unless block 182 65 168 immersiveengineering:steel_catwalk
