# 036 ars_apprentice/relay
#area 88 67 115 92
fill 88 64 67 115 91 92 minecraft:air
fill 88 60 67 115 62 92 minecraft:stone
fill 88 63 67 115 63 92 minecraft:light_gray_concrete
fill 92 64 73 115 79 73 minecraft:light_gray_concrete
fill 92 64 73 92 79 86 minecraft:light_gray_concrete
setblock 93 64 85 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "036"}','{"text": "ars_apprentice"}','{"text": "relay"}','{"text": ""}']}}
setblock 94 64 85 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "two relays"}','{"text": "bridging jars"}','{"text": "about 20 blocks"}','{"text": "apart"}']}}
fill 110 64 73 110 79 86 minecraft:light_gray_concrete
setblock 94 64 78 ars_nouveau:source_jar[fill=11]{source:10000}
setblock 99 64 78 ars_nouveau:relay
setblock 103 64 78 ars_nouveau:relay
setblock 108 64 78 ars_nouveau:source_jar[fill=0]
kw testworld use 94 64 78 south ars_nouveau:dominion_wand
kw testworld use 99 64 78 south ars_nouveau:dominion_wand
kw testworld use 99 64 78 south ars_nouveau:dominion_wand
kw testworld use 103 64 78 south ars_nouveau:dominion_wand
kw testworld use 103 64 78 south ars_nouveau:dominion_wand
kw testworld use 108 64 78 south ars_nouveau:dominion_wand
