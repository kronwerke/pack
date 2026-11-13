# 066 immersive/blast_furnace, improved_form
#area 26 158 55 184
fill 26 64 158 55 91 184 minecraft:air
fill 26 60 158 55 62 184 minecraft:stone
fill 26 63 158 55 63 184 minecraft:light_gray_concrete
fill 30 64 164 55 79 164 minecraft:light_gray_concrete
fill 30 64 164 30 79 178 minecraft:light_gray_concrete
setblock 31 64 177 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "066.1"}','{"text": "immersive"}','{"text": "blast_furnace"}','{"text": ""}']}}
setblock 32 64 177 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "crude blast"}','{"text": "furnace GUI,"}','{"text": "improved"}','{"text": "furnace with"}']}}
setblock 33 64 177 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "hopper and"}','{"text": "preheaters"}','{"text": ""}','{"text": ""}']}}
fill 40 64 164 40 79 178 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/blast_furnace 34 64 167 none
kw testworld use 35 65 169 south immersiveengineering:hammer
execute unless block 35 65 169 immersiveengineering:blastbrick
setblock 41 64 177 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "066.2"}','{"text": "immersive"}','{"text": "improved_form"}','{"text": ""}']}}
setblock 42 64 177 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Verbesserten"}','{"text": "Hochofen"}','{"text": ""}']}}
fill 50 64 164 50 79 178 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/improved_blast_furnace 44 64 167 none
kw testworld use 45 65 169 south immersiveengineering:hammer
execute unless block 45 65 169 immersiveengineering:blastbrick_reinforced
