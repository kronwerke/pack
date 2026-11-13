# 077 ars_apprentice/brazier
#area 150 126 169 151
fill 150 64 126 169 91 151 minecraft:air
fill 150 60 126 169 62 151 minecraft:stone
fill 150 63 126 169 63 151 minecraft:light_gray_concrete
fill 154 64 132 169 79 132 minecraft:light_gray_concrete
fill 154 64 132 154 79 145 minecraft:light_gray_concrete
setblock 155 64 144 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "077"}','{"text": "ars_apprentice"}','{"text": "brazier"}','{"text": ""}']}}
setblock 156 64 144 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a tablet on the"}','{"text": "lit brazier"}','{"text": ""}','{"text": ""}']}}
fill 164 64 132 164 79 145 minecraft:light_gray_concrete
setblock 159 64 137 ars_nouveau:ritual_brazier
kw testworld use 159 64 137 up ars_nouveau:ritual_flight
setblock 161 64 137 ars_nouveau:source_jar[fill=11]{source:10000}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
