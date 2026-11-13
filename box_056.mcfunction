# 056 ars_nouveau/drygmy
#area 88 88 107 113
fill 88 64 88 107 91 113 minecraft:air
fill 88 60 88 107 62 113 minecraft:stone
fill 88 63 88 107 63 113 minecraft:light_gray_concrete
fill 92 64 94 107 79 94 minecraft:light_gray_concrete
fill 92 64 94 92 79 107 minecraft:light_gray_concrete
setblock 93 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "056"}','{"text": "ars_nouveau"}','{"text": "drygmy"}','{"text": ""}']}}
setblock 94 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Drygmy henge"}','{"text": "with chest and"}','{"text": "jar"}','{"text": ""}']}}
fill 102 64 94 102 79 107 minecraft:light_gray_concrete
setblock 97 64 99 minecraft:mossy_cobblestone
kw testworld use 97 64 99 up ars_nouveau:drygmy_charm
execute unless block 97 64 99 minecraft:mossy_cobblestone
setblock 98 64 99 minecraft:chest[facing=south]{Items:[]}
setblock 96 64 99 ars_nouveau:source_jar[fill=11]{source:10000}
summon minecraft:cow 99.5 64 101.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
summon minecraft:sheep 95.5 64 101.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
