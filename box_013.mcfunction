# 013 farms/source_berries
#area 105 21 126 46
fill 105 64 21 126 91 46 minecraft:air
fill 105 60 21 126 62 46 minecraft:stone
fill 105 63 21 126 63 46 minecraft:light_gray_concrete
fill 109 64 27 126 79 27 minecraft:light_gray_concrete
fill 109 64 27 109 79 40 minecraft:light_gray_concrete
setblock 110 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "013"}','{"text": "farms"}','{"text": "source_berries"}','{"text": ""}']}}
setblock 111 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "sourceberry"}','{"text": "rows with"}','{"text": "agronomic"}','{"text": "sourcelink,"}']}}
setblock 112 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "source jar,"}','{"text": "imbuement"}','{"text": "chamber and"}','{"text": "Starbuncle"}']}}
fill 121 64 27 121 79 40 minecraft:light_gray_concrete
fill 111 63 30 119 63 34 minecraft:grass_block
setblock 112 64 31 ars_nouveau:sourceberry_bush[age=3]
setblock 112 64 33 ars_nouveau:sourceberry_bush[age=3]
setblock 113 64 31 ars_nouveau:sourceberry_bush[age=3]
setblock 113 64 33 ars_nouveau:sourceberry_bush[age=3]
setblock 114 64 31 ars_nouveau:sourceberry_bush[age=3]
setblock 114 64 33 ars_nouveau:sourceberry_bush[age=3]
setblock 115 64 31 ars_nouveau:sourceberry_bush[age=3]
setblock 115 64 33 ars_nouveau:sourceberry_bush[age=3]
setblock 116 64 31 ars_nouveau:sourceberry_bush[age=3]
setblock 116 64 33 ars_nouveau:sourceberry_bush[age=3]
setblock 117 64 31 ars_nouveau:sourceberry_bush[age=3]
setblock 117 64 33 ars_nouveau:sourceberry_bush[age=3]
setblock 118 64 31 ars_nouveau:sourceberry_bush[age=3]
setblock 118 64 33 ars_nouveau:sourceberry_bush[age=3]
setblock 114 64 32 ars_nouveau:agronomic_sourcelink
setblock 116 64 32 ars_nouveau:source_jar[fill=8]{source:7000}
setblock 118 64 32 ars_nouveau:imbuement_chamber[facing=up]
summon ars_nouveau:starbuncle 112.5 64 32.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
