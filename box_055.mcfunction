# 055 ars_apprentice/brazier
#area 120 88 139 113
fill 120 64 88 139 91 113 minecraft:air
fill 120 60 88 139 62 113 minecraft:stone
fill 120 63 88 139 63 113 minecraft:light_gray_concrete
fill 124 64 94 139 79 94 minecraft:light_gray_concrete
fill 124 64 94 124 79 107 minecraft:light_gray_concrete
setblock 125 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "055"}','{"text": "ars_apprentice"}','{"text": "brazier"}','{"text": ""}']}}
setblock 126 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a tablet on the"}','{"text": "lit brazier"}','{"text": ""}','{"text": ""}']}}
fill 134 64 94 134 79 107 minecraft:light_gray_concrete
setblock 129 64 99 ars_nouveau:ritual_brazier
kw testworld use 129 64 99 up ars_nouveau:ritual_flight
setblock 131 64 99 ars_nouveau:source_jar[fill=11]{source:10000}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
