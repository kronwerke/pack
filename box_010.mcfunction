# 010 farms/source_berries
#area 75 21 96 46
fill 75 64 21 96 91 46 minecraft:air
fill 75 60 21 96 62 46 minecraft:stone
fill 75 63 21 96 63 46 minecraft:light_gray_concrete
fill 79 64 27 96 79 27 minecraft:light_gray_concrete
fill 79 64 27 79 79 40 minecraft:light_gray_concrete
setblock 80 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "010"}','{"text": "farms"}','{"text": "source_berries"}','{"text": ""}']}}
setblock 81 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "sourceberry"}','{"text": "rows with"}','{"text": "agronomic"}','{"text": "sourcelink,"}']}}
setblock 82 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "source jar,"}','{"text": "imbuement"}','{"text": "chamber and"}','{"text": "Starbuncle"}']}}
fill 91 64 27 91 79 40 minecraft:light_gray_concrete
fill 81 63 30 89 63 34 minecraft:grass_block
setblock 82 64 31 ars_nouveau:sourceberry_bush[age=3]
setblock 82 64 33 ars_nouveau:sourceberry_bush[age=3]
setblock 83 64 31 ars_nouveau:sourceberry_bush[age=3]
setblock 83 64 33 ars_nouveau:sourceberry_bush[age=3]
setblock 84 64 31 ars_nouveau:sourceberry_bush[age=3]
setblock 84 64 33 ars_nouveau:sourceberry_bush[age=3]
setblock 85 64 31 ars_nouveau:sourceberry_bush[age=3]
setblock 85 64 33 ars_nouveau:sourceberry_bush[age=3]
setblock 86 64 31 ars_nouveau:sourceberry_bush[age=3]
setblock 86 64 33 ars_nouveau:sourceberry_bush[age=3]
setblock 87 64 31 ars_nouveau:sourceberry_bush[age=3]
setblock 87 64 33 ars_nouveau:sourceberry_bush[age=3]
setblock 88 64 31 ars_nouveau:sourceberry_bush[age=3]
setblock 88 64 33 ars_nouveau:sourceberry_bush[age=3]
setblock 84 64 32 ars_nouveau:agronomic_sourcelink
setblock 86 64 32 ars_nouveau:source_jar[fill=8]{source:7000}
setblock 88 64 32 ars_nouveau:imbuement_chamber[facing=up]
summon ars_nouveau:starbuncle 82.5 64 32.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
