# 108 immersive/tank, silo, shelf
#area 169 179 208 208
fill 169 64 179 203 94 208 minecraft:air
fill 204 64 179 208 94 208 minecraft:air
fill 169 60 179 208 62 208 minecraft:stone
fill 169 63 179 208 63 208 minecraft:light_gray_concrete
fill 173 64 185 208 82 185 minecraft:light_gray_concrete
fill 173 64 185 173 82 202 minecraft:light_gray_concrete
setblock 174 64 201 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "108.1"}','{"text": "immersive"}','{"text": "tank"}','{"text": ""}']}}
setblock 175 64 201 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the formed"}','{"text": "structures"}','{"text": ""}','{"text": ""}']}}
fill 183 64 185 183 82 202 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/sheetmetal_tank 177 64 188 none
kw testworld use 178 65 190 south immersiveengineering:hammer
execute unless block 178 65 190 immersiveengineering:sheetmetal_iron
setblock 184 64 201 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "108.2"}','{"text": "immersive"}','{"text": "silo"}','{"text": ""}']}}
setblock 185 64 201 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form ein"}','{"text": "Elementsilo"}','{"text": ""}','{"text": ""}']}}
fill 193 64 185 193 82 202 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/silo 187 64 188 none
kw testworld use 188 65 190 south immersiveengineering:hammer
execute unless block 188 65 190 immersiveengineering:sheetmetal_iron
setblock 194 64 201 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "108.3"}','{"text": "immersive"}','{"text": "shelf"}','{"text": ""}']}}
setblock 195 64 201 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form ein"}','{"text": "Kistenregal"}','{"text": ""}','{"text": ""}']}}
fill 203 64 185 203 82 202 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/shelf 196 64 188 none
kw testworld use 197 65 189 south immersiveengineering:hammer
execute unless block 197 65 189 immersiveengineering:steel_catwalk
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
