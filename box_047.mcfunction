# 047 ars_apprentice/relay
#area 88 88 109 113
fill 88 64 88 109 91 113 minecraft:air
fill 88 60 88 109 62 113 minecraft:stone
fill 88 63 88 109 63 113 minecraft:light_gray_concrete
fill 92 64 94 109 79 94 minecraft:light_gray_concrete
fill 92 64 94 92 79 107 minecraft:light_gray_concrete
setblock 93 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "047"}','{"text": "ars_apprentice"}','{"text": "relay"}','{"text": ""}']}}
setblock 94 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "two relays"}','{"text": "bridging jars"}','{"text": "about 20 blocks"}','{"text": "apart"}']}}
fill 104 64 94 104 79 107 minecraft:light_gray_concrete
setblock 95 64 99 ars_nouveau:source_jar[fill=11]{source:10000}
setblock 97 64 99 ars_nouveau:relay
setblock 99 64 99 ars_nouveau:relay
setblock 101 64 99 ars_nouveau:source_jar[fill=0]
kw testworld use 95 64 99 south ars_nouveau:dominion_wand
kw testworld use 97 64 99 south ars_nouveau:dominion_wand
kw testworld use 97 64 99 south ars_nouveau:dominion_wand
kw testworld use 99 64 99 south ars_nouveau:dominion_wand
kw testworld use 99 64 99 south ars_nouveau:dominion_wand
kw testworld use 101 64 99 south ars_nouveau:dominion_wand
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
