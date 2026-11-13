# 045 ars_apprentice/brazier
#area 105 86 124 111
fill 105 64 86 124 91 111 minecraft:air
fill 105 60 86 124 62 111 minecraft:stone
fill 105 63 86 124 63 111 minecraft:light_gray_concrete
fill 109 64 92 124 79 92 minecraft:light_gray_concrete
fill 109 64 92 109 79 105 minecraft:light_gray_concrete
setblock 110 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "045"}','{"text": "ars_apprentice"}','{"text": "brazier"}','{"text": ""}']}}
setblock 111 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a tablet on the"}','{"text": "lit brazier"}','{"text": ""}','{"text": ""}']}}
fill 119 64 92 119 79 105 minecraft:light_gray_concrete
setblock 114 64 97 ars_nouveau:ritual_brazier
kw testworld use 114 64 97 up ars_nouveau:ritual_flight
setblock 116 64 97 ars_nouveau:source_jar[fill=11]{source:10000}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
