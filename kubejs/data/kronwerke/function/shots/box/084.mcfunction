# 084 ars_nouveau/imbuement, first_gem
fill 0 63 148 21 63 161 minecraft:light_gray_concrete
fill 0 64 148 21 71 148 minecraft:light_gray_concrete
fill 0 64 148 0 71 161 minecraft:light_gray_concrete
setblock 1 64 160 minecraft:air
setblock 1 64 160 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "084.1"}','{"text": "ars_nouveau"}','{"text": "imbuement"}','{"text": ""}']}}
setblock 2 64 160 minecraft:air
setblock 2 64 160 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the chamber"}','{"text": "with an"}','{"text": "amethyst shard,"}','{"text": "then with a"}']}}
setblock 3 64 160 minecraft:air
setblock 3 64 160 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "finished gem"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
summon text_display 5.5 71 153.5 {text:'[{"text": "084.1  ", "color": "gold"}, {"text": "ars_nouveau/imbuement", "color": "gray"}, {"text": "\\nBau eine Imbuement-Kammer", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 5 64 153 ars_nouveau:imbuement_chamber
setblock 3 64 153 ars_nouveau:source_jar
setblock 9 64 157 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"minecraft:amethyst_shard",count:16},{Slot:1b,id:"ars_nouveau:source_gem",count:4}]}
setblock 11 64 160 minecraft:air
setblock 11 64 160 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "084.2"}','{"text": "ars_nouveau"}','{"text": "first_gem"}','{"text": ""}']}}
setblock 12 64 160 minecraft:air
setblock 12 64 160 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Mach dein"}','{"text": "erstes"}','{"text": "Quelljuwel"}','{"text": ""}']}}
summon text_display 15.5 71 153.5 {text:'[{"text": "084.2  ", "color": "gold"}, {"text": "ars_nouveau/first_gem", "color": "gray"}, {"text": "\\nMach dein erstes Quelljuwel", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 15 64 153 ars_nouveau:imbuement_chamber
setblock 13 64 153 ars_nouveau:source_jar
setblock 19 64 157 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"minecraft:amethyst_shard",count:16},{Slot:1b,id:"ars_nouveau:source_gem",count:4}]}
