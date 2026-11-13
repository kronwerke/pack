# 009 farms/source_berries
#area 60 21 81 46
fill 60 64 21 81 91 46 minecraft:air
fill 60 60 21 81 62 46 minecraft:stone
fill 60 63 21 81 63 46 minecraft:light_gray_concrete
fill 64 64 27 81 79 27 minecraft:light_gray_concrete
fill 64 64 27 64 79 40 minecraft:light_gray_concrete
setblock 65 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "009"}','{"text": "farms"}','{"text": "source_berries"}','{"text": ""}']}}
setblock 66 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "sourceberry"}','{"text": "rows with"}','{"text": "agronomic"}','{"text": "sourcelink,"}']}}
setblock 67 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "source jar,"}','{"text": "imbuement"}','{"text": "chamber and"}','{"text": "Starbuncle"}']}}
fill 76 64 27 76 79 40 minecraft:light_gray_concrete
fill 66 63 30 74 63 34 minecraft:grass_block
setblock 67 64 31 ars_nouveau:sourceberry_bush[age=3]
setblock 67 64 33 ars_nouveau:sourceberry_bush[age=3]
setblock 68 64 31 ars_nouveau:sourceberry_bush[age=3]
setblock 68 64 33 ars_nouveau:sourceberry_bush[age=3]
setblock 69 64 31 ars_nouveau:sourceberry_bush[age=3]
setblock 69 64 33 ars_nouveau:sourceberry_bush[age=3]
setblock 70 64 31 ars_nouveau:sourceberry_bush[age=3]
setblock 70 64 33 ars_nouveau:sourceberry_bush[age=3]
setblock 71 64 31 ars_nouveau:sourceberry_bush[age=3]
setblock 71 64 33 ars_nouveau:sourceberry_bush[age=3]
setblock 72 64 31 ars_nouveau:sourceberry_bush[age=3]
setblock 72 64 33 ars_nouveau:sourceberry_bush[age=3]
setblock 73 64 31 ars_nouveau:sourceberry_bush[age=3]
setblock 73 64 33 ars_nouveau:sourceberry_bush[age=3]
setblock 69 64 32 ars_nouveau:agronomic_sourcelink
setblock 71 64 32 ars_nouveau:source_jar[fill=8]{source:7000}
setblock 73 64 32 ars_nouveau:imbuement_chamber[facing=up]
summon ars_nouveau:starbuncle 67.5 64 32.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
