# 143 immersive/tank, silo, shelf
#area 194 219 233 248
fill 194 64 219 228 94 248 minecraft:air
fill 229 64 219 233 94 248 minecraft:air
fill 194 60 219 233 62 248 minecraft:stone
fill 194 63 219 233 63 248 minecraft:light_gray_concrete
fill 198 64 225 233 82 225 minecraft:light_gray_concrete
fill 198 64 225 198 82 242 minecraft:light_gray_concrete
setblock 199 64 241 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "143.1"}','{"text": "immersive"}','{"text": "tank"}','{"text": ""}']}}
setblock 200 64 241 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the formed"}','{"text": "structures"}','{"text": ""}','{"text": ""}']}}
fill 208 64 225 208 82 242 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/sheetmetal_tank 202 64 228 none
kw testworld use 203 65 230 south immersiveengineering:hammer
execute unless block 203 65 230 immersiveengineering:sheetmetal_iron
setblock 209 64 241 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "143.2"}','{"text": "immersive"}','{"text": "silo"}','{"text": ""}']}}
setblock 210 64 241 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form ein"}','{"text": "Elementsilo"}','{"text": ""}','{"text": ""}']}}
fill 218 64 225 218 82 242 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/silo 212 64 228 none
kw testworld use 213 65 230 south immersiveengineering:hammer
execute unless block 213 65 230 immersiveengineering:sheetmetal_iron
setblock 219 64 241 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "143.3"}','{"text": "immersive"}','{"text": "shelf"}','{"text": ""}']}}
setblock 220 64 241 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form ein"}','{"text": "Kistenregal"}','{"text": ""}','{"text": ""}']}}
fill 228 64 225 228 82 242 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/shelf 221 64 228 none
kw testworld use 222 65 229 south immersiveengineering:hammer
execute unless block 222 65 229 immersiveengineering:steel_catwalk
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
