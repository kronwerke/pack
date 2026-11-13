# 079 ars_apprentice/potions
#area 180 126 199 151
fill 180 64 126 199 91 151 minecraft:air
fill 180 60 126 199 62 151 minecraft:stone
fill 180 63 126 199 63 151 minecraft:light_gray_concrete
fill 184 64 132 199 79 132 minecraft:light_gray_concrete
fill 184 64 132 184 79 145 minecraft:light_gray_concrete
setblock 185 64 144 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "079"}','{"text": "ars_apprentice"}','{"text": "potions"}','{"text": ""}']}}
setblock 186 64 144 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "potion jars"}','{"text": "next to the"}','{"text": "cauldron and an"}','{"text": "alchemical"}']}}
setblock 187 64 144 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "sourcelink"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 194 64 132 194 79 145 minecraft:light_gray_concrete
setblock 189 64 137 ars_nouveau:wixie_cauldron[converted=true,filled=true]
setblock 187 64 137 ars_nouveau:potion_jar[fill=11]
setblock 188 64 137 ars_nouveau:potion_jar[fill=6]
setblock 191 64 137 ars_nouveau:alchemical_sourcelink
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
