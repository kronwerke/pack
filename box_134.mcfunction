# 134 eidolon/brazier, crucible, altar, stone_altar
#area 151 338 200 363
fill 151 64 338 195 91 363 minecraft:air
fill 196 64 338 200 91 363 minecraft:air
fill 151 60 338 200 62 363 minecraft:stone
fill 151 63 338 200 63 363 minecraft:light_gray_concrete
fill 155 64 344 200 79 344 minecraft:light_gray_concrete
fill 155 64 344 155 79 357 minecraft:light_gray_concrete
setblock 156 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "134.1"}','{"text": "eidolon"}','{"text": "brazier"}','{"text": ""}']}}
setblock 157 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau Brazier und"}','{"text": "Stone Hands"}','{"text": ""}','{"text": ""}']}}
fill 165 64 344 165 79 357 minecraft:light_gray_concrete
setblock 160 64 349 eidolon_repraised:brazier
setblock 158 64 349 eidolon_repraised:stone_hand[facing=east]
setblock 162 64 349 eidolon_repraised:stone_hand[facing=west]
setblock 160 64 347 eidolon_repraised:stone_hand[facing=south]
setblock 166 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "134.2"}','{"text": "eidolon"}','{"text": "crucible"}','{"text": ""}']}}
setblock 167 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz einen"}','{"text": "Crucible auf"}','{"text": ""}','{"text": ""}']}}
fill 175 64 344 175 79 357 minecraft:light_gray_concrete
setblock 170 64 349 minecraft:campfire[facing=south,lit=true]
setblock 170 65 349 eidolon_repraised:crucible
kw testworld use 170 65 349 up minecraft:water_bucket
setblock 176 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "134.3"}','{"text": "eidolon"}','{"text": "altar"}','{"text": ""}']}}
setblock 177 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen Altar"}','{"text": "mit Bildnis"}','{"text": ""}','{"text": ""}']}}
fill 185 64 344 185 79 357 minecraft:light_gray_concrete
fill 179 64 349 181 64 349 eidolon_repraised:wooden_altar
setblock 180 65 349 eidolon_repraised:straw_effigy[facing=south]
setblock 179 65 349 eidolon_repraised:candle
setblock 181 65 349 minecraft:skeleton_skull[rotation=8]
setblock 186 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "134.4"}','{"text": "eidolon"}','{"text": "stone_altar"}','{"text": ""}']}}
setblock 187 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau Stone Altar"}','{"text": "und Elder"}','{"text": "Statue"}','{"text": ""}']}}
fill 195 64 344 195 79 357 minecraft:light_gray_concrete
fill 189 64 349 191 64 349 eidolon_repraised:stone_altar
setblock 190 65 349 eidolon_repraised:unholy_effigy[facing=south]
setblock 189 65 349 eidolon_repraised:goblet
setblock 191 65 349 eidolon_repraised:candle
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
