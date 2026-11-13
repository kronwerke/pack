# 111 immersive/tank, silo, shelf
#area 169 181 208 210
fill 169 64 181 203 94 210 minecraft:air
fill 204 64 181 208 94 210 minecraft:air
fill 169 60 181 208 62 210 minecraft:stone
fill 169 63 181 208 63 210 minecraft:light_gray_concrete
fill 173 64 187 208 82 187 minecraft:light_gray_concrete
fill 173 64 187 173 82 204 minecraft:light_gray_concrete
setblock 174 64 203 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "111.1"}','{"text": "immersive"}','{"text": "tank"}','{"text": ""}']}}
setblock 175 64 203 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the formed"}','{"text": "structures"}','{"text": ""}','{"text": ""}']}}
fill 183 64 187 183 82 204 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/sheetmetal_tank 177 64 190 none
kw testworld use 178 65 192 south immersiveengineering:hammer
execute unless block 178 65 192 immersiveengineering:sheetmetal_iron
setblock 184 64 203 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "111.2"}','{"text": "immersive"}','{"text": "silo"}','{"text": ""}']}}
setblock 185 64 203 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form ein"}','{"text": "Elementsilo"}','{"text": ""}','{"text": ""}']}}
fill 193 64 187 193 82 204 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/silo 187 64 190 none
kw testworld use 188 65 192 south immersiveengineering:hammer
execute unless block 188 65 192 immersiveengineering:sheetmetal_iron
setblock 194 64 203 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "111.3"}','{"text": "immersive"}','{"text": "shelf"}','{"text": ""}']}}
setblock 195 64 203 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form ein"}','{"text": "Kistenregal"}','{"text": ""}','{"text": ""}']}}
fill 203 64 187 203 82 204 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/shelf 196 64 190 none
kw testworld use 197 65 191 south immersiveengineering:hammer
execute unless block 197 65 191 immersiveengineering:steel_catwalk
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
