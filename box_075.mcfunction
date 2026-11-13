# 075 ars_apprentice/relay
#area 118 126 139 151
fill 118 64 126 139 91 151 minecraft:air
fill 118 60 126 139 62 151 minecraft:stone
fill 118 63 126 139 63 151 minecraft:light_gray_concrete
fill 122 64 132 139 79 132 minecraft:light_gray_concrete
fill 122 64 132 122 79 145 minecraft:light_gray_concrete
setblock 123 64 144 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "075"}','{"text": "ars_apprentice"}','{"text": "relay"}','{"text": ""}']}}
setblock 124 64 144 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "two relays"}','{"text": "bridging jars"}','{"text": "about 20 blocks"}','{"text": "apart"}']}}
fill 134 64 132 134 79 145 minecraft:light_gray_concrete
setblock 125 64 137 ars_nouveau:source_jar[fill=11]{source:10000}
setblock 127 64 137 ars_nouveau:relay
setblock 129 64 137 ars_nouveau:relay
setblock 131 64 137 ars_nouveau:source_jar[fill=0]
kw testworld use 125 64 137 south ars_nouveau:dominion_wand
kw testworld use 127 64 137 south ars_nouveau:dominion_wand
kw testworld use 127 64 137 south ars_nouveau:dominion_wand
kw testworld use 129 64 137 south ars_nouveau:dominion_wand
kw testworld use 129 64 137 south ars_nouveau:dominion_wand
kw testworld use 131 64 137 south ars_nouveau:dominion_wand
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
