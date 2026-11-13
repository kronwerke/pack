# 067 ars_nouveau/drygmy
#area 88 118 107 143
fill 88 64 118 107 91 143 minecraft:air
fill 88 60 118 107 62 143 minecraft:stone
fill 88 63 118 107 63 143 minecraft:light_gray_concrete
fill 92 64 124 107 79 124 minecraft:light_gray_concrete
fill 92 64 124 92 79 137 minecraft:light_gray_concrete
setblock 93 64 136 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "067"}','{"text": "ars_nouveau"}','{"text": "drygmy"}','{"text": ""}']}}
setblock 94 64 136 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Drygmy henge"}','{"text": "with chest and"}','{"text": "jar"}','{"text": ""}']}}
fill 102 64 124 102 79 137 minecraft:light_gray_concrete
setblock 97 64 129 minecraft:mossy_cobblestone
kw testworld use 97 64 129 up ars_nouveau:drygmy_charm
execute unless block 97 64 129 minecraft:mossy_cobblestone
setblock 98 64 129 minecraft:chest[facing=south]{Items:[]}
setblock 96 64 129 ars_nouveau:source_jar[fill=11]{source:10000}
summon minecraft:cow 99.5 64 131.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
summon minecraft:sheep 95.5 64 131.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
