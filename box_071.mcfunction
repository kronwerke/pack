# 071 immersive/list_mb
#area 189 158 217 186
fill 189 64 158 217 95 186 minecraft:air
fill 189 60 158 217 62 186 minecraft:stone
fill 189 63 158 217 63 186 minecraft:light_gray_concrete
fill 193 64 164 217 83 164 minecraft:light_gray_concrete
fill 193 64 164 193 83 180 minecraft:light_gray_concrete
setblock 194 64 179 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "071"}','{"text": "immersive"}','{"text": "list_mb"}','{"text": ""}']}}
setblock 195 64 179 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "all seven stage"}','{"text": "2 structures"}','{"text": "side by side"}','{"text": ""}']}}
fill 212 64 164 212 83 180 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/sheetmetal_tank 195 64 166 none
kw testworld use 196 65 168 south immersiveengineering:hammer
execute unless block 196 65 168 immersiveengineering:sheetmetal_iron
place template immersiveengineering:multiblocks/silo 199 64 166 none
kw testworld use 200 65 168 south immersiveengineering:hammer
execute unless block 200 65 168 immersiveengineering:sheetmetal_iron
place template immersiveengineering:multiblocks/improved_blast_furnace 203 64 166 none
kw testworld use 204 65 168 south immersiveengineering:hammer
execute unless block 204 65 168 immersiveengineering:blastbrick_reinforced
place template immersiveengineering:multiblocks/shelf 207 64 166 none
kw testworld use 208 65 167 south immersiveengineering:hammer
execute unless block 208 65 167 immersiveengineering:steel_catwalk
place template immersiveengineering:multiblocks/coke_oven 197 64 172 none
kw testworld use 198 65 174 south immersiveengineering:hammer
execute unless block 198 65 174 immersiveengineering:cokebrick
place template immersiveengineering:multiblocks/blast_furnace 202 64 172 none
kw testworld use 203 65 174 south immersiveengineering:hammer
execute unless block 203 65 174 immersiveengineering:blastbrick
place template immersiveengineering:multiblocks/alloy_smelter 207 64 172 none
kw testworld use 208 65 173 south immersiveengineering:hammer
execute unless block 208 65 173 immersiveengineering:alloybrick
