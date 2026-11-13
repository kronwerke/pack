# 061 immersive/list_mb
#area 177 158 205 186
fill 177 64 158 205 95 186 minecraft:air
fill 177 60 158 205 62 186 minecraft:stone
fill 177 63 158 205 63 186 minecraft:light_gray_concrete
fill 181 64 164 205 83 164 minecraft:light_gray_concrete
fill 181 64 164 181 83 180 minecraft:light_gray_concrete
setblock 182 64 179 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "061"}','{"text": "immersive"}','{"text": "list_mb"}','{"text": ""}']}}
setblock 183 64 179 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "all seven stage"}','{"text": "2 structures"}','{"text": "side by side"}','{"text": ""}']}}
fill 200 64 164 200 83 180 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/sheetmetal_tank 183 64 166 none
kw testworld use 184 65 168 south immersiveengineering:hammer
execute unless block 184 65 168 immersiveengineering:sheetmetal_iron
place template immersiveengineering:multiblocks/silo 187 64 166 none
kw testworld use 188 65 168 south immersiveengineering:hammer
execute unless block 188 65 168 immersiveengineering:sheetmetal_iron
place template immersiveengineering:multiblocks/improved_blast_furnace 191 64 166 none
kw testworld use 192 65 168 south immersiveengineering:hammer
execute unless block 192 65 168 immersiveengineering:blastbrick_reinforced
place template immersiveengineering:multiblocks/shelf 195 64 166 none
kw testworld use 196 65 167 south immersiveengineering:hammer
execute unless block 196 65 167 immersiveengineering:steel_catwalk
place template immersiveengineering:multiblocks/coke_oven 185 64 172 none
kw testworld use 186 65 174 south immersiveengineering:hammer
execute unless block 186 65 174 immersiveengineering:cokebrick
place template immersiveengineering:multiblocks/blast_furnace 190 64 172 none
kw testworld use 191 65 174 south immersiveengineering:hammer
execute unless block 191 65 174 immersiveengineering:blastbrick
place template immersiveengineering:multiblocks/alloy_smelter 195 64 172 none
kw testworld use 196 65 173 south immersiveengineering:hammer
execute unless block 196 65 173 immersiveengineering:alloybrick
