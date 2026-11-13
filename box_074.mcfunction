# 074 ars_nouveau/drygmy
#area 103 126 122 151
fill 103 64 126 122 91 151 minecraft:air
fill 103 60 126 122 62 151 minecraft:stone
fill 103 63 126 122 63 151 minecraft:light_gray_concrete
fill 107 64 132 122 79 132 minecraft:light_gray_concrete
fill 107 64 132 107 79 145 minecraft:light_gray_concrete
setblock 108 64 144 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "074"}','{"text": "ars_nouveau"}','{"text": "drygmy"}','{"text": ""}']}}
setblock 109 64 144 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Drygmy henge"}','{"text": "with chest and"}','{"text": "jar"}','{"text": ""}']}}
fill 117 64 132 117 79 145 minecraft:light_gray_concrete
setblock 112 64 137 minecraft:mossy_cobblestone
kw testworld use 112 64 137 up ars_nouveau:drygmy_charm
execute unless block 112 64 137 minecraft:mossy_cobblestone
setblock 113 64 137 minecraft:chest[facing=south]{Items:[]}
setblock 111 64 137 ars_nouveau:source_jar[fill=11]{source:10000}
summon minecraft:cow 114.5 64 139.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
summon minecraft:sheep 110.5 64 139.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
