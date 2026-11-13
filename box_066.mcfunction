# 066 ars_apprentice/brazier
#area 120 118 139 143
fill 120 64 118 139 91 143 minecraft:air
fill 120 60 118 139 62 143 minecraft:stone
fill 120 63 118 139 63 143 minecraft:light_gray_concrete
fill 124 64 124 139 79 124 minecraft:light_gray_concrete
fill 124 64 124 124 79 137 minecraft:light_gray_concrete
setblock 125 64 136 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "066"}','{"text": "ars_apprentice"}','{"text": "brazier"}','{"text": ""}']}}
setblock 126 64 136 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a tablet on the"}','{"text": "lit brazier"}','{"text": ""}','{"text": ""}']}}
fill 134 64 124 134 79 137 minecraft:light_gray_concrete
setblock 129 64 129 ars_nouveau:ritual_brazier
kw testworld use 129 64 129 up ars_nouveau:ritual_flight
setblock 131 64 129 ars_nouveau:source_jar[fill=11]{source:10000}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
