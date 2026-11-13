# 073 ars_nouveau/starbuncle_work
#area 88 126 107 151
fill 88 64 126 107 91 151 minecraft:air
fill 88 60 126 107 62 151 minecraft:stone
fill 88 63 126 107 63 151 minecraft:light_gray_concrete
fill 92 64 132 107 79 132 minecraft:light_gray_concrete
fill 92 64 132 92 79 145 minecraft:light_gray_concrete
setblock 93 64 144 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "073"}','{"text": "ars_nouveau"}','{"text": "starbuncle_work"}','{"text": ""}']}}
setblock 94 64 144 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "dominion wand"}','{"text": "links between"}','{"text": "chamber,"}','{"text": "Starbuncle and"}']}}
setblock 95 64 144 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chest"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 102 64 132 102 79 145 minecraft:light_gray_concrete
setblock 95 64 137 ars_nouveau:imbuement_chamber[facing=up]
summon ars_nouveau:starbuncle 97.5 64 137.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 99 64 137 minecraft:chest[facing=south,type=single,waterlogged=false]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
