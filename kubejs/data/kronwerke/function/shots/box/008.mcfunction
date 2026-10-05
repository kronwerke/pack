# 008 start_here/m_gearbox, m_keystone
fill 123 63 6 144 63 19 minecraft:light_gray_concrete
fill 123 64 6 144 71 6 minecraft:light_gray_concrete
fill 123 64 6 123 71 19 minecraft:light_gray_concrete
setblock 124 64 18 minecraft:air
setblock 124 64 18 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "008.1"}','{"text": "start_here"}','{"text": "m_gearbox"}','{"text": ""}']}}
setblock 125 64 18 minecraft:air
setblock 125 64 18 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the crafting"}','{"text": "grid in JEI"}','{"text": "Rezept in JEI"}','{"text": "zeigen"}']}}
summon text_display 128.5 71 11.5 {text:'[{"text": "008.1  ", "color": "gold"}, {"text": "start_here/m_gearbox", "color": "gray"}, {"text": "\\nBau ein Steinwerk-Getriebe", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 125 64 9 minecraft:crafting_table
setblock 132 64 15 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"create:gearbox",count:1},{Slot:1b,id:"kronwerke:obelisk",count:1}]}
setblock 134 64 18 minecraft:air
setblock 134 64 18 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "008.2"}','{"text": "start_here"}','{"text": "m_keystone"}','{"text": ""}']}}
setblock 135 64 18 minecraft:air
setblock 135 64 18 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Rezept in JEI"}','{"text": "zeigen"}','{"text": ""}','{"text": ""}']}}
summon text_display 138.5 71 11.5 {text:'[{"text": "008.2  ", "color": "gold"}, {"text": "start_here/m_keystone", "color": "gray"}, {"text": "\\nBau einen Quellschlussstein", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 135 64 9 minecraft:crafting_table
setblock 142 64 15 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"create:gearbox",count:1},{Slot:1b,id:"kronwerke:obelisk",count:1}]}
