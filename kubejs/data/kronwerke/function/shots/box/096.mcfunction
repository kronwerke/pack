# 096 ars_apprentice/brazier
fill 202 63 148 213 63 161 minecraft:light_gray_concrete
fill 202 64 148 213 71 148 minecraft:light_gray_concrete
fill 202 64 148 202 71 161 minecraft:light_gray_concrete
setblock 203 64 160 minecraft:air
setblock 203 64 160 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "096"}','{"text": "ars_apprentice"}','{"text": "brazier"}','{"text": ""}']}}
setblock 204 64 160 minecraft:air
setblock 204 64 160 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a tablet on the"}','{"text": "lit brazier"}','{"text": "Tafel auf die"}','{"text": "Kohlenpfanne"}']}}
summon text_display 207.5 71 153.5 {text:'[{"text": "096  ", "color": "gold"}, {"text": "ars_apprentice/brazier", "color": "gray"}, {"text": "\\nBau das Ritual-Kohlenbecken", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 207 64 153 ars_nouveau:ritual_brazier
setblock 211 64 157 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"ars_nouveau:ritual_scrying",count:1},{Slot:1b,id:"ars_nouveau:ritual_awakening",count:1},{Slot:2b,id:"ars_nouveau:wilden_spike",count:1},{Slot:3b,id:"ars_nouveau:wilden_horn",count:1},{Slot:4b,id:"ars_nouveau:wilden_wing",count:1},{Slot:5b,id:"ars_nouveau:source_gem",count:8}]}
