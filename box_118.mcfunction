# 118 immersive/blast_furnace, improved_form
#area 26 215 55 241
fill 26 64 215 55 91 241 minecraft:air
fill 26 60 215 55 62 241 minecraft:stone
fill 26 63 215 55 63 241 minecraft:light_gray_concrete
fill 30 64 221 55 79 221 minecraft:light_gray_concrete
fill 30 64 221 30 79 235 minecraft:light_gray_concrete
setblock 31 64 234 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "118.1"}','{"text": "immersive"}','{"text": "blast_furnace"}','{"text": ""}']}}
setblock 32 64 234 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "crude blast"}','{"text": "furnace GUI,"}','{"text": "improved"}','{"text": "furnace with"}']}}
setblock 33 64 234 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "hopper and"}','{"text": "preheaters"}','{"text": ""}','{"text": ""}']}}
fill 40 64 221 40 79 235 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/blast_furnace 34 64 224 none
kw testworld use 35 65 226 south immersiveengineering:hammer
execute unless block 35 65 226 immersiveengineering:blastbrick
setblock 41 64 234 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "118.2"}','{"text": "immersive"}','{"text": "improved_form"}','{"text": ""}']}}
setblock 42 64 234 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Verbesserten"}','{"text": "Hochofen"}','{"text": ""}']}}
fill 50 64 221 50 79 235 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/improved_blast_furnace 44 64 224 none
kw testworld use 45 65 226 south immersiveengineering:hammer
execute unless block 45 65 226 immersiveengineering:blastbrick_reinforced
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
