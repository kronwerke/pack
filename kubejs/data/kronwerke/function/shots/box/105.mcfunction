# 105 ars_master/ritual_awakening
fill 337 63 148 348 63 161 minecraft:light_gray_concrete
fill 337 64 148 348 71 148 minecraft:light_gray_concrete
fill 337 64 148 337 71 161 minecraft:light_gray_concrete
setblock 338 64 160 minecraft:air
setblock 338 64 160 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "105"}','{"text": "ars_master"}','{"text": "ritual_awakening"}','{"text": ""}']}}
setblock 339 64 160 minecraft:air
setblock 339 64 160 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a Weald Walker"}','{"text": "Tafel auf die"}','{"text": "Kohlenpfanne"}','{"text": ""}']}}
summon text_display 342.5 71 153.5 {text:'[{"text": "105  ", "color": "gold"}, {"text": "ars_master/ritual_awakening", "color": "gray"}, {"text": "\\nMach die Tafel Erwachen", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 342 64 153 ars_nouveau:ritual_brazier
setblock 346 64 157 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"ars_nouveau:ritual_scrying",count:1},{Slot:1b,id:"ars_nouveau:ritual_awakening",count:1},{Slot:2b,id:"ars_nouveau:wilden_spike",count:1},{Slot:3b,id:"ars_nouveau:wilden_horn",count:1},{Slot:4b,id:"ars_nouveau:wilden_wing",count:1},{Slot:5b,id:"ars_nouveau:source_gem",count:8}]}
