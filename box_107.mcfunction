# 107 immersive/blast_furnace, improved_form
#area 26 181 55 207
fill 26 64 181 55 91 207 minecraft:air
fill 26 60 181 55 62 207 minecraft:stone
fill 26 63 181 55 63 207 minecraft:light_gray_concrete
fill 30 64 187 55 79 187 minecraft:light_gray_concrete
fill 30 64 187 30 79 201 minecraft:light_gray_concrete
setblock 31 64 200 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "107.1"}','{"text": "immersive"}','{"text": "blast_furnace"}','{"text": ""}']}}
setblock 32 64 200 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "crude blast"}','{"text": "furnace GUI,"}','{"text": "improved"}','{"text": "furnace with"}']}}
setblock 33 64 200 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "hopper and"}','{"text": "preheaters"}','{"text": ""}','{"text": ""}']}}
fill 40 64 187 40 79 201 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/blast_furnace 34 64 190 none
kw testworld use 35 65 192 south immersiveengineering:hammer
execute unless block 35 65 192 immersiveengineering:blastbrick
setblock 41 64 200 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "107.2"}','{"text": "immersive"}','{"text": "improved_form"}','{"text": ""}']}}
setblock 42 64 200 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Verbesserten"}','{"text": "Hochofen"}','{"text": ""}']}}
fill 50 64 187 50 79 201 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/improved_blast_furnace 44 64 190 none
kw testworld use 45 65 192 south immersiveengineering:hammer
execute unless block 45 65 192 immersiveengineering:blastbrick_reinforced
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
