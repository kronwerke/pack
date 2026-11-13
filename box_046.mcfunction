# 046 ars_nouveau/drygmy
#area 73 88 92 113
fill 73 64 88 92 91 113 minecraft:air
fill 73 60 88 92 62 113 minecraft:stone
fill 73 63 88 92 63 113 minecraft:light_gray_concrete
fill 77 64 94 92 79 94 minecraft:light_gray_concrete
fill 77 64 94 77 79 107 minecraft:light_gray_concrete
setblock 78 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "046"}','{"text": "ars_nouveau"}','{"text": "drygmy"}','{"text": ""}']}}
setblock 79 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Drygmy henge"}','{"text": "with chest and"}','{"text": "jar"}','{"text": ""}']}}
fill 87 64 94 87 79 107 minecraft:light_gray_concrete
setblock 82 64 99 minecraft:mossy_cobblestone
kw testworld use 82 64 99 up ars_nouveau:drygmy_charm
execute unless block 82 64 99 minecraft:mossy_cobblestone
setblock 83 64 99 minecraft:chest[facing=south]{Items:[]}
setblock 81 64 99 ars_nouveau:source_jar[fill=11]{source:10000}
summon minecraft:cow 84.5 64 101.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
summon minecraft:sheep 80.5 64 101.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
