# 054 ars_apprentice/relay
#area 103 88 124 113
fill 103 64 88 124 91 113 minecraft:air
fill 103 60 88 124 62 113 minecraft:stone
fill 103 63 88 124 63 113 minecraft:light_gray_concrete
fill 107 64 94 124 79 94 minecraft:light_gray_concrete
fill 107 64 94 107 79 107 minecraft:light_gray_concrete
setblock 108 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "054"}','{"text": "ars_apprentice"}','{"text": "relay"}','{"text": ""}']}}
setblock 109 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "two relays"}','{"text": "bridging jars"}','{"text": "about 20 blocks"}','{"text": "apart"}']}}
fill 119 64 94 119 79 107 minecraft:light_gray_concrete
setblock 110 64 99 ars_nouveau:source_jar[fill=11]{source:10000}
setblock 112 64 99 ars_nouveau:relay
setblock 114 64 99 ars_nouveau:relay
setblock 116 64 99 ars_nouveau:source_jar[fill=0]
kw testworld use 110 64 99 south ars_nouveau:dominion_wand
kw testworld use 112 64 99 south ars_nouveau:dominion_wand
kw testworld use 112 64 99 south ars_nouveau:dominion_wand
kw testworld use 114 64 99 south ars_nouveau:dominion_wand
kw testworld use 114 64 99 south ars_nouveau:dominion_wand
kw testworld use 116 64 99 south ars_nouveau:dominion_wand
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
