# 124 immersive/tank, silo, shelf
#area 169 217 208 246
fill 169 64 217 203 94 246 minecraft:air
fill 204 64 217 208 94 246 minecraft:air
fill 169 60 217 208 62 246 minecraft:stone
fill 169 63 217 208 63 246 minecraft:light_gray_concrete
fill 173 64 223 208 82 223 minecraft:light_gray_concrete
fill 173 64 223 173 82 240 minecraft:light_gray_concrete
setblock 174 64 239 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "124.1"}','{"text": "immersive"}','{"text": "tank"}','{"text": ""}']}}
setblock 175 64 239 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the formed"}','{"text": "structures"}','{"text": ""}','{"text": ""}']}}
fill 183 64 223 183 82 240 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/sheetmetal_tank 177 64 226 none
kw testworld use 178 65 228 south immersiveengineering:hammer
execute unless block 178 65 228 immersiveengineering:sheetmetal_iron
setblock 184 64 239 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "124.2"}','{"text": "immersive"}','{"text": "silo"}','{"text": ""}']}}
setblock 185 64 239 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form ein"}','{"text": "Elementsilo"}','{"text": ""}','{"text": ""}']}}
fill 193 64 223 193 82 240 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/silo 187 64 226 none
kw testworld use 188 65 228 south immersiveengineering:hammer
execute unless block 188 65 228 immersiveengineering:sheetmetal_iron
setblock 194 64 239 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "124.3"}','{"text": "immersive"}','{"text": "shelf"}','{"text": ""}']}}
setblock 195 64 239 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form ein"}','{"text": "Kistenregal"}','{"text": ""}','{"text": ""}']}}
fill 203 64 223 203 82 240 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/shelf 196 64 226 none
kw testworld use 197 65 227 south immersiveengineering:hammer
execute unless block 197 65 227 immersiveengineering:steel_catwalk
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
