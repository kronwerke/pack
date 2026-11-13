# 124 immersive/tank, silo, shelf
#area 169 215 208 244
fill 169 64 215 203 94 244 minecraft:air
fill 204 64 215 208 94 244 minecraft:air
fill 169 60 215 208 62 244 minecraft:stone
fill 169 63 215 208 63 244 minecraft:light_gray_concrete
fill 173 64 221 208 82 221 minecraft:light_gray_concrete
fill 173 64 221 173 82 238 minecraft:light_gray_concrete
setblock 174 64 237 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "124.1"}','{"text": "immersive"}','{"text": "tank"}','{"text": ""}']}}
setblock 175 64 237 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the formed"}','{"text": "structures"}','{"text": ""}','{"text": ""}']}}
fill 183 64 221 183 82 238 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/sheetmetal_tank 177 64 224 none
kw testworld use 178 65 226 south immersiveengineering:hammer
execute unless block 178 65 226 immersiveengineering:sheetmetal_iron
setblock 184 64 237 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "124.2"}','{"text": "immersive"}','{"text": "silo"}','{"text": ""}']}}
setblock 185 64 237 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form ein"}','{"text": "Elementsilo"}','{"text": ""}','{"text": ""}']}}
fill 193 64 221 193 82 238 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/silo 187 64 224 none
kw testworld use 188 65 226 south immersiveengineering:hammer
execute unless block 188 65 226 immersiveengineering:sheetmetal_iron
setblock 194 64 237 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "124.3"}','{"text": "immersive"}','{"text": "shelf"}','{"text": ""}']}}
setblock 195 64 237 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form ein"}','{"text": "Kistenregal"}','{"text": ""}','{"text": ""}']}}
fill 203 64 221 203 82 238 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/shelf 196 64 224 none
kw testworld use 197 65 225 south immersiveengineering:hammer
execute unless block 197 65 225 immersiveengineering:steel_catwalk
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
