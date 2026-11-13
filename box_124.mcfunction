# 124 immersive/list_mb
#area 204 211 232 239
fill 204 64 211 232 95 239 minecraft:air
fill 204 60 211 232 62 239 minecraft:stone
fill 204 63 211 232 63 239 minecraft:light_gray_concrete
fill 208 64 217 232 83 217 minecraft:light_gray_concrete
fill 208 64 217 208 83 233 minecraft:light_gray_concrete
setblock 209 64 232 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "124"}','{"text": "immersive"}','{"text": "list_mb"}','{"text": ""}']}}
setblock 210 64 232 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "all seven stage"}','{"text": "2 structures"}','{"text": "side by side"}','{"text": ""}']}}
fill 227 64 217 227 83 233 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/sheetmetal_tank 210 64 219 none
kw testworld use 211 65 221 south immersiveengineering:hammer
execute unless block 211 65 221 immersiveengineering:sheetmetal_iron
place template immersiveengineering:multiblocks/silo 214 64 219 none
kw testworld use 215 65 221 south immersiveengineering:hammer
execute unless block 215 65 221 immersiveengineering:sheetmetal_iron
place template immersiveengineering:multiblocks/improved_blast_furnace 218 64 219 none
kw testworld use 219 65 221 south immersiveengineering:hammer
execute unless block 219 65 221 immersiveengineering:blastbrick_reinforced
place template immersiveengineering:multiblocks/shelf 222 64 219 none
kw testworld use 223 65 220 south immersiveengineering:hammer
execute unless block 223 65 220 immersiveengineering:steel_catwalk
place template immersiveengineering:multiblocks/coke_oven 212 64 225 none
kw testworld use 213 65 227 south immersiveengineering:hammer
execute unless block 213 65 227 immersiveengineering:cokebrick
place template immersiveengineering:multiblocks/blast_furnace 217 64 225 none
kw testworld use 218 65 227 south immersiveengineering:hammer
execute unless block 218 65 227 immersiveengineering:blastbrick
place template immersiveengineering:multiblocks/alloy_smelter 222 64 225 none
kw testworld use 223 65 226 south immersiveengineering:hammer
execute unless block 223 65 226 immersiveengineering:alloybrick
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
