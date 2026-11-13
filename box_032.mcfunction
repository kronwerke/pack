# 032 ars_nouveau/drygmy
#area 73 67 92 92
fill 73 64 67 92 91 92 minecraft:air
fill 73 60 67 92 62 92 minecraft:stone
fill 73 63 67 92 63 92 minecraft:light_gray_concrete
fill 77 64 73 92 79 73 minecraft:light_gray_concrete
fill 77 64 73 77 79 86 minecraft:light_gray_concrete
setblock 78 64 85 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "032"}','{"text": "ars_nouveau"}','{"text": "drygmy"}','{"text": ""}']}}
setblock 79 64 85 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Drygmy henge"}','{"text": "with chest and"}','{"text": "jar"}','{"text": ""}']}}
fill 87 64 73 87 79 86 minecraft:light_gray_concrete
setblock 82 64 78 minecraft:mossy_cobblestone
kw testworld use 82 64 78 up ars_nouveau:drygmy_charm
execute unless block 82 64 78 minecraft:mossy_cobblestone
setblock 83 64 78 minecraft:chest[facing=south]{Items:[]}
setblock 81 64 78 ars_nouveau:source_jar[fill=11]{source:10000}
summon minecraft:cow 84.5 64 80.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
summon minecraft:sheep 80.5 64 80.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
