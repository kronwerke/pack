# 100 immersive/blast_furnace, improved_form
#area 26 179 55 205
fill 26 64 179 55 91 205 minecraft:air
fill 26 60 179 55 62 205 minecraft:stone
fill 26 63 179 55 63 205 minecraft:light_gray_concrete
fill 30 64 185 55 79 185 minecraft:light_gray_concrete
fill 30 64 185 30 79 199 minecraft:light_gray_concrete
setblock 31 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "100.1"}','{"text": "immersive"}','{"text": "blast_furnace"}','{"text": ""}']}}
setblock 32 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "crude blast"}','{"text": "furnace GUI,"}','{"text": "improved"}','{"text": "furnace with"}']}}
setblock 33 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "hopper and"}','{"text": "preheaters"}','{"text": ""}','{"text": ""}']}}
fill 40 64 185 40 79 199 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/blast_furnace 34 64 188 none
kw testworld use 35 65 190 south immersiveengineering:hammer
execute unless block 35 65 190 immersiveengineering:blastbrick
setblock 41 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "100.2"}','{"text": "immersive"}','{"text": "improved_form"}','{"text": ""}']}}
setblock 42 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Verbesserten"}','{"text": "Hochofen"}','{"text": ""}']}}
fill 50 64 185 50 79 199 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/improved_blast_furnace 44 64 188 none
kw testworld use 45 65 190 south immersiveengineering:hammer
execute unless block 45 65 190 immersiveengineering:blastbrick_reinforced
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
