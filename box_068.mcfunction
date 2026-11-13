# 068 ars_apprentice/relay
#area 103 124 124 149
fill 103 64 124 124 91 149 minecraft:air
fill 103 60 124 124 62 149 minecraft:stone
fill 103 63 124 124 63 149 minecraft:light_gray_concrete
fill 107 64 130 124 79 130 minecraft:light_gray_concrete
fill 107 64 130 107 79 143 minecraft:light_gray_concrete
setblock 108 64 142 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "068"}','{"text": "ars_apprentice"}','{"text": "relay"}','{"text": ""}']}}
setblock 109 64 142 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "two relays"}','{"text": "bridging jars"}','{"text": "about 20 blocks"}','{"text": "apart"}']}}
fill 119 64 130 119 79 143 minecraft:light_gray_concrete
setblock 110 64 135 ars_nouveau:source_jar[fill=11]{source:10000}
setblock 112 64 135 ars_nouveau:relay
setblock 114 64 135 ars_nouveau:relay
setblock 116 64 135 ars_nouveau:source_jar[fill=0]
kw testworld use 110 64 135 south ars_nouveau:dominion_wand
kw testworld use 112 64 135 south ars_nouveau:dominion_wand
kw testworld use 112 64 135 south ars_nouveau:dominion_wand
kw testworld use 114 64 135 south ars_nouveau:dominion_wand
kw testworld use 114 64 135 south ars_nouveau:dominion_wand
kw testworld use 116 64 135 south ars_nouveau:dominion_wand
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
