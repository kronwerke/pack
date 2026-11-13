# 079 botania_runes/plate_base
#area 167 109 186 134
fill 167 64 109 186 91 134 minecraft:air
fill 167 60 109 186 62 134 minecraft:stone
fill 167 63 109 186 63 134 minecraft:light_gray_concrete
fill 171 64 115 186 79 115 minecraft:light_gray_concrete
fill 171 64 115 171 79 128 minecraft:light_gray_concrete
setblock 172 64 127 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "079"}','{"text": "botania_runes"}','{"text": "plate_base"}','{"text": ""}']}}
setblock 173 64 127 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the 3x3 lapis"}','{"text": "and livingrock"}','{"text": "base with plate"}','{"text": "and sparks"}']}}
fill 181 64 115 181 79 128 minecraft:light_gray_concrete
setblock 175 64 119 botania:livingrock
setblock 175 64 120 minecraft:lapis_block
setblock 175 64 121 botania:livingrock
setblock 176 64 119 minecraft:lapis_block
setblock 176 64 120 botania:livingrock
setblock 176 64 121 minecraft:lapis_block
setblock 177 64 119 botania:livingrock
setblock 177 64 120 minecraft:lapis_block
setblock 177 64 121 botania:livingrock
setblock 176 65 120 botania:terrestrial_agglomeration_plate
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
