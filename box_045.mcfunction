# 045 immersive/blast_furnace, improved_form
#area 26 144 55 170
fill 26 64 144 55 91 170 minecraft:air
fill 26 60 144 55 62 170 minecraft:stone
fill 26 63 144 55 63 170 minecraft:light_gray_concrete
fill 30 64 150 55 79 150 minecraft:light_gray_concrete
fill 30 64 150 30 79 164 minecraft:light_gray_concrete
setblock 31 64 163 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "045.1"}','{"text": "immersive"}','{"text": "blast_furnace"}','{"text": ""}']}}
setblock 32 64 163 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "crude blast"}','{"text": "furnace GUI,"}','{"text": "improved"}','{"text": "furnace with"}']}}
setblock 33 64 163 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "hopper and"}','{"text": "preheaters"}','{"text": ""}','{"text": ""}']}}
fill 40 64 150 40 79 164 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/blast_furnace 34 64 153 none
kw testworld use 35 65 155 south immersiveengineering:hammer
execute unless block 35 65 155 immersiveengineering:blastbrick
setblock 41 64 163 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "045.2"}','{"text": "immersive"}','{"text": "improved_form"}','{"text": ""}']}}
setblock 42 64 163 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Verbesserten"}','{"text": "Hochofen"}','{"text": ""}']}}
fill 50 64 150 50 79 164 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/improved_blast_furnace 44 64 153 none
kw testworld use 45 65 155 south immersiveengineering:hammer
execute unless block 45 65 155 immersiveengineering:blastbrick_reinforced
