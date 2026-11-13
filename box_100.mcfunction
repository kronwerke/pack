# 100 botania_runes/plate_base
#area 167 147 186 172
fill 167 64 147 186 91 172 minecraft:air
fill 167 60 147 186 62 172 minecraft:stone
fill 167 63 147 186 63 172 minecraft:light_gray_concrete
fill 171 64 153 186 79 153 minecraft:light_gray_concrete
fill 171 64 153 171 79 166 minecraft:light_gray_concrete
setblock 172 64 165 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "100"}','{"text": "botania_runes"}','{"text": "plate_base"}','{"text": ""}']}}
setblock 173 64 165 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the 3x3 lapis"}','{"text": "and livingrock"}','{"text": "base with plate"}','{"text": "and sparks"}']}}
fill 181 64 153 181 79 166 minecraft:light_gray_concrete
setblock 175 64 157 botania:livingrock
setblock 175 64 158 minecraft:lapis_block
setblock 175 64 159 botania:livingrock
setblock 176 64 157 minecraft:lapis_block
setblock 176 64 158 botania:livingrock
setblock 176 64 159 minecraft:lapis_block
setblock 177 64 157 botania:livingrock
setblock 177 64 158 minecraft:lapis_block
setblock 177 64 159 botania:livingrock
setblock 176 65 158 botania:terrestrial_agglomeration_plate
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
