# 071 immersive/blast_furnace, improved_form
#area 26 177 55 203
fill 26 64 177 55 91 203 minecraft:air
fill 26 60 177 55 62 203 minecraft:stone
fill 26 63 177 55 63 203 minecraft:light_gray_concrete
fill 30 64 183 55 79 183 minecraft:light_gray_concrete
fill 30 64 183 30 79 197 minecraft:light_gray_concrete
setblock 31 64 196 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "071.1"}','{"text": "immersive"}','{"text": "blast_furnace"}','{"text": ""}']}}
setblock 32 64 196 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "crude blast"}','{"text": "furnace GUI,"}','{"text": "improved"}','{"text": "furnace with"}']}}
setblock 33 64 196 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "hopper and"}','{"text": "preheaters"}','{"text": ""}','{"text": ""}']}}
fill 40 64 183 40 79 197 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/blast_furnace 34 64 186 none
kw testworld use 35 65 188 south immersiveengineering:hammer
execute unless block 35 65 188 immersiveengineering:blastbrick
setblock 41 64 196 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "071.2"}','{"text": "immersive"}','{"text": "improved_form"}','{"text": ""}']}}
setblock 42 64 196 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Verbesserten"}','{"text": "Hochofen"}','{"text": ""}']}}
fill 50 64 183 50 79 197 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/improved_blast_furnace 44 64 186 none
kw testworld use 45 65 188 south immersiveengineering:hammer
execute unless block 45 65 188 immersiveengineering:blastbrick_reinforced
