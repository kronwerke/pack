# 090 botania_runes/plate_base
#area 167 143 186 168
fill 167 64 143 186 91 168 minecraft:air
fill 167 60 143 186 62 168 minecraft:stone
fill 167 63 143 186 63 168 minecraft:light_gray_concrete
fill 171 64 149 186 79 149 minecraft:light_gray_concrete
fill 171 64 149 171 79 162 minecraft:light_gray_concrete
setblock 172 64 161 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "090"}','{"text": "botania_runes"}','{"text": "plate_base"}','{"text": ""}']}}
setblock 173 64 161 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the 3x3 lapis"}','{"text": "and livingrock"}','{"text": "base with plate"}','{"text": "and sparks"}']}}
fill 181 64 149 181 79 162 minecraft:light_gray_concrete
setblock 175 64 153 botania:livingrock
setblock 175 64 154 minecraft:lapis_block
setblock 175 64 155 botania:livingrock
setblock 176 64 153 minecraft:lapis_block
setblock 176 64 154 botania:livingrock
setblock 176 64 155 minecraft:lapis_block
setblock 177 64 153 botania:livingrock
setblock 177 64 154 minecraft:lapis_block
setblock 177 64 155 botania:livingrock
setblock 176 65 154 botania:terrestrial_agglomeration_plate
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
