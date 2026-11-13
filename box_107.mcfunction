# 107 immersive/list_mb
#area 204 179 232 207
fill 204 64 179 232 95 207 minecraft:air
fill 204 60 179 232 62 207 minecraft:stone
fill 204 63 179 232 63 207 minecraft:light_gray_concrete
fill 208 64 185 232 83 185 minecraft:light_gray_concrete
fill 208 64 185 208 83 201 minecraft:light_gray_concrete
setblock 209 64 200 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "107"}','{"text": "immersive"}','{"text": "list_mb"}','{"text": ""}']}}
setblock 210 64 200 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "all seven stage"}','{"text": "2 structures"}','{"text": "side by side"}','{"text": ""}']}}
fill 227 64 185 227 83 201 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/sheetmetal_tank 210 64 187 none
kw testworld use 211 65 189 south immersiveengineering:hammer
execute unless block 211 65 189 immersiveengineering:sheetmetal_iron
place template immersiveengineering:multiblocks/silo 214 64 187 none
kw testworld use 215 65 189 south immersiveengineering:hammer
execute unless block 215 65 189 immersiveengineering:sheetmetal_iron
place template immersiveengineering:multiblocks/improved_blast_furnace 218 64 187 none
kw testworld use 219 65 189 south immersiveengineering:hammer
execute unless block 219 65 189 immersiveengineering:blastbrick_reinforced
place template immersiveengineering:multiblocks/shelf 222 64 187 none
kw testworld use 223 65 188 south immersiveengineering:hammer
execute unless block 223 65 188 immersiveengineering:steel_catwalk
place template immersiveengineering:multiblocks/coke_oven 212 64 193 none
kw testworld use 213 65 195 south immersiveengineering:hammer
execute unless block 213 65 195 immersiveengineering:cokebrick
place template immersiveengineering:multiblocks/blast_furnace 217 64 193 none
kw testworld use 218 65 195 south immersiveengineering:hammer
execute unless block 218 65 195 immersiveengineering:blastbrick
place template immersiveengineering:multiblocks/alloy_smelter 222 64 193 none
kw testworld use 223 65 194 south immersiveengineering:hammer
execute unless block 223 65 194 immersiveengineering:alloybrick
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
