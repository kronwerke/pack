# 077 immersive/list_mb
#area 191 177 219 205
fill 191 64 177 219 95 205 minecraft:air
fill 191 60 177 219 62 205 minecraft:stone
fill 191 63 177 219 63 205 minecraft:light_gray_concrete
fill 195 64 183 219 83 183 minecraft:light_gray_concrete
fill 195 64 183 195 83 199 minecraft:light_gray_concrete
setblock 196 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "077"}','{"text": "immersive"}','{"text": "list_mb"}','{"text": ""}']}}
setblock 197 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "all seven stage"}','{"text": "2 structures"}','{"text": "side by side"}','{"text": ""}']}}
fill 214 64 183 214 83 199 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/sheetmetal_tank 197 64 185 none
kw testworld use 198 65 187 south immersiveengineering:hammer
execute unless block 198 65 187 immersiveengineering:sheetmetal_iron
place template immersiveengineering:multiblocks/silo 201 64 185 none
kw testworld use 202 65 187 south immersiveengineering:hammer
execute unless block 202 65 187 immersiveengineering:sheetmetal_iron
place template immersiveengineering:multiblocks/improved_blast_furnace 205 64 185 none
kw testworld use 206 65 187 south immersiveengineering:hammer
execute unless block 206 65 187 immersiveengineering:blastbrick_reinforced
place template immersiveengineering:multiblocks/shelf 209 64 185 none
kw testworld use 210 65 186 south immersiveengineering:hammer
execute unless block 210 65 186 immersiveengineering:steel_catwalk
place template immersiveengineering:multiblocks/coke_oven 199 64 191 none
kw testworld use 200 65 193 south immersiveengineering:hammer
execute unless block 200 65 193 immersiveengineering:cokebrick
place template immersiveengineering:multiblocks/blast_furnace 204 64 191 none
kw testworld use 205 65 193 south immersiveengineering:hammer
execute unless block 205 65 193 immersiveengineering:blastbrick
place template immersiveengineering:multiblocks/alloy_smelter 209 64 191 none
kw testworld use 210 65 192 south immersiveengineering:hammer
execute unless block 210 65 192 immersiveengineering:alloybrick
