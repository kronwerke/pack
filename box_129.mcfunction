# 129 immersive/list_mb
#area 229 217 257 245
fill 229 64 217 257 95 245 minecraft:air
fill 229 60 217 257 62 245 minecraft:stone
fill 229 63 217 257 63 245 minecraft:light_gray_concrete
fill 233 64 223 257 83 223 minecraft:light_gray_concrete
fill 233 64 223 233 83 239 minecraft:light_gray_concrete
setblock 234 64 238 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "129"}','{"text": "immersive"}','{"text": "list_mb"}','{"text": ""}']}}
setblock 235 64 238 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "all seven stage"}','{"text": "2 structures"}','{"text": "side by side"}','{"text": ""}']}}
fill 252 64 223 252 83 239 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/sheetmetal_tank 235 64 225 none
kw testworld use 236 65 227 south immersiveengineering:hammer
execute unless block 236 65 227 immersiveengineering:sheetmetal_iron
place template immersiveengineering:multiblocks/silo 239 64 225 none
kw testworld use 240 65 227 south immersiveengineering:hammer
execute unless block 240 65 227 immersiveengineering:sheetmetal_iron
place template immersiveengineering:multiblocks/improved_blast_furnace 243 64 225 none
kw testworld use 244 65 227 south immersiveengineering:hammer
execute unless block 244 65 227 immersiveengineering:blastbrick_reinforced
place template immersiveengineering:multiblocks/shelf 247 64 225 none
kw testworld use 248 65 226 south immersiveengineering:hammer
execute unless block 248 65 226 immersiveengineering:steel_catwalk
place template immersiveengineering:multiblocks/coke_oven 237 64 231 none
kw testworld use 238 65 233 south immersiveengineering:hammer
execute unless block 238 65 233 immersiveengineering:cokebrick
place template immersiveengineering:multiblocks/blast_furnace 242 64 231 none
kw testworld use 243 65 233 south immersiveengineering:hammer
execute unless block 243 65 233 immersiveengineering:blastbrick
place template immersiveengineering:multiblocks/alloy_smelter 247 64 231 none
kw testworld use 248 65 232 south immersiveengineering:hammer
execute unless block 248 65 232 immersiveengineering:alloybrick
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
