# 048 ars_apprentice/brazier
#area 105 88 124 113
fill 105 64 88 124 91 113 minecraft:air
fill 105 60 88 124 62 113 minecraft:stone
fill 105 63 88 124 63 113 minecraft:light_gray_concrete
fill 109 64 94 124 79 94 minecraft:light_gray_concrete
fill 109 64 94 109 79 107 minecraft:light_gray_concrete
setblock 110 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "048"}','{"text": "ars_apprentice"}','{"text": "brazier"}','{"text": ""}']}}
setblock 111 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a tablet on the"}','{"text": "lit brazier"}','{"text": ""}','{"text": ""}']}}
fill 119 64 94 119 79 107 minecraft:light_gray_concrete
setblock 114 64 99 ars_nouveau:ritual_brazier
kw testworld use 114 64 99 up ars_nouveau:ritual_flight
setblock 116 64 99 ars_nouveau:source_jar[fill=11]{source:10000}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
