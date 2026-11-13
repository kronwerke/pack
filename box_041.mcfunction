# 041 ars_apprentice/brazier
#area 107 86 126 111
fill 107 64 86 126 91 111 minecraft:air
fill 107 60 86 126 62 111 minecraft:stone
fill 107 63 86 126 63 111 minecraft:light_gray_concrete
fill 111 64 92 126 79 92 minecraft:light_gray_concrete
fill 111 64 92 111 79 105 minecraft:light_gray_concrete
setblock 112 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "041"}','{"text": "ars_apprentice"}','{"text": "brazier"}','{"text": ""}']}}
setblock 113 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a tablet on the"}','{"text": "lit brazier"}','{"text": ""}','{"text": ""}']}}
fill 121 64 92 121 79 105 minecraft:light_gray_concrete
setblock 116 64 97 ars_nouveau:ritual_brazier
kw testworld use 116 64 97 up ars_nouveau:ritual_flight
setblock 118 64 97 ars_nouveau:source_jar[fill=11]{source:10000}
