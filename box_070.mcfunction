# 070 ars_apprentice/brazier
#area 120 124 139 149
fill 120 64 124 139 91 149 minecraft:air
fill 120 60 124 139 62 149 minecraft:stone
fill 120 63 124 139 63 149 minecraft:light_gray_concrete
fill 124 64 130 139 79 130 minecraft:light_gray_concrete
fill 124 64 130 124 79 143 minecraft:light_gray_concrete
setblock 125 64 142 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "070"}','{"text": "ars_apprentice"}','{"text": "brazier"}','{"text": ""}']}}
setblock 126 64 142 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a tablet on the"}','{"text": "lit brazier"}','{"text": ""}','{"text": ""}']}}
fill 134 64 130 134 79 143 minecraft:light_gray_concrete
setblock 129 64 135 ars_nouveau:ritual_brazier
kw testworld use 129 64 135 up ars_nouveau:ritual_flight
setblock 131 64 135 ars_nouveau:source_jar[fill=11]{source:10000}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
