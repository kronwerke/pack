# 091 ars_nouveau/starbuncle_work
fill 115 63 130 126 63 143 minecraft:light_gray_concrete
fill 115 64 130 126 71 130 minecraft:light_gray_concrete
fill 115 64 130 115 71 143 minecraft:light_gray_concrete
setblock 116 64 142 minecraft:air
setblock 116 64 142 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "091"}','{"text": "ars_nouveau"}','{"text": "starbuncle_work"}','{"text": ""}']}}
setblock 117 64 142 minecraft:air
setblock 117 64 142 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "dominion wand"}','{"text": "links between"}','{"text": "chamber,"}','{"text": "Starbuncle and"}']}}
setblock 118 64 142 minecraft:air
setblock 118 64 142 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chest"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
setblock 118 64 135 ars_nouveau:imbuement_chamber
setblock 122 64 135 minecraft:chest
summon ars_nouveau:starbuncle 120.5 64 136.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 124 64 139 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"ars_nouveau:dominion_wand",count:1}]}
