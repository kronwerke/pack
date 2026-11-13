# 120 immersive/tank, silo, shelf
#area 169 211 208 240
fill 169 64 211 203 94 240 minecraft:air
fill 204 64 211 208 94 240 minecraft:air
fill 169 60 211 208 62 240 minecraft:stone
fill 169 63 211 208 63 240 minecraft:light_gray_concrete
fill 173 64 217 208 82 217 minecraft:light_gray_concrete
fill 173 64 217 173 82 234 minecraft:light_gray_concrete
setblock 174 64 233 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "120.1"}','{"text": "immersive"}','{"text": "tank"}','{"text": ""}']}}
setblock 175 64 233 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the formed"}','{"text": "structures"}','{"text": ""}','{"text": ""}']}}
fill 183 64 217 183 82 234 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/sheetmetal_tank 177 64 220 none
kw testworld use 178 65 222 south immersiveengineering:hammer
execute unless block 178 65 222 immersiveengineering:sheetmetal_iron
setblock 184 64 233 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "120.2"}','{"text": "immersive"}','{"text": "silo"}','{"text": ""}']}}
setblock 185 64 233 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form ein"}','{"text": "Elementsilo"}','{"text": ""}','{"text": ""}']}}
fill 193 64 217 193 82 234 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/silo 187 64 220 none
kw testworld use 188 65 222 south immersiveengineering:hammer
execute unless block 188 65 222 immersiveengineering:sheetmetal_iron
setblock 194 64 233 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "120.3"}','{"text": "immersive"}','{"text": "shelf"}','{"text": ""}']}}
setblock 195 64 233 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form ein"}','{"text": "Kistenregal"}','{"text": ""}','{"text": ""}']}}
fill 203 64 217 203 82 234 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/shelf 196 64 220 none
kw testworld use 197 65 221 south immersiveengineering:hammer
execute unless block 197 65 221 immersiveengineering:steel_catwalk
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
