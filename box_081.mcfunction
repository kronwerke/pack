# 081 immersive/tank, silo, shelf
#area 128 177 167 206
fill 128 64 177 162 94 206 minecraft:air
fill 163 64 177 167 94 206 minecraft:air
fill 128 60 177 167 62 206 minecraft:stone
fill 128 63 177 167 63 206 minecraft:light_gray_concrete
fill 132 64 183 167 82 183 minecraft:light_gray_concrete
fill 132 64 183 132 82 200 minecraft:light_gray_concrete
setblock 133 64 199 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "081.1"}','{"text": "immersive"}','{"text": "tank"}','{"text": ""}']}}
setblock 134 64 199 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the formed"}','{"text": "structures"}','{"text": ""}','{"text": ""}']}}
fill 142 64 183 142 82 200 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/sheetmetal_tank 136 64 186 none
kw testworld use 137 65 188 south immersiveengineering:hammer
execute unless block 137 65 188 immersiveengineering:sheetmetal_iron
setblock 143 64 199 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "081.2"}','{"text": "immersive"}','{"text": "silo"}','{"text": ""}']}}
setblock 144 64 199 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form ein"}','{"text": "Elementsilo"}','{"text": ""}','{"text": ""}']}}
fill 152 64 183 152 82 200 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/silo 146 64 186 none
kw testworld use 147 65 188 south immersiveengineering:hammer
execute unless block 147 65 188 immersiveengineering:sheetmetal_iron
setblock 153 64 199 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "081.3"}','{"text": "immersive"}','{"text": "shelf"}','{"text": ""}']}}
setblock 154 64 199 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form ein"}','{"text": "Kistenregal"}','{"text": ""}','{"text": ""}']}}
fill 162 64 183 162 82 200 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/shelf 155 64 186 none
kw testworld use 156 65 187 south immersiveengineering:hammer
execute unless block 156 65 187 immersiveengineering:steel_catwalk
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
