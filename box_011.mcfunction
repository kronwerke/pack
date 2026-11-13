# 011 farms/source_berries
#area 90 21 111 46
fill 90 64 21 111 91 46 minecraft:air
fill 90 60 21 111 62 46 minecraft:stone
fill 90 63 21 111 63 46 minecraft:light_gray_concrete
fill 94 64 27 111 79 27 minecraft:light_gray_concrete
fill 94 64 27 94 79 40 minecraft:light_gray_concrete
setblock 95 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "011"}','{"text": "farms"}','{"text": "source_berries"}','{"text": ""}']}}
setblock 96 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "sourceberry"}','{"text": "rows with"}','{"text": "agronomic"}','{"text": "sourcelink,"}']}}
setblock 97 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "source jar,"}','{"text": "imbuement"}','{"text": "chamber and"}','{"text": "Starbuncle"}']}}
fill 106 64 27 106 79 40 minecraft:light_gray_concrete
fill 96 63 30 104 63 34 minecraft:grass_block
setblock 97 64 31 ars_nouveau:sourceberry_bush[age=3]
setblock 97 64 33 ars_nouveau:sourceberry_bush[age=3]
setblock 98 64 31 ars_nouveau:sourceberry_bush[age=3]
setblock 98 64 33 ars_nouveau:sourceberry_bush[age=3]
setblock 99 64 31 ars_nouveau:sourceberry_bush[age=3]
setblock 99 64 33 ars_nouveau:sourceberry_bush[age=3]
setblock 100 64 31 ars_nouveau:sourceberry_bush[age=3]
setblock 100 64 33 ars_nouveau:sourceberry_bush[age=3]
setblock 101 64 31 ars_nouveau:sourceberry_bush[age=3]
setblock 101 64 33 ars_nouveau:sourceberry_bush[age=3]
setblock 102 64 31 ars_nouveau:sourceberry_bush[age=3]
setblock 102 64 33 ars_nouveau:sourceberry_bush[age=3]
setblock 103 64 31 ars_nouveau:sourceberry_bush[age=3]
setblock 103 64 33 ars_nouveau:sourceberry_bush[age=3]
setblock 99 64 32 ars_nouveau:agronomic_sourcelink
setblock 101 64 32 ars_nouveau:source_jar[fill=8]{source:7000}
setblock 103 64 32 ars_nouveau:imbuement_chamber[facing=up]
summon ars_nouveau:starbuncle 97.5 64 32.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
