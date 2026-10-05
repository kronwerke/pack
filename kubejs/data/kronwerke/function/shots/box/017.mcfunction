# 017 farms/source_berries
fill 113 63 27 126 63 40 minecraft:light_gray_concrete
fill 113 64 27 126 71 27 minecraft:light_gray_concrete
fill 113 64 27 113 71 40 minecraft:light_gray_concrete
setblock 114 64 39 minecraft:air
setblock 114 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "017"}','{"text": "farms"}','{"text": "source_berries"}','{"text": ""}']}}
setblock 115 64 39 minecraft:air
setblock 115 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "sourceberry"}','{"text": "rows with"}','{"text": "agronomic"}','{"text": "sourcelink,"}']}}
setblock 116 64 39 minecraft:air
setblock 116 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "source jar,"}','{"text": "imbuement"}','{"text": "chamber and"}','{"text": "Starbuncle"}']}}
fill 115 64 30 121 64 31 ars_nouveau:sourceberry_bush[age=3]
setblock 118 64 33 ars_nouveau:agronomic_sourcelink
setblock 120 64 33 ars_nouveau:source_jar
setblock 122 64 33 ars_nouveau:imbuement_chamber
summon ars_nouveau:starbuncle 117.5 64 34.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
