# 007 farms/source_berries
#area 26 21 47 46
fill 26 64 21 47 91 46 minecraft:air
fill 26 60 21 47 62 46 minecraft:stone
fill 26 63 21 47 63 46 minecraft:light_gray_concrete
fill 30 64 27 47 79 27 minecraft:light_gray_concrete
fill 30 64 27 30 79 40 minecraft:light_gray_concrete
setblock 31 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "007"}','{"text": "farms"}','{"text": "source_berries"}','{"text": ""}']}}
setblock 32 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "sourceberry"}','{"text": "rows with"}','{"text": "agronomic"}','{"text": "sourcelink,"}']}}
setblock 33 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "source jar,"}','{"text": "imbuement"}','{"text": "chamber and"}','{"text": "Starbuncle"}']}}
fill 42 64 27 42 79 40 minecraft:light_gray_concrete
fill 32 63 30 40 63 34 minecraft:grass_block
setblock 33 64 31 ars_nouveau:sourceberry_bush[age=3]
setblock 33 64 33 ars_nouveau:sourceberry_bush[age=3]
setblock 34 64 31 ars_nouveau:sourceberry_bush[age=3]
setblock 34 64 33 ars_nouveau:sourceberry_bush[age=3]
setblock 35 64 31 ars_nouveau:sourceberry_bush[age=3]
setblock 35 64 33 ars_nouveau:sourceberry_bush[age=3]
setblock 36 64 31 ars_nouveau:sourceberry_bush[age=3]
setblock 36 64 33 ars_nouveau:sourceberry_bush[age=3]
setblock 37 64 31 ars_nouveau:sourceberry_bush[age=3]
setblock 37 64 33 ars_nouveau:sourceberry_bush[age=3]
setblock 38 64 31 ars_nouveau:sourceberry_bush[age=3]
setblock 38 64 33 ars_nouveau:sourceberry_bush[age=3]
setblock 39 64 31 ars_nouveau:sourceberry_bush[age=3]
setblock 39 64 33 ars_nouveau:sourceberry_bush[age=3]
setblock 35 64 32 ars_nouveau:agronomic_sourcelink
setblock 37 64 32 ars_nouveau:source_jar[fill=8]{source:7000}
setblock 39 64 32 ars_nouveau:imbuement_chamber[facing=up]
summon ars_nouveau:starbuncle 33.5 64 32.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
