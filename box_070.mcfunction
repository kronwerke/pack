# 070 botania_runes/plate_base
#area 167 107 186 132
fill 167 64 107 186 91 132 minecraft:air
fill 167 60 107 186 62 132 minecraft:stone
fill 167 63 107 186 63 132 minecraft:light_gray_concrete
fill 171 64 113 186 79 113 minecraft:light_gray_concrete
fill 171 64 113 171 79 126 minecraft:light_gray_concrete
setblock 172 64 125 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "070"}','{"text": "botania_runes"}','{"text": "plate_base"}','{"text": ""}']}}
setblock 173 64 125 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the 3x3 lapis"}','{"text": "and livingrock"}','{"text": "base with plate"}','{"text": "and sparks"}']}}
fill 181 64 113 181 79 126 minecraft:light_gray_concrete
setblock 175 64 117 botania:livingrock
setblock 175 64 118 minecraft:lapis_block
setblock 175 64 119 botania:livingrock
setblock 176 64 117 minecraft:lapis_block
setblock 176 64 118 botania:livingrock
setblock 176 64 119 minecraft:lapis_block
setblock 177 64 117 botania:livingrock
setblock 177 64 118 minecraft:lapis_block
setblock 177 64 119 botania:livingrock
setblock 176 65 118 botania:terrestrial_agglomeration_plate
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
