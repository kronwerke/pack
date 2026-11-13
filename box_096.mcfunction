# 096 immersive/tank, silo, shelf
#area 159 179 198 208
fill 159 64 179 193 94 208 minecraft:air
fill 194 64 179 198 94 208 minecraft:air
fill 159 60 179 198 62 208 minecraft:stone
fill 159 63 179 198 63 208 minecraft:light_gray_concrete
fill 163 64 185 198 82 185 minecraft:light_gray_concrete
fill 163 64 185 163 82 202 minecraft:light_gray_concrete
setblock 164 64 201 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "096.1"}','{"text": "immersive"}','{"text": "tank"}','{"text": ""}']}}
setblock 165 64 201 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the formed"}','{"text": "structures"}','{"text": ""}','{"text": ""}']}}
fill 173 64 185 173 82 202 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/sheetmetal_tank 167 64 188 none
kw testworld use 168 65 190 south immersiveengineering:hammer
execute unless block 168 65 190 immersiveengineering:sheetmetal_iron
setblock 174 64 201 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "096.2"}','{"text": "immersive"}','{"text": "silo"}','{"text": ""}']}}
setblock 175 64 201 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form ein"}','{"text": "Elementsilo"}','{"text": ""}','{"text": ""}']}}
fill 183 64 185 183 82 202 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/silo 177 64 188 none
kw testworld use 178 65 190 south immersiveengineering:hammer
execute unless block 178 65 190 immersiveengineering:sheetmetal_iron
setblock 184 64 201 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "096.3"}','{"text": "immersive"}','{"text": "shelf"}','{"text": ""}']}}
setblock 185 64 201 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form ein"}','{"text": "Kistenregal"}','{"text": ""}','{"text": ""}']}}
fill 193 64 185 193 82 202 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/shelf 186 64 188 none
kw testworld use 187 65 189 south immersiveengineering:hammer
execute unless block 187 65 189 immersiveengineering:steel_catwalk
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
