# 117 eidolon/brazier, crucible, altar, stone_altar
#area 151 336 200 361
fill 151 64 336 195 91 361 minecraft:air
fill 196 64 336 200 91 361 minecraft:air
fill 151 60 336 200 62 361 minecraft:stone
fill 151 63 336 200 63 361 minecraft:light_gray_concrete
fill 155 64 342 200 79 342 minecraft:light_gray_concrete
fill 155 64 342 155 79 355 minecraft:light_gray_concrete
setblock 156 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "117.1"}','{"text": "eidolon"}','{"text": "brazier"}','{"text": ""}']}}
setblock 157 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau Brazier und"}','{"text": "Stone Hands"}','{"text": ""}','{"text": ""}']}}
fill 165 64 342 165 79 355 minecraft:light_gray_concrete
setblock 160 64 347 eidolon_repraised:brazier
setblock 158 64 347 eidolon_repraised:stone_hand[facing=east]
setblock 162 64 347 eidolon_repraised:stone_hand[facing=west]
setblock 160 64 345 eidolon_repraised:stone_hand[facing=south]
setblock 166 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "117.2"}','{"text": "eidolon"}','{"text": "crucible"}','{"text": ""}']}}
setblock 167 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz einen"}','{"text": "Crucible auf"}','{"text": ""}','{"text": ""}']}}
fill 175 64 342 175 79 355 minecraft:light_gray_concrete
setblock 170 64 347 minecraft:campfire[facing=south,lit=true]
setblock 170 65 347 eidolon_repraised:crucible
kw testworld use 170 65 347 up minecraft:water_bucket
setblock 176 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "117.3"}','{"text": "eidolon"}','{"text": "altar"}','{"text": ""}']}}
setblock 177 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen Altar"}','{"text": "mit Bildnis"}','{"text": ""}','{"text": ""}']}}
fill 185 64 342 185 79 355 minecraft:light_gray_concrete
fill 179 64 347 181 64 347 eidolon_repraised:wooden_altar
setblock 180 65 347 eidolon_repraised:straw_effigy[facing=south]
setblock 179 65 347 eidolon_repraised:candle
setblock 181 65 347 minecraft:skeleton_skull[rotation=8]
setblock 186 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "117.4"}','{"text": "eidolon"}','{"text": "stone_altar"}','{"text": ""}']}}
setblock 187 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau Stone Altar"}','{"text": "und Elder"}','{"text": "Statue"}','{"text": ""}']}}
fill 195 64 342 195 79 355 minecraft:light_gray_concrete
fill 189 64 347 191 64 347 eidolon_repraised:stone_altar
setblock 190 65 347 eidolon_repraised:unholy_effigy[facing=south]
setblock 189 65 347 eidolon_repraised:goblet
setblock 191 65 347 eidolon_repraised:candle
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
