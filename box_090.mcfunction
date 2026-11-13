# 090 botania_runes/plate_base
#area 167 145 186 170
fill 167 64 145 186 91 170 minecraft:air
fill 167 60 145 186 62 170 minecraft:stone
fill 167 63 145 186 63 170 minecraft:light_gray_concrete
fill 171 64 151 186 79 151 minecraft:light_gray_concrete
fill 171 64 151 171 79 164 minecraft:light_gray_concrete
setblock 172 64 163 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "090"}','{"text": "botania_runes"}','{"text": "plate_base"}','{"text": ""}']}}
setblock 173 64 163 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the 3x3 lapis"}','{"text": "and livingrock"}','{"text": "base with plate"}','{"text": "and sparks"}']}}
fill 181 64 151 181 79 164 minecraft:light_gray_concrete
setblock 175 64 155 botania:livingrock
setblock 175 64 156 minecraft:lapis_block
setblock 175 64 157 botania:livingrock
setblock 176 64 155 minecraft:lapis_block
setblock 176 64 156 botania:livingrock
setblock 176 64 157 minecraft:lapis_block
setblock 177 64 155 botania:livingrock
setblock 177 64 156 minecraft:lapis_block
setblock 177 64 157 botania:livingrock
setblock 176 65 156 botania:terrestrial_agglomeration_plate
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
