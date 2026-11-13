# 040 ars_apprentice/relay
#area 88 86 109 111
fill 88 64 86 109 91 111 minecraft:air
fill 88 60 86 109 62 111 minecraft:stone
fill 88 63 86 109 63 111 minecraft:light_gray_concrete
fill 92 64 92 109 79 92 minecraft:light_gray_concrete
fill 92 64 92 92 79 105 minecraft:light_gray_concrete
setblock 93 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "040"}','{"text": "ars_apprentice"}','{"text": "relay"}','{"text": ""}']}}
setblock 94 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "two relays"}','{"text": "bridging jars"}','{"text": "about 20 blocks"}','{"text": "apart"}']}}
fill 104 64 92 104 79 105 minecraft:light_gray_concrete
setblock 95 64 97 ars_nouveau:source_jar[fill=11]{source:10000}
setblock 97 64 97 ars_nouveau:relay
setblock 99 64 97 ars_nouveau:relay
setblock 101 64 97 ars_nouveau:source_jar[fill=0]
kw testworld use 95 64 97 south ars_nouveau:dominion_wand
kw testworld use 97 64 97 south ars_nouveau:dominion_wand
kw testworld use 97 64 97 south ars_nouveau:dominion_wand
kw testworld use 99 64 97 south ars_nouveau:dominion_wand
kw testworld use 99 64 97 south ars_nouveau:dominion_wand
kw testworld use 101 64 97 south ars_nouveau:dominion_wand
