# 128 immersive/tank, silo, shelf
#area 194 217 233 246
fill 194 64 217 228 94 246 minecraft:air
fill 229 64 217 233 94 246 minecraft:air
fill 194 60 217 233 62 246 minecraft:stone
fill 194 63 217 233 63 246 minecraft:light_gray_concrete
fill 198 64 223 233 82 223 minecraft:light_gray_concrete
fill 198 64 223 198 82 240 minecraft:light_gray_concrete
setblock 199 64 239 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "128.1"}','{"text": "immersive"}','{"text": "tank"}','{"text": ""}']}}
setblock 200 64 239 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the formed"}','{"text": "structures"}','{"text": ""}','{"text": ""}']}}
fill 208 64 223 208 82 240 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/sheetmetal_tank 202 64 226 none
kw testworld use 203 65 228 south immersiveengineering:hammer
execute unless block 203 65 228 immersiveengineering:sheetmetal_iron
setblock 209 64 239 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "128.2"}','{"text": "immersive"}','{"text": "silo"}','{"text": ""}']}}
setblock 210 64 239 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form ein"}','{"text": "Elementsilo"}','{"text": ""}','{"text": ""}']}}
fill 218 64 223 218 82 240 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/silo 212 64 226 none
kw testworld use 213 65 228 south immersiveengineering:hammer
execute unless block 213 65 228 immersiveengineering:sheetmetal_iron
setblock 219 64 239 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "128.3"}','{"text": "immersive"}','{"text": "shelf"}','{"text": ""}']}}
setblock 220 64 239 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form ein"}','{"text": "Kistenregal"}','{"text": ""}','{"text": ""}']}}
fill 228 64 223 228 82 240 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/shelf 221 64 226 none
kw testworld use 222 65 227 south immersiveengineering:hammer
execute unless block 222 65 227 immersiveengineering:steel_catwalk
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
