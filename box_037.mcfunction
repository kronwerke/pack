# 037 ars_apprentice/brazier
#area 111 67 130 92
fill 111 64 67 130 91 92 minecraft:air
fill 111 60 67 130 62 92 minecraft:stone
fill 111 63 67 130 63 92 minecraft:light_gray_concrete
fill 115 64 73 130 79 73 minecraft:light_gray_concrete
fill 115 64 73 115 79 86 minecraft:light_gray_concrete
setblock 116 64 85 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "037"}','{"text": "ars_apprentice"}','{"text": "brazier"}','{"text": ""}']}}
setblock 117 64 85 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a tablet on the"}','{"text": "lit brazier"}','{"text": ""}','{"text": ""}']}}
fill 125 64 73 125 79 86 minecraft:light_gray_concrete
setblock 120 64 78 ars_nouveau:ritual_brazier
kw testworld use 120 64 78 up ars_nouveau:ritual_flight
setblock 122 64 78 ars_nouveau:source_jar[fill=11]{source:10000}
