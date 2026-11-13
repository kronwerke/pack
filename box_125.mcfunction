# 125 immersive/list_mb
#area 204 217 232 245
fill 204 64 217 232 95 245 minecraft:air
fill 204 60 217 232 62 245 minecraft:stone
fill 204 63 217 232 63 245 minecraft:light_gray_concrete
fill 208 64 223 232 83 223 minecraft:light_gray_concrete
fill 208 64 223 208 83 239 minecraft:light_gray_concrete
setblock 209 64 238 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "125"}','{"text": "immersive"}','{"text": "list_mb"}','{"text": ""}']}}
setblock 210 64 238 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "all seven stage"}','{"text": "2 structures"}','{"text": "side by side"}','{"text": ""}']}}
fill 227 64 223 227 83 239 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/sheetmetal_tank 210 64 225 none
kw testworld use 211 65 227 south immersiveengineering:hammer
execute unless block 211 65 227 immersiveengineering:sheetmetal_iron
place template immersiveengineering:multiblocks/silo 214 64 225 none
kw testworld use 215 65 227 south immersiveengineering:hammer
execute unless block 215 65 227 immersiveengineering:sheetmetal_iron
place template immersiveengineering:multiblocks/improved_blast_furnace 218 64 225 none
kw testworld use 219 65 227 south immersiveengineering:hammer
execute unless block 219 65 227 immersiveengineering:blastbrick_reinforced
place template immersiveengineering:multiblocks/shelf 222 64 225 none
kw testworld use 223 65 226 south immersiveengineering:hammer
execute unless block 223 65 226 immersiveengineering:steel_catwalk
place template immersiveengineering:multiblocks/coke_oven 212 64 231 none
kw testworld use 213 65 233 south immersiveengineering:hammer
execute unless block 213 65 233 immersiveengineering:cokebrick
place template immersiveengineering:multiblocks/blast_furnace 217 64 231 none
kw testworld use 218 65 233 south immersiveengineering:hammer
execute unless block 218 65 233 immersiveengineering:blastbrick
place template immersiveengineering:multiblocks/alloy_smelter 222 64 231 none
kw testworld use 223 65 232 south immersiveengineering:hammer
execute unless block 223 65 232 immersiveengineering:alloybrick
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
