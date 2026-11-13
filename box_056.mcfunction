# 056 ars_apprentice/potions
#area 135 88 154 113
fill 135 64 88 154 91 113 minecraft:air
fill 135 60 88 154 62 113 minecraft:stone
fill 135 63 88 154 63 113 minecraft:light_gray_concrete
fill 139 64 94 154 79 94 minecraft:light_gray_concrete
fill 139 64 94 139 79 107 minecraft:light_gray_concrete
setblock 140 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "056"}','{"text": "ars_apprentice"}','{"text": "potions"}','{"text": ""}']}}
setblock 141 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "potion jars"}','{"text": "next to the"}','{"text": "cauldron and an"}','{"text": "alchemical"}']}}
setblock 142 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "sourcelink"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 149 64 94 149 79 107 minecraft:light_gray_concrete
setblock 144 64 99 ars_nouveau:wixie_cauldron[converted=true,filled=true]
setblock 142 64 99 ars_nouveau:potion_jar[fill=11]
setblock 143 64 99 ars_nouveau:potion_jar[fill=6]
setblock 146 64 99 ars_nouveau:alchemical_sourcelink
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
