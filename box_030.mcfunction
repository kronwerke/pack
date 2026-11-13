# 030 ars_apprentice/brazier
#area 88 67 107 92
fill 88 64 67 107 91 92 minecraft:air
fill 88 60 67 107 62 92 minecraft:stone
fill 88 63 67 107 63 92 minecraft:light_gray_concrete
fill 92 64 73 107 79 73 minecraft:light_gray_concrete
fill 92 64 73 92 79 86 minecraft:light_gray_concrete
setblock 93 64 85 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "030"}','{"text": "ars_apprentice"}','{"text": "brazier"}','{"text": ""}']}}
setblock 94 64 85 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a tablet on the"}','{"text": "lit brazier"}','{"text": ""}','{"text": ""}']}}
fill 102 64 73 102 79 86 minecraft:light_gray_concrete
setblock 97 64 78 ars_nouveau:ritual_brazier
kw testworld use 97 64 78 up ars_nouveau:ritual_flight
kw testworld use 97 64 78 up minecraft:air
setblock 99 64 78 ars_nouveau:source_jar[fill=11]{source:10000}
