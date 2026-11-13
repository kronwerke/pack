# 099 eidolon/brazier, crucible, altar, stone_altar
#area 11 309 60 334
fill 11 64 309 55 91 334 minecraft:air
fill 56 64 309 60 91 334 minecraft:air
fill 11 60 309 60 62 334 minecraft:stone
fill 11 63 309 60 63 334 minecraft:light_gray_concrete
fill 15 64 315 60 79 315 minecraft:light_gray_concrete
fill 15 64 315 15 79 328 minecraft:light_gray_concrete
setblock 16 64 327 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "099.1"}','{"text": "eidolon"}','{"text": "brazier"}','{"text": ""}']}}
setblock 17 64 327 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau Brazier und"}','{"text": "Stone Hands"}','{"text": ""}','{"text": ""}']}}
fill 25 64 315 25 79 328 minecraft:light_gray_concrete
setblock 20 64 320 eidolon_repraised:brazier
setblock 18 64 320 eidolon_repraised:stone_hand[facing=east]
setblock 22 64 320 eidolon_repraised:stone_hand[facing=west]
setblock 20 64 318 eidolon_repraised:stone_hand[facing=south]
setblock 26 64 327 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "099.2"}','{"text": "eidolon"}','{"text": "crucible"}','{"text": ""}']}}
setblock 27 64 327 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz einen"}','{"text": "Crucible auf"}','{"text": ""}','{"text": ""}']}}
fill 35 64 315 35 79 328 minecraft:light_gray_concrete
setblock 30 64 320 minecraft:campfire[facing=south,lit=true]
setblock 30 65 320 eidolon_repraised:crucible
kw testworld use 30 65 320 up minecraft:water_bucket
setblock 36 64 327 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "099.3"}','{"text": "eidolon"}','{"text": "altar"}','{"text": ""}']}}
setblock 37 64 327 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen Altar"}','{"text": "mit Bildnis"}','{"text": ""}','{"text": ""}']}}
fill 45 64 315 45 79 328 minecraft:light_gray_concrete
fill 39 64 320 41 64 320 eidolon_repraised:wooden_altar
setblock 40 65 320 eidolon_repraised:straw_effigy[facing=south]
setblock 39 65 320 eidolon_repraised:candle
setblock 41 65 320 minecraft:skeleton_skull[rotation=8]
setblock 46 64 327 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "099.4"}','{"text": "eidolon"}','{"text": "stone_altar"}','{"text": ""}']}}
setblock 47 64 327 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau Stone Altar"}','{"text": "und Elder"}','{"text": "Statue"}','{"text": ""}']}}
fill 55 64 315 55 79 328 minecraft:light_gray_concrete
fill 49 64 320 51 64 320 eidolon_repraised:stone_altar
setblock 50 65 320 eidolon_repraised:unholy_effigy[facing=south]
setblock 49 65 320 eidolon_repraised:goblet
setblock 51 65 320 eidolon_repraised:candle
