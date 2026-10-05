# 103 ars_master/wilden_ritual
fill 307 63 148 318 63 161 minecraft:light_gray_concrete
fill 307 64 148 318 71 148 minecraft:light_gray_concrete
fill 307 64 148 307 71 161 minecraft:light_gray_concrete
setblock 308 64 160 minecraft:air
setblock 308 64 160 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "103"}','{"text": "ars_master"}','{"text": "wilden_ritual"}','{"text": ""}']}}
setblock 309 64 160 minecraft:air
setblock 309 64 160 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "brazier with"}','{"text": "spike, horn and"}','{"text": "wing"}','{"text": "Tafel auf die"}']}}
setblock 310 64 160 minecraft:air
setblock 310 64 160 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Kohlenpfanne"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
summon text_display 312.5 71 153.5 {text:'[{"text": "103  ", "color": "gold"}, {"text": "ars_master/wilden_ritual", "color": "gray"}, {"text": "\\nMach die Tafel Beschwöre Wilden", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 312 64 153 ars_nouveau:ritual_brazier
setblock 316 64 157 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"ars_nouveau:ritual_scrying",count:1},{Slot:1b,id:"ars_nouveau:ritual_awakening",count:1},{Slot:2b,id:"ars_nouveau:wilden_spike",count:1},{Slot:3b,id:"ars_nouveau:wilden_horn",count:1},{Slot:4b,id:"ars_nouveau:wilden_wing",count:1},{Slot:5b,id:"ars_nouveau:source_gem",count:8}]}
