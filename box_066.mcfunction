# 066 ars_nouveau/starbuncle_work
#area 73 118 92 143
fill 73 64 118 92 91 143 minecraft:air
fill 73 60 118 92 62 143 minecraft:stone
fill 73 63 118 92 63 143 minecraft:light_gray_concrete
fill 77 64 124 92 79 124 minecraft:light_gray_concrete
fill 77 64 124 77 79 137 minecraft:light_gray_concrete
setblock 78 64 136 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "066"}','{"text": "ars_nouveau"}','{"text": "starbuncle_work"}','{"text": ""}']}}
setblock 79 64 136 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "dominion wand"}','{"text": "links between"}','{"text": "chamber,"}','{"text": "Starbuncle and"}']}}
setblock 80 64 136 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chest"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 87 64 124 87 79 137 minecraft:light_gray_concrete
setblock 80 64 129 ars_nouveau:imbuement_chamber[facing=up]
summon ars_nouveau:starbuncle 82.5 64 129.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 84 64 129 minecraft:chest[facing=south,type=single,waterlogged=false]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
