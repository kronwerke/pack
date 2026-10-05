# 095 ars_apprentice/collector
fill 187 63 148 198 63 161 minecraft:light_gray_concrete
fill 187 64 148 198 71 148 minecraft:light_gray_concrete
fill 187 64 148 187 71 161 minecraft:light_gray_concrete
setblock 188 64 160 minecraft:air
setblock 188 64 160 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "095"}','{"text": "ars_apprentice"}','{"text": "collector"}','{"text": ""}']}}
setblock 189 64 160 minecraft:air
setblock 189 64 160 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "collector at"}','{"text": "the link farm,"}','{"text": "depositor at"}','{"text": "the workshop"}']}}
summon text_display 192.5 71 153.5 {text:'[{"text": "095  ", "color": "gold"}, {"text": "ars_apprentice/collector", "color": "gray"}, {"text": "\\nBau Kollektor und Einzahler", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 189 64 151 ars_nouveau:relay_collector
setblock 191 64 151 ars_nouveau:relay_deposit
setblock 196 64 157 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"ars_nouveau:dominion_wand",count:1}]}
