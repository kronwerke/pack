# 067 ars_nouveau/starbuncle_work
#area 73 124 92 149
fill 73 64 124 92 91 149 minecraft:air
fill 73 60 124 92 62 149 minecraft:stone
fill 73 63 124 92 63 149 minecraft:light_gray_concrete
fill 77 64 130 92 79 130 minecraft:light_gray_concrete
fill 77 64 130 77 79 143 minecraft:light_gray_concrete
setblock 78 64 142 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "067"}','{"text": "ars_nouveau"}','{"text": "starbuncle_work"}','{"text": ""}']}}
setblock 79 64 142 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "dominion wand"}','{"text": "links between"}','{"text": "chamber,"}','{"text": "Starbuncle and"}']}}
setblock 80 64 142 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chest"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 87 64 130 87 79 143 minecraft:light_gray_concrete
setblock 80 64 135 ars_nouveau:imbuement_chamber[facing=up]
summon ars_nouveau:starbuncle 82.5 64 135.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 84 64 135 minecraft:chest[facing=south,type=single,waterlogged=false]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
