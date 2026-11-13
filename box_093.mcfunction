# 093 immersive/list_mb
#area 194 179 222 207
fill 194 64 179 222 95 207 minecraft:air
fill 194 60 179 222 62 207 minecraft:stone
fill 194 63 179 222 63 207 minecraft:light_gray_concrete
fill 198 64 185 222 83 185 minecraft:light_gray_concrete
fill 198 64 185 198 83 201 minecraft:light_gray_concrete
setblock 199 64 200 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "093"}','{"text": "immersive"}','{"text": "list_mb"}','{"text": ""}']}}
setblock 200 64 200 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "all seven stage"}','{"text": "2 structures"}','{"text": "side by side"}','{"text": ""}']}}
fill 217 64 185 217 83 201 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/sheetmetal_tank 200 64 187 none
kw testworld use 201 65 189 south immersiveengineering:hammer
execute unless block 201 65 189 immersiveengineering:sheetmetal_iron
place template immersiveengineering:multiblocks/silo 204 64 187 none
kw testworld use 205 65 189 south immersiveengineering:hammer
execute unless block 205 65 189 immersiveengineering:sheetmetal_iron
place template immersiveengineering:multiblocks/improved_blast_furnace 208 64 187 none
kw testworld use 209 65 189 south immersiveengineering:hammer
execute unless block 209 65 189 immersiveengineering:blastbrick_reinforced
place template immersiveengineering:multiblocks/shelf 212 64 187 none
kw testworld use 213 65 188 south immersiveengineering:hammer
execute unless block 213 65 188 immersiveengineering:steel_catwalk
place template immersiveengineering:multiblocks/coke_oven 202 64 193 none
kw testworld use 203 65 195 south immersiveengineering:hammer
execute unless block 203 65 195 immersiveengineering:cokebrick
place template immersiveengineering:multiblocks/blast_furnace 207 64 193 none
kw testworld use 208 65 195 south immersiveengineering:hammer
execute unless block 208 65 195 immersiveengineering:blastbrick
place template immersiveengineering:multiblocks/alloy_smelter 212 64 193 none
kw testworld use 213 65 194 south immersiveengineering:hammer
execute unless block 213 65 194 immersiveengineering:alloybrick
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
