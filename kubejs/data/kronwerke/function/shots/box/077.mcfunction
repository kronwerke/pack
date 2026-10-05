# 077 mekanism_elite/polonium
fill 328 63 108 339 63 121 minecraft:light_gray_concrete
fill 328 64 108 339 71 108 minecraft:light_gray_concrete
fill 328 64 108 328 71 121 minecraft:light_gray_concrete
setblock 329 64 120 minecraft:air
setblock 329 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "077"}','{"text": "mekanism_elite"}','{"text": "polonium"}','{"text": ""}']}}
setblock 330 64 120 minecraft:air
setblock 330 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "NuclearCraft"}','{"text": "irradiation"}','{"text": "chain"}','{"text": "Bestrahlungskette"}']}}
setblock 331 64 120 minecraft:air
setblock 331 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "NuclearCraft"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
summon text_display 333.5 71 113.5 {text:'[{"text": "077  ", "color": "gold"}, {"text": "mekanism_elite/polonium", "color": "gray"}, {"text": "\\nHol Polonium aus NuclearCraft", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 330 64 111 nuclearcraft:irradiator
setblock 332 64 111 mekanism:isotopic_centrifuge
