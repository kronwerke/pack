# 068 ars_nouveau/drygmy
#area 88 124 107 149
fill 88 64 124 107 91 149 minecraft:air
fill 88 60 124 107 62 149 minecraft:stone
fill 88 63 124 107 63 149 minecraft:light_gray_concrete
fill 92 64 130 107 79 130 minecraft:light_gray_concrete
fill 92 64 130 92 79 143 minecraft:light_gray_concrete
setblock 93 64 142 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "068"}','{"text": "ars_nouveau"}','{"text": "drygmy"}','{"text": ""}']}}
setblock 94 64 142 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Drygmy henge"}','{"text": "with chest and"}','{"text": "jar"}','{"text": ""}']}}
fill 102 64 130 102 79 143 minecraft:light_gray_concrete
setblock 97 64 135 minecraft:mossy_cobblestone
kw testworld use 97 64 135 up ars_nouveau:drygmy_charm
execute unless block 97 64 135 minecraft:mossy_cobblestone
setblock 98 64 135 minecraft:chest[facing=south]{Items:[]}
setblock 96 64 135 ars_nouveau:source_jar[fill=11]{source:10000}
summon minecraft:cow 99.5 64 137.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
summon minecraft:sheep 95.5 64 137.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
