# 165 eidolon/brazier, crucible, altar, stone_altar
#area 171 401 220 426
fill 171 64 401 215 91 426 minecraft:air
fill 216 64 401 220 91 426 minecraft:air
fill 171 60 401 220 62 426 minecraft:stone
fill 171 63 401 220 63 426 minecraft:light_gray_concrete
fill 175 64 407 220 79 407 minecraft:light_gray_concrete
fill 175 64 407 175 79 420 minecraft:light_gray_concrete
setblock 176 64 419 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "165.1"}','{"text": "eidolon"}','{"text": "brazier"}','{"text": ""}']}}
setblock 177 64 419 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau Brazier und"}','{"text": "Stone Hands"}','{"text": ""}','{"text": ""}']}}
fill 185 64 407 185 79 420 minecraft:light_gray_concrete
setblock 180 64 412 eidolon_repraised:brazier
setblock 178 64 412 eidolon_repraised:stone_hand[facing=east]
setblock 182 64 412 eidolon_repraised:stone_hand[facing=west]
setblock 180 64 410 eidolon_repraised:stone_hand[facing=south]
setblock 186 64 419 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "165.2"}','{"text": "eidolon"}','{"text": "crucible"}','{"text": ""}']}}
setblock 187 64 419 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz einen"}','{"text": "Crucible auf"}','{"text": ""}','{"text": ""}']}}
fill 195 64 407 195 79 420 minecraft:light_gray_concrete
setblock 190 64 412 minecraft:campfire[facing=south,lit=true]
setblock 190 65 412 eidolon_repraised:crucible
kw testworld use 190 65 412 up minecraft:water_bucket
setblock 196 64 419 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "165.3"}','{"text": "eidolon"}','{"text": "altar"}','{"text": ""}']}}
setblock 197 64 419 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen Altar"}','{"text": "mit Bildnis"}','{"text": ""}','{"text": ""}']}}
fill 205 64 407 205 79 420 minecraft:light_gray_concrete
fill 199 64 412 201 64 412 eidolon_repraised:wooden_altar
setblock 200 65 412 eidolon_repraised:straw_effigy[facing=south]
setblock 199 65 412 eidolon_repraised:candle
setblock 201 65 412 minecraft:skeleton_skull[rotation=8]
setblock 206 64 419 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "165.4"}','{"text": "eidolon"}','{"text": "stone_altar"}','{"text": ""}']}}
setblock 207 64 419 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau Stone Altar"}','{"text": "und Elder"}','{"text": "Statue"}','{"text": ""}']}}
fill 215 64 407 215 79 420 minecraft:light_gray_concrete
fill 209 64 412 211 64 412 eidolon_repraised:stone_altar
setblock 210 65 412 eidolon_repraised:unholy_effigy[facing=south]
setblock 209 65 412 eidolon_repraised:goblet
setblock 211 65 412 eidolon_repraised:candle
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
