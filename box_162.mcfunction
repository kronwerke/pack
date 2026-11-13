# 162 eidolon/brazier, crucible, altar, stone_altar
#area 151 370 200 395
fill 151 64 370 195 91 395 minecraft:air
fill 196 64 370 200 91 395 minecraft:air
fill 151 60 370 200 62 395 minecraft:stone
fill 151 63 370 200 63 395 minecraft:light_gray_concrete
fill 155 64 376 200 79 376 minecraft:light_gray_concrete
fill 155 64 376 155 79 389 minecraft:light_gray_concrete
setblock 156 64 388 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "162.1"}','{"text": "eidolon"}','{"text": "brazier"}','{"text": ""}']}}
setblock 157 64 388 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau Brazier und"}','{"text": "Stone Hands"}','{"text": ""}','{"text": ""}']}}
fill 165 64 376 165 79 389 minecraft:light_gray_concrete
setblock 160 64 381 eidolon_repraised:brazier
setblock 158 64 381 eidolon_repraised:stone_hand[facing=east]
setblock 162 64 381 eidolon_repraised:stone_hand[facing=west]
setblock 160 64 379 eidolon_repraised:stone_hand[facing=south]
setblock 166 64 388 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "162.2"}','{"text": "eidolon"}','{"text": "crucible"}','{"text": ""}']}}
setblock 167 64 388 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz einen"}','{"text": "Crucible auf"}','{"text": ""}','{"text": ""}']}}
fill 175 64 376 175 79 389 minecraft:light_gray_concrete
setblock 170 64 381 minecraft:campfire[facing=south,lit=true]
setblock 170 65 381 eidolon_repraised:crucible
kw testworld use 170 65 381 up minecraft:water_bucket
setblock 176 64 388 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "162.3"}','{"text": "eidolon"}','{"text": "altar"}','{"text": ""}']}}
setblock 177 64 388 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen Altar"}','{"text": "mit Bildnis"}','{"text": ""}','{"text": ""}']}}
fill 185 64 376 185 79 389 minecraft:light_gray_concrete
fill 179 64 381 181 64 381 eidolon_repraised:wooden_altar
setblock 180 65 381 eidolon_repraised:straw_effigy[facing=south]
setblock 179 65 381 eidolon_repraised:candle
setblock 181 65 381 minecraft:skeleton_skull[rotation=8]
setblock 186 64 388 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "162.4"}','{"text": "eidolon"}','{"text": "stone_altar"}','{"text": ""}']}}
setblock 187 64 388 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau Stone Altar"}','{"text": "und Elder"}','{"text": "Statue"}','{"text": ""}']}}
fill 195 64 376 195 79 389 minecraft:light_gray_concrete
fill 189 64 381 191 64 381 eidolon_repraised:stone_altar
setblock 190 65 381 eidolon_repraised:unholy_effigy[facing=south]
setblock 189 65 381 eidolon_repraised:goblet
setblock 191 65 381 eidolon_repraised:candle
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
