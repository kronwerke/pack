# 072 eidolon/brazier, crucible, altar
#area -4 290 35 315
fill -4 64 290 35 91 315 minecraft:air
fill -4 60 290 35 62 315 minecraft:stone
fill -4 63 290 35 63 315 minecraft:light_gray_concrete
fill 0 64 296 35 79 296 minecraft:light_gray_concrete
fill 0 64 296 0 79 309 minecraft:light_gray_concrete
setblock 1 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "072.1"}','{"text": "eidolon"}','{"text": "brazier"}','{"text": ""}']}}
setblock 2 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau Brazier und"}','{"text": "Stone Hands"}','{"text": ""}','{"text": ""}']}}
fill 10 64 296 10 79 309 minecraft:light_gray_concrete
setblock 5 64 301 eidolon_repraised:brazier
setblock 3 64 301 eidolon_repraised:stone_hand[facing=east]
setblock 7 64 301 eidolon_repraised:stone_hand[facing=west]
setblock 5 64 299 eidolon_repraised:stone_hand[facing=south]
setblock 11 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "072.2"}','{"text": "eidolon"}','{"text": "crucible"}','{"text": ""}']}}
setblock 12 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz einen"}','{"text": "Crucible auf"}','{"text": ""}','{"text": ""}']}}
fill 20 64 296 20 79 309 minecraft:light_gray_concrete
setblock 15 64 301 minecraft:campfire[facing=south,lit=true]
setblock 15 65 301 eidolon_repraised:crucible
kw testworld use 15 65 301 up minecraft:water_bucket
setblock 21 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "072.3"}','{"text": "eidolon"}','{"text": "altar"}','{"text": ""}']}}
setblock 22 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen Altar"}','{"text": "mit Bildnis"}','{"text": ""}','{"text": ""}']}}
fill 30 64 296 30 79 309 minecraft:light_gray_concrete
fill 24 64 301 26 64 301 eidolon_repraised:wooden_altar
setblock 25 65 301 eidolon_repraised:straw_effigy[facing=south]
setblock 24 65 301 eidolon_repraised:candle
setblock 26 65 301 minecraft:skeleton_skull[rotation=8]
