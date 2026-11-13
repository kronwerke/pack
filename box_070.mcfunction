# 070 ars_apprentice/potions
#area 135 118 154 143
fill 135 64 118 154 91 143 minecraft:air
fill 135 60 118 154 62 143 minecraft:stone
fill 135 63 118 154 63 143 minecraft:light_gray_concrete
fill 139 64 124 154 79 124 minecraft:light_gray_concrete
fill 139 64 124 139 79 137 minecraft:light_gray_concrete
setblock 140 64 136 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "070"}','{"text": "ars_apprentice"}','{"text": "potions"}','{"text": ""}']}}
setblock 141 64 136 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "potion jars"}','{"text": "next to the"}','{"text": "cauldron and an"}','{"text": "alchemical"}']}}
setblock 142 64 136 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "sourcelink"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 149 64 124 149 79 137 minecraft:light_gray_concrete
setblock 144 64 129 ars_nouveau:wixie_cauldron[converted=true,filled=true]
setblock 142 64 129 ars_nouveau:potion_jar[fill=11]
setblock 143 64 129 ars_nouveau:potion_jar[fill=6]
setblock 146 64 129 ars_nouveau:alchemical_sourcelink
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
