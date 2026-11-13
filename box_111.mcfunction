# 111 immersive/list_mb
#area 204 181 232 209
fill 204 64 181 232 95 209 minecraft:air
fill 204 60 181 232 62 209 minecraft:stone
fill 204 63 181 232 63 209 minecraft:light_gray_concrete
fill 208 64 187 232 83 187 minecraft:light_gray_concrete
fill 208 64 187 208 83 203 minecraft:light_gray_concrete
setblock 209 64 202 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "111"}','{"text": "immersive"}','{"text": "list_mb"}','{"text": ""}']}}
setblock 210 64 202 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "all seven stage"}','{"text": "2 structures"}','{"text": "side by side"}','{"text": ""}']}}
fill 227 64 187 227 83 203 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/sheetmetal_tank 210 64 189 none
kw testworld use 211 65 191 south immersiveengineering:hammer
execute unless block 211 65 191 immersiveengineering:sheetmetal_iron
place template immersiveengineering:multiblocks/silo 214 64 189 none
kw testworld use 215 65 191 south immersiveengineering:hammer
execute unless block 215 65 191 immersiveengineering:sheetmetal_iron
place template immersiveengineering:multiblocks/improved_blast_furnace 218 64 189 none
kw testworld use 219 65 191 south immersiveengineering:hammer
execute unless block 219 65 191 immersiveengineering:blastbrick_reinforced
place template immersiveengineering:multiblocks/shelf 222 64 189 none
kw testworld use 223 65 190 south immersiveengineering:hammer
execute unless block 223 65 190 immersiveengineering:steel_catwalk
place template immersiveengineering:multiblocks/coke_oven 212 64 195 none
kw testworld use 213 65 197 south immersiveengineering:hammer
execute unless block 213 65 197 immersiveengineering:cokebrick
place template immersiveengineering:multiblocks/blast_furnace 217 64 195 none
kw testworld use 218 65 197 south immersiveengineering:hammer
execute unless block 218 65 197 immersiveengineering:blastbrick
place template immersiveengineering:multiblocks/alloy_smelter 222 64 195 none
kw testworld use 223 65 196 south immersiveengineering:hammer
execute unless block 223 65 196 immersiveengineering:alloybrick
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
