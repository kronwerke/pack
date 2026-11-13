# 082 immersive/list_mb
#area 163 177 191 205
fill 163 64 177 191 95 205 minecraft:air
fill 163 60 177 191 62 205 minecraft:stone
fill 163 63 177 191 63 205 minecraft:light_gray_concrete
fill 167 64 183 191 83 183 minecraft:light_gray_concrete
fill 167 64 183 167 83 199 minecraft:light_gray_concrete
setblock 168 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "082"}','{"text": "immersive"}','{"text": "list_mb"}','{"text": ""}']}}
setblock 169 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "all seven stage"}','{"text": "2 structures"}','{"text": "side by side"}','{"text": ""}']}}
fill 186 64 183 186 83 199 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/sheetmetal_tank 169 64 185 none
kw testworld use 170 65 187 south immersiveengineering:hammer
execute unless block 170 65 187 immersiveengineering:sheetmetal_iron
place template immersiveengineering:multiblocks/silo 173 64 185 none
kw testworld use 174 65 187 south immersiveengineering:hammer
execute unless block 174 65 187 immersiveengineering:sheetmetal_iron
place template immersiveengineering:multiblocks/improved_blast_furnace 177 64 185 none
kw testworld use 178 65 187 south immersiveengineering:hammer
execute unless block 178 65 187 immersiveengineering:blastbrick_reinforced
place template immersiveengineering:multiblocks/shelf 181 64 185 none
kw testworld use 182 65 186 south immersiveengineering:hammer
execute unless block 182 65 186 immersiveengineering:steel_catwalk
place template immersiveengineering:multiblocks/coke_oven 171 64 191 none
kw testworld use 172 65 193 south immersiveengineering:hammer
execute unless block 172 65 193 immersiveengineering:cokebrick
place template immersiveengineering:multiblocks/blast_furnace 176 64 191 none
kw testworld use 177 65 193 south immersiveengineering:hammer
execute unless block 177 65 193 immersiveengineering:blastbrick
place template immersiveengineering:multiblocks/alloy_smelter 181 64 191 none
kw testworld use 182 65 192 south immersiveengineering:hammer
execute unless block 182 65 192 immersiveengineering:alloybrick
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
