# 054 ars_nouveau/starbuncle_work
#area 73 88 92 113
fill 73 64 88 92 91 113 minecraft:air
fill 73 60 88 92 62 113 minecraft:stone
fill 73 63 88 92 63 113 minecraft:light_gray_concrete
fill 77 64 94 92 79 94 minecraft:light_gray_concrete
fill 77 64 94 77 79 107 minecraft:light_gray_concrete
setblock 78 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "054"}','{"text": "ars_nouveau"}','{"text": "starbuncle_work"}','{"text": ""}']}}
setblock 79 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "dominion wand"}','{"text": "links between"}','{"text": "chamber,"}','{"text": "Starbuncle and"}']}}
setblock 80 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chest"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 87 64 94 87 79 107 minecraft:light_gray_concrete
setblock 80 64 99 ars_nouveau:imbuement_chamber[facing=up]
summon ars_nouveau:starbuncle 82.5 64 99.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 84 64 99 minecraft:chest[facing=south,type=single,waterlogged=false]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
