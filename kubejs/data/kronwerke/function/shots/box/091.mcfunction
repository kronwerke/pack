# 091 ars_nouveau/starbuncle_work
fill 115 63 148 126 63 161 minecraft:light_gray_concrete
fill 115 64 148 126 71 148 minecraft:light_gray_concrete
fill 115 64 148 115 71 161 minecraft:light_gray_concrete
setblock 116 64 160 minecraft:air
setblock 116 64 160 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "091"}','{"text": "ars_nouveau"}','{"text": "starbuncle_work"}','{"text": ""}']}}
setblock 117 64 160 minecraft:air
setblock 117 64 160 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "dominion wand"}','{"text": "links between"}','{"text": "chamber,"}','{"text": "Starbuncle and"}']}}
setblock 118 64 160 minecraft:air
setblock 118 64 160 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chest"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
summon text_display 120.5 71 153.5 {text:'[{"text": "091  ", "color": "gold"}, {"text": "ars_nouveau/starbuncle_work", "color": "gray"}, {"text": "\\nRichte den Sternbunkel ein", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 118 64 153 ars_nouveau:imbuement_chamber
setblock 122 64 153 minecraft:chest
summon ars_nouveau:starbuncle 120.5 64 154.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 124 64 157 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"ars_nouveau:dominion_wand",count:1}]}
