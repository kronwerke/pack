# 069 ars_apprentice/brazier
#area 120 122 139 147
fill 120 64 122 139 91 147 minecraft:air
fill 120 60 122 139 62 147 minecraft:stone
fill 120 63 122 139 63 147 minecraft:light_gray_concrete
fill 124 64 128 139 79 128 minecraft:light_gray_concrete
fill 124 64 128 124 79 141 minecraft:light_gray_concrete
setblock 125 64 140 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "069"}','{"text": "ars_apprentice"}','{"text": "brazier"}','{"text": ""}']}}
setblock 126 64 140 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a tablet on the"}','{"text": "lit brazier"}','{"text": ""}','{"text": ""}']}}
fill 134 64 128 134 79 141 minecraft:light_gray_concrete
setblock 129 64 133 ars_nouveau:ritual_brazier
kw testworld use 129 64 133 up ars_nouveau:ritual_flight
setblock 131 64 133 ars_nouveau:source_jar[fill=11]{source:10000}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
