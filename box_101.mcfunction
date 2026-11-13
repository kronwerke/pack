# 101 eidolon/brazier, crucible, altar, stone_altar
#area 11 311 60 336
fill 11 64 311 55 91 336 minecraft:air
fill 56 64 311 60 91 336 minecraft:air
fill 11 60 311 60 62 336 minecraft:stone
fill 11 63 311 60 63 336 minecraft:light_gray_concrete
fill 15 64 317 60 79 317 minecraft:light_gray_concrete
fill 15 64 317 15 79 330 minecraft:light_gray_concrete
setblock 16 64 329 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "101.1"}','{"text": "eidolon"}','{"text": "brazier"}','{"text": ""}']}}
setblock 17 64 329 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau Brazier und"}','{"text": "Stone Hands"}','{"text": ""}','{"text": ""}']}}
fill 25 64 317 25 79 330 minecraft:light_gray_concrete
setblock 20 64 322 eidolon_repraised:brazier
setblock 18 64 322 eidolon_repraised:stone_hand[facing=east]
setblock 22 64 322 eidolon_repraised:stone_hand[facing=west]
setblock 20 64 320 eidolon_repraised:stone_hand[facing=south]
setblock 26 64 329 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "101.2"}','{"text": "eidolon"}','{"text": "crucible"}','{"text": ""}']}}
setblock 27 64 329 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz einen"}','{"text": "Crucible auf"}','{"text": ""}','{"text": ""}']}}
fill 35 64 317 35 79 330 minecraft:light_gray_concrete
setblock 30 64 322 minecraft:campfire[facing=south,lit=true]
setblock 30 65 322 eidolon_repraised:crucible
kw testworld use 30 65 322 up minecraft:water_bucket
setblock 36 64 329 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "101.3"}','{"text": "eidolon"}','{"text": "altar"}','{"text": ""}']}}
setblock 37 64 329 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen Altar"}','{"text": "mit Bildnis"}','{"text": ""}','{"text": ""}']}}
fill 45 64 317 45 79 330 minecraft:light_gray_concrete
fill 39 64 322 41 64 322 eidolon_repraised:wooden_altar
setblock 40 65 322 eidolon_repraised:straw_effigy[facing=south]
setblock 39 65 322 eidolon_repraised:candle
setblock 41 65 322 minecraft:skeleton_skull[rotation=8]
setblock 46 64 329 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "101.4"}','{"text": "eidolon"}','{"text": "stone_altar"}','{"text": ""}']}}
setblock 47 64 329 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau Stone Altar"}','{"text": "und Elder"}','{"text": "Statue"}','{"text": ""}']}}
fill 55 64 317 55 79 330 minecraft:light_gray_concrete
fill 49 64 322 51 64 322 eidolon_repraised:stone_altar
setblock 50 65 322 eidolon_repraised:unholy_effigy[facing=south]
setblock 49 65 322 eidolon_repraised:goblet
setblock 51 65 322 eidolon_repraised:candle
