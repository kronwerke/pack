# 165 eidolon/brazier, crucible, altar, stone_altar
#area 171 378 220 403
fill 171 64 378 215 91 403 minecraft:air
fill 216 64 378 220 91 403 minecraft:air
fill 171 60 378 220 62 403 minecraft:stone
fill 171 63 378 220 63 403 minecraft:light_gray_concrete
fill 175 64 384 220 79 384 minecraft:light_gray_concrete
fill 175 64 384 175 79 397 minecraft:light_gray_concrete
setblock 176 64 396 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "165.1"}','{"text": "eidolon"}','{"text": "brazier"}','{"text": ""}']}}
setblock 177 64 396 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau Brazier und"}','{"text": "Stone Hands"}','{"text": ""}','{"text": ""}']}}
fill 185 64 384 185 79 397 minecraft:light_gray_concrete
setblock 180 64 389 eidolon_repraised:brazier
setblock 178 64 389 eidolon_repraised:stone_hand[facing=east]
setblock 182 64 389 eidolon_repraised:stone_hand[facing=west]
setblock 180 64 387 eidolon_repraised:stone_hand[facing=south]
setblock 186 64 396 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "165.2"}','{"text": "eidolon"}','{"text": "crucible"}','{"text": ""}']}}
setblock 187 64 396 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz einen"}','{"text": "Crucible auf"}','{"text": ""}','{"text": ""}']}}
fill 195 64 384 195 79 397 minecraft:light_gray_concrete
setblock 190 64 389 minecraft:campfire[facing=south,lit=true]
setblock 190 65 389 eidolon_repraised:crucible
kw testworld use 190 65 389 up minecraft:water_bucket
setblock 196 64 396 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "165.3"}','{"text": "eidolon"}','{"text": "altar"}','{"text": ""}']}}
setblock 197 64 396 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen Altar"}','{"text": "mit Bildnis"}','{"text": ""}','{"text": ""}']}}
fill 205 64 384 205 79 397 minecraft:light_gray_concrete
fill 199 64 389 201 64 389 eidolon_repraised:wooden_altar
setblock 200 65 389 eidolon_repraised:straw_effigy[facing=south]
setblock 199 65 389 eidolon_repraised:candle
setblock 201 65 389 minecraft:skeleton_skull[rotation=8]
setblock 206 64 396 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "165.4"}','{"text": "eidolon"}','{"text": "stone_altar"}','{"text": ""}']}}
setblock 207 64 396 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau Stone Altar"}','{"text": "und Elder"}','{"text": "Statue"}','{"text": ""}']}}
fill 215 64 384 215 79 397 minecraft:light_gray_concrete
fill 209 64 389 211 64 389 eidolon_repraised:stone_altar
setblock 210 65 389 eidolon_repraised:unholy_effigy[facing=south]
setblock 209 65 389 eidolon_repraised:goblet
setblock 211 65 389 eidolon_repraised:candle
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
