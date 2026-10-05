# 006 start_here/m_ritual
fill 93 63 6 104 63 19 minecraft:light_gray_concrete
fill 93 64 6 104 71 6 minecraft:light_gray_concrete
fill 93 64 6 93 71 19 minecraft:light_gray_concrete
setblock 94 64 18 minecraft:air
setblock 94 64 18 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "006"}','{"text": "start_here"}','{"text": "m_ritual"}','{"text": ""}']}}
setblock 95 64 18 minecraft:air
setblock 95 64 18 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the gold powder"}','{"text": "ring with"}','{"text": "wooden stands"}','{"text": "and a sapling"}']}}
setblock 96 64 18 minecraft:air
setblock 96 64 18 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "in the middle"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
summon text_display 98.5 71 11.5 {text:'[{"text": "006  ", "color": "gold"}, {"text": "start_here/m_ritual", "color": "gray"}, {"text": "\\nBereite das Ritual des Waldes vor", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 96 64 9 naturesaura:gold_powder
setblock 96 64 10 naturesaura:gold_powder
setblock 96 64 11 naturesaura:gold_powder
setblock 96 64 12 naturesaura:gold_powder
setblock 96 64 13 naturesaura:gold_powder
setblock 97 64 9 naturesaura:gold_powder
setblock 97 64 13 naturesaura:gold_powder
setblock 98 64 9 naturesaura:gold_powder
setblock 98 64 13 naturesaura:gold_powder
setblock 99 64 9 naturesaura:gold_powder
setblock 99 64 13 naturesaura:gold_powder
setblock 100 64 9 naturesaura:gold_powder
setblock 100 64 10 naturesaura:gold_powder
setblock 100 64 11 naturesaura:gold_powder
setblock 100 64 12 naturesaura:gold_powder
setblock 100 64 13 naturesaura:gold_powder
setblock 96 64 9 naturesaura:wood_stand
setblock 100 64 9 naturesaura:wood_stand
setblock 96 64 13 naturesaura:wood_stand
setblock 100 64 13 naturesaura:wood_stand
setblock 98 64 11 minecraft:oak_sapling
setblock 102 64 15 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"naturesaura:gold_leaf",count:1},{Slot:1b,id:"minecraft:oak_sapling",count:1},{Slot:2b,id:"minecraft:stone",count:4},{Slot:3b,id:"minecraft:cobblestone",count:2}]}
