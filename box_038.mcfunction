# 038 ars_nouveau/drygmy
#area 73 86 92 111
fill 73 64 86 92 91 111 minecraft:air
fill 73 60 86 92 62 111 minecraft:stone
fill 73 63 86 92 63 111 minecraft:light_gray_concrete
fill 77 64 92 92 79 92 minecraft:light_gray_concrete
fill 77 64 92 77 79 105 minecraft:light_gray_concrete
setblock 78 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "038"}','{"text": "ars_nouveau"}','{"text": "drygmy"}','{"text": ""}']}}
setblock 79 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Drygmy henge"}','{"text": "with chest and"}','{"text": "jar"}','{"text": ""}']}}
fill 87 64 92 87 79 105 minecraft:light_gray_concrete
setblock 82 64 97 minecraft:mossy_cobblestone
kw testworld use 82 64 97 up ars_nouveau:drygmy_charm
execute unless block 82 64 97 minecraft:mossy_cobblestone
setblock 83 64 97 minecraft:chest[facing=south]{Items:[]}
setblock 81 64 97 ars_nouveau:source_jar[fill=11]{source:10000}
summon minecraft:cow 84.5 64 99.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
summon minecraft:sheep 80.5 64 99.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
