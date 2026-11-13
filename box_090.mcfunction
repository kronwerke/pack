# 090 botania_runes/plate_base
#area 167 139 186 164
fill 167 64 139 186 91 164 minecraft:air
fill 167 60 139 186 62 164 minecraft:stone
fill 167 63 139 186 63 164 minecraft:light_gray_concrete
fill 171 64 145 186 79 145 minecraft:light_gray_concrete
fill 171 64 145 171 79 158 minecraft:light_gray_concrete
setblock 172 64 157 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "090"}','{"text": "botania_runes"}','{"text": "plate_base"}','{"text": ""}']}}
setblock 173 64 157 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the 3x3 lapis"}','{"text": "and livingrock"}','{"text": "base with plate"}','{"text": "and sparks"}']}}
fill 181 64 145 181 79 158 minecraft:light_gray_concrete
setblock 175 64 149 botania:livingrock
setblock 175 64 150 minecraft:lapis_block
setblock 175 64 151 botania:livingrock
setblock 176 64 149 minecraft:lapis_block
setblock 176 64 150 botania:livingrock
setblock 176 64 151 minecraft:lapis_block
setblock 177 64 149 botania:livingrock
setblock 177 64 150 minecraft:lapis_block
setblock 177 64 151 botania:livingrock
setblock 176 65 150 botania:terrestrial_agglomeration_plate
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
