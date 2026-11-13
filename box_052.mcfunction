# 052 botania_runes/plate_base
#area 137 105 156 130
fill 137 64 105 156 91 130 minecraft:air
fill 137 60 105 156 62 130 minecraft:stone
fill 137 63 105 156 63 130 minecraft:light_gray_concrete
fill 141 64 111 156 79 111 minecraft:light_gray_concrete
fill 141 64 111 141 79 124 minecraft:light_gray_concrete
setblock 142 64 123 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "052"}','{"text": "botania_runes"}','{"text": "plate_base"}','{"text": ""}']}}
setblock 143 64 123 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the 3x3 lapis"}','{"text": "and livingrock"}','{"text": "base with plate"}','{"text": "and sparks"}']}}
fill 151 64 111 151 79 124 minecraft:light_gray_concrete
setblock 145 64 115 botania:livingrock
setblock 145 64 116 minecraft:lapis_block
setblock 145 64 117 botania:livingrock
setblock 146 64 115 minecraft:lapis_block
setblock 146 64 116 botania:livingrock
setblock 146 64 117 minecraft:lapis_block
setblock 147 64 115 botania:livingrock
setblock 147 64 116 minecraft:lapis_block
setblock 147 64 117 botania:livingrock
setblock 146 65 116 botania:terrestrial_agglomeration_plate
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
