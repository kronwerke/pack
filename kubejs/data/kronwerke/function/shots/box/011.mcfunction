# 011 farms/wood_saw
fill 17 63 27 30 63 42 minecraft:light_gray_concrete
fill 17 64 27 30 71 27 minecraft:light_gray_concrete
fill 17 64 27 17 71 42 minecraft:light_gray_concrete
setblock 18 64 41 minecraft:air
setblock 18 64 41 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "011"}','{"text": "farms"}','{"text": "wood_saw"}','{"text": ""}']}}
setblock 19 64 41 minecraft:air
setblock 19 64 41 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "mechanical"}','{"text": "bearing with a"}','{"text": "saw arm over a"}','{"text": "ring of"}']}}
setblock 20 64 41 minecraft:air
setblock 20 64 41 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "saplings, glued"}','{"text": "chest and"}','{"text": "portable"}','{"text": "storage"}']}}
setblock 21 64 41 minecraft:air
setblock 21 64 41 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "interface"}','{"text": "Lager mit Motor"}','{"text": "drunter, Kleber"}','{"text": "setzen, Lager"}']}}
setblock 22 64 41 minecraft:air
setblock 22 64 41 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "starten"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
setblock 19 64 33 minecraft:oak_sapling
setblock 27 64 33 minecraft:oak_sapling
setblock 23 64 29 minecraft:oak_sapling
setblock 23 64 37 minecraft:oak_sapling
setblock 20 64 30 minecraft:oak_sapling
setblock 26 64 30 minecraft:oak_sapling
setblock 20 64 36 minecraft:oak_sapling
setblock 26 64 36 minecraft:oak_sapling
setblock 23 64 33 create:mechanical_bearing[facing=up]
setblock 23 63 33 create:shaft[axis=y]
fill 23 65 33 27 65 33 create:andesite_casing
setblock 27 65 34 create:mechanical_saw[facing=south]
setblock 24 65 34 minecraft:chest
setblock 24 65 32 create:portable_storage_interface[facing=north]
setblock 28 64 38 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"create:super_glue",count:1},{Slot:1b,id:"create:portable_storage_interface",count:1}]}
