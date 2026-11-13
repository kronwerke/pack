# 070 ars_apprentice/potions
#area 135 122 154 147
fill 135 64 122 154 91 147 minecraft:air
fill 135 60 122 154 62 147 minecraft:stone
fill 135 63 122 154 63 147 minecraft:light_gray_concrete
fill 139 64 128 154 79 128 minecraft:light_gray_concrete
fill 139 64 128 139 79 141 minecraft:light_gray_concrete
setblock 140 64 140 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "070"}','{"text": "ars_apprentice"}','{"text": "potions"}','{"text": ""}']}}
setblock 141 64 140 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "potion jars"}','{"text": "next to the"}','{"text": "cauldron and an"}','{"text": "alchemical"}']}}
setblock 142 64 140 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "sourcelink"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 149 64 128 149 79 141 minecraft:light_gray_concrete
setblock 144 64 133 ars_nouveau:wixie_cauldron[converted=true,filled=true]
setblock 142 64 133 ars_nouveau:potion_jar[fill=11]
setblock 143 64 133 ars_nouveau:potion_jar[fill=6]
setblock 146 64 133 ars_nouveau:alchemical_sourcelink
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
