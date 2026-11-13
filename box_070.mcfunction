# 070 ars_apprentice/potions
#area 135 124 154 149
fill 135 64 124 154 91 149 minecraft:air
fill 135 60 124 154 62 149 minecraft:stone
fill 135 63 124 154 63 149 minecraft:light_gray_concrete
fill 139 64 130 154 79 130 minecraft:light_gray_concrete
fill 139 64 130 139 79 143 minecraft:light_gray_concrete
setblock 140 64 142 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "070"}','{"text": "ars_apprentice"}','{"text": "potions"}','{"text": ""}']}}
setblock 141 64 142 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "potion jars"}','{"text": "next to the"}','{"text": "cauldron and an"}','{"text": "alchemical"}']}}
setblock 142 64 142 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "sourcelink"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 149 64 130 149 79 143 minecraft:light_gray_concrete
setblock 144 64 135 ars_nouveau:wixie_cauldron[converted=true,filled=true]
setblock 142 64 135 ars_nouveau:potion_jar[fill=11]
setblock 143 64 135 ars_nouveau:potion_jar[fill=6]
setblock 146 64 135 ars_nouveau:alchemical_sourcelink
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
