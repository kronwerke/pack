# 118 immersive/blast_furnace, improved_form
#area 26 217 55 243
fill 26 64 217 55 91 243 minecraft:air
fill 26 60 217 55 62 243 minecraft:stone
fill 26 63 217 55 63 243 minecraft:light_gray_concrete
fill 30 64 223 55 79 223 minecraft:light_gray_concrete
fill 30 64 223 30 79 237 minecraft:light_gray_concrete
setblock 31 64 236 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "118.1"}','{"text": "immersive"}','{"text": "blast_furnace"}','{"text": ""}']}}
setblock 32 64 236 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "crude blast"}','{"text": "furnace GUI,"}','{"text": "improved"}','{"text": "furnace with"}']}}
setblock 33 64 236 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "hopper and"}','{"text": "preheaters"}','{"text": ""}','{"text": ""}']}}
fill 40 64 223 40 79 237 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/blast_furnace 34 64 226 none
kw testworld use 35 65 228 south immersiveengineering:hammer
execute unless block 35 65 228 immersiveengineering:blastbrick
setblock 41 64 236 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "118.2"}','{"text": "immersive"}','{"text": "improved_form"}','{"text": ""}']}}
setblock 42 64 236 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Verbesserten"}','{"text": "Hochofen"}','{"text": ""}']}}
fill 50 64 223 50 79 237 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/improved_blast_furnace 44 64 226 none
kw testworld use 45 65 228 south immersiveengineering:hammer
execute unless block 45 65 228 immersiveengineering:blastbrick_reinforced
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
