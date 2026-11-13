# 073 immersive/list_mb
#area 191 158 219 186
fill 191 64 158 219 95 186 minecraft:air
fill 191 60 158 219 62 186 minecraft:stone
fill 191 63 158 219 63 186 minecraft:light_gray_concrete
fill 195 64 164 219 83 164 minecraft:light_gray_concrete
fill 195 64 164 195 83 180 minecraft:light_gray_concrete
setblock 196 64 179 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "073"}','{"text": "immersive"}','{"text": "list_mb"}','{"text": ""}']}}
setblock 197 64 179 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "all seven stage"}','{"text": "2 structures"}','{"text": "side by side"}','{"text": ""}']}}
fill 214 64 164 214 83 180 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/sheetmetal_tank 197 64 166 none
kw testworld use 198 65 168 south immersiveengineering:hammer
execute unless block 198 65 168 immersiveengineering:sheetmetal_iron
place template immersiveengineering:multiblocks/silo 201 64 166 none
kw testworld use 202 65 168 south immersiveengineering:hammer
execute unless block 202 65 168 immersiveengineering:sheetmetal_iron
place template immersiveengineering:multiblocks/improved_blast_furnace 205 64 166 none
kw testworld use 206 65 168 south immersiveengineering:hammer
execute unless block 206 65 168 immersiveengineering:blastbrick_reinforced
place template immersiveengineering:multiblocks/shelf 209 64 166 none
kw testworld use 210 65 167 south immersiveengineering:hammer
execute unless block 210 65 167 immersiveengineering:steel_catwalk
place template immersiveengineering:multiblocks/coke_oven 199 64 172 none
kw testworld use 200 65 174 south immersiveengineering:hammer
execute unless block 200 65 174 immersiveengineering:cokebrick
place template immersiveengineering:multiblocks/blast_furnace 204 64 172 none
kw testworld use 205 65 174 south immersiveengineering:hammer
execute unless block 205 65 174 immersiveengineering:blastbrick
place template immersiveengineering:multiblocks/alloy_smelter 209 64 172 none
kw testworld use 210 65 173 south immersiveengineering:hammer
execute unless block 210 65 173 immersiveengineering:alloybrick
