# 011 farms/wood_saw
fill 17 63 31 30 63 46 minecraft:light_gray_concrete
fill 17 64 31 30 71 31 minecraft:light_gray_concrete
fill 17 64 31 17 71 46 minecraft:light_gray_concrete
setblock 18 64 45 minecraft:air
setblock 18 64 45 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "011"}','{"text": "farms"}','{"text": "wood_saw"}','{"text": ""}']}}
setblock 19 64 45 minecraft:air
setblock 19 64 45 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "mechanical"}','{"text": "bearing with a"}','{"text": "saw arm over a"}','{"text": "ring of"}']}}
setblock 20 64 45 minecraft:air
setblock 20 64 45 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "saplings, glued"}','{"text": "chest and"}','{"text": "portable"}','{"text": "storage"}']}}
setblock 21 64 45 minecraft:air
setblock 21 64 45 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "interface"}','{"text": "Lager mit Motor"}','{"text": "drunter, Kleber"}','{"text": "setzen, Lager"}']}}
setblock 22 64 45 minecraft:air
setblock 22 64 45 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "starten"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
summon text_display 23.5 71 37.5 {text:'[{"text": "011  ", "color": "gold"}, {"text": "farms/wood_saw", "color": "gray"}, {"text": "\\nLass Sägen Bäume fällen", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 19 64 37 minecraft:oak_sapling
setblock 27 64 37 minecraft:oak_sapling
setblock 23 64 33 minecraft:oak_sapling
setblock 23 64 41 minecraft:oak_sapling
setblock 20 64 34 minecraft:oak_sapling
setblock 26 64 34 minecraft:oak_sapling
setblock 20 64 40 minecraft:oak_sapling
setblock 26 64 40 minecraft:oak_sapling
setblock 23 64 37 create:mechanical_bearing[facing=up]
setblock 23 63 37 create:shaft[axis=y]
fill 23 65 37 27 65 37 create:andesite_casing
setblock 27 65 38 create:mechanical_saw[facing=south]
setblock 24 65 38 minecraft:chest
setblock 24 65 36 create:portable_storage_interface[facing=north]
setblock 28 64 42 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"create:super_glue",count:1},{Slot:1b,id:"create:portable_storage_interface",count:1}]}
