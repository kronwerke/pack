# 067 ars_nouveau/drygmy
#area 88 122 107 147
fill 88 64 122 107 91 147 minecraft:air
fill 88 60 122 107 62 147 minecraft:stone
fill 88 63 122 107 63 147 minecraft:light_gray_concrete
fill 92 64 128 107 79 128 minecraft:light_gray_concrete
fill 92 64 128 92 79 141 minecraft:light_gray_concrete
setblock 93 64 140 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "067"}','{"text": "ars_nouveau"}','{"text": "drygmy"}','{"text": ""}']}}
setblock 94 64 140 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Drygmy henge"}','{"text": "with chest and"}','{"text": "jar"}','{"text": ""}']}}
fill 102 64 128 102 79 141 minecraft:light_gray_concrete
setblock 97 64 133 minecraft:mossy_cobblestone
kw testworld use 97 64 133 up ars_nouveau:drygmy_charm
execute unless block 97 64 133 minecraft:mossy_cobblestone
setblock 98 64 133 minecraft:chest[facing=south]{Items:[]}
setblock 96 64 133 ars_nouveau:source_jar[fill=11]{source:10000}
summon minecraft:cow 99.5 64 135.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
summon minecraft:sheep 95.5 64 135.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
