# 066 ars_nouveau/starbuncle_work
#area 73 122 92 147
fill 73 64 122 92 91 147 minecraft:air
fill 73 60 122 92 62 147 minecraft:stone
fill 73 63 122 92 63 147 minecraft:light_gray_concrete
fill 77 64 128 92 79 128 minecraft:light_gray_concrete
fill 77 64 128 77 79 141 minecraft:light_gray_concrete
setblock 78 64 140 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "066"}','{"text": "ars_nouveau"}','{"text": "starbuncle_work"}','{"text": ""}']}}
setblock 79 64 140 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "dominion wand"}','{"text": "links between"}','{"text": "chamber,"}','{"text": "Starbuncle and"}']}}
setblock 80 64 140 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chest"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 87 64 128 87 79 141 minecraft:light_gray_concrete
setblock 80 64 133 ars_nouveau:imbuement_chamber[facing=up]
summon ars_nouveau:starbuncle 82.5 64 133.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 84 64 133 minecraft:chest[facing=south,type=single,waterlogged=false]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
