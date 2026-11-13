# 058 botania_runes/plate_base
#area 167 105 186 130
fill 167 64 105 186 91 130 minecraft:air
fill 167 60 105 186 62 130 minecraft:stone
fill 167 63 105 186 63 130 minecraft:light_gray_concrete
fill 171 64 111 186 79 111 minecraft:light_gray_concrete
fill 171 64 111 171 79 124 minecraft:light_gray_concrete
setblock 172 64 123 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "058"}','{"text": "botania_runes"}','{"text": "plate_base"}','{"text": ""}']}}
setblock 173 64 123 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the 3x3 lapis"}','{"text": "and livingrock"}','{"text": "base with plate"}','{"text": "and sparks"}']}}
fill 181 64 111 181 79 124 minecraft:light_gray_concrete
setblock 175 64 115 botania:livingrock
setblock 175 64 116 minecraft:lapis_block
setblock 175 64 117 botania:livingrock
setblock 176 64 115 minecraft:lapis_block
setblock 176 64 116 botania:livingrock
setblock 176 64 117 minecraft:lapis_block
setblock 177 64 115 botania:livingrock
setblock 177 64 116 minecraft:lapis_block
setblock 177 64 117 botania:livingrock
setblock 176 65 116 botania:terrestrial_agglomeration_plate
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
