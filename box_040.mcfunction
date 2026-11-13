# 040 ars_apprentice/relay
#area 88 86 111 111
fill 88 64 86 111 91 111 minecraft:air
fill 88 60 86 111 62 111 minecraft:stone
fill 88 63 86 111 63 111 minecraft:light_gray_concrete
fill 92 64 92 111 79 92 minecraft:light_gray_concrete
fill 92 64 92 92 79 105 minecraft:light_gray_concrete
setblock 93 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "040"}','{"text": "ars_apprentice"}','{"text": "relay"}','{"text": ""}']}}
setblock 94 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "two relays"}','{"text": "bridging jars"}','{"text": "about 20 blocks"}','{"text": "apart"}']}}
fill 106 64 92 106 79 105 minecraft:light_gray_concrete
setblock 94 64 97 ars_nouveau:source_jar[fill=11]{source:10000}
setblock 97 64 97 ars_nouveau:relay
setblock 101 64 97 ars_nouveau:relay
setblock 104 64 97 ars_nouveau:source_jar[fill=0]
kw testworld use 94 64 97 south ars_nouveau:dominion_wand
kw testworld use 97 64 97 south ars_nouveau:dominion_wand
kw testworld use 97 64 97 south ars_nouveau:dominion_wand
kw testworld use 101 64 97 south ars_nouveau:dominion_wand
kw testworld use 101 64 97 south ars_nouveau:dominion_wand
kw testworld use 104 64 97 south ars_nouveau:dominion_wand
