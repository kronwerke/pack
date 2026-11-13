# 125 immersive/list_mb
#area 204 215 232 243
fill 204 64 215 232 95 243 minecraft:air
fill 204 60 215 232 62 243 minecraft:stone
fill 204 63 215 232 63 243 minecraft:light_gray_concrete
fill 208 64 221 232 83 221 minecraft:light_gray_concrete
fill 208 64 221 208 83 237 minecraft:light_gray_concrete
setblock 209 64 236 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "125"}','{"text": "immersive"}','{"text": "list_mb"}','{"text": ""}']}}
setblock 210 64 236 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "all seven stage"}','{"text": "2 structures"}','{"text": "side by side"}','{"text": ""}']}}
fill 227 64 221 227 83 237 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/sheetmetal_tank 210 64 223 none
kw testworld use 211 65 225 south immersiveengineering:hammer
execute unless block 211 65 225 immersiveengineering:sheetmetal_iron
place template immersiveengineering:multiblocks/silo 214 64 223 none
kw testworld use 215 65 225 south immersiveengineering:hammer
execute unless block 215 65 225 immersiveengineering:sheetmetal_iron
place template immersiveengineering:multiblocks/improved_blast_furnace 218 64 223 none
kw testworld use 219 65 225 south immersiveengineering:hammer
execute unless block 219 65 225 immersiveengineering:blastbrick_reinforced
place template immersiveengineering:multiblocks/shelf 222 64 223 none
kw testworld use 223 65 224 south immersiveengineering:hammer
execute unless block 223 65 224 immersiveengineering:steel_catwalk
place template immersiveengineering:multiblocks/coke_oven 212 64 229 none
kw testworld use 213 65 231 south immersiveengineering:hammer
execute unless block 213 65 231 immersiveengineering:cokebrick
place template immersiveengineering:multiblocks/blast_furnace 217 64 229 none
kw testworld use 218 65 231 south immersiveengineering:hammer
execute unless block 218 65 231 immersiveengineering:blastbrick
place template immersiveengineering:multiblocks/alloy_smelter 222 64 229 none
kw testworld use 223 65 230 south immersiveengineering:hammer
execute unless block 223 65 230 immersiveengineering:alloybrick
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
