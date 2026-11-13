# 096 eidolon/brazier, crucible, altar, stone_altar
#area 11 290 60 315
fill 11 64 290 55 91 315 minecraft:air
fill 56 64 290 60 91 315 minecraft:air
fill 11 60 290 60 62 315 minecraft:stone
fill 11 63 290 60 63 315 minecraft:light_gray_concrete
fill 15 64 296 60 79 296 minecraft:light_gray_concrete
fill 15 64 296 15 79 309 minecraft:light_gray_concrete
setblock 16 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "096.1"}','{"text": "eidolon"}','{"text": "brazier"}','{"text": ""}']}}
setblock 17 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau Brazier und"}','{"text": "Stone Hands"}','{"text": ""}','{"text": ""}']}}
fill 25 64 296 25 79 309 minecraft:light_gray_concrete
setblock 20 64 301 eidolon_repraised:brazier
setblock 18 64 301 eidolon_repraised:stone_hand[facing=east]
setblock 22 64 301 eidolon_repraised:stone_hand[facing=west]
setblock 20 64 299 eidolon_repraised:stone_hand[facing=south]
setblock 26 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "096.2"}','{"text": "eidolon"}','{"text": "crucible"}','{"text": ""}']}}
setblock 27 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz einen"}','{"text": "Crucible auf"}','{"text": ""}','{"text": ""}']}}
fill 35 64 296 35 79 309 minecraft:light_gray_concrete
setblock 30 64 301 minecraft:campfire[facing=south,lit=true]
setblock 30 65 301 eidolon_repraised:crucible
kw testworld use 30 65 301 up minecraft:water_bucket
setblock 36 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "096.3"}','{"text": "eidolon"}','{"text": "altar"}','{"text": ""}']}}
setblock 37 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen Altar"}','{"text": "mit Bildnis"}','{"text": ""}','{"text": ""}']}}
fill 45 64 296 45 79 309 minecraft:light_gray_concrete
fill 39 64 301 41 64 301 eidolon_repraised:wooden_altar
setblock 40 65 301 eidolon_repraised:straw_effigy[facing=south]
setblock 39 65 301 eidolon_repraised:candle
setblock 41 65 301 minecraft:skeleton_skull[rotation=8]
setblock 46 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "096.4"}','{"text": "eidolon"}','{"text": "stone_altar"}','{"text": ""}']}}
setblock 47 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau Stone Altar"}','{"text": "und Elder"}','{"text": "Statue"}','{"text": ""}']}}
fill 55 64 296 55 79 309 minecraft:light_gray_concrete
fill 49 64 301 51 64 301 eidolon_repraised:stone_altar
setblock 50 65 301 eidolon_repraised:unholy_effigy[facing=south]
setblock 49 65 301 eidolon_repraised:goblet
setblock 51 65 301 eidolon_repraised:candle
