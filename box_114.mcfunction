# 114 immersive/blast_furnace, improved_form
#area 26 211 55 237
fill 26 64 211 55 91 237 minecraft:air
fill 26 60 211 55 62 237 minecraft:stone
fill 26 63 211 55 63 237 minecraft:light_gray_concrete
fill 30 64 217 55 79 217 minecraft:light_gray_concrete
fill 30 64 217 30 79 231 minecraft:light_gray_concrete
setblock 31 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "114.1"}','{"text": "immersive"}','{"text": "blast_furnace"}','{"text": ""}']}}
setblock 32 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "crude blast"}','{"text": "furnace GUI,"}','{"text": "improved"}','{"text": "furnace with"}']}}
setblock 33 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "hopper and"}','{"text": "preheaters"}','{"text": ""}','{"text": ""}']}}
fill 40 64 217 40 79 231 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/blast_furnace 34 64 220 none
kw testworld use 35 65 222 south immersiveengineering:hammer
execute unless block 35 65 222 immersiveengineering:blastbrick
setblock 41 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "114.2"}','{"text": "immersive"}','{"text": "improved_form"}','{"text": ""}']}}
setblock 42 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Verbesserten"}','{"text": "Hochofen"}','{"text": ""}']}}
fill 50 64 217 50 79 231 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/improved_blast_furnace 44 64 220 none
kw testworld use 45 65 222 south immersiveengineering:hammer
execute unless block 45 65 222 immersiveengineering:blastbrick_reinforced
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
