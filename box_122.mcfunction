# 122 immersive/blast_furnace, improved_form
#area 51 217 80 243
fill 51 64 217 80 91 243 minecraft:air
fill 51 60 217 80 62 243 minecraft:stone
fill 51 63 217 80 63 243 minecraft:light_gray_concrete
fill 55 64 223 80 79 223 minecraft:light_gray_concrete
fill 55 64 223 55 79 237 minecraft:light_gray_concrete
setblock 56 64 236 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "122.1"}','{"text": "immersive"}','{"text": "blast_furnace"}','{"text": ""}']}}
setblock 57 64 236 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "crude blast"}','{"text": "furnace GUI,"}','{"text": "improved"}','{"text": "furnace with"}']}}
setblock 58 64 236 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "hopper and"}','{"text": "preheaters"}','{"text": ""}','{"text": ""}']}}
fill 65 64 223 65 79 237 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/blast_furnace 59 64 226 none
kw testworld use 60 65 228 south immersiveengineering:hammer
execute unless block 60 65 228 immersiveengineering:blastbrick
setblock 66 64 236 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "122.2"}','{"text": "immersive"}','{"text": "improved_form"}','{"text": ""}']}}
setblock 67 64 236 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Verbesserten"}','{"text": "Hochofen"}','{"text": ""}']}}
fill 75 64 223 75 79 237 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/improved_blast_furnace 69 64 226 none
kw testworld use 70 65 228 south immersiveengineering:hammer
execute unless block 70 65 228 immersiveengineering:blastbrick_reinforced
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
