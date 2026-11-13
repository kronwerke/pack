# 144 immersive/list_mb
#area 229 219 257 247
fill 229 64 219 257 95 247 minecraft:air
fill 229 60 219 257 62 247 minecraft:stone
fill 229 63 219 257 63 247 minecraft:light_gray_concrete
fill 233 64 225 257 83 225 minecraft:light_gray_concrete
fill 233 64 225 233 83 241 minecraft:light_gray_concrete
setblock 234 64 240 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "144"}','{"text": "immersive"}','{"text": "list_mb"}','{"text": ""}']}}
setblock 235 64 240 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "all seven stage"}','{"text": "2 structures"}','{"text": "side by side"}','{"text": ""}']}}
fill 252 64 225 252 83 241 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/sheetmetal_tank 235 64 227 none
kw testworld use 236 65 229 south immersiveengineering:hammer
execute unless block 236 65 229 immersiveengineering:sheetmetal_iron
place template immersiveengineering:multiblocks/silo 239 64 227 none
kw testworld use 240 65 229 south immersiveengineering:hammer
execute unless block 240 65 229 immersiveengineering:sheetmetal_iron
place template immersiveengineering:multiblocks/improved_blast_furnace 243 64 227 none
kw testworld use 244 65 229 south immersiveengineering:hammer
execute unless block 244 65 229 immersiveengineering:blastbrick_reinforced
place template immersiveengineering:multiblocks/shelf 247 64 227 none
kw testworld use 248 65 228 south immersiveengineering:hammer
execute unless block 248 65 228 immersiveengineering:steel_catwalk
place template immersiveengineering:multiblocks/coke_oven 237 64 233 none
kw testworld use 238 65 235 south immersiveengineering:hammer
execute unless block 238 65 235 immersiveengineering:cokebrick
place template immersiveengineering:multiblocks/blast_furnace 242 64 233 none
kw testworld use 243 65 235 south immersiveengineering:hammer
execute unless block 243 65 235 immersiveengineering:blastbrick
place template immersiveengineering:multiblocks/alloy_smelter 247 64 233 none
kw testworld use 248 65 234 south immersiveengineering:hammer
execute unless block 248 65 234 immersiveengineering:alloybrick
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
