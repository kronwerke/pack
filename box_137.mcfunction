# 137 immersive/blast_furnace, improved_form
#area 51 219 80 245
fill 51 64 219 80 91 245 minecraft:air
fill 51 60 219 80 62 245 minecraft:stone
fill 51 63 219 80 63 245 minecraft:light_gray_concrete
fill 55 64 225 80 79 225 minecraft:light_gray_concrete
fill 55 64 225 55 79 239 minecraft:light_gray_concrete
setblock 56 64 238 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "137.1"}','{"text": "immersive"}','{"text": "blast_furnace"}','{"text": ""}']}}
setblock 57 64 238 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "crude blast"}','{"text": "furnace GUI,"}','{"text": "improved"}','{"text": "furnace with"}']}}
setblock 58 64 238 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "hopper and"}','{"text": "preheaters"}','{"text": ""}','{"text": ""}']}}
fill 65 64 225 65 79 239 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/blast_furnace 59 64 228 none
kw testworld use 60 65 230 south immersiveengineering:hammer
execute unless block 60 65 230 immersiveengineering:blastbrick
setblock 66 64 238 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "137.2"}','{"text": "immersive"}','{"text": "improved_form"}','{"text": ""}']}}
setblock 67 64 238 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Verbesserten"}','{"text": "Hochofen"}','{"text": ""}']}}
fill 75 64 225 75 79 239 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/improved_blast_furnace 69 64 228 none
kw testworld use 70 65 230 south immersiveengineering:hammer
execute unless block 70 65 230 immersiveengineering:blastbrick_reinforced
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
